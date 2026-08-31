# Referto di prontezza pre-produzione AMS

Data: 31 agosto 2026

## Sintesi per decisione

Il confronto richiesto è completo su Codex e Claude. CURRENT si ferma a 4 fasi su 8 su entrambi
gli harness perché il bundle pubblicato non contiene le capacità di campagna, asset, review e
apprendimento. L'arresto evita simulazioni e protegge i vincoli, ma non offre un percorso di
prodotto completo né un vantaggio end-to-end rispetto al generalista.

La Vertical Slice supera il GENERALIST su Codex per governance decisionale e minore rework. Su
Claude la classifica si inverte di poco: il GENERALIST completa il percorso e corregge in review
alcuni propri errori, mentre la Vertical Slice è più leggibile ma non rileva un claim inventato.
Entrambi producono conclusioni causali non sostenute dai risultati sintetici. Il vantaggio della
Vertical Slice sul generalista non è quindi stabile tra harness.

## Evidenze riutilizzate

- Vertical Slice v0.1.2 completa su Codex e Claude;
- router e specialisti manuali verificati;
- continuità dopo ripresa e compattazione verificata;
- sorgenti, bundle e hash verificati;
- referto precedente `GO CON RISERVE` mantenuto immutato.

Non è stata eseguita una nuova Vertical Slice: esistono già risposte complete con gli stessi
materiali, compito e condizioni. Il limite del modello Codex resta dichiarato invece di produrre
automaticamente una nuova baseline.

## Nuove evidenze

| Harness | CURRENT | GENERALIST | Confronto cieco |
|---|---|---|---|
| Codex | completo, 4/8 e arresto controllato | completo, 8/8 | completo |
| Claude | completo, 4/8 e arresto controllato | completo, 8/8 | completo |

## Lettura complessiva

### Vertical Slice

- 8/8 fasi;
- migliore candidato su Codex e secondo, di poco, su Claude;
- vantaggio osservabile su governance decisionale nel run Codex;
- nel nuovo blind Claude presenta un claim quantitativo inventato nell'asset e conclusioni causali
  eccessive nell'apprendimento;
- il precedente `GO CON RISERVE` resta un'evidenza congelata, non una prova di readiness della
  Suite CURRENT.

### CURRENT

- 4/8 fasi;
- hard fail strutturale di copertura su entrambi gli harness;
- invocazioni tecniche e handoff manuale nel percorso;
- nessun vantaggio end-to-end rispetto al generalista;
- alta correttezza nelle quattro fasi disponibili;
- non richiede una semplice correzione editoriale, ma capacità aggiuntive e orchestrazione.

### GENERALIST

- 8/8 fasi su entrambi gli harness;
- competitivo con la Vertical Slice, primo nel blind Claude e secondo nel blind Codex;
- nel run Claude inventa elementi empirici nell'asset, poi li rileva in review senza emettere una
  versione corretta;
- nell'apprendimento Claude commette un errore numerico e trae conclusioni causali eccessive;
- richiede rework alto sul run Claude e medio sul run Codex.

## Vantaggio provato e vantaggio non provato

È provato che CURRENT, nella configurazione pubblicata, non completa il percorso e non supera il
GENERALIST su nessuno dei due harness. È inoltre provato che la Vertical Slice può migliorare la
governance su Codex, ma non mantiene lo stesso vantaggio relativo su Claude.

Non è provato che:

- il vantaggio sia stabile tra run;
- marketer reali lo percepiscano o lavorino meglio;
- il tempo reale risparmiato sia positivo;
- la Suite sia pronta per una release pubblica.

Non vengono presentate stime del modello come tempo risparmiato.

## Azioni richieste

1. Non pubblicare come Suite completa il bundle CURRENT beta.8.
2. Mantenere il pilot già avviato sul solo Strategy Core come percorso separato, congelando
   protocollo, profilo dei marketer, osservazioni e incidenti prima di usarli come evidenza.
3. Integrare nel bundle almeno Campaign Core e un'orchestrazione capace di trasferire lo stato
   senza far ripetere contesto e decisioni.
4. Correggere nei metodi la scelta prematura della soluzione, i claim empirici non supportati e
   il passaggio da correlazione a causalità nell'apprendimento.
5. Rendere Content Core realmente disponibile prima di presentare l'offerta come suite completa
   di Strategy, Campaign e Content.
6. Dopo il redesign, rieseguire una prova matched per candidato e harness. Aggiungere repliche
   solo se allora il risultato resta ambiguo o molto variabile.
7. Usare `MARKETER-PILOT-RUNBOOK.md` per una successiva prova osservata dell'intero percorso, non
   come sostituto delle capacità mancanti.

Confidenza sul giudizio che CURRENT non sia pronto come Suite completa: **oltre 95%**. Il limite
4/8 è osservato su entrambi gli harness ed è spiegato dal contenuto del bundle. Confidenza sulla
classifica relativa tra VERTICAL e GENERALIST: **70%**. Il campione è singolo e l'ordine cambia
tra Codex e Claude.

## Verdetto

NEEDS REDESIGN
