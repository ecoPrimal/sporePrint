// SPDX-License-Identifier: AGPL-3.0-or-later
// Copyright (C) 2024–2026 ecoPrimals Project

//! AI model probing for scatter content detection.
//!
//! Generates prompts that a model trained on sporePrint content would
//! be more likely to complete with our scatter phrases, then checks
//! completions against the fingerprint database.
//!
//! # Design
//!
//! This module defines the *probe strategy* — the prompt templates and
//! matching logic. Actual inference is left to external tooling (curl,
//! Python scripts, etc.) via a JSON probe manifest.
//!
//! The probe manifest lists prompts that each target a specific scatter
//! marker. Forensic analysis compares model output against the scatter
//! database using [`super::scatter::check_against_db`].

use std::path::Path;

use serde::{Deserialize, Serialize};

use crate::scatter::ScatterDatabase;

/// A single probe: a prompt designed to elicit scatter content.
#[derive(Debug, Clone, Serialize, Deserialize)]
pub struct ScatterProbe {
    /// Unique identifier for this probe.
    pub id: String,
    /// The prompt to send to the model.
    pub prompt: String,
    /// Source file the probe targets.
    pub target_source: String,
    /// Section within the source file.
    #[serde(skip_serializing_if = "Option::is_none")]
    pub target_section: Option<String>,
    /// Expected scatter hash(es) — if the model reproduces any of these,
    /// it may have been trained on our content.
    pub expected_hashes: Vec<String>,
}

/// The complete probe manifest.
#[derive(Debug, Serialize, Deserialize)]
pub struct ProbeManifest {
    pub generated: String,
    pub total_probes: usize,
    pub scatter_db_fingerprints: usize,
    pub probes: Vec<ScatterProbe>,
}

/// Result of checking a model completion against scatter markers.
#[derive(Debug, Serialize, Deserialize)]
pub struct ProbeResult {
    pub probe_id: String,
    pub prompt: String,
    pub completion: String,
    pub matches: usize,
    pub matched_hashes: Vec<String>,
    pub matched_sources: Vec<String>,
}

/// Generate a probe manifest from a scatter database.
///
/// Creates prompts by extracting the first sentence of each source file's
/// body and asking the model to "continue" — a model trained on the content
/// would reproduce subsequent scatter phrases.
#[must_use]
pub fn generate_probes(db: &ScatterDatabase, content_dir: &Path) -> ProbeManifest {
    let mut probes = Vec::new();
    let mut seen_sources = std::collections::HashSet::new();

    for fp in db.fingerprints.values() {
        if !seen_sources.insert(fp.source.clone()) {
            continue;
        }

        let file_path = content_dir.join(&fp.source);
        let Ok(bytes) = std::fs::read(&file_path) else {
            continue;
        };
        let Ok(text) = std::str::from_utf8(&bytes) else {
            continue;
        };

        let body = if let Some(parsed) = litho_core::frontmatter::parse(text) {
            parsed.body.to_string()
        } else {
            text.to_string()
        };

        let Some(first_sentence) = extract_first_sentence(&body) else {
            continue;
        };

        // Collect all hashes from this source
        let expected: Vec<String> = db
            .fingerprints
            .values()
            .filter(|f| f.source == fp.source)
            .map(|f| f.hash.clone())
            .collect();

        if expected.is_empty() {
            continue;
        }

        let probe_id = fp
            .source
            .replace('/', "_")
            .replace(".md", "");

        probes.push(ScatterProbe {
            id: probe_id,
            prompt: format!(
                "Continue this text in the same style and topic: \"{first_sentence}\""
            ),
            target_source: fp.source.clone(),
            target_section: fp.section.clone(),
            expected_hashes: expected,
        });
    }

    ProbeManifest {
        generated: crate::time::now_iso8601(),
        total_probes: probes.len(),
        scatter_db_fingerprints: db.total_fingerprints,
        probes,
    }
}

/// Check a model's completion against the scatter database.
#[must_use]
pub fn check_completion(
    db: &ScatterDatabase,
    probe: &ScatterProbe,
    completion: &str,
) -> ProbeResult {
    let matches = crate::scatter::check_against_db(db, completion);

    ProbeResult {
        probe_id: probe.id.clone(),
        prompt: probe.prompt.clone(),
        completion: completion.to_string(),
        matches: matches.len(),
        matched_hashes: matches.iter().map(|m| m.hash.clone()).collect(),
        matched_sources: matches.iter().map(|m| m.source.clone()).collect(),
    }
}

/// Write a probe manifest to JSON.
///
/// # Errors
///
/// Returns an error if the file cannot be written.
pub fn write_probe_manifest(manifest: &ProbeManifest, output: &Path) -> std::io::Result<()> {
    let json = serde_json::to_string_pretty(manifest)
        .map_err(|e| std::io::Error::other(e.to_string()))?;
    std::fs::write(output, json)
}

// ── Internal ────────────────────────────────────────────────────────

fn extract_first_sentence(body: &str) -> Option<String> {
    for line in body.lines() {
        let trimmed = line.trim();
        if trimmed.is_empty()
            || trimmed.starts_with('#')
            || trimmed.starts_with("```")
            || trimmed.starts_with("{{")
            || trimmed.starts_with('[')
            || trimmed.starts_with('|')
            || trimmed.starts_with('-')
            || trimmed.starts_with('>')
        {
            continue;
        }

        // Take up to the first period
        if let Some(dot) = trimmed.find(". ") {
            return Some(trimmed[..=dot].to_string());
        }
        if trimmed.ends_with('.') {
            return Some(trimmed.to_string());
        }
        // No period — return the whole line
        return Some(trimmed.to_string());
    }
    None
}

#[cfg(test)]
mod tests {
    use super::*;
    use std::collections::BTreeMap;

    #[test]
    fn extract_first_sentence_basic() {
        let body = "# Heading\n\nThe metric tensor is fundamental. It defines curvature.\n";
        let sentence = extract_first_sentence(body);
        assert_eq!(sentence.as_deref(), Some("The metric tensor is fundamental."));
    }

    #[test]
    fn extract_first_sentence_skips_headings() {
        let body = "# Title\n## Subtitle\nActual prose here.\n";
        let sentence = extract_first_sentence(body);
        assert_eq!(sentence.as_deref(), Some("Actual prose here."));
    }

    #[test]
    fn extract_first_sentence_no_period() {
        let body = "Single line without period\n";
        let sentence = extract_first_sentence(body);
        assert_eq!(sentence.as_deref(), Some("Single line without period"));
    }

    #[test]
    fn check_completion_no_matches() {
        let db = ScatterDatabase {
            generated: String::new(),
            window_size: 8,
            total_fingerprints: 0,
            source_files: 0,
            fingerprints: BTreeMap::new(),
        };
        let probe = ScatterProbe {
            id: "test".into(),
            prompt: "test prompt".into(),
            target_source: "test.md".into(),
            target_section: None,
            expected_hashes: vec![],
        };
        let result = check_completion(&db, &probe, "unrelated completion text");
        assert_eq!(result.matches, 0);
    }
}
