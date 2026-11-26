# Catalogo dei componenti riusabili

Prima di scrivere codice nuovo, cerca qui (`LINEAGUIDA.md` §6).
Dopo aver scritto qualcosa di riusabile, aggiungilo con una riga firmata.
Stato: `pronto` (testato e in uso), `da estrarre` (funziona ma è legato al progetto), `da verificare`.

| Componente | Cosa fa | Repository · percorso | Tecnologia | Stato | Firma |
| --- | --- | --- | --- | --- | --- |
| Account e sessioni | Registrazione, accesso, PBKDF2, token di sessione con hash, freno ai tentativi, cancellazione GDPR | `penna-viva` · `worker/src/auth.js` | Cloudflare Worker + D1 | da estrarre | [Claude] |
| Coda lavori IA multi-fornitore | Lavori IA in coda, catena Gemini → OpenRouter con riserva, tetto di spesa giornaliero e quota per utente | `penna-viva` · `worker/src/jobs.js`, `providers.js` | Worker + D1 | da estrarre | [Claude] |
| Validazione JSON dai modelli | Ripulisce e valida le risposte JSON dei modelli | `penna-viva` · `shared/parse.js` | JS puro | pronto | [Claude] |
| Dettatura vocale | Dettatura in italiano con Web Speech API, testo provvisorio e definitivo | `penna-viva` · `app/src/voce.js`, `CampoVoce` in `componenti.jsx` | Browser / Preact | pronto | [Claude] |
| Accedi con OpenRouter | OAuth PKCE: l'utente collega il proprio account IA | `penna-viva` · `app/src/openrouter.js` | Browser | pronto | [Claude] |
| Immagini da condividere | Card 1080×1350 disegnate sul telefono + foglio di condivisione | `penna-viva` · `app/src/condividi.js` | Canvas | pronto | [Claude] |
| Pagina pubblica condivisibile | Pagina HTML con anteprima social e invito "crea il tuo" | `penna-viva` · `worker/src/pagina.js` | Worker | da estrarre | [Claude] |
| Sicurezza PHP | Funzioni di sicurezza comuni del sito | `stampa3dbologna` · `includes/security.php` | PHP | da verificare | [Claude] |
| Pagamenti PHP | Logica comune dei pagamenti | `stampa3dbologna` · `payment_common.php` | PHP | da verificare | [Claude] |
| Generatore modelli 3D con IA | Integrazione Meshy con webhook firmato | `stampa3dbologna` · `meshy_webhook.php` | PHP | da verificare | [Claude] |
| Proxy modelli 3D | Ricerca/proxy di modelli compatibili | `reborn` / `stampa3dbologna` · `reborn_model_proxy.php` | PHP | da verificare | [Claude] |
| CLI per software tecnici | CLI verificate per Blender, FreeCAD, 3MF, CloudCompare, Inkscape, LibreOffice | CLI-Anything (HKUDS) | Python | da verificare | [Claude] |

## Candidati a pacchetto condiviso

Quando un componente serve in 3 progetti si estrae (decisione di Gian).

- **Account + coda IA + tetto di spesa** (Penna Viva) → probabile base comune per tutte le app con IA. `[Claude]`
