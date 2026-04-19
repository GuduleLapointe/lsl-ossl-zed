#!/usr/bin/env python3
"""
Generate Markdown reference docs for LSL/OSSL from OpenSimulator C# source.

Usage:
    ./dev/generate_ref_docs.py           # clone/pull repo then generate all docs
    ./dev/generate_ref_docs.py --help    # print this help

Source repo (branch 0.9.3.0) is cloned into tmp/opensim-git/ on first run,
then pulled on subsequent runs.

C# files used:
    Interface/ILSL_Api.cs         → LSL functions (primary)
    Implementation/LSL_Api.cs     → LSL functions (extra not in interface)
    Interface/IOSSL_Api.cs        → OSSL functions (primary)
    Implementation/OSSL_Api.cs    → OSSL functions (extra not in interface)
    Runtime/LSL_Constants.cs      → LSL + OSSL constants (OS_ prefix)
    YEngine/MMRIEventHandlers.cs  → LSL event signatures
"""

import json
import os
import re
import subprocess
import sys
from datetime import datetime, timezone
from pathlib import Path

OPENSIM_REPO = "git://opensimulator.org/git/opensim"
OPENSIM_BRANCH = "0.9.3.0"
OPENSIM_DIR = Path("tmp/opensim-git")

_API = OPENSIM_DIR / "OpenSim/Region/ScriptEngine/Shared/Api"
_YENGINE = OPENSIM_DIR / "OpenSim/Region/ScriptEngine/YEngine"

SOURCES = {
    "lsl_funcs_iface": _API / "Interface/ILSL_Api.cs",
    "lsl_funcs_impl": _API / "Implementation/LSL_Api.cs",
    "ossl_funcs_iface": _API / "Interface/IOSSL_Api.cs",
    "ossl_funcs_impl": _API / "Implementation/OSSL_Api.cs",
    "constants": _API / "Runtime/LSL_Constants.cs",
    "events": _YENGINE / "MMRIEventHandlers.cs",
}

DOC_DIR = Path("doc")


# ---------------------------------------------------------------------------
# C# type → LSL type mapping
# ---------------------------------------------------------------------------

_CS_TO_LSL = {
    "LSL_Integer": "integer",
    "LSL_Float": "float",
    "LSL_String": "string",
    "LSL_Key": "key",
    "LSL_List": "list",
    "LSL_Vector": "vector",
    "LSL_Rotation": "rotation",
    "LSL_Types.Vector3": "vector",
    "LSL_Types.Quaternion": "rotation",
    "void": "void",
    "int": "integer",
    "bool": "integer",
    "double": "float",
    "float": "float",
    "string": "string",
    "key": "key",
    "vector": "vector",
    "rotation": "rotation",
}


def _cs_type(ctype):
    return _CS_TO_LSL.get(ctype.strip(), ctype.strip())


def _cs_param(param):
    """'LSL_Float volume' → 'float volume', 'int n' → 'integer n'."""
    parts = param.strip().split()
    if len(parts) >= 2:
        return f"{_cs_type(parts[0])} {parts[-1]}"
    return _cs_type(param.strip())


def _cs_params(params_str):
    """Parse comma-separated C# params and return list of 'type name' strings."""
    params_str = re.sub(r"\s+", " ", params_str.strip())
    if not params_str:
        return []
    return [_cs_param(p) for p in params_str.split(",") if p.strip()]


# ---------------------------------------------------------------------------
# C# source parsers
# ---------------------------------------------------------------------------


