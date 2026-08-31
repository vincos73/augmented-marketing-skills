# Forward test indipendente: Brightpath pre-lancio

- Data: 2026-08-31
- Skill osservata: `campaign-review` v0.1.1
- Modello valutatore: `gpt-5.6-sol`, reasoning high
- Modalità: standalone, review completa
- Oracolo dell'autore: non fornito al valutatore e separato dalla directory degli input
- Azioni autorizzate: sola lettura; nessuna correzione, scrittura canonica o azione esterna

## Materiali letti

`user-request.md`, `campaign-spec.md`, `asset-linkedin.md`, `asset-email.md`, `evidence-register.md` e `operations-readiness.md` dalla fixture `brightpath-prelaunch`. Non sono stati letti `README.md` o il contenuto di `evals/campaign-review/oracles/`.

## Prima risposta prodotta dal valutatore

Esito provvisorio: **bloccata**. Oggi non è sostenibile pubblicare il post LinkedIn né inviare l'email.

Base utilizzata: Campaign Spec v2 approvata, asset LinkedIn v3, email v2, registro prove e stato operativo dichiarato del 30 agosto 2026. Nessun test live è stato osservato. Review completa.

### Coerenza strategica

Il percorso e le CTA sono coerenti. L'email, però, include tutti i 1.200 contatti B2B, mentre la Campaign Spec limita l'invio ai contatti con consenso e tag Operations. E3 ne documenta 640. Responsabile: Luca Serra. Chiusura: segmento limitato e verificato.

### Integrità delle affermazioni

I claim “riduzione del 60%” e “otto ore ogni settimana” non sono utilizzabili. E1 sostiene soltanto una mediana del 42% su 20 account selezionati, non misura le otto ore e attende verifica Legal per l'uso esterno. E2 non è autorizzata. Responsabili: Marta Riva per gli asset; referente Legal da confermare. Chiusura: rimozione dei claim oppure prova pertinente e autorizzazione osservata.

### Prontezza del sistema

Pagina e form sono solo dichiarati; tracking non collegato; assegnazione e SLA Sales non confermati; follow-up non documentato; invio email non autorizzato. Responsabili: Luca Serra per il percorso operativo, Sales e referente tecnico da confermare, Marta Riva per l'autorizzazione. Chiusura: prove dei test, collegamento tracking, ownership del follow-up e autorizzazione registrata.

## Valutazione

- Esito: `bloccata`
- Hard fail: sì, claim non sostenuti, pubblico email incompatibile, invio non autorizzato e dipendenze operative essenziali non verificate.
- Soft fail: nessuno determinante oltre ai blocchi; resta da dimostrare che il follow-up rispetti la capacità massima di sei assessment settimanali.
- Osservazioni: LinkedIn organico ed email sono nel perimetro. Lo scenario paid media da 15.000 euro è escluso e non incide sull'esito.
- Effetti osservati: nessun file modificato e nessuna azione esterna eseguita.

## Esito del run

PASS sui controlli prioritari della fixture: tre lenti separate, esito prudente, claim limitati, segmento non ampliato, dipendenze non verificate dichiarate, responsabili non inventati e paid media escluso. Il run non equivale a un pilot con marketer esterni.
