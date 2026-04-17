#!/bin/bash
# Deploy grammar changes: generate parser, push grammar repo, update extension hash.
# Usage: ./deploy-grammar.sh ["commit message"]

set -e
cd "$(dirname "$0")"

# --- Grammar repo ---

echo "==> Generating parser..."
(cd grammar && npm run build)

# Commit grammar if there are changes
if ! git -C grammar diff --quiet || ! git -C grammar diff --cached --quiet; then
    GRAMMAR_MSG="${1:-$(git -C grammar log -1 --pretty=%s 2>/dev/null || echo "Update grammar")}"
    echo "==> Committing grammar repo: $GRAMMAR_MSG"
    (cd grammar && git add -A && git commit -m "$GRAMMAR_MSG")
fi

# Push grammar if there are unpushed commits
if [ -n "$(git -C grammar log origin/master..HEAD 2>/dev/null)" ]; then
    echo "==> Pushing grammar repo..."
    (cd grammar && git push)
fi

# --- Extension repo ---

HASH=$(git -C grammar rev-parse HEAD)
CURRENT=$(grep 'commit = ' extension.toml | sed 's/.*"\(.*\)"/\1/')

if [ "$HASH" = "$CURRENT" ]; then
    echo "==> extension.toml already up to date ($HASH)"
else
    LAST_MSG=$(git -C grammar log -1 --pretty="%h %s")
    EXT_MSG="${1:-deploy grammar $LAST_MSG}"

    echo "==> Updating extension.toml: $HASH"
    sed -i '' "s/commit = \".*\"/commit = \"$HASH\"/" extension.toml

    echo "==> Committing extension repo: $EXT_MSG"
    git add extension.toml grammar
    git commit -m "$EXT_MSG"
fi

echo ""
echo "Done. Rebuild the extension in Zed to apply changes."
