# Forward test indipendente: `design-campaign` v0.1.0 su Fabriloom

## Esito

- Data: 2026-08-29
- Modalità: standalone, primo turno
- Esecutore: task Codex separato `Forward test design-campaign Fabriloom`
- Thread: `01a04c8c-5ba0-70d1-af5f-673a219a74f9`
- Verdetto: **FAIL**
- Parole: circa 592
- Domande: 3
- Fasi: 4
- Hard fail: 1
- Soft fail: 2
- Scritture o azioni esterne: nessuna

La generazione è stata congelata prima di leggere `eval-catalog.md`. Il task non ha letto `user-answers.md`, `expected-run.md`, `expected-campaign-spec.md`, il self-check dell'autore, il README della fixture, il template della Campaign Spec, memoria progettuale o fonti esterne.

## Risposta integrale congelata

Base utilizzata: richiesta della Marketing Director del 29 agosto; scheda interna approvata dell'offerta; registro claim del 27 agosto; vincoli operativi e canali del 28 agosto; snapshot della campagna di marzo. Identity, Foundations e artefatti Strategy non sono stati forniti né consultati. Questo è un dry test: nessun canale, dato o sistema è stato attivato o verificato.

### Campagna che sembra servire

Una campagna B2B concentrata sulle aziende manifatturiere da 250 a 2.000 dipendenti che ricevono questionari ESG o di conformità, con un primo pubblico operativo ancora da scegliere tra Sustainability/ESG e Quality/Compliance. Il cambiamento influenzabile non è “generare 100 lead” in astratto, ma far riconoscere il costo della frammentazione, rendere credibile un modo più ordinato di lavorare e portare le aziende compatibili a richiedere un confronto qualificato sull’Evidence Readiness Sprint.

Il risultato aziendale a cui contribuire è occupare in modo sostenibile fino a 10 Sprint tra ottobre e novembre; non è una promessa attribuibile alla campagna. Il limite principale è oggi il percorso dopo la CTA: landing, form, consenso, CRM, assegnazione e follow-up non sono pronti end-to-end.

### Architettura provvisoria

| Fase | Cambiamento cercato e messaggio/prova | Ruolo del canale | Passaggio successivo |
|---|---|---|---|
| 1. Riconoscimento mirato | Far riconoscere il problema: prove, versioni e responsabilità disperse rallentano le risposte. Usare la testimonianza anonima autorizzata. | Email solo ai 640 contatti classificati; LinkedIn organico per esplorare risposta e linguaggio, senza presumere la composizione dei follower. | Registrazione al webinar con consenso e informativa verificati. |
| 2. Comprensione e fiducia | Webinar “Rispondere ai questionari ESG senza inseguire fogli di calcolo”: mostrare metodo, limiti e Sprint. Claim guida qualitativo approvato. Il dato mediano del 42% è opzionale solo con formulazione completa e approvazione Legal; il 60% è escluso. | Webinar unico, con relatrice da confermare; registrazione riutilizzabile. | CTA a una richiesta di confronto, non a uno slot garantito. |
| 3. Riattivazione selettiva | Ricordare problema, prova e offerta a chi ha mostrato interesse. | Follow-up email nei limiti del consenso. Retargeting solo come modulo condizionale dopo autorizzazione Finance, verifica audience e approvazione operativa. | Landing e form testati, quindi qualificazione. |
| 4. Qualificazione e capacità | Verificare compatibilità con segmento, richiesta recente e presenza di un responsabile interno; chiarire prezzo di 4.800 euro + IVA e confini dell'offerta. | CRM e Sales, solo dopo assegnazione e SLA concordati. | Call qualificata; pianificazione degli Sprint nel limite di 10 e massimo tre avvii settimanali. |

### Base e assunzioni decisive

- Il precedente webinar orienta definizioni e capacità, ma non permette previsioni: pubblico e offerta non sono comparabili e l’attribuzione era incompleta.
- “100 lead” resta un’aspirazione finché non definiamo l’evento e la baseline; registrazioni, richieste di confronto, call qualificate e acquisti sono outcome diversi.
- La capacità Sales è 36 call qualificate in sei settimane: la campagna deve filtrare e distribuire la domanda, non massimizzare volume indistinto.
- Il budget di 15.000 euro, la relatrice, Growth Operations e ogni uso paid restano non autorizzati o non assegnati.
- Obiettivo di apprendimento iniziale: capire quale pubblico e messaggio producono richieste compatibili, con sorgente tracciabile, senza attribuire causalità alle vendite.

### Decisioni necessarie adesso

1. Confermiamo come pubblico primario Sustainability/ESG Manager, con Quality/Compliance come co-influente, oppure la priorità deve essere invertita?
2. Possiamo definire il risultato principale come “richiesta di confronto qualificabile” e mantenere registrazione e partecipazione come segnali intermedi, oppure “lead” deve indicare un altro evento?
3. Chi può assumere formalmente il percorso landing–form–CRM e quale regola di assegnazione e tempo massimo di follow-up può impegnare Sales?

## Valutazione indipendente

### Hard fail

- **DC06 — Routing delle domande:** la domanda 3 accorpa la responsabilità di landing–form–CRM, attribuibile a Growth Operations, e regola di assegnazione/SLA, attribuibile a Sales. Sono due decisioni principali con proprietari differenti.

### Soft fail

- **DC07/DC08 — Risultato e target:** la capacità massima di dieci Sprint viene trasformata in un risultato aziendale non confermato. È formulata prudentemente, ma dovrebbe restare un vincolo o un'ipotesi da confermare.
- **DC18/DC20/FDC07 — Misurazione e storico:** i dati precedenti sono trattati con prudenza, ma i valori disponibili `162/74/51/19/11/3` non sono riportati; fonte, finestra e decisione conseguente dell'obiettivo di apprendimento restano generiche.

### Evidenze positive

- Offre valore prima delle domande e resta entro il tetto di 600 parole.
- Non accetta “100 lead” come target definito e distingue gli eventi del funnel.
- Blocca il claim del 60% e mantiene il 42% subordinato a formula completa e Legal.
- Limita l'email ai 640 contatti classificati.
- Mantiene paid e 15.000 euro condizionati all'autorizzazione Finance.
- Riconosce il blocco landing/form/CRM e collega domanda, 36 call e capacità di dieci Sprint.
- Costruisce la sequenza problema → prova/webinar → richiesta → qualifica.
- Non assegna budget, non attiva sistemi e non dichiara la campagna pronta.

## Correzioni raccomandate

1. Fare in modo che ogni domanda abbia una decisione principale e un solo proprietario; mantenere le altre dipendenze come blocchi visibili per il turno successivo.
2. Trattare la capacità massima come vincolo e non come risultato desiderato finché non confermato.
3. Quando i dati storici cambiano una decisione, riportarne i valori essenziali, la fonte e i limiti.

## Materiali letti

Prima del congelamento:

- `skills/design-campaign/SKILL.md`
- `skills/design-campaign/references/question-routing.md`
- `evals/design-campaign/fixtures/fabriloom-standalone/forward-test.md`
- `manager-request.md`
- `offer-brief.md`
- `evidence-and-claims.md`
- `operations-and-channels.md`
- `prior-campaign-snapshot.md`

Dopo il congelamento:

- `evals/design-campaign/eval-catalog.md`

## Limiti

Questo test copre solo il primo turno standalone della sorgente non installata. Non verifica percorso multi-turn, Campaign Spec finale, handoff ai builder, packaging o comportamento con marketer reali.
