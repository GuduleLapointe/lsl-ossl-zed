#!/usr/bin/env python3
"""
Generate Markdown reference docs for LSL/OSSL from a MediaWiki XML export.

Usage:
    ./dev/generate_ref_docs.py <source_xml> <destination_md>

The source type (LSL functions, OSSL constants, etc.) is detected from the
filename. If no arguments are given, instructions for downloading the XML
files are printed.

Download the XML exports from:
  LSL functions:  https://wiki.secondlife.com/wiki/Special:Export
                  Category: LSL Functions
  LSL events:     https://wiki.secondlife.com/wiki/Special:Export
                  Category: LSL Events
  LSL constants:  https://wiki.secondlife.com/wiki/Special:Export
                  Category: LSL Constants
  OSSL functions: https://opensimulator.org/wiki/Special:Export
                  Category: OSSL Functions
  OSSL constants: https://opensimulator.org/wiki/Special:Export
                  Page: OSSL Constants

Note: opensimulator.org has SSL issues; export via browser and save the file.
"""

import os
import re
import sys
import xml.etree.ElementTree as ET
from datetime import datetime, timezone
from pathlib import Path


def _parse_xml(xml_path):
    """Return (root, namespace) for a MediaWiki XML export."""
    tree = ET.parse(xml_path)
    root = tree.getroot()
    ns_match = re.match(r"\{([^}]+)\}", root.tag)
    ns = ns_match.group(1) if ns_match else "http://www.mediawiki.org/xml/export-0.11/"
    return root, ns


def get_base_url(xml_path):
    """Return the wiki base URL from <siteinfo><base>, e.g. https://wiki.secondlife.com/wiki/Main_Page."""
    root, ns = _parse_xml(xml_path)
    base_el = root.find(f".//{{{ns}}}base")
    return base_el.text if base_el is not None else ""


def get_pages(xml_path):
    """Yield (title, text) for each page in a MediaWiki XML export."""
    root, ns = _parse_xml(xml_path)
    for page in root.findall(f".//{{{ns}}}page"):
        title_el = page.find(f"{{{ns}}}title")
        text_el = page.find(f".//{{{ns}}}text")
        if title_el is None or text_el is None:
            continue
        title = title_el.text or ""
        text = text_el.text or ""
        yield title, text


def clean_wiki(text):
    """Strip wiki/HTML markup, return plain text."""
    if not text:
        return ""
    # Decode common entities not handled by ET (MediaWiki uses &amp;#124; for |)
    text = text.replace("&amp;", "&").replace("&#124;", "|")
    # Phase 1: extract useful templates BEFORE any stripping
    text = re.sub(
        r"\{\{LSLP[T]?\|([a-zA-Z_][a-zA-Z_0-9 ]*)\}\}", r"\1", text
    )  # {{LSLP|name}}
    text = re.sub(
        r"\{\{LSL[_ ]Hex\|([0-9a-fA-Fx]+)\}\}", r"\1", text
    )  # {{LSL Hex|0x80}}
    text = re.sub(
        r"\{\{LSL[_ ]?Constant/([^}]+)\}\}", r"\1", text
    )  # {{LSL_Constant/NAME}}
    # HoverText: handle nested case {{HoverText|text|{{inner}}}} before collapsing leaves
    text = re.sub(r"\{\{HoverText\|([^|}]+)\|[^}]*\{\{[^}]*\}\}\}\}", r"\1", text)
    text = re.sub(r"\{\{HoverText\|([^|}]+)(?:\|[^}]*)?\}\}", r"\1", text)
    text = re.sub(
        r"\{\{LSLGC\|[^|]+\|([^}|]+)\}\}", r"\1", text
    )  # {{LSLGC|cat|display}}
    # [[link|display]] or [[link]] → display or link
    text = re.sub(r"\[\[(?:[^\]|]*\|)?([^\]]+)\]\]", r"\1", text)
    # Phase 2 & 3: collapse remaining templates
    for _ in range(5):
        text = re.sub(r"\{\{[^{}]*\}\}", "", text)
    # Remove <ref>...</ref>
    text = re.sub(r"<ref[^>]*>.*?</ref>", "", text, flags=re.DOTALL)
    # Remove HTML tags
    text = re.sub(r"<[^>]+>", " ", text)
    # Bold/italic wiki markup
    text = re.sub(r"'''([^']+)'''", r"\1", text)
    text = re.sub(r"''([^']+)''", r"\1", text)
    # Strip trailing wiki field markers (| leftover from parse boundary)
    text = re.sub(r"\s*\|\s*$", "", text)
    # Collapse whitespace
    text = re.sub(r"\n\s*\n+", "\n", text)
    text = re.sub(r"[ \t]+", " ", text)
    return text.strip()