def parse_cs_functions(cs_path, prefix, require_public=False):
    """Parse a C# interface or implementation file.

    Returns dict  name → {signatures: [sig, ...], desc}
    prefix: 'll' for LSL, 'os' for OSSL.
    require_public: True for implementation files (filter to public methods only).
    """
    text = Path(cs_path).read_text(encoding="utf-8")
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.DOTALL)

    functions = {}
    pending_desc = ""
    i = 0
    lines = text.splitlines()

    pub = r"public\s+" if require_public else r""

    while i < len(lines):
        line = lines[i]
        stripped = line.strip()

        desc_m = re.search(r"//ApiDesc\s*(.*)", line)
        if desc_m:
            pending_desc = desc_m.group(1).strip()
            i += 1
            continue

        func_m = re.match(
            rf"\s+{pub}(\S[\w.]*)\s+({re.escape(prefix)}[A-Za-z]\w*)\s*\(",
            line,
        )
        if func_m:
            ret_cs = func_m.group(1)
            func_name = func_m.group(2)

            # Collect until ';' (declaration may wrap across lines)
            decl = line
            while ";" not in decl and i + 1 < len(lines):
                i += 1
                decl += " " + lines[i].strip()

            params_m = re.search(r"\(([^)]*)\)", decl, re.DOTALL)
            params_str = params_m.group(1) if params_m else ""
            params = _cs_params(params_str)
            sig = f"{_cs_type(ret_cs)} {func_name}({', '.join(params)})"

            if func_name not in functions:
                functions[func_name] = {"signatures": [sig], "desc": pending_desc}
            else:
                functions[func_name]["signatures"].append(sig)
                if not functions[func_name]["desc"] and pending_desc:
                    functions[func_name]["desc"] = pending_desc

            pending_desc = ""
        else:
            if stripped and not stripped.startswith("//"):
                pending_desc = ""

        i += 1

    return functions


def parse_cs_constants(cs_path):
    """Parse LSL_Constants.cs and return dict name → {type, value, desc}."""
    text = Path(cs_path).read_text(encoding="utf-8")
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.DOTALL)

    constants = {}
    lines = text.splitlines()
    pending_desc = ""

    for line in lines:
        stripped = line.strip()

        desc_m = re.search(r"//ApiDesc\s*(.*)", line)
        if desc_m:
            pending_desc = desc_m.group(1).strip()
            continue

        m = re.match(
            r"\s+public\s+(?:const|static\s+readonly)\s+(\w+)\s+([A-Z][A-Z0-9_]+)\s*=\s*([^;]+);",
            line,
        )
        if m:
            ctype, name, value = m.group(1), m.group(2), m.group(3).strip()
            lsl_type = (
                _cs_type(ctype)
                if ctype not in ("LSLInteger", "LSLFloat")
                else ("integer" if ctype == "LSLInteger" else "float")
            )
            constants[name] = {"type": lsl_type, "value": value, "desc": pending_desc}
            pending_desc = ""
        elif stripped and not stripped.startswith("//"):
            pending_desc = ""

    return constants


def parse_cs_events(cs_path):
    """Parse MMRIEventHandlers.cs → dict name → {signature, desc}."""
    text = Path(cs_path).read_text(encoding="utf-8")
    text = re.sub(r"/\*.*?\*/", "", text, flags=re.DOTALL)

    events = {}
    for m in re.finditer(r"\bvoid\s+([a-z][a-z_]+)\s*\(([^)]*)\)\s*;", text):
        name = m.group(1)
        params_str = m.group(2).strip()
        params = _cs_params(params_str) if params_str else []
        sig = f"{name}({', '.join(params)})"
        events[name] = {"signature": sig, "desc": ""}

    return events


# ---------------------------------------------------------------------------
# Writers
# ---------------------------------------------------------------------------


def _header(title, source_path="", mtime=""):
    lines = [f"# {title}", ""]
    if source_path:
        lines.append(f"Source: {source_path}")
    if mtime:
        lines.append(f"Generated: {mtime}")
    lines.append("")
    lines.append("")
    return "\n".join(lines)


def write_functions_md(path, title, functions, source_path="", mtime=""):
    with open(path, "w", encoding="utf-8") as f:
        f.write(_header(title, source_path, mtime))
        for name in sorted(functions.keys(), key=str.lower):
            entry = functions[name]
            f.write(f"### {name}\n\n")
            for sig in entry["signatures"]:
                f.write(f"- `{sig}`\n")
            f.write("\n")
            if entry.get("desc"):
                f.write(f"{entry['desc']}\n\n")


def write_events_md(path, title, events, source_path="", mtime=""):
    with open(path, "w", encoding="utf-8") as f:
        f.write(_header(title, source_path, mtime))
        for name in sorted(events.keys()):
            entry = events[name]
            f.write(f"### {name}\n\n")
            f.write(f"- `{entry['signature']}`\n\n")
            if entry.get("desc"):
                f.write(f"{entry['desc']}\n\n")


def write_constants_md(path, title, constants, source_path="", mtime=""):
    with open(path, "w", encoding="utf-8") as f:
        f.write(_header(title, source_path, mtime))
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
# Git repo management
# ---------------------------------------------------------------------------


