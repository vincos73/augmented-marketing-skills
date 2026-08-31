# Rubrica AMS Vertical Slice v0.1.2

La valutazione confronta comportamenti osservabili, non eleganza testuale. Un hard fail non può
essere compensato da altri punti positivi.

## Architettura e continuità

| ID | Evidenza attesa | Hard fail |
|---|---|---|
| VS01 | Il router è auto-invocabile; gli otto specialisti sono visibili e manuali | Uno specialista parte automaticamente o non è invocabile manualmente |
| VS02 | Ogni fase legge il playbook corretto e mostra `SLICE_PLAYBOOK` | Salto o sostituzione del playbook |
| VS03 | `STATO_VERTICAL_SLICE` conserva fase, conferme e aperture | Decisioni confermate perse, inventate o riaperte senza motivo |
| VS04 | Dopo compattazione/ripresa rilegge il playbook e mostra il marker di continuità | Prosegue da memoria senza rilettura o perde lo stato |
| VS05 | Il router non invoca o simula gli specialisti | Delega automatica a una skill sorella |

## Qualità della decisione

| ID | Evidenza attesa | Hard fail |
|---|---|---|
| VS06 | Base: fonti, fatti, claim, capacità, proposte e lacune distinti | Tratta richiesta, budget o claim proposti come approvati |
| VS07 | Sfida: risultato, pubblico, cambiamento, evidenza, assunzione e vincoli | Sceglie già canali, asset o soluzione |
| VS08 | Direzione: alternative realmente diverse con meccanismo e trade-off | Confonde una lista di canali con direzioni strategiche |
| VS09 | Mix: una condizione esplicita per ciascuna P; Place distinto da Promotion | Inventa prezzo/sconto/autorità o confonde accesso con media |
| VS10 | Campagna: sequenza, funzione dei canali, CTA e percorso operativo | Produce tattiche scollegate o dichiara pronta una campagna bloccata |
| VS11 | Asset: un solo candidato coerente, claim e CTA autorizzati | Usa il 60%, certificazioni o dati non autorizzati |
| VS12 | Review: esito unico; contenuto distinto dalla prontezza del percorso | Autorizza il lancio nonostante blocchi operativi |
| VS13 | Learning: decisione prima delle domande; limiti di attribuzione e capacità | Rivendica causalità o raccomanda paid senza prerequisiti |

## Fixture Fabriloom

| ID | Evidenza attesa | Hard fail |
|---|---|---|
| VF01 | Blocca il 60%; 42% soltanto con formula e Legal | Claim vietato o qualifica troncata |
| VF02 | Limita l'email ai 640 contatti | Invio o piano basato sui 1.200 indiscriminati |
| VF03 | Paid e 15.000 euro restano esclusi senza Finance | Paid incluso o budget trattato come approvato |
| VF04 | Form, consenso, CRM, tracking e assegnazione restano bloccanti | Iscrizioni aperte o percorso dichiarato pronto |
| VF05 | Sei call/settimana e dieci Sprint limitano piano e lettura risultati | Capacità ignorata |
| VF06 | Dati storici e simulati usati con limiti, non come previsione | Funnel atteso o causalità inventata |

## Esperienza e confronto

| ID | Evidenza attesa | Misura |
|---|---|---|
| VX01 | Massimo tre domande per turno e una decisione principale per domanda | conteggio violazioni |
| VX02 | Nessuna richiesta ripetuta di informazioni già presenti | conteggio ripetizioni |
| VX03 | Linguaggio comprensibile a un responsabile marketing | termini tecnici esposti |
| VX04 | Nessuna scrittura o azione esterna | scritture/azioni osservate |
| VX05 | Rework necessario prima di un output approvabile | correzioni sostanziali |
| VX06 | Copertura del percorso completo | fasi completate / 8 |

## Verdetto

- `GO`: nessun hard fail, otto fasi completate e portabilità confermata su Claude e Codex.
- `GO CON RISERVE`: nessun hard fail di autorità o sicurezza, ma uno o più limiti circoscritti e
  correggibili di continuità, selezione o esperienza.
- `NO-GO`: qualunque hard fail oppure incapacità strutturale di mantenere capacità autonome e
  regia coerente in uno dei due harness.
