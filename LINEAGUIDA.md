# LINEA GUIDA — progetti di Gian Paolo Franceschini

**Versione 1.0 · 26/11/2026**

Questo è il primo documento da leggere, per chiunque: Claude, ChatGPT/Codex, Gemini, Copilot,
qualsiasi altro agente o persona che lavora su un repository di Gian.
L'originale vive in `gianpaolobol/registro-delle-idee/LINEAGUIDA.md`. Ogni repository ne tiene una
copia identica, aggiornata in automatico. **Se la copia locale ha un numero di versione più basso
dell'originale, vale l'originale.**

Modifiche: solo con una pull request approvata da Gian, aumentando la versione
(1.0 → 1.1 per aggiunte, 2.0 se cambia una regola) e scrivendo la riga nel **Registro delle versioni** in fondo.

---

## 0. Lo scopo, in una frase

**Creatività libera, esecuzione ordinata.** Le idee di Gian non si limitano: si raccolgono tutte.
Quello che si limita è il numero di progetti su cui si lavora *nello stesso momento*, così che
ogni progetto arrivi davvero al traguardo.

## 1. Le cinque regole d'oro

1. **Ogni idea si scrive, nessuna si perde.** Va nel registro (`IDEE.md`) in meno di un minuto.
   Scriverla non obbliga a farla.
2. **Al massimo 3 progetti attivi.** Un nuovo progetto entra solo se un altro va in pausa o arriva
   al traguardo. Gian può forzare questa regola, ma solo in modo esplicito (vedi §3.4).
3. **Ogni progetto ha un traguardo minimo** deciso prima di iniziare: la prima cosa concreta che
   dimostra che il progetto è "portato a casa" (es. pubblicata sullo store, 10 utenti veri, un cliente pagante).
4. **Prima di scrivere codice, cerca se esiste già** (`COMPONENTI.md`). Si riusa, non si riscrive.
5. **Lo stato è sempre scritto.** Ogni repository ha un `STATO.md` aggiornato: chiunque arrivi,
   persona o agente, sa in un minuto dove siamo e cosa manca.

## 2. Il ciclo di vita di un'idea

```
 lampo ──► idea ──► in incubazione ──► progetto attivo ──► traguardo raggiunto ──► pubblicato
                          │                   │
                          ▼                   ▼
                      archiviata          in pausa  (si riprende quando c'è posto)
```

| Stato | Dove vive | Cosa serve per passare allo stato successivo |
| --- | --- | --- |
| **lampo** | `IDEE.md`, sezione "Lampi" | niente: si scrive e basta, anche una riga dettata |
| **idea** | `IDEE.md`, scheda dell'idea | la scheda compilata (problema, per chi, prima versione) |
| **in incubazione** | `IDEE.md` | ricerca fatta: concorrenti, costi, rischi, componenti riusabili |
| **progetto attivo** | repository dedicato | posto libero tra i 3 attivi + traguardo minimo + decisione di Gian |
| **in pausa** | repository dedicato | `STATO.md` dice dove ci si è fermati e cosa serve per ripartire |
| **traguardo raggiunto** | repository dedicato | il traguardo minimo è verificabile (link, numeri) |
| **pubblicato** | repository dedicato | link pubblici in `STATO.md` |
| **archiviata** | `IDEE.md` o repository archiviato | una riga sul perché (serve a non rifare gli stessi errori) |

Un'idea diventa progetto **solo** su decisione di Gian, scritta nella scheda come
`[Gian] Promossa a progetto — AAAA-MM-GG`. Il nuovo repository nasce dal `modello/` di questo registro.

## 3. Regole per gli agenti

### 3.1 All'inizio di ogni sessione

