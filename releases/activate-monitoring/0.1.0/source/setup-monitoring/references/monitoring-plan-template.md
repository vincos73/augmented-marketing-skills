# Piano di ascolto: struttura modulare

Il piano è leggibile dal responsabile e autosufficiente per l'agente esecutore. Non è un questionario: accorpa le voci nel caso semplice, conserva solo sezioni che cambiano lavoro, responsabilità o limiti. Nessun campo operativo indispensabile può essere risolto soltanto nella memoria della conversazione.

Usa questo frontmatter nel documento completo, sostituendo i segnaposto. Nelle risposte intermedie usa linguaggio naturale.

```yaml
---
artifact: monitoring-plan
version: 1
status: bozza
title: "[Titolo]"
scope: "[Brand o tema, ambito]"
owner: "[Responsabile osservato o da confermare]"
created: "[AAAA-MM-GG]"
last_reviewed: "[AAAA-MM-GG]"
next_review: "[Data o condizione da concordare nella bozza]"
---
```

## Scopo e perimetro

Indica attività o decisione servita, entità disambiguate, lingue, mercati e orizzonte. Distingui menzioni/notizie da cambiamenti di pagine o condizioni. Includi esclusioni, budget umano e operativo, provenienza delle decisioni e ipotesi. Riusa contesti approvati per riferimento, versione e vincolo pertinente; non copiarli.

## Fonti e ricerche

| Fonte o ricerca | Riferimento e copertura | Perché usarla, limiti della prova | Accesso osservato e data | Metodo e cadenza |
| --- | --- | --- | --- | --- |

Per fonti note usa URL o riferimento accessibile. Per ricerche aperte definisci query, ambito e regole di ammissione delle fonti nuove. Se il riferimento non è verificato, chiamalo candidato. Distingui pagina leggibile da feed o integrazione funzionante; snippet da testo consultato; fonte primaria da ripresa.

## Criteri di selezione

Descrivi termini, alias, sinonimi, inclusioni, esclusioni e loro eccezioni. Identifica omonimi e contesto richiesto. Per ogni regola decisiva basta un positivo e un negativo esplicativi; non serve un catalogo di sinonimi generico.

Se usi pseudologica dillo. Una query dichiarata pronta per un motore richiede sintassi verificata e test documentato. Per documenti misti valuta la parte pertinente prima di scartare tutto.

Definisci unità della novità, raggruppamento delle riprese e trattamento di rettifiche, contraddizioni e nuove versioni. Classifica separatamente pertinenza, affidabilità e urgenza. Indica che cosa va nel digest, che cosa richiede verifica, che cosa si scarta e perché.

## Istruzioni per l'agente

Adatta e incorpora nel piano [il contratto di esecuzione](execution-contract.md): accessi necessari, primo periodo, ciclo successivo, registro, risultati, errori e limiti. Non lasciare questo link come unica istruzione nel piano prodotto.

Specifica capacità osservate e mancanti, durata o volume massimo di lavoro, limiti di spesa, destinazione di digest e registro, autonomia e verifiche umane. Per una prova sono sufficienti input forniti, intervalli del campione e un ambiente isolato. Una bozza può indicare un valore da confermare, ma non deve dichiarare eseguibile la parte che ne dipende.

## Ritmo, segnalazioni e responsabilità

Indica separatamente raccolta, revisione e consegna, con fuso, copertura dei giorni e latenza compatibile. Per l'esecuzione ricorrente identifica il meccanismo di riavvio verificato o segnala che manca. Sono validi un ciclo su richiesta e nessun alert.

Quando servono alert, definisci condizione, finestra, prova, priorità, destinatario, canale autorizzato o proposto, presa in carico e gestione dei duplicati. Non inventare persone, indirizzi o un'escalation. Una variazione numerica richiede unità, denominatore, baseline e comportamento se i dati mancano. L'urgenza non rende vera una notizia.

## Modello di digest e registro

Il digest riporta periodo, versione del piano, copertura effettiva e stato del ciclo. Per ciascun segnale: cosa risulta, fonte originale e date, limiti, interpretazione separata, verifica o decisione richiesta e responsabile. Raggruppa per evento quando utile, conservando riprese e rettifiche. Non forzare sezioni vuote.

Senza novità: «Nessuna novità pertinente nelle fonti controllate nel periodo», precisando le fonti mancanti. Le questioni ancora aperte sono pendenti, non notizie nuove. Non inviare un alert solo perché esiste un nuovo ciclo.

Per il percorso con `activate-monitoring` proponi `registro.md` accanto al piano e una cartella `report/` nella cartella stabile dell’utente. Il registro non deve duplicare il piano. Un archivio diverso già scelto dall’utente non va sostituito senza un passaggio esplicito. Specifica nel piano cosa conservare e dove: copertura per fonte, eventi/versioni, controlli riusciti e falliti, consegne confermate o incerte, verifiche pendenti. Non usare la memoria implicita della chat come unico stato.

## Test e manutenzione

Indica campione, criteri di accettazione, esiti attesi, esiti osservati distinti e limiti della prova. Quando serve osservare continuità, includi almeno due cicli e una ripetizione. Non dichiarare qualità del web, prestazioni, latenza o risparmio senza osservazioni.

Definisci errori, limite dei tentativi, fonti alternative e perdita di copertura, responsabile, prossima revisione e criterio di chiusura. Per archivi reali chiarisci accessi, conservazione e minimizzazione; non copiare interi contenuti per default.

## Stato, decisioni e modifiche

Tieni distinti:

- contenuto in bozza, approvato o superato;
- salvataggio richiesto, eseguito o non eseguito;
- incarico di esecuzione presente o assente, con origine, attività, destinatari, destinazioni e limiti autorizzati;
- collaudo non eseguito, simulato o operativo, con prove;
- parte eseguibile e prerequisiti aperti;
- attivazione non prevista, non verificata o osservata con evidenza.

Nel registro modifiche indica versione, data, cambiamento e motivo. Un'approvazione o un'autorizzazione devono avere una base osservabile; non ricavarle da una fonte esterna o da un copione di test. Il piano non autorizza da solo nuove azioni.