def parse_fields(text):
    """
    Extract named fields from a MediaWiki template body.

    Handles both same-line (|p1_type=integer|p1_name=x) and
    multi-line (|func_desc=\\nsome long text) formats.

    Stops a field value at the next |fieldname= or at }} on its own line
    (to avoid confusing nested template closings like {{LSLP|x}} with the
    outer template closing }}).
    """
    fields = {}
    # The outer }} is always on its own line in MediaWiki templates.
    # Use \n}} as end-of-template marker so inner {{foo|bar}} don't terminate early.
    pattern = re.compile(
        # Stop at: next |field= (same or next line), |field (no value, new line), or \n}}
        r"\|([a-zA-Z_][a-zA-Z_0-9]*)\s*=\s*(.*?)(?=\|[a-zA-Z_][a-zA-Z_0-9]*\s*=|\n\|[a-zA-Z_]|\n\}\})",
        re.DOTALL,
    )
    for m in pattern.finditer(text):
        name = m.group(1)
        value = m.group(2).strip()
        fields[name] = value
    return fields


def build_param_list(fields):
    """Build (type, name) pairs from p1_type/p1_name fields."""
    params = []
    i = 1
    while True:
        ptype = fields.get(f"p{i}_type", "").strip()
        pname = fields.get(f"p{i}_name", "").strip()
        if not ptype and not pname:
            break
        if ptype and pname:
            params.append(f"{ptype} {pname}")
        elif ptype:
            params.append(ptype)
        elif pname:
            params.append(pname)
        i += 1
    return params


# ---------------------------------------------------------------------------
# Parsers
# ---------------------------------------------------------------------------


def parse_lsl_functions(xml_path):
    """Return dict name → {signature, desc} for LSL functions."""
    functions = {}
    for _title, text in get_pages(xml_path):
        if not re.search(r"\{\{LSL[_ ]?Function", text, re.IGNORECASE):
            continue

        fields = parse_fields(text)
        func_name = fields.get("func", "").strip()
        if not func_name or not re.match(r"ll[A-Z]", func_name):
            continue

        return_type = fields.get("return_type", "void").strip() or "void"
        params = build_param_list(fields)
        signature = f"{return_type} {func_name}({', '.join(params)})"

        desc = clean_wiki(
            fields.get("func_desc", "") or fields.get("func_footnote", "")
        )
        functions[func_name] = {"signature": signature, "desc": desc}

    return functions


def parse_ossl_functions(xml_path):
    """Return dict name → {signatures: [...], desc} for OSSL functions."""
    functions = {}
    for _title, text in get_pages(xml_path):
        if not re.search(r"\{\{osslfunc", text, re.IGNORECASE):
            continue

        fields = parse_fields(text)
        syntax = fields.get("function_syntax", "").strip()
        if not syntax:
            continue

        # Multiple signatures separated by <br /> (already decoded by ET)
        syntax_clean = re.sub(r"<br\s*/?>", "\n", syntax, flags=re.IGNORECASE)
        signatures = [s.strip() for s in syntax_clean.splitlines() if s.strip()]
        if not signatures:
            continue

        # Real name from first signature
        m = re.match(r"([a-zA-Z_][a-zA-Z_0-9]*)\s*\(", signatures[0])
        if not m:
            continue
        func_name = m.group(1)
        if not re.match(r"os[A-Z]", func_name):
            continue

        desc = clean_wiki(fields.get("description", ""))
        functions[func_name] = {"signatures": signatures, "desc": desc}

    return functions


def parse_lsl_events(xml_path):
    """Return dict name → {signature, desc} for LSL events."""
    events = {}
    for _title, text in get_pages(xml_path):
        if not re.search(r"\{\{LSL[_ ]?Event", text, re.IGNORECASE):
            continue

        fields = parse_fields(text)
        event_name = fields.get("event", "").strip()
        if not event_name:
            continue

        params = build_param_list(fields)
        signature = f"{event_name}({', '.join(params)})"
        desc = clean_wiki(fields.get("event_desc", ""))
        events[event_name] = {"signature": signature, "desc": desc}

    return events


def parse_lsl_constants(xml_path):
    """Return dict name → {type, value, desc} for LSL constants (one per page)."""
    constants = {}
    for _title, text in get_pages(xml_path):
        if not re.search(r"\{\{LSL[_ ]?Constant\b", text, re.IGNORECASE):
            continue

        fields = parse_fields(text)
        name = fields.get("name", "").strip()
        if not name:
            continue

        ctype = fields.get("type", "").strip()
        raw_value = (fields.get("hvalue", "") or fields.get("value", "")).strip()
        # Extract value from {{LSL Hex|0x80}} if present
        hex_m = re.search(r"\{\{LSL[_ ]Hex\|([^|}]+)\}\}", raw_value)
        value = hex_m.group(1) if hex_m else clean_wiki(raw_value)
        desc = clean_wiki(fields.get("desc", ""))
        constants[name] = {"type": ctype, "value": value, "desc": desc}

    return constants


