#!/usr/bin/env python3
"""
Update grammar/grammar.js with the full lists of LSL/OSSL functions,
constants, and event handlers extracted from doc/*.md.

Usage:
    ./dev/update_grammar.py

Reads:
    doc/LSL_Functions.md   → lsl_function rule
    doc/OSSL_Functions.md  → ossl_function rule
    doc/LSL_Constants.md
    doc/OSSL_Constants.md  → constant rule (merged)
    doc/LSL_Events.md      → event_name rule

Writes:
    grammar/grammar.js     (in-place)

Run generate_ref_docs.py first to refresh doc/ from the XML sources.
"""

import re
import sys
from pathlib import Path


def extract_names(md_path, sig_pattern=None):
    """Return all function names from a Markdown reference file.

    Includes both ### Name headers and function names found in signature
    bullet lines (e.g. overloads documented under a parent function's header).
    sig_pattern: regex to match function names in signature lines (optional).
    """
    text = md_path.read_text(encoding="utf-8")
    names = set(re.findall(r"^### (\w+)", text, re.MULTILINE))
    if sig_pattern:
        for m in re.finditer(sig_pattern, text):
            names.add(m.group(1))
    return sorted(names, key=str.lower)


def make_choice(names, depth=3):
    """Render a tree-sitter choice(...) block at the given tab depth."""
    t = "\t" * depth
    ti = "\t" * (depth + 1)
    items = "\n".join(f'{ti}"{name}",' for name in sorted(names, key=str.lower))
    return f"choice(\n{items}\n{t}),"


def replace_rule(js, rule_name, names):
    """Replace the choice(...) body of a named rule in grammar.js."""
    depth = 3
    t = "\t" * depth
    pattern = re.compile(
        rf"({re.escape(rule_name)}: \(\$\) =>\n{t})choice\(.*?\n{t}\),",
        re.DOTALL,
    )
    new_block = make_choice(names, depth)
    result, count = pattern.subn(rf"\g<1>{new_block}", js)
    if count == 0:
        print(f"⚠️  Rule '{rule_name}' not found in grammar.js")
    return result


def main():
    doc_dir = Path("doc")
    grammar_path = Path("grammar/grammar.js")

    missing = [p for p in [
        doc_dir / "LSL_Functions.md",
        doc_dir / "OSSL_Functions.md",
        doc_dir / "LSL_Constants.md",
        doc_dir / "OSSL_Constants.md",
        doc_dir / "LSL_Events.md",
        grammar_path,
    ] if not p.exists()]
    if missing:
        for p in missing:
            print(f"❌ Not found: {p}")
        sys.exit(1)

    lsl_names  = set(extract_names(doc_dir / "LSL_Functions.md",
                                   sig_pattern=r"\b(ll[A-Za-z]\w+)\s*\("))
    ossl_names = set(extract_names(doc_dir / "OSSL_Functions.md",
                                   sig_pattern=r"\b(os[A-Za-z]\w+)\s*\("))

    # Merge supplemental files (manually curated, not overwritten by generate_ref_docs.py)
    lsl_supp = doc_dir / "LSL_supplement.md"
    ossl_supp = doc_dir / "OSSL_supplement.md"
    if lsl_supp.exists():
        lsl_names.update(extract_names(lsl_supp, sig_pattern=r"\b(ll[A-Za-z]\w+)\s*\("))
    if ossl_supp.exists():
        ossl_names.update(extract_names(ossl_supp, sig_pattern=r"\b(os[A-Za-z]\w+)\s*\("))

    lsl_funcs  = sorted(lsl_names,  key=str.lower)
    ossl_funcs = sorted(ossl_names, key=str.lower)
    constants  = sorted(
        set(extract_names(doc_dir / "LSL_Constants.md") +
            extract_names(doc_dir / "OSSL_Constants.md")),
        key=str.lower,
    )
    events     = extract_names(doc_dir / "LSL_Events.md")

    print(f"  lsl_function : {len(lsl_funcs)}")
    print(f"  ossl_function: {len(ossl_funcs)}")
    print(f"  constant     : {len(constants)}")
    print(f"  event_name   : {len(events)}")

    js = grammar_path.read_text(encoding="utf-8")
    js = replace_rule(js, "constant",     constants)
    js = replace_rule(js, "lsl_function", lsl_funcs)
    js = replace_rule(js, "ossl_function", ossl_funcs)
    js = replace_rule(js, "event_name",   events)
    grammar_path.write_text(js, encoding="utf-8")

    print(f"✅ grammar/grammar.js updated")


if __name__ == "__main__":
    main()
