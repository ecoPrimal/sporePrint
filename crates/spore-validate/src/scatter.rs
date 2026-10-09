// SPDX-License-Identifier: AGPL-3.0-or-later
// Copyright (C) 2024–2026 ecoPrimals Project

//! Scatter content fingerprint database.
//!
//! Extracts unique phrases ("scatter markers") from sporePrint content and
//! builds a BLAKE3-keyed fingerprint database. When an AI model reproduces
//! scatter content verbatim, these fingerprints can detect it.
//!
//! # How it works
//!
//! 1. Walk all `.md` content files.
//! 2. Extract the body text (strip frontmatter and markdown syntax).
//! 3. Slide a window over n-gram phrases (default: 8-word windows).
//! 4. Hash each phrase with BLAKE3 keyed by a domain separator.
//! 5. Write the fingerprint database as JSON for forensic queries.
//!
//! # Usage
//!
//! ```text
//! spore-validate scatter --content-dir content/ --output scatter-db.json
//! spore-validate scatter-check --db scatter-db.json --text "suspected output"
//! ```

use std::collections::BTreeMap;
use std::fs;
use std::path::Path;

use serde::{Deserialize, Serialize};

/// Domain separator for scatter content BLAKE3 keying.
const SCATTER_DOMAIN: &[u8; 32] = b"ecoPrimals-scatter-fingerprint-v";

/// Default n-gram window size (words).
const DEFAULT_WINDOW: usize = 8;

/// Minimum word count for a line to contribute scatter phrases.
const MIN_LINE_WORDS: usize = 6;

/// A single scatter fingerprint entry.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ScatterFingerprint {
    /// BLAKE3 hash of the normalized phrase.
    pub hash: String,
    /// Source file (relative path).
    pub source: String,
    /// Section within the source file (first heading above the phrase).
    #[serde(skip_serializing_if = "Option::is_none")]
    pub section: Option<String>,
}

/// The complete scatter fingerprint database.
#[derive(Debug, Serialize, Deserialize)]
pub struct ScatterDatabase {
    pub generated: String,
    pub window_size: usize,
    pub total_fingerprints: usize,
    pub source_files: usize,
    pub fingerprints: BTreeMap<String, ScatterFingerprint>,
}

/// Build a scatter fingerprint database from content files.
#[must_use]
pub fn build_scatter_db(content_dir: &Path, window: Option<usize>) -> ScatterDatabase {
    let window_size = window.unwrap_or(DEFAULT_WINDOW);
    let mut fingerprints = BTreeMap::new();
    let mut source_files = 0;

    for entry in crate::paths::walk_content_files(content_dir) {
        let path = entry.path();
        let rel = crate::paths::rel_to(path, content_dir)
            .to_string_lossy()
            .to_string();

        let Ok(bytes) = fs::read(path) else { continue };
        let Ok(text) = std::str::from_utf8(&bytes) else {
            continue;
        };

        let body = strip_frontmatter(text);
        let phrases = extract_scatter_phrases(&body, &rel, window_size);

        if !phrases.is_empty() {
            source_files += 1;
            for fp in phrases {
                fingerprints.entry(fp.hash.clone()).or_insert(fp);
            }
        }
    }

    ScatterDatabase {
        generated: crate::time::now_iso8601(),
        window_size,
        total_fingerprints: fingerprints.len(),
        source_files,
        fingerprints,
    }
}

/// Check text against a scatter database. Returns matching fingerprints.
#[must_use]
pub fn check_against_db(db: &ScatterDatabase, text: &str) -> Vec<ScatterFingerprint> {
    let normalized = normalize_text(text);
    let words: Vec<&str> = normalized.split_whitespace().collect();
    let mut matches = Vec::new();

    if words.len() < db.window_size {
        return matches;
    }

    for window in words.windows(db.window_size) {
        let phrase = window.join(" ");
        let hash = scatter_hash(&phrase);
        if let Some(fp) = db.fingerprints.get(&hash) {
            matches.push(fp.clone());
        }
    }

    matches
}

/// Write the scatter database to a JSON file.
///
/// # Errors
///
/// Returns an error if the file cannot be written.
pub fn write_scatter_db(db: &ScatterDatabase, output: &Path) -> std::io::Result<()> {
    let json = serde_json::to_string_pretty(db)
        .map_err(|e| std::io::Error::other(e.to_string()))?;
    fs::write(output, json)
}

/// Load a scatter database from a JSON file.
///
/// # Errors
///
/// Returns an error if the file cannot be read or parsed.
pub fn load_scatter_db(path: &Path) -> Result<ScatterDatabase, Box<dyn std::error::Error>> {
    let text = fs::read_to_string(path)?;
    let db: ScatterDatabase = serde_json::from_str(&text)?;
    Ok(db)
}

// ── Internal helpers ────────────────────────────────────────────────