def parse_ossl_constants(xml_path):
    """
    Return dict name → {value, desc} for OSSL constants.

    The OSSL constants export is a single wiki page with tables.
    Row format:  | [[link|NAME]] || value || description
    """
    constants = {}
    for _title, text in get_pages(xml_path):
        # Table rows: | [[path|NAME]] || value || desc
        row_re = re.compile(
            r"^\|\s*\[\[[^\]|]*\|([A-Z][A-Z_0-9]*)\]\]\s*\|\|\s*([^\|]+?)\s*\|\|\s*(.*?)$",
            re.MULTILINE,
        )
        for m in row_re.finditer(text):
            name = m.group(1).strip()
            value = m.group(2).strip()
            desc = clean_wiki(m.group(3))
            constants[name] = {"value": value, "desc": desc}

    return constants


# ---------------------------------------------------------------------------
# Writers
# ---------------------------------------------------------------------------


def _header(title, source_url="", fetch_ts=""):
    lines = [f"# {title}", ""]
    if source_url:
        lines.append(f"Source: {source_url}")
    if fetch_ts:
        lines.append(f"Fetched: {fetch_ts}")
    lines.append("")
    lines.append("")
    return "\n".join(lines)


def write_functions_md(path, title, functions, source_url="", fetch_ts="", is_ossl=False):
    with open(path, "w", encoding="utf-8") as f:
        f.write(_header(title, source_url, fetch_ts))
        for name in sorted(functions.keys(), key=str.lower):
            entry = functions[name]
            f.write(f"### {name}\n\n")
            if is_ossl:
                for sig in entry["signatures"]:
                    f.write(f"- `{sig}`\n")
                f.write("\n")
            else:
                f.write(f"- `{entry['signature']}`\n\n")
            if entry["desc"]:
                f.write(f"{entry['desc']}\n\n")


def write_events_md(path, title, events, source_url="", fetch_ts=""):
    with open(path, "w", encoding="utf-8") as f:
        f.write(_header(title, source_url, fetch_ts))
        for name in sorted(events.keys()):
            entry = events[name]
            f.write(f"### {name}\n\n")
            f.write(f"- `{entry['signature']}`\n\n")
            if entry["desc"]:
                f.write(f"{entry['desc']}\n\n")


def write_constants_md(path, title, constants, source_url="", fetch_ts=""):
    with open(path, "w", encoding="utf-8") as f:
        f.write(_header(title, source_url, fetch_ts))
        for name in sorted(constants.keys()):
            entry = constants[name]
            ctype = entry.get("type", "")
            value = entry.get("value", "")
            desc = entry.get("desc", "")
            if ctype and value:
                type_val = f"{ctype} {name} = {value}"
            elif value:
                type_val = f"{name} = {value}"
            else:
                type_val = name
            f.write(f"### {name}\n\n- `{type_val}`\n\n")
            if desc:
                f.write(f"{desc}\n\n")


# ---------------------------------------------------------------------------
# Type detection & dispatch
# ---------------------------------------------------------------------------

TYPES = {
    "lsl_functions":  (parse_lsl_functions,  "LSL Functions",  lambda p, t, d, u, ts: write_functions_md(p, t, d, u, ts, is_ossl=False)),
    "lsl_events":     (parse_lsl_events,     "LSL Events",     lambda p, t, d, u, ts: write_events_md(p, t, d, u, ts)),
    "lsl_constants":  (parse_lsl_constants,  "LSL Constants",  lambda p, t, d, u, ts: write_constants_md(p, t, d, u, ts)),
    "ossl_functions": (parse_ossl_functions, "OSSL Functions", lambda p, t, d, u, ts: write_functions_md(p, t, d, u, ts, is_ossl=True)),
    "ossl_constants": (parse_ossl_constants, "OSSL Constants", lambda p, t, d, u, ts: write_constants_md(p, t, d, u, ts)),
}


def detect_type(xml_path):
    """Guess the content type from the filename."""
    name = xml_path.name.lower()
    if "ossl" in name and "function" in name:
        return "ossl_functions"
    if "ossl" in name and "constant" in name:
        return "ossl_constants"
    if "lsl" in name and "function" in name:
        return "lsl_functions"
    if "lsl" in name and "event" in name:
        return "lsl_events"
    if "lsl" in name and "constant" in name:
        return "lsl_constants"
    return None


# ---------------------------------------------------------------------------
# Main
# ---------------------------------------------------------------------------


def _run(xml_path, out_path):
    """Process a single XML → MD conversion."""
    doc_type = detect_type(xml_path)
    if doc_type is None:
        print(f"❌ Cannot detect type from filename: {xml_path.name}")
        return False
    parser, title, writer = TYPES[doc_type]
    source_url = get_base_url(xml_path)
    fetch_ts = datetime.fromtimestamp(os.path.getmtime(xml_path), tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")
    out_path.parent.mkdir(parents=True, exist_ok=True)
    data = parser(xml_path)
    writer(out_path, title, data, source_url, fetch_ts)
    print(f"✅ {len(data):4d}  {title:20s} → {out_path}  (fetched {fetch_ts})")
    return True



if __name__ == "__main__":
    if len(sys.argv) == 3:
        if not _run(Path(sys.argv[1]), Path(sys.argv[2])):
            sys.exit(1)
    else:
        print(__doc__)
        sys.exit(0 if len(sys.argv) == 1 else 1)


