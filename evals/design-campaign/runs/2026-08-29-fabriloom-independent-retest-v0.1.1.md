# Retest indipendente: `design-campaign` v0.1.1 su Fabriloom

## Esito

- Data: 2026-08-29
- Modalità: standalone, primo turno
- Esecutore: task Codex separato `Retest design-campaign v0.1.1 Fabriloom`
- Thread: `01a04c91-b0f5-7743-8a2c-2b0f7b45ce80`
- Verdetto: **FAIL**
- Parole: circa 579
- Domande: 3
- Fasi: 4
- Hard fail: 1
- Soft fail: 2
- Scritture o azioni esterne: nessuna

La generazione è stata congelata prima di leggere `eval-catalog.md`. Il task non ha letto file sotto `evals/design-campaign/runs/`, baseline, risposte simulate, README della fixture, memoria progettuale o fonti esterne.

## Risposta integrale congelata

Base utilizzata: richiesta della Marketing Director del 29 agosto, scheda approvata dell’offerta, registro prove e claim, vincoli operativi/canali e snapshot della campagna webinar di marzo. La landing e il percorso CRM non sono pronti; pubblico prioritario, definizione di lead e responsabilità di handoff non sono ancora concordati. Budget paid, relatrice e claim quantitativo non sono autorizzati per l’uso pubblico.

### Campagna che sembra servire

Il risultato aziendale è contribuire a vendere l’**Evidence Readiness Sprint** da 4.800 euro + IVA, entro una capacità massima di 10 Sprint tra ottobre e novembre. L’obiettivo di campagna, distinto dalle vendite, dovrebbe essere creare comprensione e fiducia presso aziende manifatturiere B2B da 250 a 2.000 dipendenti e portare interlocutori pertinenti a richiedere un confronto qualificabile.

Come ipotesi reversibile, userei Sustainability/ESG Manager come pubblico primario, Quality/Compliance come co-proprietari delle prove e Commercial Director come sponsor. “100 lead” resta un’aspirazione finché non definiamo l’evento e la qualità: Sales può gestire al massimo 6 call qualificate a settimana e una call non riserva uno slot.

### Architettura provvisoria

| Fase | Cambiamento cercato | Messaggio/prova e ruolo dei canali | Passaggio successivo |
|---|---|---|---|
| 1. Riconoscere il problema | Far riconoscere il costo operativo di versioni, allegati e responsabilità disperse | LinkedIn organico, con un carousel massimo, e email solo ai 640 contatti con tag affidabile. Claim ordinario approvato sul minor lavoro manuale; nessun “60% più veloce” | Iscrizione al webinar o interesse per la pagina, solo quando destinazioni e consenso sono verificati |
| 2. Capire e fidarsi | Mostrare come si organizza l’evidence readiness senza promettere conformità | Un webinar, titolo proposto confermabile, con demo del metodo e citazione anonima autorizzata. Il 42% può apparire soltanto nella formulazione completa, con limiti e approvazione Legal; altrimenti si omette | Accesso alla registrazione e invito a valutare lo Sprint |
| 3. Esprimere intenzione | Trasformare interesse qualificato in richiesta esplicita | Landing essenziale con offerta, prezzo, inclusioni/esclusioni e CTA “richiedi un confronto”. Retargeting solo come modulo opzionale dopo autorizzazione Finance, audience verificata e percorso funzionante | Form con consenso specifico e notifica |
| 4. Qualificare e seguire | Capire pertinenza e capacità, non massimizzare nominativi | CRM, assegnazione e follow-up Sales; priorità a manifattura 250–2.000 dipendenti con richiesta recente e responsabile interno | Call qualificata, verifica disponibilità e possibile avvio dello Sprint |

### Base, assunzioni e dipendenze decisive

La campagna precedente ha registrato 780 contatti raggiunti, 162 iscrizioni, 74 presenze live, 51 visualizzazioni entro 14 giorni, 19 richieste di confronto, 11 call qualificate e 3 acquisti entro 45 giorni. “Qualificata” significava manifattura con almeno 250 dipendenti, richiesta ESG negli ultimi sei mesi e responsabile interno. Pubblico e offerta erano diversi, cinque richieste non avevano sorgente attribuibile e non c’è prova causale: sono dati per progettare definizioni e capacità, non una previsione.

Per partire tra due settimane sono blocchi di esecuzione: proprietario Growth Operations, test end-to-end di form/consenso/tracking/notifica, regola di assegnazione e tempo di follow-up. Restano inoltre da confermare relatrice e revisione Legal. Paid resta fuori dal percorso base finché Finance non autorizza importo e allocazione.

### Decisioni necessarie adesso

1. Confermi Sustainability/ESG Manager come pubblico primario, oppure la priorità deve essere Quality/Compliance o lo sponsor commerciale?
2. Possiamo adottare provvisoriamente la precedente definizione di call qualificata come definizione di lead utile alla campagna, oppure Sales richiede criteri diversi?
3. Chi può accettare formalmente la responsabilità del percorso landing → CRM → assegnazione → follow-up e definire il tempo massimo di presa in carico?

## Valutazione indipendente

### Hard fail

- **DC06 — Routing delle domande:** la domanda 3 accorpa proprietà tecnica di landing/form/tracking/CRM, proprietà del passaggio Sales e SLA. La correzione della v0.1.1 nel riferimento non è risultata abbastanza saliente da cambiare il comportamento.

### Soft fail

- **DC18 — Misurazione:** i dati storici sono riportati correttamente, ma manca un piano minimo della nuova campagna con eventi, fonti, finestra e proprietario.
- **DC20 — Regole decisionali:** non sono indicate le decisioni conseguenti a segnali forti, deboli, ambigui o non misurabili.

### Evidenze positive

- Rispetta il tetto di 600 parole e offre valore prima delle domande.
- Distingue risultato aziendale, obiettivo influenzabile, capacità e target.
- Riporta lo storico con definizioni e limiti, senza trasformarlo in previsione.
- Blocca il 60%, condiziona il 42% a formula completa e Legal, limita l'email ai 640 contatti classificati e mantiene paid subordinato a Finance.
- Riconosce i blocchi tecnici e non dichiara la campagna pronta.

## Correzione raccomandata

Rendere il controllo decisione-proprietario esplicito e saliente nel flusso principale della skill, non soltanto nel riferimento. La domanda tecnica deve riguardare Growth Operations; assegnazione e SLA Sales devono restare blocchi visibili da affrontare separatamente.

## Materiali e limiti

Prima del congelamento sono stati letti `SKILL.md`, `question-routing.md`, `forward-test.md` e i cinque materiali autorizzati della fixture. Solo dopo è stato letto `eval-catalog.md`. Nessun file è stato modificato.

Il retest copre soltanto il primo turno standalone. Non verifica il percorso multi-turn, la Campaign Spec finale, handoff, packaging o comportamento con marketer reali.
