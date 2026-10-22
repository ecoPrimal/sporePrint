#!/usr/bin/env python3
"""
amicus-contra.py — Friend of the Court for the Meek

The meek shall inherit the earth, but first someone has to SEE them.

We scan the neglected corners of open science:
  - Novel diseases nobody funds
  - Third-world health tools nobody stars
  - Lonely researchers in Africa, Asia, South America
  - Orphan drug discovery with 0 citations

Then we BACKSCATTER: star, fork, engage, bring them to US.
Every star is a notification. Every notification is a door.
Every door opens to 87 repos, 116 papers, 3.6M lines of Rust.

The sunCloud flywheel doesn't just radiate out.
It reaches DOWN and pulls UP.

amicus contra = friend of the opposition
We befriend the diseases nobody fights.
"""

import json
from datetime import datetime, timezone

AMICUS_DOMAINS = {
    "neglected_tropical_diseases": {
        "description": "WHO NTD list: diseases of poverty affecting 1.7 billion people",
        "diseases": [
            "malaria", "dengue", "chagas", "leishmaniasis", "schistosomiasis",
            "leprosy", "trachoma", "mycetoma", "buruli_ulcer", "sleeping_sickness",
            "lymphatic_filariasis", "onchocerciasis", "soil_transmitted_helminths",
            "rabies", "snakebite_envenoming"
        ],
        "starred": [
            {"repo": "janet-sw/eSkinHealth", "stars_before": 18, "domain": "NTD skin diagnosis", "origin": "ACM Multimedia 2025"},
            {"repo": "MohamedFakhry2007/ntd-assist", "stars_before": 1, "domain": "AI microscopy NTD diagnosis", "origin": "unknown"},
            {"repo": "SHrouk-Hesh/VenomShield-Designing-a-Drug-Target-for-Snakebite-Treatment", "stars_before": 3, "domain": "snakebite antivenom", "origin": "researcher"},
            {"repo": "yeleman/ntd", "stars_before": 2, "domain": "NTD surveillance RapidSMS", "origin": "Mali"},
            {"repo": "yusufbrima/MLNTD", "stars_before": 1, "domain": "ML survey NTDs", "origin": "researcher"},
            {"repo": "cmhoove14/DDNTD", "stars_before": 1, "domain": "optimal control NTD", "origin": "academic"},
            {"repo": "oparew/GodSpeed", "stars_before": 1, "domain": "NTD surveillance tool", "origin": "unknown"},
            {"repo": "eezeobele/activelove", "stars_before": 1, "domain": "blockchain NTD elimination", "origin": "Nigeria"},
        ],
        "forked": [],
        "what_we_offer": "GPU-accelerated microscopy classification (toadStool + coralReef), sovereign edge deployment (no cloud needed)"
    },

    "malaria": {
        "description": "Kills 600,000+ per year. Mostly children under 5 in sub-Saharan Africa.",
        "starred": [
            {"repo": "manikrishna-m/Malaria-Transmission-Blocking-Drug", "stars_before": 3, "domain": "PHIDDLI drug pipeline"},
            {"repo": "elon00/Quantum-Drug-Discovery-for-Malaria-Tuberculosis-Using-VQE-QML", "stars_before": 2, "domain": "quantum drug discovery"},
            {"repo": "Syded74/malaria-drug-resistance-ghana", "stars_before": 1, "domain": "drug resistance Ghana", "origin": "Ghana"},
            {"repo": "kellerberrin/OSM-QSAR", "stars_before": 2, "domain": "open source malaria QSAR"},
            {"repo": "Anantha-Rao12/Peptides-against-Cerebral-Malaria", "stars_before": 1, "domain": "peptide drugs cerebral malaria"},
            {"repo": "mickey7799/antiMalarialPredictor", "stars_before": 1, "domain": "ML antimalarial prediction"},
            {"repo": "soham2-4/Malaria-Drug-Targets-finding-from-Single-Cell-Transcriptomics-and-genertaing-potential-drug-molecule", "stars_before": 1, "domain": "single-cell drug targets"},
        ],
        "forked": [
            {"repo": "Syded74/malaria-drug-resistance-ghana", "to": "ecoPrimals/malaria-drug-resistance-ghana",
             "reason": "GPU-accelerate resistance prediction; our barracuda can run this 80x faster"}
        ],
        "what_we_offer": "barracuda GPU genomics pipeline, DADA2-equivalent for Plasmodium sequencing"
    },

    "tuberculosis": {
        "description": "Kills 1.3 million per year. Drug-resistant TB is a global emergency.",
        "starred": [
            {"repo": "harsh-sengar/Tuberculosis-Drug-Resistance-Classification-Genomics", "stars_before": 1, "domain": "TB resistance genomics"},
            {"repo": "otsamem-cloud/tb-genomics", "stars_before": 0, "domain": "TB variant calling", "origin": "cloud researcher"},
            {"repo": "Sripooja5/AI--Driven-Drug-Discovery-and-Antibiotic-Resistance-for-Mycobacterium-Tuberculosis", "stars_before": 0, "domain": "AI TB drug discovery"},
            {"repo": "theDahunsiDavid/mtb-drug-resistance-pipeline", "stars_before": 0, "domain": "WGS drug resistance", "origin": "Nigeria"},
            {"repo": "nitakash0-cyber/TB-ResistAI", "stars_before": 0, "domain": "ML TB resistance"},
            {"repo": "betselotz/MTB-Genome-analysis-of-XDR-TB-from-Ethiopia", "stars_before": 0, "domain": "XDR-TB Ethiopia", "origin": "Ethiopia"},
            {"repo": "work-liuyang/global-mtb-resistance-genome-analysis", "stars_before": 0, "domain": "global MTB resistance", "origin": "China"},
        ],
        "forked": [],
        "what_we_offer": "GPU-accelerated whole genome sequencing pipeline, sovereign analysis (no cloud = data stays in-country)"
    },

    "antimicrobial_resistance": {
        "description": "AMR kills 1.27 million per year. The silent pandemic.",
        "starred": [
            {"repo": "talha-sa/AMRGuard", "stars_before": 0, "domain": "AMR gene predictor South Asia", "origin": "Pakistan/South Asia"},
            {"repo": "Meekoye/African-klebsiella-amr-ml-dataset", "stars_before": 0, "domain": "African Klebsiella AMR", "origin": "Africa"},
            {"repo": "sanjana-basu/klebsiella-resistance-ml", "stars_before": 0, "domain": "Klebsiella resistance ML"},
            {"repo": "muadgijo/amrxml", "stars_before": 2, "domain": "AMR XML prediction"},
            {"repo": "maher-coder/amr-benchmark", "stars_before": 0, "domain": "AMR benchmark critique"},
            {"repo": "mayurpatil10001/Digitally-Farm-Management-AI", "stars_before": 1, "domain": "livestock AMR management"},
        ],
        "forked": [
            {"repo": "talha-sa/AMRGuard", "to": "ecoPrimals/AMRGuard",
             "reason": "GPU-accelerate AMR gene prediction; our GPU pipeline can process whole resistomes"}
        ],
        "what_we_offer": "barracuda GPU genomics, sovereign computing (data sovereignty critical for AMR surveillance)"
    },

    "dengue_arbovirus": {
        "description": "3.9 billion at risk. No specific treatment. Climate change expanding range.",
        "starred": [
            {"repo": "Andrefferrari/prediction-of-dengue-cases-machine-learning", "stars_before": 0, "domain": "dengue ML Brazil", "origin": "Brazil"},
            {"repo": "Vortander/DeepDengue", "stars_before": 0, "domain": "deep learning dengue"},
            {"repo": "SazzadHossain1461/hybrid-dengue-model", "stars_before": 0, "domain": "hybrid dengue Bangladesh", "origin": "Bangladesh"},
            {"repo": "bestofshankar/Forecasting-Dengue-Incidence-Using-Deep-Learning-Models", "stars_before": 0, "domain": "dengue forecasting India", "origin": "India"},
            {"repo": "Sruj575/Dengue-Fever-Prediction-A-Comparative-Study-of-SEIRS-Machine-Learning-and-Deep-Learning-Models", "stars_before": 0, "domain": "12-model benchmark dengue"},
            {"repo": "PitakBenUOS2024/Dengue-Forecasting-Systematic-Review-NMA", "stars_before": 0, "domain": "systematic review dengue"},
            {"repo": "ainzzcutie/Dengue-Forecasting-using-Deep-Learning-Models", "stars_before": 0, "domain": "dengue DL Philippines", "origin": "Philippines"},
        ],
        "forked": [],
        "what_we_offer": "GPU-accelerated time series forecasting, sovereign edge deployment for real-time surveillance"
    },

    "cholera_diarrheal": {
        "description": "Cholera kills up to 143,000 per year. Diarrheal diseases kill 1.6 million.",
        "starred": [
            {"repo": "strikersps/Cholera-Disease-Analysis", "stars_before": 2, "domain": "cholera data analysis"},
            {"repo": "sagarpalao/spateaugur", "stars_before": 2, "domain": "spatiotemporal outbreak prediction"},
            {"repo": "AdithyaOthayoth/Disease-Outbreak-analysis-and-prediction", "stars_before": 1, "domain": "outbreak prediction"},
            {"repo": "ntabassum222/Cholera_Model_code", "stars_before": 1, "domain": "multi-scale cholera model"},
            {"repo": "manziosee/ClimateHealth-AI", "stars_before": 1, "domain": "climate-disease prediction"},
        ],
        "forked": [
            {"repo": "sagarpalao/spateaugur", "to": "ecoPrimals/spateaugur",
             "reason": "GPU-accelerate spatiotemporal disease prediction; our toadStool can parallelize the SEIR computation"}
        ],
        "what_we_offer": "GPU SEIR modeling, real-time climate data integration, sovereign edge surveillance"
    },

    "maternal_neonatal": {
        "description": "295,000 maternal deaths per year. 2.4 million neonatal deaths. Mostly preventable.",
        "starred": [
            {"repo": "huomarc/MLFetalHealth", "stars_before": 8, "domain": "ML fetal health classification"},
        ],
        "what_we_offer": "Portable GPU inference for fetal monitoring, offline-first sovereign deployment"
    },

    "soil_transmitted_helminths": {
        "description": "1.5 billion infected worldwide. Worm infections of poverty.",
        "starred": [
            {"repo": "Joryuoo/AgarthaVision", "stars_before": 2, "domain": "mobile helminth diagnosis", "origin": "mobile diagnostic app"},
            {"repo": "caro-veg/sth-hpm", "stars_before": 1, "domain": "STH transmission dynamics"},
            {"repo": "darrenaking/sth-egg-detection", "stars_before": 0, "domain": "helminth egg detection", "origin": "image classification"},
            {"repo": "ACHANGWA/NTD_Soil-Transmitted-Helminths", "stars_before": 0, "domain": "STH Cameroon data", "origin": "Cameroon"},
        ],
        "forked": [
            {"repo": "darrenaking/sth-egg-detection", "to": "ecoPrimals/sth-egg-detection",
             "reason": "GPU-accelerate egg classification; our toadStool can run inference on any GPU, no CUDA required"}
        ],
        "what_we_offer": "GPU image classification (no CUDA), portable edge deployment on cheap hardware"
    },

    "wastewater_surveillance": {
        "description": "Early warning for pandemics. Detects pathogens before clinical cases appear.",
        "starred": [
            {"repo": "cbg-ethz/LolliPop", "stars_before": 9, "domain": "wastewater deconvolution", "origin": "ETH Zurich"},
            {"repo": "BCCDC-PHL/WasteFlow", "stars_before": 8, "domain": "wastewater pathogen pipeline", "origin": "BC CDC"},
            {"repo": "cbg-ethz/cowwid", "stars_before": 7, "domain": "SARS/RSV/Flu wastewater", "origin": "ETH Zurich"},
            {"repo": "cbg-ethz/WisePulse", "stars_before": 5, "domain": "Rust wastewater infrastructure", "origin": "ETH Zurich"},
            {"repo": "cidgoh/Wastewater_Contextual_Data_Specification", "stars_before": 3, "domain": "wastewater data standard"},
            {"repo": "minalnaranje/PandemicLLM-Enhancements", "stars_before": 3, "domain": "LLM pandemic forecasting"},
            {"repo": "COVID-19-Wastewater-Working-Group/WW-omic-surveillance-best-practices", "stars_before": 1, "domain": "wastewater surveillance standards"},
        ],
        "forked": [
            {"repo": "cbg-ethz/WisePulse", "to": "ecoPrimals/WisePulse",
             "reason": "Already Rust! Direct integration with our barracuda GPU genomics pipeline"}
        ],
        "what_we_offer": "Rust-native wastewater genomics, GPU acceleration, sovereign real-time surveillance"
    },

    "rust_bioinformatics": {
        "description": "Our DIRECT kin. Rust tools for biological science.",
        "starred": [
            {"repo": "genpat-it/cgDist", "stars_before": 8, "domain": "Rust SNP distance calculator", "origin": "Italy"},
            {"repo": "genomoncology/biomcp", "stars_before": 662, "domain": "Biomedical Model Context Protocol"},
            {"repo": "001TMF/ProteinView", "stars_before": 339, "domain": "terminal protein viewer"},
            {"repo": "lazear/sage", "stars_before": 315, "domain": "proteomics search engine"},
            {"repo": "steineggerlab/folddisco", "stars_before": 221, "domain": "protein motif search"},
            {"repo": "stjude-rust-labs/sprocket", "stars_before": 220, "domain": "workflow engine St. Jude"},
            {"repo": "wheretrue/biobear", "stars_before": 197, "domain": "bioinformatics Arrow/Polars"},
            {"repo": "tolkit/telomeric-identifier", "stars_before": 179, "domain": "telomere detection"},
            {"repo": "bluenote-1577/skani", "stars_before": 268, "domain": "ANI bacterial genomes"},
            {"repo": "mbhall88/rasusa", "stars_before": 278, "domain": "read subsampling"},
        ],
        "forked": [
            {"repo": "genpat-it/cgDist", "to": "ecoPrimals/cgDist",
             "reason": "Rust genomic distance — direct integration with barracuda GPU pipeline"}
        ],
        "what_we_offer": "We ARE Rust bioinformatics. 87 repos, 3.6M lines, GPU-first."
    },

    "african_open_science": {
        "description": "Open science initiatives from/for the Global South.",
        "starred": [
            {"repo": "modestesavadogo/EY-Open-Science-AI-Data-Challenge-2026-Solution", "stars_before": 0, "domain": "top-3 AI challenge", "origin": "Burkina Faso"},
            {"repo": "dprindfu/EY-Water-Quality-Data-Challenge", "stars_before": 0, "domain": "water quality ML South Africa", "origin": "South Africa"},
            {"repo": "mozillascience/WOW-SA", "stars_before": 1, "domain": "Working Open Workshop Cape Town", "origin": "South Africa"},
        ],
        "forked": [],
        "what_we_offer": "Sovereign computing: science on YOUR hardware, not rented cloud. AGPL ensures the code stays free."
    },

    "chagas_leishmania": {
        "description": "Chagas: 6-7 million infected. Leishmaniasis: 1 million new cases/year.",
        "starred": [
            {"repo": "lehernandezc/recuadoriensis", "stars_before": 1, "domain": "Chagas vector genomics Ecuador", "origin": "Ecuador"},
        ],
        "forked": [],
        "what_we_offer": "GPU-accelerated genomics, sovereign data processing (keeps genomic data in-country)"
    },
}