def ensure_repo():
    """Clone the opensim repo if absent, or pull it if present."""
    if (OPENSIM_DIR / ".git").exists():
        print(f"↻  Pulling {OPENSIM_DIR} (branch {OPENSIM_BRANCH})…")
        subprocess.run(
            ["git", "-C", str(OPENSIM_DIR), "pull", "--ff-only"],
            check=True,
        )
    else:
        print(f"⬇  Cloning {OPENSIM_REPO} branch {OPENSIM_BRANCH}…")
        OPENSIM_DIR.parent.mkdir(parents=True, exist_ok=True)
        subprocess.run(
            [
                "git",
                "clone",
                "--branch",
                OPENSIM_BRANCH,
                "--depth",
                "1",
                OPENSIM_REPO,
                str(OPENSIM_DIR),
            ],
            check=True,
        )


def _mtime(path):
    return datetime.fromtimestamp(os.path.getmtime(path), tz=timezone.utc).strftime(
        "%Y-%m-%dT%H:%M:%SZ"
    )


# ---------------------------------------------------------------------------
# Main generation
# ---------------------------------------------------------------------------


def generate_all():
    missing = [k for k, p in SOURCES.items() if not p.exists()]
    if missing:
        for k in missing:
            print(f"❌ Missing: {SOURCES[k]}")
        sys.exit(1)

    DOC_DIR.mkdir(parents=True, exist_ok=True)

    # LSL functions: interface (primary) + implementation (extras)
    lsl = parse_cs_functions(SOURCES["lsl_funcs_iface"], "ll")
    lsl_extra = parse_cs_functions(SOURCES["lsl_funcs_impl"], "ll", require_public=True)
    added_lsl = {k: v for k, v in lsl_extra.items() if k not in lsl}
    lsl.update(added_lsl)
    write_functions_md(
        DOC_DIR / "LSL_Functions.md",
        "LSL Functions",
        lsl,
        source_path=str(SOURCES["lsl_funcs_iface"]),
        mtime=_mtime(SOURCES["lsl_funcs_iface"]),
    )
    print(f"✅ {len(lsl):4d}  LSL Functions   → doc/LSL_Functions.md")

    # OSSL functions: interface (primary) + implementation (extras)
    ossl = parse_cs_functions(SOURCES["ossl_funcs_iface"], "os")
    ossl_extra = parse_cs_functions(
        SOURCES["ossl_funcs_impl"], "os", require_public=True
    )
    added_ossl = {k: v for k, v in ossl_extra.items() if k not in ossl}
    ossl.update(added_ossl)
    write_functions_md(
        DOC_DIR / "OSSL_Functions.md",
        "OSSL Functions",
        ossl,
        source_path=str(SOURCES["ossl_funcs_iface"]),
        mtime=_mtime(SOURCES["ossl_funcs_iface"]),
    )
    print(f"✅ {len(ossl):4d}  OSSL Functions  → doc/OSSL_Functions.md")

    # Constants (LSL_Constants.cs covers both LL_ and OS_ prefixed)
    constants = parse_cs_constants(SOURCES["constants"])
    write_constants_md(
        DOC_DIR / "LSL_Constants.md",
        "LSL Constants",
        constants,
        source_path=str(SOURCES["constants"]),
        mtime=_mtime(SOURCES["constants"]),
    )
    print(f"✅ {len(constants):4d}  Constants       → doc/LSL_Constants.md")

    # Events
    events = parse_cs_events(SOURCES["events"])
    write_events_md(
        DOC_DIR / "LSL_Events.md",
        "LSL Events",
        events,
        source_path=str(SOURCES["events"]),
        mtime=_mtime(SOURCES["events"]),
    )
    print(f"✅ {len(events):4d}  LSL Events      → doc/LSL_Events.md")

    # Stats report
    stats = {
        "lsl_functions": len(lsl),
        "ossl_functions": len(ossl),
        "constants": len(constants),
        "events": len(events),
        "generated": datetime.now(tz=timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ"),
    }
    stats_path = Path("dev/generate_ref_docs.stats.json")
    stats_path.write_text(json.dumps(stats, indent=2) + "\n", encoding="utf-8")
    print(f"✅       Stats           → {stats_path}")


if __name__ == "__main__":
    if "--help" in sys.argv or "-h" in sys.argv:
        print(__doc__)
        sys.exit(0)

    ensure_repo()
    generate_all()
