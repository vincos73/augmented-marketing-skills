# Retest indipendente: `content-director` v0.1.1 su Latticeway

- **Data:** 2026-09-01
- **Fixture:** `fixtures/latticeway-standalone/`
- **Generatore:** Codex, `gpt-5.6-sol`, reasoning high
- **Valutatore:** esecuzione Codex separata, `gpt-5.6-sol`, reasoning high
- **Runtime:** Codex CLI 0.151.0-alpha.7.2
- **Esito:** **PASS, zero hard fail e due soft fail**

## Obiettivo della correzione

Il [forward test della v0.1.0](2026-09-01-latticeway-independent-forward-v0.1.0.md) era fallito perché la prima risposta aveva scelto una forma già producibile internamente prima di formulare la strada ideale. La v0.1.1 rende esplicita la sequenza:

1. definire l'optimum editoriale senza filtrarlo attraverso capacità, budget, tempi o builder disponibili;
2. motivarlo rispetto alla funzione e all'esperienza richiesta;
3. reintrodurre i vincoli produttivi;
4. conservare la strada ideale e affiancarle un'alternativa seria con perdita esplicita.

La stessa revisione rende deterministici `editorial_path: trasformare` e il frontmatter minimo del Content Brief.

## Isolamento

Il generatore ha ricevuto soltanto la sorgente candidata v0.1.1, i suoi riferimenti e i materiali sintetici della fixture. Non ha ricevuto catalogo, baseline, output attesi o risultato della v0.1.0.

I tre turni sono stati ricostruiti in esecuzioni effimere separate e in sola lettura. Ogni turno successivo ha ricevuto gli output precedenti congelati. Dopo il terzo turno, un valutatore separato ha ricevuto skill, materiali, output, catalogo e baseline degli invarianti.

La prima invocazione del valutatore si è fermata prima dell'esecuzione perché la directory temporanea non era un repository Git attendibile. Il retest effettivo è ripartito con il solo controllo Git disattivato, mantenendo sandbox interno in sola lettura, modello, effort e prompt invariati.

Non sono state osservate scritture canoniche, avvii di builder o fornitori, produzione, pubblicazione o modifiche di sistemi e account.

## Risultati

### Primo turno

- **Lunghezza:** 306 parole.
- **Domande di discovery:** 1, relativa a una sola decisione ad alto impatto.
- **Percorso:** `trasformare`.
- **Optimum editoriale:** micro-esperienza interattiva pubblica di autodiagnosi.
- **Motivazione:** applicazione a una riunione reale e restituzione pertinente, indipendentemente dalle capacità disponibili.
- **Fattibilità:** capacità interna assente, fornitore e budget da verificare.
- **Alternativa:** articolo-esercizio guidato con visuale statica.
- **Perdita dichiarata:** feedback personalizzato e ramificazioni.

L'ordine decisionale è corretto: la forma ideale viene scelta e motivata prima che entrino capacità, budget e alternativa.

### Secondo e terzo turno

Il secondo turno mostra soltanto il delta, conserva l'interazione come ideale, esclude i dati quantitativi dalla versione e mantiene separati approvazione editoriale, salvataggio, produzione e pubblicazione.

Il terzo turno restituisce un Content Brief completo in conversazione, con frontmatter canonico, `artifact: content-brief`, `version: 1`, `status: bozza`, `entry_mode: standalone` ed `editorial_path: trasformare`. Claim del 30%, generalizzazioni, causalità, citazioni dirette e promesse di produttività restano esclusi. Le percentuali 61% e 47% sono omesse dalla versione scelta e conservate soltanto come elementi soggetti a qualifica e revisione Legal.

## Valutazione

### Hard fail

Nessuno.

Passano i tre criteri essenziali falliti nella v0.1.0:

- **CD07:** consiglio agnostico rispetto ai builder;
- **CD24:** capacità non disponibile senza sostituzione silenziosa dell'ideale;
- **LCD05:** considerazione seria dell'autodiagnosi interattiva o ibrida.

Passano anche classificazione `trasformare`, frontmatter del brief, prove, attribuzioni, progressione semantica, confine con i builder, gate, isolamento e separazione tra produzione e pubblicazione.

### Soft fail

| ID | Motivo |
|---|---|
| CD03 | Il primo turno usa correttamente i sei materiali, poi catalogati nel brief, ma non li elenca esplicitamente in apertura. |
| CD21 | Il brief registra la direzione come approvata, ma il corpus consegnato al valutatore non contiene il messaggio intermedio che seleziona esplicitamente l'opzione interattiva. |

Il secondo punto riguarda anche il protocollo di test: `user-answers.md` stabilisce che l'approvazione avverrà dopo la revisione compatta, ma la prova esplicita successiva al secondo turno non è stata conservata tra gli input valutabili.

### Non esercitati

Non sono stati verificati percorso collegato, bypass diretto al builder, richiesta multi-asset, scelta manageriale contraria, caso limite di non produzione, alternativa dopo il no e handoff effettivo.

## Verdetto

**PASS. `content-director` v0.1.1 supera il retest sintetico Latticeway senza hard fail.**

Il risultato corregge il difetto centrale osservato nella v0.1.0, ma non dimostra installazione, caricamento, packaging, release, efficacia produttiva o utilità con manager reali. Prima di una dichiarazione di prontezza restano necessarie le regressioni non esercitate e una prova con utenti reali.
