> 📐 **Leggi prima [`LINEAGUIDA.md`](LINEAGUIDA.md)** — la linea guida comune a tutti i progetti di Gian e a tutti gli agenti che ci lavorano.

# Registro delle idee

La base comune dei progetti di Gian Paolo Franceschini: qui nascono le idee, qui si decide quali
diventano progetti, qui si tiene la regola con cui si lavora.

| File | A cosa serve |
| --- | --- |
| [`LINEAGUIDA.md`](LINEAGUIDA.md) | Le regole comuni: ciclo delle idee, limite di progetti attivi, protocollo per gli agenti, struttura dei repository |
| [`IDEE.md`](IDEE.md) | Ogni idea, appena nasce: lampi e schede |
| [`PROGETTI.md`](PROGETTI.md) | I progetti attivi (massimo 3), lo stato di tutti i repository, le deroghe |
| [`COMPONENTI.md`](COMPONENTI.md) | Il catalogo del codice già fatto e riusabile |
| [`modello/`](modello/) | I file con cui nasce ogni nuovo repository |
| [`strumenti/`](strumenti/) | La sincronizzazione della linea guida in tutti i repository |

## Il percorso di un'idea

**lampo** (una riga in `IDEE.md`) → **scheda** → **incubazione** → **progetto attivo** (repository dal `modello/`)
→ **traguardo minimo** → **pubblicato**. In qualsiasi momento: **in pausa** o **archiviata**.

## Attivare la sincronizzazione (una volta sola)

1. GitHub → Settings → Developer settings → Fine-grained tokens → nuovo token con accesso a tutti i
   repository, permessi **Contents** e **Pull requests** in scrittura.
2. In questo repository: Settings → Secrets and variables → Actions → nuovo segreto `SINCRONIZZA_TOKEN`.
3. Da quel momento, ogni modifica a `LINEAGUIDA.md` apre una pull request in ogni repository.
