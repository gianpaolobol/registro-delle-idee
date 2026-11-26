#!/usr/bin/env bash
# Prepara la cartella di un nuovo progetto conforme alla linea guida.
# Uso: strumenti/nuovo-progetto.sh <cartella-di-destinazione> "<Nome del progetto>"
set -euo pipefail
cd "$(dirname "$0")/.."
dest="${1:?cartella di destinazione}"; nome="${2:?nome del progetto}"
mkdir -p "$dest"
cp -rn modello/. "$dest/"
cp LINEAGUIDA.md "$dest/"
sed -i "s/<Nome del progetto>/$nome/g" "$dest/README.md" "$dest/STATO.md"
echo "Pronto: $dest (ricorda: scheda in IDEE.md con [Gian] Promossa a progetto, riga in PROGETTI.md)"
