#!/usr/bin/env python3
"""Applica le linee guida correnti a un repository (idempotente, solo aggiunte o blocchi gestiti).

Uso: python3 strumenti/sincronizza.py <cartella-registro> <cartella-repository> [nome-repository]

Gestisce:
- LINEE_GUIDA.md e i file in sincronizzati/ (copiati così come sono);
- il blocco <!-- inizio-protocollo-comune --> in AGENTS.md (creato o aggiornato);
- le righe @LINEE_GUIDA.md e @AGENTS.md in CLAUDE.md;
- il riquadro <!-- inizio-riquadro-linee-guida --> in README.md;
- la sezione "## Linee guida" di STATO.md (creato dal modello se manca).
Il resto del contenuto dei file non viene toccato.
"""
import os, re, shutil, sys

HUB, REPO = sys.argv[1], sys.argv[2]
NAME = sys.argv[3] if len(sys.argv) > 3 else os.path.basename(os.path.abspath(REPO))

linee = open(os.path.join(HUB, 'LINEE_GUIDA.md'), encoding='utf-8').read()
VERSION = re.search(r'linee-guida-versione: (\d+\.\d+\.\d+)', linee).group(1)
changed = []

def rd(rel):
    p = os.path.join(REPO, rel)
    return open(p, encoding='utf-8').read() if os.path.isfile(p) else None

def wr(rel, text):
    p = os.path.join(REPO, rel)
    if rd(rel) == text:
        return
    os.makedirs(os.path.dirname(p) or '.', exist_ok=True)
    open(p, 'w', encoding='utf-8').write(text)
    changed.append(rel)

def after_title(text, block):
    lines = text.split('\n')
    if lines and lines[0].startswith('# '):
        return '\n'.join([lines[0], '', block.rstrip(), ''] + lines[1:])
    return block.rstrip() + '\n\n' + text

def upsert_block(text, start, end, block):
    pat = re.compile(re.escape(start) + r'.*?' + re.escape(end) + r'\n?', re.S)
    if pat.search(text):
        return pat.sub(lambda _: block.rstrip() + '\n', text, count=1)
    return None

# 1. copie gestite
wr('LINEE_GUIDA.md', linee)
src = os.path.join(HUB, 'sincronizzati')
for base, _, files in os.walk(src):
    for f in files:
        rel = os.path.relpath(os.path.join(base, f), src)
        content = open(os.path.join(base, f), encoding='utf-8').read()
        existing = rd(rel)
        if rel == 'GEMINI.md' and existing is not None and 'sincronizzazione delle linee guida' not in existing:
            if '@./LINEE_GUIDA.md' not in existing:
                wr(rel, after_title(existing, '@./LINEE_GUIDA.md\n\n@./AGENTS.md\n'))
            continue
        wr(rel, content)

# 2. AGENTS.md
section = open(os.path.join(HUB, 'modelli', 'SEZIONE_AGENTS.md'), encoding='utf-8').read()
agents = rd('AGENTS.md')
if agents is None:
    wr('AGENTS.md', f'# Istruzioni per gli agenti AI — {NAME}\n\n' + section)
else:
    updated = upsert_block(agents, '<!-- inizio-protocollo-comune -->', '<!-- fine-protocollo-comune -->', section)
    if updated is None:
        updated = after_title(agents, section)
    wr('AGENTS.md', updated)

# 3. CLAUDE.md
claude = rd('CLAUDE.md')
if claude is None:
    wr('CLAUDE.md', '@LINEE_GUIDA.md\n@AGENTS.md\n')
else:
    missing = [l for l in ('@LINEE_GUIDA.md', '@AGENTS.md') if l not in claude]
    if missing:
        wr('CLAUDE.md', after_title(claude, '\n'.join(missing) + '\n'))

# 4. README.md
banner = (f"<!-- inizio-riquadro-linee-guida -->\n> **Linee guida v{VERSION}** — Questo progetto segue le linee guida comuni dei progetti di Gian Paolo Franceschini: "
          "leggi prima [`LINEE_GUIDA.md`](LINEE_GUIDA.md), poi [`AGENTS.md`](AGENTS.md) e [`STATO.md`](STATO.md).\n<!-- fine-riquadro-linee-guida -->\n")
readme = rd('README.md')
if readme is None:
    wr('README.md', f'# {NAME}\n\n' + banner)
else:
    updated = upsert_block(readme, '<!-- inizio-riquadro-linee-guida -->', '<!-- fine-riquadro-linee-guida -->', banner)
    wr('README.md', updated if updated is not None else after_title(readme, banner))

# 5. STATO.md
stato = rd('STATO.md')
if stato is None:
    stato = open(os.path.join(HUB, 'modelli', 'STATO.md'), encoding='utf-8').read().replace('NOME PROGETTO', NAME)
line = f'Segue la versione **{VERSION}** (`LINEE_GUIDA.md`).'
if re.search(r'^## Linee guida\n', stato, re.M):
    stato = re.sub(r'(^## Linee guida\n)(?:\n?Segue la versione \*\*[\d.]+\*\* \(`LINEE_GUIDA\.md`\)\.\n)?', lambda m: m.group(1) + line + '\n', stato, count=1, flags=re.M)
else:
    stato = re.sub(r'^## Registro aggiornamenti', f'## Linee guida\n{line}\n\n## Registro aggiornamenti', stato, count=1, flags=re.M)
wr('STATO.md', stato)

print(f'{NAME}: linee guida {VERSION}; file cambiati: {", ".join(changed) or "nessuno"}')
