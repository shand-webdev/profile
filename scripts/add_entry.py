#!/usr/bin/env python3
"""
Cheeko Product Development Archivist & Builder Database Helper
Usage:
    python scripts/add_entry.py --interactive
    python scripts/add_entry.py --file path/to/draft.json
"""

import json
import os
import sys
import re
from datetime import datetime

DATABASE_PATH = os.path.join(os.path.dirname(__file__), "..", "data", "builder-database.json")

CONFIDENTIAL_KEYWORDS = [
    r"api[-_]?key", r"password", r"secret", r"token", r"proprietary prompt",
    r"supplier\s*name", r"bom\s*cost", r"margin", r"₹\s*\d+", r"\$\s*\d+",
    r"unreleased", r"confidential", r"internal spec"
]

VALID_CATEGORIES = [
    "Product", "AI", "Hardware", "UX", "UI", "Industrial Design",
    "Manufacturing", "DFM", "Packaging", "Compliance", "Vendors",
    "Growth", "Operations", "Testing", "Other"
]

def scan_confidentiality(text_blob):
    """Flags any content that might trigger confidentiality rules."""
    flags = []
    for kw in CONFIDENTIAL_KEYWORDS:
        if re.search(kw, text_blob, re.IGNORECASE):
            flags.append(kw)
    return flags

def slugify(title):
    return re.sub(r"[^a-z0-9]+", "-", title.lower()).strip("-")

def load_database():
    if not os.path.exists(DATABASE_PATH):
        return []
    with open(DATABASE_PATH, "r", encoding="utf-8") as f:
        return json.load(f)

def save_database(data):
    with open(DATABASE_PATH, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=2, ensure_ascii=False)
    print(f"✓ Saved database with {len(data)} entries to {DATABASE_PATH}")

def add_entry(entry):
    db = load_database()
    
    # Auto-generate ID if missing
    if "id" not in entry or not entry["id"]:
        entry["id"] = f"{slugify(entry.get('project', 'entry'))}-{slugify(entry.get('title', 'log'))}"
    
    # Ensure date
    if "date" not in entry or not entry["date"]:
        entry["date"] = datetime.now().strftime("%Y-%m-%d")

    # Confidentiality check
    all_text = " ".join([str(v) for v in entry.values() if isinstance(v, (str, list))])
    flags = scan_confidentiality(all_text)
    
    if flags:
        print(f"⚠️ Confidentiality flags detected: {flags}")
        print("  -> Defaulting visibility to PRIVATE.")
        entry["visibility"] = "PRIVATE"
        entry["confidentiality_level"] = "CONFIDENTIAL_PRIVATE"
    else:
        if "visibility" not in entry:
            entry["visibility"] = "PUBLIC"
        if "confidentiality_level" not in entry:
            entry["confidentiality_level"] = "PUBLIC"

    # Check for existing ID
    existing_idx = next((i for i, item in enumerate(db) if item["id"] == entry["id"]), None)
    if existing_idx is not None:
        print(f"Updating existing entry: {entry['id']}")
        db[existing_idx] = entry
    else:
        print(f"Adding new entry: {entry['id']}")
        db.insert(0, entry) # Most recent first

    save_database(db)
    return entry

if __name__ == "__main__":
    if len(sys.argv) > 2 and sys.argv[1] == "--file":
        with open(sys.argv[2], "r", encoding="utf-8") as f:
            entry = json.load(f)
            add_entry(entry)
    else:
        print("Cheeko Builder Database Manager.")
        print(f"Current entries: {len(load_database())}")
