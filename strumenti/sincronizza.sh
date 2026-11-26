#!/usr/bin/env bash
# Propone la linea guida aggiornata a ogni repository con una pull request.
# Aggiunge i file "cartello" solo se mancano: non modifica mai file esistenti
# diversi da LINEAGUIDA.md (regola "si aggiunge, non si riscrive").
# Uso: GH_TOKEN=<token> OWNER=gianpaolobol strumenti/sincronizza.sh [repo...]
set -euo pipefail
cd "$(dirname "$0")/.."
OWNER="${OWNER:-gianpaolobol}"
VERSIONE="$(grep -m1 -oE 'Versione [0-9]+\.[0-9]+' LINEAGUIDA.md | cut -d' ' -f2)"
RAMO="linea-guida/v${VERSIONE}"
CARTELLI=(CLAUDE.md GEMINI.md .gemini/settings.json .github/copilot-instructions.md .github/workflows/linea-guida.yml)

if [ $# -gt 0 ]; then REPOS=("$@"); else mapfile -t REPOS < <(grep -vE '^\s*(#|$)' strumenti/repository.txt); fi

contenuto_b64() { base64 -w0 "$1"; }

for repo in "${REPOS[@]}"; do
  echo "== $repo"
  base="$(gh api "repos/$OWNER/$repo" --jq .default_branch 2>/dev/null)" || { echo "   non raggiungibile, salto"; continue; }
  attuale="$(gh api "repos/$OWNER/$repo/contents/LINEAGUIDA.md?ref=$base" --jq .content 2>/dev/null | base64 -d 2>/dev/null || true)"
  if [ "$attuale" == "$(cat LINEAGUIDA.md)" ]; then echo "   già allineato"; continue; fi
  if gh api "repos/$OWNER/$repo/pulls?head=$OWNER:$RAMO&state=open" --jq 'length' | grep -q '^[1-9]'; then echo "   PR già aperta"; continue; fi

  sha_base="$(gh api "repos/$OWNER/$repo/git/ref/heads/$base" --jq .object.sha)"
  gh api -X POST "repos/$OWNER/$repo/git/refs" -f ref="refs/heads/$RAMO" -f sha="$sha_base" >/dev/null 2>&1 || true

  metti() { # percorso_nel_repo file_locale messaggio
    local sha; sha="$(gh api "repos/$OWNER/$repo/contents/$1?ref=$RAMO" --jq .sha 2>/dev/null || true)"
    gh api -X PUT "repos/$OWNER/$repo/contents/$1" -f message="$3" -f branch="$RAMO" \
      -f content="$(contenuto_b64 "$2")" ${sha:+-f sha="$sha"} >/dev/null
  }

  metti LINEAGUIDA.md LINEAGUIDA.md "Linea guida v$VERSIONE [registro-delle-idee]"
  aggiunti=()
  for c in "${CARTELLI[@]}"; do
    if ! gh api "repos/$OWNER/$repo/contents/$c?ref=$base" >/dev/null 2>&1; then
      metti "$c" "modello/$c" "Aggiunge $c (LINEAGUIDA §4.1)"; aggiunti+=("$c")
    fi
  done
  nota=""
  if ! gh api "repos/$OWNER/$repo/contents/AGENTS.md?ref=$base" >/dev/null 2>&1; then
    metti AGENTS.md modello/AGENTS.md "Aggiunge AGENTS.md (LINEAGUIDA §4.1)"; aggiunti+=(AGENTS.md)
  else
    nota="- \`AGENTS.md\` esiste già: non è stato toccato. Se non rimanda a \`LINEAGUIDA.md\`, va aggiunta una sezione firmata in cima."
  fi
  if ! gh api "repos/$OWNER/$repo/contents/STATO.md?ref=$base" >/dev/null 2>&1; then
    nota="$nota
- Manca \`STATO.md\`: va scritto da un agente che conosce il progetto (modello in \`registro-delle-idee/modello/STATO.md\`)."
  fi

  corpo="Aggiorna la copia della **LINEAGUIDA** alla versione **$VERSIONE** dall'originale in \`registro-delle-idee\`.

File cartello aggiunti perché mancanti: ${aggiunti[*]:-nessuno}
$nota

Nessun file esistente è stato modificato oltre a \`LINEAGUIDA.md\`. Da approvare: [Gian]."
  gh api -X POST "repos/$OWNER/$repo/pulls" -f title="Linea guida v$VERSIONE" -f head="$RAMO" -f base="$base" -f body="$corpo" --jq .html_url
done
