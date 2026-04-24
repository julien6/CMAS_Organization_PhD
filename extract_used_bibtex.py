#!/usr/bin/env python3
"""Extract BibTeX entries effectively cited in a LaTeX document.

Usage:
    python extract_used_bibtex.py paper.tex references.bib clean_references.bib
"""

from __future__ import annotations

import re
import sys
from pathlib import Path


CITE_PATTERN = re.compile(r"\\cite[a-zA-Z*]*\s*(?:\[[^\]]*\]\s*)*\{([^}]*)\}")


def extract_citation_keys(tex_content: str) -> set[str]:
    keys: set[str] = set()
    for match in CITE_PATTERN.finditer(tex_content):
        raw_keys = match.group(1).split(",")
        for key in raw_keys:
            cleaned = key.strip()
            if cleaned:
                keys.add(cleaned)
    return keys


def iter_bib_entries(bib_content: str):
    i = 0
    n = len(bib_content)
    while i < n:
        at_pos = bib_content.find("@", i)
        if at_pos == -1:
            break

        type_match = re.match(r"@([A-Za-z]+)\s*\{", bib_content[at_pos:])
        if not type_match:
            i = at_pos + 1
            continue

        entry_type = type_match.group(1).lower()
        open_brace_pos = at_pos + type_match.end() - 1

        depth = 0
        j = open_brace_pos
        while j < n:
            char = bib_content[j]
            if char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
                if depth == 0:
                    entry_text = bib_content[at_pos : j + 1]
                    yield entry_type, entry_text
                    i = j + 1
                    break
            j += 1
        else:
            raise ValueError("Unbalanced braces while parsing BibTeX file.")


def entry_key(entry_text: str) -> str | None:
    match = re.match(r"@[A-Za-z]+\s*\{\s*([^,\s]+)\s*,", entry_text, re.DOTALL)
    if match:
        return match.group(1).strip()
    return None


def select_entries(bib_content: str, used_keys: set[str]) -> list[str]:
    selected: list[str] = []
    for entry_type, text in iter_bib_entries(bib_content):
        if entry_type in {"comment", "preamble", "string"}:
            continue
        key = entry_key(text)
        if key and key in used_keys:
            selected.append(text.strip())
    return selected


def main() -> int:
    if len(sys.argv) != 4:
        print(
            "Usage: python extract_used_bibtex.py <paper.tex> <references.bib> <clean_references.bib>",
            file=sys.stderr,
        )
        return 1

    tex_path = Path(sys.argv[1])
    bib_path = Path(sys.argv[2])
    out_path = Path(sys.argv[3])

    tex_content = tex_path.read_text(encoding="utf-8")
    bib_content = bib_path.read_text(encoding="utf-8")

    used_keys = extract_citation_keys(tex_content)
    selected_entries = select_entries(bib_content, used_keys)

    missing_keys = sorted(used_keys - {entry_key(entry) for entry in selected_entries if entry_key(entry)})
    if missing_keys:
        print("Warning: missing BibTeX entries for keys:", ", ".join(missing_keys), file=sys.stderr)

    output = "\n\n".join(selected_entries).strip() + "\n"
    out_path.write_text(output, encoding="utf-8")

    print(f"Extracted {len(selected_entries)} entries to {out_path}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
