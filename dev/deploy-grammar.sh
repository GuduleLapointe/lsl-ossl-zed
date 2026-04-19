#!/bin/bash
# Deploy: commit and push grammar, update extension, bump version, commit, tag, push.
#
# Prerequisites:
#   1. dev/generate_ref_docs.py  — populate doc/
#   2. dev/build_grammar.py      — build grammar/grammar.js and grammar/.stats
#
# Usage: ./deploy-grammar.sh

set -e
cd "$(dirname "$0")/.."

# --- Read build stats ---

STATS_FILE="dev/build_grammar.stats.json"
if [ ! -f "$STATS_FILE" ]; then
    echo "❌ $STATS_FILE not found — run dev/build_grammar.py first"
    exit 1
fi

LSL=$(python3 -c "import json; d=json.load(open('$STATS_FILE')); print(d['lsl_functions'])")
OSSL=$(python3 -c "import json; d=json.load(open('$STATS_FILE')); print(d['ossl_functions'])")
CONSTANTS=$(python3 -c "import json; d=json.load(open('$STATS_FILE')); print(d['constants'])")
EVENTS=$(python3 -c "import json; d=json.load(open('$STATS_FILE')); print(d['events'])")
GRAMMAR_MSG="update grammar, ${LSL} LSL functions, ${OSSL} OSSL functions, ${CONSTANTS} constants, ${EVENTS} events"

# --- Grammar repo ---

if ! git -C grammar diff --quiet || ! git -C grammar diff --cached --quiet; then
    echo "==> Committing grammar repo: $GRAMMAR_MSG"
    (cd grammar && git add -A && git commit -m "$GRAMMAR_MSG")
else
    echo "==> Grammar repo: nothing to commit"
fi

if [ -n "$(git -C grammar log origin/master..HEAD 2>/dev/null)" ]; then
    echo "==> Pushing grammar repo…"
    (cd grammar && git push)
else
    echo "==> Grammar repo: already up to date"
fi

# --- Extension repo ---

HASH=$(git -C grammar rev-parse HEAD)
CURRENT=$(grep 'commit = ' extension.toml | sed 's/.*"\(.*\)"/\1/')

if [ "$HASH" != "$CURRENT" ]; then
    echo "==> Updating extension.toml: grammar commit → $HASH"
    sed -i '' "s/commit = \".*\"/commit = \"$HASH\"/" extension.toml
fi

# Bump patch version in extension.toml
OLD_VER=$(grep '^version = ' extension.toml | sed 's/version = "\(.*\)"/\1/')
PATCH=$(echo "$OLD_VER" | cut -d. -f3)
NEW_PATCH=$((PATCH + 1))
NEW_VER=$(echo "$OLD_VER" | sed "s/\.[0-9]*$/.${NEW_PATCH}/")
echo "==> Bumping version: $OLD_VER → $NEW_VER"
sed -i '' "s/^version = \".*\"/version = \"${NEW_VER}\"/" extension.toml

# Commit and tag main repo
EXT_MSG="deploy grammar v${NEW_VER}: ${GRAMMAR_MSG}"
echo "==> Committing extension repo: $EXT_MSG"
git add extension.toml grammar
git commit -m "$EXT_MSG"

TAG="v${NEW_VER}"
echo "==> Tagging: $TAG"
git tag "$TAG"

# Push main repo
echo "==> Pushing main repo…"
git push
git push --tags

echo ""
echo "Done. Version $NEW_VER deployed."
