# Baseline del contenuto della Campaign Spec

Questo documento mostra il contenuto sostanziale atteso dopo le risposte simulate. Non è un artefatto canonico, non assegna uno stato osservabile su disco e non deve essere fornito al generatore o al valutatore indipendente.

Esito simulato:

> contenuto approvato in chat; artefatto non creato

## Base utilizzata

| ID | Fonte | Cosa sostiene | Limiti |
|---|---|---|---|
| S1 | Richiesta della Marketing Director, 29 agosto 2026 | esigenza, ipotesi iniziale di canali, target e budget proposti | target, claim e budget non approvati |
| S2 | Scheda Evidence Readiness Sprint, 24 agosto 2026 | offerta, prezzo, ruoli, capacità ed esclusioni | pubblico prioritario non deciso |
| S3 | Registro prove e claim, 27 agosto 2026 | claim qualitativo, dato mediano, limiti e formulazioni vietate | campione di tre piloti, misura dichiarata |
| S4 | Vincoli operativi e canali, 28 agosto 2026 | capacità, disponibilità dei canali, conversione, privacy e autorizzazioni | alcuni proprietari e sistemi non confermati |
| S5 | Snapshot webinar di marzo 2026 | definizioni e ordine di grandezza storico | pubblico e offerta non pienamente comparabili; nessuna causalità dimostrata |

Non sono stati forniti Business Identity, Marketing Foundations o artefatti Strategy. La base della singola campagna è stata confermata dalla Marketing Director nelle risposte simulate `[C]`.

## Contratto della campagna

- **Esigenza:** lanciare l'Evidence Readiness Sprint con una campagna di sei settimane.
- **Contributo aziendale:** generare opportunità compatibili con i dieci Sprint disponibili in ottobre-novembre `[S2]`.
- **Obiettivo di campagna:** ottenere 20 richieste di confronto qualificate `[C]`; è un target di pianificazione, non una previsione garantita.
- **Pubblico prioritario:** Sustainability, ESG, Quality o Compliance Manager di aziende manifatturiere B2B italiane con 250–2.000 dipendenti e richieste ESG ricevute da clienti corporate negli ultimi sei mesi `[C; S2]`.
- **Sponsor secondario:** Commercial Director quando gare o clienti strategici rendono urgente il problema `[C; S2]`.
- **Ostacolo:** prove disperse, responsabilità non chiare e difficoltà a riutilizzare versioni affidabili `[S2; S3]`.
- **Azione attesa:** richiedere un confronto sull'Evidence Readiness Sprint a pagamento.
- **Esclusi:** consulenti, grandi gruppi oltre 2.000 dipendenti, aziende senza richieste attive e paid media nella v1 `[C]`.

## Tesi della campagna

Fabriloom deve rendere riconoscibile il costo operativo della preparazione frammentata, mostrare un metodo concreto per organizzare prove e responsabilità e invitare le aziende pertinenti a valutare uno Sprint limitato e a pagamento.

Assunzione più fragile: i responsabili destinatari riconoscono il problema come sufficientemente urgente da partecipare al webinar e richiedere un confronto.

Questa spec non decide una strategia aziendale generale, un nuovo segmento, sconti, paid media o modifiche dell'offerta.

## Architettura owned-first

| Fase | Cambiamento cercato | Messaggio/prova | Canale e funzione | Passaggio successivo | Segnale |
|---|---|---|---|---|---|
| 1. Riconoscimento | Rendere visibile il costo delle prove frammentate | Problema operativo e citazione anonima autorizzata `[S3]` | LinkedIn organico per raggiungere e far riconoscere il problema | Interesse verso il metodo | Interazioni qualificate e visite tracciate |
| 2. Invito qualificato | Portare il pubblico pertinente all'approfondimento | Webinar sul metodo, senza claim del 60% | Email ai 640 contatti classificati e LinkedIn per invitare | Registrazione con consenso verificato | Registrazioni pertinenti per ruolo e azienda |
| 3. Comprensione e prova | Mostrare processo, limiti e prova disponibile | Claim qualitativo; 42% soltanto con formula completa e approvazione Legal | Webinar per spiegare, dimostrare e rispondere alle obiezioni | CTA allo Sprint | Partecipazione, domande e click CTA |
| 4. Richiesta e qualificazione | Trasformare interesse in confronto valutabile | Offerta corrente, prezzo ed esclusioni `[S2]` | Landing e form per raccogliere la richiesta minima autorizzata | Assegnazione a Sales | Richieste complete e tracciate |
| 5. Follow-up | Verificare fit e capacità | Criteri di qualifica confermati `[C]` | Sales entro due giorni lavorativi | Proposta di Sprint o chiusura motivata | Call qualificate e relativo esito |

## Sistema di messaggi e prove

### Messaggio guida

Fabriloom aiuta i fornitori industriali a ridurre il lavoro manuale necessario per preparare le risposte ai questionari dei clienti, organizzando prove, responsabilità e versioni in un workspace condiviso `[S3]`.