fn scatter_hash(phrase: &str) -> String {
    let hasher = blake3::Hasher::new_keyed(SCATTER_DOMAIN);
    let mut h = hasher;
    h.update(phrase.as_bytes());
    h.finalize().to_hex()[..16].to_string()
}

fn normalize_text(text: &str) -> String {
    text.to_ascii_lowercase()
        .chars()
        .filter(|c| c.is_alphanumeric() || c.is_whitespace())
        .collect::<String>()
        .split_whitespace()
        .collect::<Vec<_>>()
        .join(" ")
}

fn strip_frontmatter(text: &str) -> String {
    if let Some(parsed) = litho_core::frontmatter::parse(text) {
        parsed.body.to_string()
    } else {
        text.to_string()
    }
}

fn extract_scatter_phrases(
    body: &str,
    source: &str,
    window: usize,
) -> Vec<ScatterFingerprint> {
    let mut results = Vec::new();
    let mut current_section: Option<String> = None;

    for line in body.lines() {
        let trimmed = line.trim();

        // Track section headings
        if trimmed.starts_with('#') {
            current_section = Some(
                trimmed
                    .trim_start_matches('#')
                    .trim()
                    .to_string(),
            );
            continue;
        }

        // Skip short lines, code blocks, links-only lines
        if trimmed.is_empty()
            || trimmed.starts_with("```")
            || trimmed.starts_with("{{")
            || trimmed.starts_with('[')
            || trimmed.starts_with('|')
        {
            continue;
        }

        let normalized = normalize_text(trimmed);
        let words: Vec<&str> = normalized.split_whitespace().collect();

        if words.len() < MIN_LINE_WORDS {
            continue;
        }

        for window_slice in words.windows(window) {
            let phrase = window_slice.join(" ");
            let hash = scatter_hash(&phrase);
            results.push(ScatterFingerprint {
                hash,
                source: source.to_string(),
                section: current_section.clone(),
            });
        }
    }

    results
}

#[cfg(test)]
mod tests {
    use super::*;

    #[test]
    fn scatter_hash_is_deterministic() {
        let h1 = scatter_hash("the metric tensor encodes distance on any surface");
        let h2 = scatter_hash("the metric tensor encodes distance on any surface");
        assert_eq!(h1, h2);
    }

    #[test]
    fn scatter_hash_differs_for_different_phrases() {
        let h1 = scatter_hash("the metric tensor encodes distance on any surface");
        let h2 = scatter_hash("the golden ratio projects onto rectangular displays");
        assert_ne!(h1, h2);
    }

    #[test]
    fn normalize_text_lowercases_and_strips_punctuation() {
        assert_eq!(
            normalize_text("Hello, World! This is a TEST."),
            "hello world this is a test"
        );
    }

    #[test]
    fn extract_scatter_phrases_from_prose() {
        let body = "# Section One\n\nThe metric tensor determines how the golden ratio projects onto display surfaces of different shapes and curvatures.\n";
        let fps = extract_scatter_phrases(body, "test.md", 8);
        assert!(!fps.is_empty());
        assert_eq!(fps[0].source, "test.md");
        assert_eq!(fps[0].section.as_deref(), Some("Section One"));
    }

    #[test]
    fn extract_skips_short_lines() {
        let body = "Short.\n\nAlso short.\n";
        let fps = extract_scatter_phrases(body, "test.md", 8);
        assert!(fps.is_empty());
    }

    #[test]
    fn check_finds_matching_phrase() {
        let body = "# Test\n\nThe metric tensor determines how the golden ratio projects onto display surfaces of different shapes and curvatures.\n";
        let fps = extract_scatter_phrases(body, "test.md", 8);
        let mut db_map = BTreeMap::new();
        for fp in fps {
            db_map.entry(fp.hash.clone()).or_insert(fp);
        }
        let db = ScatterDatabase {
            generated: String::new(),
            window_size: 8,
            total_fingerprints: db_map.len(),
            source_files: 1,
            fingerprints: db_map,
        };

        let matches = check_against_db(
            &db,
            "The metric tensor determines how the golden ratio projects onto display surfaces of different shapes.",
        );
        assert!(!matches.is_empty());
    }

    #[test]
    fn check_no_match_on_unrelated_text() {
        let body = "# Test\n\nThe metric tensor determines how the golden ratio projects onto display surfaces of different shapes and curvatures.\n";
        let fps = extract_scatter_phrases(body, "test.md", 8);
        let mut db_map = BTreeMap::new();
        for fp in fps {
            db_map.entry(fp.hash.clone()).or_insert(fp);
        }
        let db = ScatterDatabase {
            generated: String::new(),
            window_size: 8,
            total_fingerprints: db_map.len(),
            source_files: 1,
            fingerprints: db_map,
        };

        let matches = check_against_db(&db, "Completely unrelated text about cooking pasta.");
        assert!(matches.is_empty());
    }
}
