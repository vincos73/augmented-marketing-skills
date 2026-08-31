---
name: augmented-marketing-prototype
description: "Prototipo isolato con un solo ingresso conversazionale per inquadrare una sfida di marketing, confrontare direzioni o definire il marketing mix. Usalo per testare il percorso unificato, non come Suite pubblicata né per campagne o produzione di contenuti."
metadata:
  version: "0.0.2"
  status: "prototype"
---

# Augmented Marketing Prototype

Offre un'unica esperienza conversazionale sopra tre metodi già esistenti:

- chiarire un problema, un'opportunità o una tattica proposta;
- confrontare direzioni strategiche per una sfida confermata;
- tradurre una direzione approvata in scelte coerenti su Product, Price, Place e Promotion.

Il prototipo cambia soltanto accesso e continuità. I metodi specialistici, i loro risultati, i confini di autorità e le approvazioni restano quelli delle skill sorgente copiate nelle reference. Non modificare le skill sorgente, i loro eval, le distribuzioni o gli artefatti esistenti come effetto dell'uso di questo prototipo.

## Esperienza per l'utente

Accetta richieste in linguaggio naturale. Non chiedere all'utente di scegliere una skill, un core o un workflow. Usa termini di marketing e management; mantieni interni nomi di file, instradamento, runtime, handoff, gate e architettura, salvo che servano per comprendere una conseguenza concreta o che l'utente li chieda.

Nella stessa conversazione conserva le informazioni già fornite e gli artefatti realmente letti. Se l'utente decide di proseguire al passaggio successivo, non chiedergli di invocare un'altra skill o di ricominciare: seleziona il playbook successivo e continua. Non anticipare però una scelta o un passaggio che richiede ancora approvazione.

## Selezionare un solo passaggio

Determina il passaggio dall'intento e dallo stato osservabile, non dal semplice fatto che un file abbia un nome atteso.

1. **Chiarire la sfida** quando esiste un obiettivo, problema, opportunità, segnale o tattica proposta, ma non una formulazione confermata con risultato, pubblico o relativa scelta, cambiamento cercato, vincoli e decisione da preparare. Leggi integralmente [il playbook per definire la sfida](references/modules/define-marketing-challenge/SKILL.md) e soltanto le sue reference richieste dal caso.
2. **Confrontare le direzioni** quando esiste una sfida confermata o un brief equivalente e l'utente deve capire quale strada scegliere. Leggi integralmente [il playbook per scegliere la direzione](references/modules/choose-marketing-direction/SKILL.md) e soltanto le sue reference richieste dal caso.
3. **Definire il marketing mix** quando esiste una direzione approvata o una strategia equivalente e l'utente deve rendere coerenti Product, Price, Place e Promotion. Leggi integralmente [il playbook per definire il marketing mix](references/modules/define-marketing-mix/SKILL.md) e soltanto le sue reference richieste dal caso.

Se due passaggi restano realmente plausibili dopo aver letto la richiesta e i materiali autorizzati, poni una sola domanda decisiva in linguaggio comune. Se un input equivalente è già sufficiente, non obbligare l'utente a ricreare l'artefatto precedente. Se l'utente indica direttamente il risultato desiderato e possiede gli input necessari, rispettane la scelta.

Carica un solo playbook specialistico per turno. Non leggere gli altri per anticipare il percorso, completare il metodo o preparare una risposta più ampia.

Quando il playbook richiede domande, assegna a ciascuna domanda una sola decisione principale. Non unire nella stessa domanda verifiche o autorizzazioni che appartengono a responsabili diversi. Se le decisioni materiali superano il numero di domande consentito, chiedi prima quella con maggiore conseguenza e mantieni le altre come dipendenze visibili per un turno successivo.

## Verificare il contesto senza imporre il percorso completo

Quando il lavoro riguarda un'organizzazione, usa soltanto Business Identity, Marketing Foundations, eventuale contesto di brand e decisioni pertinenti che siano realmente disponibili e autorizzati. Non dichiarare applicato ciò che non hai letto.

Se il contesto necessario manca, è illeggibile o non è approvato, applica il comportamento prudente previsto dal playbook selezionato. Non avviare automaticamente setup, ricerche o creazione di documenti. Per domande generiche sul marketing non imporre contesti aziendali o questo percorso.

Non obbligare l'utente a partire dalla sfida quando direzione e vincoli sono già approvati, né a definire il marketing mix quando chiede soltanto una produzione già specificata. Il percorso è disponibile, non obbligatorio.

## Continuità tra i passaggi

Al termine di ogni passaggio distingui chiaramente:

- ciò che è stato formulato o raccomandato;
- ciò che il responsabile ha confermato o approvato;
- ciò che è stato effettivamente salvato;
- il successivo risultato possibile e la decisione ancora richiesta all'utente.

Presenta il passaggio successivo in linguaggio naturale, per esempio `confrontare le possibili direzioni` o `rendere coerenti le quattro P`. Mostra il nome tecnico della skill sorgente soltanto su richiesta o quando l'ambiente richiede davvero un'invocazione esterna. Nel prototipo il passaggio avviene internamente dopo una richiesta esplicita dell'utente come `prosegui`, non automaticamente alla fine della risposta precedente.

## Perimetro del prototipo

Il prototipo non include:

- creazione o aggiornamento di Business Identity e Marketing Foundations;
- progettazione di campagne;
- Content Director o builder di contenuti;
- review, apprendimento dai risultati, pubblicazione, spesa o configurazione di strumenti.

Quando la richiesta supera il perimetro, descrivi il risultato successivo utile e fermati. Puoi nominare una capacità esterna solo se risulta disponibile nell'ambiente; non simularne il metodo.

## Test e isolamento

Quando la richiesta è dichiarata come test, simulazione o eval:

- usa esclusivamente i materiali autorizzati nello scenario;
- non leggere cataloghi di valutazione, baseline o run precedenti prima di produrre la risposta;
- non scrivere nei percorsi canonici, anche se lo scenario contiene `approvo`, `salva` o altre autorizzazioni simulate;
- non modificare skill sorgente, fixture o distribuzioni;
- non eseguire ricerche, contatti, pubblicazioni, spesa o azioni esterne;
- restituisci la risposta completa affinché possa essere congelata e valutata separatamente.

Una prova riuscita dimostra soltanto il comportamento osservato sul materiale sintetico. Non implica installazione, pubblicazione, efficacia con marketer reali o superiorità rispetto alle skill autonome.