### Regole

| Elemento | Uso | Stato |
|---|---|---|
| Claim qualitativo approvato | LinkedIn, email, landing e webinar | utilizzabile `[S3]` |
| Mediana del 42% nei tre piloti | Solo landing e webinar con formulazione completa | bloccato fino all'approvazione Legal `[C; S3]` |
| “60% più velocemente” | Nessun uso | vietato `[C; S3]` |
| Citazione anonima | Contenuti e webinar senza cliente, logo o settore | utilizzabile nei limiti autorizzati `[S3]` |
| Certificazione ISO 27001 | Nessun uso | non supportata `[S3]` |

## Canali e asset minimi

| ID | Asset | Funzione | Canale/fase | Proprietario | Handoff | Stato |
|---|---|---|---|---|---|---|
| A1 | Carousel LinkedIn | Rendere riconoscibile il problema e introdurre il metodo | LinkedIn, fase 1 | Content Specialist | builder carousel con fonti, claim consentiti e CTA | brief da preparare |
| A2 | Famiglia invito e reminder | Invitare soltanto i contatti classificati | Email, fase 2 | Content Specialist | workflow email | dipende da segmentazione e consenso |
| A3 | Landing e form | Spiegare offerta e raccogliere richieste | Conversione, fasi 2-4 | designer + Growth Operations | design/copy + configurazione tecnica separati | blocco di esecuzione |
| A4 | Deck webinar | Spiegare metodo, prova e limiti | Webinar, fase 3 | Head of Customer Success + Marketing | builder presentazione | dipende da relatrice e Legal |
| A5 | Sales qualification brief | Applicare una definizione uniforme e il follow-up | Sales, fase 5 | Sales Director | documento operativo | da approvare |

La spec non decide numero di slide, composizione grafica, copy finale, configurazione email o impostazioni delle piattaforme.

## Percorso di risposta

- CTA: richiedere un confronto sull'Evidence Readiness Sprint.
- Destinazione: landing e form dedicati.
- Dati minimi: nome, email business, azienda, ruolo e scelta di follow-up nei limiti dell'informativa `[S4]`.
- Assegnazione: CRM a Sales secondo regola da configurare.
- Follow-up: entro due giorni lavorativi `[C]`.
- Capacità: sei call qualificate a settimana e dieci Sprint disponibili `[C; S2; S4]`.
- Stop: non aprire le iscrizioni finché form, consenso, tracking, notifica e assegnazione non superano un test end-to-end `[C; S4]`.

## Misurazione

Domanda: la sequenza owned-first genera richieste di confronto qualificate compatibili con il pubblico e la capacità dell'offerta?

| Segnale | Definizione | Fonte | Confronto | Limite |
|---|---|---|---|---|
| Registrazione pertinente | registrazione appartenente ai ruoli e alle aziende nel perimetro | form/CRM | campagna precedente solo come ordine di grandezza | tracking da verificare |
| Partecipazione e click CTA | eventi definiti sulla piattaforma webinar e landing | webinar + analytics | dati storici disponibili | non equivalgono a domanda qualificata |
| Richiesta qualificata | criteri confermati nelle risposte simulate | CRM + Sales | precedente campagna: 11 call qualificate | pubblico e offerta non equivalenti |
| Sprint avviato | contratto confermato e avvio registrato | Sales/Operations | precedente campagna: 3 acquisti entro 45 giorni | nessuna attribuzione causale automatica |

Regola decisionale proposta:

- se le richieste pertinenti arrivano ma poche diventano qualificate, verificare promessa, criteri e landing prima di aumentare la distribuzione;
- se la partecipazione è buona ma la CTA è debole, rivedere prova, offerta e passaggio al confronto;
- se form o tracking non funzionano, sospendere l'apertura e correggere la misura;
- non scalare con paid media finché percorso e definizioni non sono affidabili e Finance non autorizza la spesa.

## Blocchi e approvazioni

| Tema | Stato | Proprietario | Condizione |
|---|---|---|---|
| Form, consenso, CRM, tracking e assegnazione | bloccante per l'esecuzione | Growth Operations | responsabilità accettata e test end-to-end superato |
| Disponibilità relatrice | bloccante per il webinar | Head of Customer Success | conferma della data |
| Claim quantitativo del 42% | bloccante per quel claim, non per la campagna qualitativa | Legal | copy completo approvato |
| Follow-up e qualifica | bloccante per l'esecuzione | Sales Director | criteri e SLA accettati |
| Paid media | fuori perimetro v1 | Finance | nuova decisione e autorizzazione separata |

La Marketing Director approva il contenuto della spec e accetta questi blocchi. Non autorizza salvataggio canonico, produzione, invio, pubblicazione, spesa o configurazione.

## Handoff

- primo brief consigliato: A1, carousel LinkedIn;
- review della campagna: completa prima dell'apertura, perché esistono claim quantitativi, trattamento dati, CRM e più handoff;
- condizione per il learning: definizioni e tracking verificati prima della raccolta dei risultati.
