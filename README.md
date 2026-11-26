# Registro delle idee

<!-- inizio-riquadro-linee-guida -->
> **Linee guida v1.1.0** — Questo progetto segue le linee guida comuni dei progetti di Gian Paolo Franceschini: leggi prima [`LINEE_GUIDA.md`](LINEE_GUIDA.md), poi [`AGENTS.md`](AGENTS.md) e [`STATO.md`](STATO.md).
<!-- fine-riquadro-linee-guida -->


Il centro della piattaforma di Gian Paolo Franceschini: le **linee guida** comuni a tutti i progetti, l'automazione che le tiene aggiornate in ogni repository, il registro delle idee e lo stato delle app.

| File | A cosa serve |
|---|---|
| [LINEE_GUIDA.md](LINEE_GUIDA.md) | **L'originale delle linee guida**: flusso idea → progetto, struttura standard, regole di lavoro, protocollo per le AI, deroghe. È il primo documento che ogni persona e ogni AI legge. |
| `REGISTRO_IDEE.md`, `MAPPA_COLLEGAMENTI.md`, `STATO_APP.md` | Registro delle idee, mappa dei componenti riusabili e stato delle app: **pubblicati solo quando il repository sarà privato**. |
| [repository.txt](repository.txt) | I repository che ricevono gli aggiornamenti delle linee guida. |
| [modello-progetto/](modello-progetto/) | Base per i repository nuovi. |
| [modelli/](modelli/) | Modelli per idee, `STATO.md` e sezione comune di `AGENTS.md`. |
| [sincronizzati/](sincronizzati/) e [strumenti/](strumenti/) | File copiati in ogni repository e script di sincronizzazione. |

## Come funziona

- **Nuova idea:** una scheda in `REGISTRO_IDEE.md` (modello `modelli/IDEA.md`).
- **L'idea diventa progetto (decide Gian):** si crea il repository, si copia `modello-progetto/`, si aggiunge il nome a `repository.txt`, si esegue `python3 strumenti/sincronizza.py . <cartella-del-repository> <nome>`.
- **Si aggiornano le linee guida:** si modifica `LINEE_GUIDA.md` (con nuova versione) con una pull request. Una volta integrata, l'automazione apre in ogni repository una pull request di allineamento.
- **Deroghe:** solo Gian, nella sezione `## [Gian] Deroghe alle linee guida` dell'`AGENTS.md` del repository.

## Configurazione una tantum

L'automazione usa il segreto `LINEE_GUIDA_TOKEN`: un token GitHub *fine-grained* con accesso ai repository di `repository.txt` e permessi **Contents**, **Pull requests** e **Workflows** in lettura e scrittura (Workflows serve perché la sincronizzazione aggiorna anche il controllo automatico) (Settings → Secrets and variables → Actions).
