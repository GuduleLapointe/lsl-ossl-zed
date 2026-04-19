#!/usr/bin/env python3
"""
Build grammar/grammar.js from the template and compile it with tree-sitter.

Usage:
    ./dev/build_grammar.py

Steps:
    1. Read grammar/src/grammar-template.js (human-editable template)
    2. Insert LSL/OSSL function, constant, and event lists from doc/*.md
    3. Write grammar/grammar.js (generated — do not edit by hand)
    4. Run `npm run build` in grammar/ to compile the parser
    5. Write grammar/.stats for use by deploy-grammar.sh

Prerequisites: run generate_ref_docs.py first to populate doc/.
"""

import json
import re
import subprocess
import sys
from pathlib import Path


def extract_names(md_path, sig_pattern=None):
    """Return sorted function/constant/event names from a Markdown reference file.

    Collects ### Name headers, plus any names matched by sig_pattern on
    signature bullet lines only (lines starting with '- `'), to avoid
    false positives from function names mentioned in description text.
    """
    text = md_path.read_text(encoding="utf-8")
    names = set(re.findall(r"^### (\w+)", text, re.MULTILINE))
    if sig_pattern:
        for line in text.splitlines():
            if line.startswith("- `"):
                for m in re.finditer(sig_pattern, line):
                    names.add(m.group(1))
    return sorted(names, key=str.lower)


def make_choice(names, depth=3):
    """Render a tree-sitter choice(...) block at the given tab depth."""
    t = "\t" * depth
    ti = "\t" * (depth + 1)
    items = "\n".join(f'{ti}"{name}",' for name in sorted(names, key=str.lower))
    return f"choice(\n{items}\n{t}),"


def replace_placeholder(js, rule_name, names):
    """Replace a placeholder choice() in the template with the full choice(...) block.

    Matches lines of the form (2-tab indent):
        \t\trule_name: ($) => choice(), // WHATEVER_PLACEHOLDER
    and replaces them with the expanded multi-line choice(...) block.
    """
    pattern = re.compile(
        rf"^(\t\t{re.escape(rule_name)}: \(\$\) =>)\s*choice\(\),.*$",
        re.MULTILINE,
    )
    new_choice = make_choice(names, depth=3)

    def repl(m):
        return f"{m.group(1)}\n\t\t\t{new_choice}"

    result, count = pattern.subn(repl, js)
    if count == 0:
        print(f"⚠️  Placeholder for '{rule_name}' not found in template")
    return result


def main():
    doc_dir = Path("doc")
    template_path = Path("grammar/src/grammar-template.js")
    grammar_path = Path("grammar/grammar.js")
    stats_path = Path("logs/build_grammar.stats.json")
    stats_path.parent.mkdir(exist_ok=True)

    missing = [p for p in [
        doc_dir / "LSL_Functions.md",
        doc_dir / "OSSL_Functions.md",
        doc_dir / "LSL_Constants.md",
        doc_dir / "LSL_Events.md",
        template_path,
    ] if not p.exists()]
    if missing:
        for p in missing:
            print(f"❌ Not found: {p}")
        sys.exit(1)

    lsl_names  = set(extract_names(doc_dir / "LSL_Functions.md",
                                   sig_pattern=r"\b(ll[A-Za-z]\w+)\s*\("))
    ossl_names = set(extract_names(doc_dir / "OSSL_Functions.md",
                                   sig_pattern=r"\b(os[A-Za-z]\w+)\s*\("))

    lsl_funcs  = sorted(lsl_names,  key=str.lower)
    ossl_funcs = sorted(ossl_names, key=str.lower)
    constants  = extract_names(doc_dir / "LSL_Constants.md")
    events     = extract_names(doc_dir / "LSL_Events.md")

    # Generate grammar.js from template
    js = template_path.read_text(encoding="utf-8")
    js = replace_placeholder(js, "constant",      constants)
    js = replace_placeholder(js, "lsl_function",  lsl_funcs)
    js = replace_placeholder(js, "ossl_function", ossl_funcs)
    js = replace_placeholder(js, "event_name",    events)
    grammar_path.write_text(js, encoding="utf-8")

    print(f"✅ {len(lsl_funcs):4d}  LSL functions   → grammar/grammar.js")
    print(f"✅ {len(ossl_funcs):4d}  OSSL functions  → grammar/grammar.js")
    print(f"✅ {len(constants):4d}  constants       → grammar/grammar.js")
    print(f"✅ {len(events):4d}  events          → grammar/grammar.js")

    # Compile parser
    print("==> Running npm run build in grammar/…")
    subprocess.run(["npm", "run", "build"], cwd="grammar", check=True)
    print("✅ Parser compiled")

    # Write stats for deploy step
    stats = {
        "lsl_functions": len(lsl_funcs),
        "ossl_functions": len(ossl_funcs),
        "constants": len(constants),
        "events": len(events),
    }
    stats_path.write_text(json.dumps(stats, indent=2) + "\n", encoding="utf-8")
    print(f"✅ Stats written → {stats_path}")


if __name__ == "__main__":
    main()
