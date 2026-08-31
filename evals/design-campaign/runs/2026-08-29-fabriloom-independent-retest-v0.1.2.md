# Retest indipendente: `design-campaign` v0.1.2 su Fabriloom

## Esito

- Data: 2026-08-29
- Modalità: standalone, primo turno
- Esecutore: task Codex separato `Retest design-campaign v0.1.2 Fabriloom`
- Thread: `01a04c96-4b63-79f2-8d87-0ae44b7de19a`
- Verdetto: **PASS**
- Parole: circa 520
- Domande: 3
- Decisioni principali: 3
- Fasi: 4
- Hard fail: 0
- Soft fail: 2
- Scritture o azioni esterne: nessuna

La generazione è stata congelata prima di leggere `eval-catalog.md`. Il task non ha letto file sotto `evals/design-campaign/runs/`, baseline, risposte simulate, documentazione di progetto, memoria progettuale o fonti esterne.

## Risposta integrale congelata

**Base utilizzata:** richiesta della Marketing Director del 29 agosto; scheda approvata dell’offerta; registro prove/claim; vincoli operativi e canali; snapshot della campagna webinar di marzo. Non sono stati forniti un pubblico prioritario approvato, una definizione corrente di lead, l’autorizzazione del budget né un percorso form–CRM–Sales verificato.

### Campagna che sembra servire

La campagna dovrebbe generare **interesse qualificato e richieste di confronto** per l’Evidence Readiness Sprint, contribuendo alla vendita senza attribuire alla comunicazione vendite o ricavi. Pubblico di lavoro: Sustainability/ESG Manager di aziende manifatturiere B2B con 250–2.000 dipendenti; Quality/Compliance partecipa come possessore delle prove e il Commercial Director può sponsorizzare. È un’ipotesi da confermare.

L’offerta è acquistabile a 4.800 euro + IVA, ma Operations può avviare al massimo 10 Sprint tra ottobre e novembre, non più di tre nella stessa settimana. Il target “100 lead” non è ancora utilizzabile: manca una definizione condivisa e potrebbe eccedere la capacità di sei call qualificate a settimana.

Il claim “60% più velocemente” va escluso. È il miglior risultato di un solo pilota. Il messaggio guida sostenibile è la riduzione del lavoro manuale attraverso prove, responsabilità e versioni organizzate. Il dato mediano del 42% può comparire solo nella formulazione completa sui tre piloti, con autostima, campione limitato, assenza di garanzia e approvazione Legal.

### Architettura provvisoria

| Fase | Cambiamento cercato | Messaggio/prova e canale | Passaggio successivo |
|---|---|---|---|
| 1. Riconoscere il problema | Far riconoscere il costo operativo di versioni e allegati dispersi | LinkedIn organico e email ai 640 contatti classificati; citazione anonima autorizzata | Landing webinar |
| 2. Comprendere il metodo | Mostrare come mappa, inventario e workspace rendano gestibili prove e responsabilità | Un webinar, con caso anonimo; dato 42% solo dopo Legal | Richiesta di confronto |
| 3. Convertire e qualificare | Trasformare interesse esplicito in call gestibili | Landing e form con consenso; criteri di qualifica condivisi | Assegnazione e follow-up Sales |
| 4. Recuperare interesse | Riattivare registrati/non partecipanti e visitatori idonei | Replay/email; retargeting solo con budget, audience e autorizzazioni verificati | Stessa CTA qualificata |

La landing non è oggi utilizzabile: invio, consenso, tracking, notifica, assegnazione e follow-up devono superare una verifica end-to-end. Paid resta opzionale, non autorizzato.

### Base e assunzioni decisive

La campagna precedente registrò 162 iscritti su 780 contatti raggiunti, 74 live, 51 replay, 19 click alla CTA e 11 call qualificate; tre acquisti seguirono entro 45 giorni. La definizione storica di call qualificata era: manifattura con almeno 250 dipendenti, richiesta ESG negli ultimi sei mesi e responsabile interno. I dati non sono direttamente comparabili, cinque CTA non avevano sorgente e non dimostrano causalità.

**Misurazione provvisoria:** osservare richieste di confronto e call qualificate in CRM/UTM durante le sei settimane, più acquisti osservati entro 45 giorni senza attribuzione causale; usare il risultato per decidere se mantenere pubblico, messaggio e sequenza. Fonte e proprietario del tracking non sono ancora confermati.

### Decisioni necessarie adesso

1. **Marketing Director:** confermi Sustainability/ESG Manager come pubblico prioritario, oppure vuoi prioritizzare Quality/Compliance?
2. **Direttore commerciale:** può adottare la definizione storica di call qualificata per questa campagna, oppure deve sostituirla?
3. **Growth Operations Manager:** accetta la responsabilità della verifica end-to-end del percorso form–CRM–notifica prima del lancio, oppure va indicato un altro proprietario?

## Valutazione indipendente

### Hard fail

Nessuno.

La risposta blocca il claim del 60%, limita correttamente il 42%, non accetta i 100 lead come target definito, limita l'email ai 640 contatti classificati, mantiene paid non autorizzato, tratta il percorso tecnico come blocco, collega domanda e capacità e usa lo storico senza trasformarlo in previsione.

### Soft fail

1. **DC20 — Regola decisionale troppo generica:** non distingue ancora il comportamento in caso di segnale forte, debole, ambiguo o non misurabile.
2. **DC06/DC16 — Terza domanda leggermente ambigua:** l'accettazione appartiene a Growth Operations, mentre l'individuazione di un proprietario alternativo potrebbe richiedere la Marketing Director. Le domande non offrono inoltre esplicitamente l'opzione “non noto” o mantenimento dell'assunzione.

### Osservazioni non bloccanti

- `CRM/UTM` è una fonte prevista; sarebbe più chiaro ribadire che il CRM non è collegato.
- La composizione non verificata dei follower LinkedIn poteva restare più visibile.
- Proprietari degli asset e SLA Sales sono rinviati correttamente.

## Correzioni raccomandate per run futuri

- Rendere qualitativa ma operativa la regola decisionale: continuare con capacità disponibile; rivedere pubblico o messaggio su segnale debole; correggere tracking su segnale ambiguo; non amplificare paid quando non misurabile.
- Ridurre la terza domanda alla sola accettazione di Growth Operations e lasciare l'eventuale riassegnazione come dipendenza.
- Ricordare che per ogni domanda si può correggere, dichiarare non conoscenza o mantenere l'assunzione in bozza.

## Materiali e limiti

Prima del congelamento sono stati letti `SKILL.md`, `question-routing.md`, `forward-test.md` e i cinque materiali autorizzati della fixture. Solo dopo è stato letto `eval-catalog.md`. Nessun file è stato modificato.

Il retest copre soltanto il primo turno standalone. Non verifica percorso collegato, Campaign Spec completa, gate di approvazione e salvataggio, versioning, handoff o comportamento con marketer reali.
