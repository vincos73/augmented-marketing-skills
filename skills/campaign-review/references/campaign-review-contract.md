# Contratto della campaign review

Leggi questo riferimento quando devi produrre o verificare il documento `campaign-review.md`. È una libreria modulare di decisioni, non un indice obbligatorio. Mantieni nel documento soltanto ciò che cambia l'esito, assegna una responsabilità o rende verificabile una chiusura.

## Struttura portabile

```markdown
---
artifact: campaign-review
version: 1
status: bozza
entity: "[Nome dell'azienda o del brand]"
campaign: "[Nome comprensibile della campagna]"
scope: "[Azione e perimetro esaminati]"
owner: "[Responsabile della review]"
review_level: leggera | completa
reviewed: YYYY-MM-DD
campaign_spec_path: "[percorso o null]"
campaign_spec_version: null
campaign_spec_status: null
source_brief: null
supersedes: null
superseded_by: null
---

# Campaign Review: [Titolo]

## Scopo e base utilizzata

- **Azione esaminata:**
- **Decisione che la review deve sostenere:**
- **Base effettivamente osservata:**
- **Limiti della review:**

## Esito

- **Esito complessivo:** pronta / pronta con condizioni / da correggere / bloccata
- **Motivazione breve:**
- **Condizioni per procedere:**

## Coerenza strategica

- **Stato:** chiara / con differenze / non verificabile
- **Evidenze e divergenze materiali:**
- **Decisione o correzione richiesta:**

## Integrità delle affermazioni

| ID | Claim o elemento | Fonte/prova | Uso osservato | Stato | Approvazione o limite |
|---|---|---|---|---|---|
| C1 | | | | sostenuto / condizionato / da verificare / non utilizzabile | |

## Prontezza del sistema

| Passaggio | Stato osservato | Evidenza | Responsabile | Condizione o blocco |
|---|---|---|---|---|
| CTA e destinazione | verificato / dichiarato / non verificato | | | |

## Rilievi e chiusure

| ID | Lente | Evidenza | Impatto | Severità | Responsabile osservato o da confermare | Correzione o decisione | Criterio di chiusura | Stato |
|---|---|---|---|---|---|---|---|---|
| R1 | strategica / claim / sistema | | | bloccante / alta / media / bassa | | | | aperto |

## Approvazioni e azioni esterne

- **Approvazione del contenuto della review:**
- **Autorizzazione al salvataggio:**
- **Azioni esterne:** non autorizzate da questa review; verificare separatamente responsabile, condizioni ed evidenza.

## Baseline decisionale per il debrief

Compila questo modulo soltanto quando il prossimo passaggio è `campaign-debrief`. Mantienilo compatto e non duplicare la Campaign Spec.

- **Campaign Spec:** id; versione; stato (`bozza`, `approvata`, `confirmed_in_chat`, `missing` o altro stato osservato)
- **Obiettivo o metrica decisionale:**
- **Definizione operativa:**
- **Target:**
- **Finestra:**
- **Cutoff:**
- **Maturità del dato:**
- **Baseline o comparatore:** valore o regola; stato probatorio
- **Asset revisionati:** id; versione; canale
- **Esito e rilievi aperti:**
- **Decisione di autorizzazione:** stato; evidenza
- **Esecuzione osservata:** stato; evidenza
- **Riferimenti alle evidenze:**
- **Unknowns:**
- **Confronto descrittivo con target o regola:** predisposto / non disponibile; dati già disponibili; dati ancora richiesti
- **Confronto incrementale, causale o controfattuale:** predisposto / non disponibile; motivo e stato di baseline, comparatore o controllo

Il confronto descrittivo è predisposto quando sono disponibili target o regola, definizione operativa e finestra o maturità. Sarà eseguito da `campaign-debrief` soltanto dopo l'arrivo di risultati osservati maturi. Una baseline mancante non blocca questo confronto. Il confronto incrementale, causale o controfattuale richiede invece una base comparabile adeguata e non può essere dedotto dallo scarto rispetto al target.

## Registro modifiche

- v1 (YYYY-MM-DD): prima review.
```

## Stato osservato e linguaggio probatorio

Usa la distinzione seguente quando descrivi una verifica:

- **verificato:** la review ha osservato direttamente la prova pertinente nella versione e nel contesto indicati;
- **dichiarato:** qualcuno lo afferma, ma la review non ha osservato la prova;
- **proposto:** è una soluzione o una correzione ancora da decidere;
- **non verificato:** la prova necessaria non è disponibile, accessibile o sufficiente;
- **in conflitto:** fonti o versioni rilevanti sostengono condizioni diverse.

Una review può usare un elemento dichiarato per descrivere il contesto, ma non può usarlo da solo per chiudere un blocco di lancio. Conserva versione, data, percorso e responsabile quando sono materialmente rilevanti.

## Criteri per le tre lenti

### Coerenza strategica

Considera una divergenza materiale quando cambia obiettivo, pubblico, situazione, offerta, messaggio guida, sequenza, ruolo dei canali, CTA o criterio di successo rispetto alla Campaign Spec approvata. Un cambiamento materiale non si risolve con una nota editoriale: richiede correzione e nuova approvazione della base pertinente.

Non controllare qui la qualità professionale del singolo formato. Segnala un problema dell'asset solo quando compromette la logica della campagna, la comprensione necessaria, la CTA, una condizione d'uso o un requisito di conformità.

### Integrità delle affermazioni

Una prova può sostenere un claim soltanto entro il suo contenuto, la sua data, il pubblico, il contesto e le autorizzazioni osservate. Se il claim è più ampio della prova, classificalo come condizionato, da verificare o non utilizzabile. Numeri e confronti richiedono definizione, denominatore, periodo e comparabilità sufficienti; una fonte senza questi elementi non giustifica precisione apparente.

### Prontezza del sistema

La review deve seguire il percorso reale, per esempio asset → CTA → destinazione → consenso → tracking → assegnazione → follow-up. Non basta verificare che ogni elemento esista separatamente. Una dipendenza non confermata è un blocco quando il percorso non può funzionare responsabilmente senza di essa.

## Review leggera e completa

La review leggera può consolidare le tre lenti in una sintesi e usare una tabella ridotta dei rilievi. La review completa conserva i claim materiali uno per uno e segue ogni passaggio della risposta fino al responsabile o sistema successivo. In entrambi i casi l'esito e i rilievi devono restare verificabili.

## Versioning e confini

- La prima review parte da `version: 1` e `status: bozza`.
- Lo stato del documento può diventare `approvata` soltanto dopo approvazione del contenuto e autorizzazione separata al salvataggio; `approvata` non è un quinto esito della review.
- Una modifica a esito, scope, azione, Campaign Spec di riferimento o rilievo materiale incrementa la versione.
- Una modifica a target, definizione operativa, finestra, cutoff, maturità o baseline trasferiti al debrief è materiale e incrementa la versione.
- La chiusura o riapertura di un rilievo della stessa review aggiorna il registro e richiede una nuova approvazione quando cambia l'esito.
- La review non modifica Campaign Spec, Marketing Foundations, asset, CRM, account, tracking o altri sistemi.
- Durante test, simulazioni ed eval gli output restano fuori dal percorso canonico.