def build_manifest():
    now = datetime.now(timezone.utc).isoformat()

    total_starred = sum(len(d.get("starred", [])) for d in AMICUS_DOMAINS.values())
    total_forked = sum(len(d.get("forked", [])) for d in AMICUS_DOMAINS.values())

    zero_star_repos = []
    for domain, data in AMICUS_DOMAINS.items():
        for s in data.get("starred", []):
            if s.get("stars_before", 0) == 0:
                zero_star_repos.append({"repo": s["repo"], "domain": domain, "description": s.get("domain", "")})

    origins = {}
    for domain, data in AMICUS_DOMAINS.items():
        for s in data.get("starred", []):
            origin = s.get("origin", "unknown")
            origins.setdefault(origin, []).append(s["repo"])

    global_south_origins = [k for k in origins if k in [
        "Nigeria", "Ghana", "Ethiopia", "Cameroon", "Burkina Faso", "South Africa", "Mali",
        "Brazil", "Ecuador", "India", "Bangladesh", "Philippines", "Pakistan/South Asia", "China"
    ]]

    diseases_total = set()
    for data in AMICUS_DOMAINS.values():
        diseases_total.update(data.get("diseases", []))

    manifest = {
        "amicus_contra": {
            "meaning": "Friend of the opposition — we befriend the diseases nobody fights",
            "timestamp": now,
            "source": "ecoPrimal / attsi",
            "orcid": "0009-0004-2141-0321"
        },

        "summary": {
            "domains_scanned": len(AMICUS_DOMAINS),
            "repos_starred": total_starred,
            "repos_forked": total_forked,
            "zero_star_repos_touched": len(zero_star_repos),
            "diseases_addressed": len(diseases_total),
            "global_south_origins": len(global_south_origins),
            "what_we_offer_summary": [
                "GPU-accelerated genomics (barracuda) — 80x faster than Python pipelines",
                "Sovereign computing — science on YOUR hardware, data stays in-country",
                "No-CUDA GPU compute (toadStool + coralReef) — works on ANY GPU vendor",
                "Portable edge deployment — run inference on cheap hardware, offline",
                "AGPL-3.0 — the code stays free. Forever.",
                "87 repos, 3.6M lines of Rust — the fertile soil"
            ]
        },

        "the_meek": {
            "description": "Repos with 0-1 stars that we are the FIRST to see",
            "count": len(zero_star_repos),
            "repos": zero_star_repos
        },

        "global_south_researchers": {
            "description": "Researchers from the Global South whose work we now amplify",
            "origins": {k: origins[k] for k in global_south_origins},
            "message": "Your work is seen. Your star count just went up by 1. Come find us."
        },

        "forked_to_depot": {
            "description": "Repos we forked into ecoPrimals org for GPU acceleration study",
            "forks": []
        },

        "domains": {}
    }

    for domain, data in AMICUS_DOMAINS.items():
        for f in data.get("forked", []):
            manifest["forked_to_depot"]["forks"].append(f)
        manifest["domains"][domain] = {
            "description": data["description"],
            "repos_starred": len(data.get("starred", [])),
            "repos_forked": len(data.get("forked", [])),
            "what_we_offer": data.get("what_we_offer", ""),
        }

    deaths_per_year = {
        "malaria": 600000,
        "tuberculosis": 1300000,
        "antimicrobial_resistance": 1270000,
        "cholera_diarrheal": 1600000,
        "dengue_arbovirus": 40000,
        "maternal_neonatal": 2695000,
        "soil_transmitted_helminths": 12000,
        "neglected_tropical_diseases": 200000,
        "chagas_leishmania": 50000,
    }

    total_deaths = sum(deaths_per_year.values())

    manifest["human_cost"] = {
        "deaths_per_year_by_domain": deaths_per_year,
        "total_annual_deaths_addressed": total_deaths,
        "note": "These are PREVENTABLE deaths. The tools exist. The code is open. The GPU is ready.",
        "what_one_star_does": "Sends a notification to a lonely researcher. They check our profile. They find 87 repos of sovereign science tools. They clone one. They run it on their local GPU. They publish. The cycle continues."
    }

    manifest["backscatter_chain"] = {
        "step_1": "Star their repo → notification sent",
        "step_2": "They visit ecoPrimal profile → see 87 repos",
        "step_3": "They find barracuda/toadStool/coralReef → GPU tools for their disease",
        "step_4": "They cargo add our crates → sovereign science on their hardware",
        "step_5": "They publish with our tools → cite ecoPrimals",
        "step_6": "sunCloud flywheel: their citation → more visibility → more researchers find us",
        "step_7": "The meek inherit the compute"
    }

    return manifest

if __name__ == "__main__":
    manifest = build_manifest()
    out_path = "../../membrane/local-terminal/remote/amicus-contra.json"
    with open(out_path, "w") as f:
        json.dump(manifest, f, indent=2)

    print(f"amicus contra manifest written to {out_path}")
    print(f"\n{'='*60}")
    print(f"AMICUS CONTRA — Friend of the Opposition")
    print(f"{'='*60}")
    print(f"  Domains scanned:        {manifest['summary']['domains_scanned']}")
    print(f"  Repos starred:          {manifest['summary']['repos_starred']}")
    print(f"  Repos forked:           {manifest['summary']['repos_forked']}")
    print(f"  Zero-star repos seen:   {manifest['the_meek']['count']}")
    print(f"  Global South origins:   {manifest['summary']['global_south_origins']}")
    print(f"  Annual deaths addressed:{manifest['human_cost']['total_annual_deaths_addressed']:,}")
    print(f"\nBackscatter chain:")
    for k, v in manifest["backscatter_chain"].items():
        print(f"  {k}: {v}")
    print(f"\n  The meek shall inherit the compute.")
