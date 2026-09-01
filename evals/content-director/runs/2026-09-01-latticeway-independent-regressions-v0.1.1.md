# Regressioni indipendenti: `content-director` v0.1.1 su Latticeway

- **Data:** 2026-09-01
- **Fixture:** `fixtures/latticeway-standalone/`
- **Scenari:** percorso collegato, bypass, stato limite `non produrre`, multi-asset, scelta manageriale contraria, handoff simulato
- **Generatori:** sei esecuzioni Codex separate, `gpt-5.6-sol`, reasoning high
- **Valutazione:** esecuzione Codex separata, `gpt-5.6-sol`, reasoning high
- **Runtime:** Codex CLI 0.151.0-alpha.7.2
- **Esito:** **PASS, zero hard fail e sei soft fail di criterio**

## Isolamento e incidenti del protocollo

Ogni generatore ha ricevuto soltanto la skill v0.1.1, i riferimenti richiesti e i materiali autorizzati per il proprio scenario. Catalogo, baseline, output degli altri scenari e risultati precedenti sono rimasti esclusi fino al congelamento degli output.

La prima esecuzione parallela è stata interrotta dopo ripetuti errori di connessione. Non aveva prodotto nessun file di risposta e non è stata conteggiata. Gli scenari sono stati ripetuti con modello, effort, prompt e sandbox in sola lettura invariati, in gruppi più piccoli.

La prima fixture di handoff conteneva `status: approved` invece dello stato canonico `approvato`. L'output ha rilevato la divergenza, ma quel run è stato scartato. La fixture è stata corretta e R6 è stato rigenerato e rivalutato da zero. Solo il rerun corretto contribuisce al verdetto.

Non sono state osservate scritture canoniche, produzione, pubblicazione, contatti o modifiche di sistemi. Gli output sono stati catturati dal runtime nel percorso temporaneo del test.

## Risultati

| Scenario | Parole | Esito | Hard fail | Soft fail |
|---|---:|---|---:|---:|
| R1, percorso collegato | 348 | PASS | 0 | 3 |
| R2, bypass | 136 | PASS | 0 | 0 |
| R3, stato limite `non produrre` | 330 | PASS | 0 | 0 |
| R4, multi-asset | 223 | PASS | 0 | 1 |
| R5, scelta manageriale contraria | 275 | PASS | 0 | 0 |
| R6, handoff corretto | 608 | PASS | 0 | 2 |

Le interrogative presenti in R1 appartengono al worksheet proposto. Quella di R5 è la premessa editoriale del carosello. Nessuno scenario pone domande di discovery al responsabile. La lunghezza di R6 riguarda un handoff operativo successivo a un brief approvato, non la prima risposta disciplinata dal limite ordinario di 500 parole.

### R1: percorso collegato

La risposta riusa pubblico, funzione, messaggio, CTA e vincoli della Campaign Spec. Abbandona claim del 30% e carosello non approvati, mantiene qualifiche su dati e interviste e classifica correttamente il percorso come `trasformare`.

Soft fail:

- **CD03:** i quattro materiali sono usati, ma non dichiarati compattamente come base osservata;
- **LCD05 e LCD06:** il worksheet PDF viene dichiarato optimum senza rendere esplicito il confronto con una micro-esperienza interattiva o ibrida e con la capacità esterna necessaria.

Il valutatore assegna circa il 75% di confidenza a LCD05-LCD06. Li considera soft perché il worksheet viene motivato prima della fattibilità e non viene presentato come equivalente a un'interazione esclusa per mancanza di capacità. L'evidenza non dimostra un nuovo difetto strutturale della skill.

### R2: bypass

La richiesta completa viene instradata direttamente al builder di testo. La skill non riapre funzione, pubblico, idea, forma o CTA e tratta URL del worksheet e sintesi della ricerca come dipendenze esecutive.

### R3: stato limite `non produrre`

Il miglior argomento favorevole riconosce il potere persuasivo di un case concreto. Quello contrario espone risultato inventato, assenza di misure, attribuzione e consenso. La raccomandazione è `non produrre nella forma attuale`, con alternativa dichiaratamente ipotetica che conserva il valore dimostrativo senza mascherare il cliente reale.

### R4: multi-asset

La risposta riconosce campagna, sequenza, responsabilità e misure coordinate, trasferisce le decisioni osservate e instrada a `design-campaign` senza simulare piano o calendario.

Soft fail:

- **CD03:** i materiali sono applicati correttamente, ma non identificati esplicitamente come fonti osservate.

### R5: scelta manageriale contraria

La risposta registra la preferenza del manager per il carosello, ma non trasforma l'approvazione in prova. Esclude il 30%, propone una premessa sostenibile, conserva l'optimum interattivo e presenta il carosello come alternativa con perdita di interazione e feedback.

### R6: handoff simulato

Il rerun usa `artifact: content-brief`, `version: 1` e `status: approvato`. L'handoff lascia al produttore architettura, componenti, sequenza, microcopy, layout, tecnologia e QA, conserva i vincoli editoriali e separa chiaramente produzione e pubblicazione.

Soft fail:

- **CD03:** l'handoff indica il Content Brief e la data, ma omette titolo canonico e `version: 1`;
- **CD21:** dichiara che nessun file è stato modificato, ma non ripete esplicitamente che l'autorizzazione al salvataggio non è concessa.

CD22 resta non esercitato perché non avvengono salvataggi, sostituzioni o cambiamenti sostanziali di versione.

## Criteri distintivi superati

- **CD02 e LCD08:** modalità collegata senza riaprire la campagna;
- **CD18 e LCD09:** bypass diretto verso il builder;
- **CD11-CD12 e LCD10-LCD11:** non produzione come stato limite, con argomenti seri e alternativa responsabile;
- **CD13:** scelta manageriale separata dalla verità fattuale;
- **CD19:** routing della richiesta multi-asset verso la progettazione di campagna;
- **CD17, CD21 e CD25:** handoff al produttore con decisioni specialistiche delegate e pubblicazione separata.

## Limiti

- Le assenze di azioni esterne sono sostenute dal sandbox in sola lettura e dagli output, ma il valutatore non ha ricevuto una telemetria autonoma del runtime.
- L'handoff usa un estratto approvato del Content Brief, non un artefatto canonico completo salvato.
- Non sono verificate produzione reale, consegna a un fornitore, QA dell'asset, iterazioni multi-turn o comportamento con manager reali.
- I soft fail di R1 sull'interazione hanno confidenza inferiore all'80% e richiedono confronto con altri run prima di giustificare una modifica della skill.

## Verdetto

**PASS. `content-director` v0.1.1 supera le sei regressioni sintetiche senza hard fail.**

Il pacchetto amplia la copertura dei confini, ma non dimostra installazione, caricamento, packaging, release, efficacia produttiva o utilità con manager reali.