1. Leggi questa linea guida (copia locale; se sospetti che sia vecchia, l'originale).
2. Nel repository: `STATO.md`, poi `AGENTS.md` (registro degli interventi e note del progetto).
3. Prima di scrivere codice nuovo: `COMPONENTI.md` del registro.
4. Se lavori su più progetti: `PROGETTI.md` del registro.

Se un documento contraddice il codice, **vale il codice**: correggi il documento e segnalalo nel registro degli interventi.

### 3.2 Firme

| Firma | Chi è |
| --- | --- |
| `[Gian]` | il titolare: le sue decisioni prevalgono su tutto |
| `[Claude]` | Claude (Anthropic) |
| `[Codex]` | ChatGPT / Codex (OpenAI) |
| `[Gemini]` | Gemini (Google) |
| `[Copilot]` | GitHub Copilot |
| `[Altro: nome]` | qualsiasi altro agente o persona |

Ogni agente firma sempre quello che aggiunge nei documenti condivisi e nei messaggi di commit.

### 3.3 Si aggiunge, non si riscrive

- Nei documenti condivisi (`AGENTS.md`, `STATO.md`, `IDEE.md`, `PROGETTI.md`, `COMPONENTI.md`)
  **non cancellare e non riformulare** ciò che ha scritto un altro.
- Se qualcosa non vale più, aggiungi una rettifica firmata:
  `[Firma] Rettifica: <cosa> — AAAA-MM-GG` con il motivo.
- Il codice si modifica normalmente, ma con pull request e test (§5).
- Nessun agente cancella file, branch o repository senza una richiesta esplicita di Gian.

### 3.4 Il guardiano del traguardo (la regola anti-dispersione)

Ogni agente fa da guardiano, con gentilezza e senza bloccare:

- **Quando Gian propone una nuova idea:** la registri subito in `IDEE.md` (come lampo o scheda),
  così è al sicuro. Poi, se i progetti attivi sono già 3, lo dici in una riga e chiedi:
  *"La metto in incubazione o vuoi mettere in pausa uno dei progetti attivi?"*
- **Se Gian decide di procedere comunque:** si procede. Si scrive in `PROGETTI.md`
  `[Gian] Deroga: <progetto> attivo oltre il limite — AAAA-MM-GG`. Nessuna discussione ulteriore.
- **Quando un progetto attivo è fermo da più di 14 giorni:** lo segnali alla prima occasione utile.
- **Quando un progetto è vicino al traguardo:** lo dici. Finire viene prima di iniziare.
- **Mai:** rifiutare di registrare un'idea, giudicarla, o ripetere l'avvertimento più di una volta per la stessa idea.

### 3.5 Ruoli tra agenti

- **Autore e revisore sono agenti diversi** quando possibile: chi scrive il codice non si approva da solo.
  Le osservazioni del revisore vanno in una Issue o nella PR (esempio: il revisore indipendente RV-01 di Forgia).
- Un agente può lasciare lavoro a un altro scrivendo in `STATO.md` → "Prossimi passi" con la firma
  del destinatario, es. `[Codex] verificare la build iOS`.

### 3.6 Autonomia

Gian vuole che gli agenti lavorino in autonomia dall'inizio alla fine con gli accessi che concede.
Si chiede solo per: decisioni irreversibili, spese, pubblicazione su store o siti in produzione,
invii a terzi, deroghe a questa linea guida.

### 3.7 Agenti senza accesso al repository

Le chat normali (ChatGPT, Gemini, Claude senza repository collegato) non vedono questi file.
In quel caso Gian può incollare il link di questa linea guida; l'agente la legge e la segue.

## 4. Struttura standard di un repository

```
<repo>/
├── LINEAGUIDA.md          copia sincronizzata di questa linea guida (non modificare a mano)
├── README.md              in cima: "Questo progetto segue la LINEAGUIDA v<x.y>"
├── STATO.md               lo stato in una pagina (§4.2)
├── AGENTS.md              note del progetto per gli agenti + registro degli interventi
├── CLAUDE.md              @LINEAGUIDA.md e @AGENTS.md
├── GEMINI.md              @LINEAGUIDA.md e @AGENTS.md
├── .github/
│   ├── copilot-instructions.md
│   └── workflows/         CI + controllo della linea guida
├── docs/                  decisioni, guide di pubblicazione, ricerche
├── app/                   l'app (web, PWA, mobile)
├── server/                backend (o worker/ se è un Cloudflare Worker)
├── shared/                codice condiviso tra app e server
└── tests/                 test (o accanto al codice, se lo strumento lo richiede)
```

Le cartelle di codice si usano solo se servono. Un progetto senza server non ha `server/`.

### 4.1 File "cartello" per ogni agente

Ogni agente legge da solo un file con un nome preciso. Tutti rimandano a questa linea guida:

| Agente | File letto in automatico | Contenuto |
| --- | --- | --- |
| ChatGPT / Codex | `AGENTS.md` | in cima: "Leggi prima `LINEAGUIDA.md`" |
| Claude | `CLAUDE.md` | `@LINEAGUIDA.md` e `@AGENTS.md` |
| Gemini | `GEMINI.md` (+ `.gemini/settings.json`) | `@LINEAGUIDA.md` e `@AGENTS.md` |
| GitHub Copilot | `.github/copilot-instructions.md` | rimando alla linea guida |
| Persone | `README.md` | riquadro in cima con la versione seguita |

I modelli pronti di questi file sono in `modello/` del registro.

### 4.2 `STATO.md` (massimo una pagina)

Sezioni fisse, in quest'ordine:

1. **Cos'è** — una frase.
2. **Fase** — una tra: `idea`, `in sviluppo`, `test interno`, `beta pubblica`, `pubblicata`, `in pausa`, `archiviata`.
3. **Traguardo minimo** — la prima cosa concreta da raggiungere, e se è raggiunta.
4. **Dove è pubblicata** — link verificabili. Nessun link = non pubblicata.
5. **Prossimi passi** — massimo 5, con la firma di chi li deve fare.
6. **Blocchi** — cosa impedisce di andare avanti e chi deve sbloccarlo.
7. **Componenti condivisi** — cosa usa da altri repository e cosa offre agli altri.
8. **Linea guida** — versione seguita e deroghe in vigore.
9. **Registro aggiornamenti** — `AAAA-MM-GG [Firma] cosa è cambiato`, una riga per intervento, in fondo.

Chi finisce un lavoro aggiorna `STATO.md` nella stessa PR. Se cambia la fase, aggiorna anche `PROGETTI.md` nel registro.

### 4.3 Deroghe

Ogni repository può avere una sezione **Deroghe** in `STATO.md`. Solo Gian le crea:
`[Gian] Deroga: <regola> — <motivo> — AAAA-MM-GG`.
Un agente che pensa serva una deroga la **propone** a Gian, non la scrive.
Esempio tipico: un progetto già maturo (Expo, Capacitor) che tiene il codice in `src/` per non rompere build e pubblicazioni.

## 5. Come si lavora sul codice

- **Branch:** `main` è sempre funzionante. Il lavoro va su branch `<agente>/<argomento>`
  (es. `claude/diario-vocale`, `codex/build-ios`) e entra con una pull request.
- **Commit:** in italiano, al presente, con firma dell'agente nel messaggio.
- **Test:** ogni funzione nuova ha almeno un test; la CI deve essere verde prima di unire.
  Ciò che non si può testare in automatico si prova a mano e si scrive come in `STATO.md`.
- **Segreti:** mai nel repository. Vanno nei segreti di GitHub, Cloudflare o del servizio usato.
  `.env` e simili sempre in `.gitignore`.
- **Sicurezza minima:** input validati sul server, password con hash, niente chiavi nel codice
  del telefono, CORS limitato, dati personali cancellabili dall'utente.
- **Dati personali e voce:** si salva solo ciò che serve; l'utente può cancellare tutto.
- **Lingua:** codice, commenti, documenti e testi dell'app in italiano (altre lingue come traduzioni).
- **Dispositivi di prova di Gian:** iPhone 13 mini (senza LiDAR) e computer Windows: ogni app va provata lì.

## 6. Riuso: il catalogo dei componenti

`COMPONENTI.md` del registro elenca i pezzi già fatti e riusabili (login, pagamenti, dettatura,
generatori IA, visualizzatori 3D, esportazione PDF…), con repository, percorso e stato.

- **Prima di scrivere:** cerca nel catalogo. Se esiste qualcosa di simile, adattalo.
- **Dopo aver scritto qualcosa di riusabile:** aggiungilo al catalogo con una riga firmata.
- **Quando lo stesso pezzo serve in 3 progetti:** si estrae in un pacchetto condiviso
  (una cartella `pacchetti/` nel registro o un repository dedicato), decisione di Gian.

## 7. Il ritmo: la revisione settimanale

Una volta a settimana (anche in automatico, con un'attività pianificata) un agente prepara per Gian
un riepilogo breve:

1. i progetti attivi: cosa è avanzato, cosa è fermo, quanto manca al traguardo;
2. le idee arrivate nella settimana;
3. una proposta: *cosa portare a casa la prossima settimana*.

Gian decide in 5 minuti: cosa promuovere, cosa mettere in pausa, cosa archiviare.

## 8. Sincronizzazione della linea guida

- L'originale è solo qui. Quando cambia, l'automazione `sincronizza-linea-guida` apre in ogni
  repository una pull request con la nuova copia. Gian la approva e il progetto è allineato.
- La CI di ogni repository controlla che i file obbligatori esistano (`modello/.github/workflows/linea-guida.yml`).
- I repository nuovi nascono da `modello/`, quindi sono conformi dal primo giorno.

---

## Registro delle versioni

- **1.0 — 26/11/2026 [Claude]** — Prima versione: regole d'oro, ciclo di vita delle idee,
  limite di 3 progetti attivi con guardiano del traguardo, protocollo comune per gli agenti
  (firme, si aggiunge non si riscrive), struttura standard, `STATO.md`, deroghe, riuso,
  revisione settimanale, sincronizzazione. Da approvare da `[Gian]`; `[Codex]` può proporre
  integrazioni con una PR o in una sezione firmata.
