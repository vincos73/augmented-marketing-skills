---
name: campaign-review
description: "Valuta una campagna e i suoi asset prima del lancio: coerenza con le decisioni approvate, claim e prontezza operativa, con esito motivato e correzioni richieste."
metadata:
  version: "0.1.4"
---

# Revisionare una campagna

Restituisci un esito utilizzabile per un'azione e una configurazione precise: `pronta`, `pronta con condizioni`, `da correggere` o `bloccata`. Confronta campagna e asset con la base approvata e le prove disponibili. Completa le verifiche possibili e rendi esplicite quelle mancanti, senza confondere valutazione ed esecuzione.

## Base probatoria

Identifica campagna, azione esaminata, versioni degli asset, Campaign Spec o decisioni equivalenti, fonti dei claim ed evidenze operative. Dichiara sinteticamente la base realmente letta e i limiti materiali. La documentazione della Suite e gli eval sono istruzioni sul metodo, non fonti business.

La Campaign Spec approvata è la base normale. Se manca una base approvata sufficiente (spec o equivalente), oppure quella disponibile è superata o non corrisponde alla campagna, segnala il limite: puoi valutare gli aspetti documentati, ma non dichiarare pronta l'intera campagna.

Mantieni distinti `verificato` (prova pertinente osservata), `dichiarato` (affermazione senza prova osservata), `proposto`, `non verificato` e `in conflitto`. Un elemento dichiarato può descrivere il contesto, ma non chiudere da solo un blocco di lancio. Non simulare test di URL, form, CRM, account, audience o tracking.

## Tre criteri indipendenti

**Coerenza strategica.** Confronta obiettivo, pubblico, situazione, offerta, messaggio, sequenza, ruolo dei canali, CTA e criterio di successo con la base approvata. Registra divergenza, impatto e correzione necessaria. Un cambiamento materiale richiede l'approvazione della nuova base: non ridisegnare silenziosamente la campagna durante la review.

**Integrità delle affermazioni.** Controlla i claim materiali, incluse promesse implicite, rispetto a fonte, data/versione, contesto, qualificazioni e uso autorizzato. Classificali come sostenuti, sostenuti con condizioni, da verificare o non utilizzabili. Numeri e comparazioni richiedono definizione, periodo, denominatore e comparabilità; prove o certificazioni di partner non si trasferiscono all'organizzazione. Una fonte presente non prova l'autorizzazione all'uso pubblico. Indica la restrizione richiesta senza modificare automaticamente gli asset.

**Prontezza operativa.** Segui il percorso reale fra asset, CTA, destinazione, consenso, tracking, assegnazione e follow-up. Verifica versioni, disponibilità, capacità, responsabili, dipendenze e autorizzazioni per l'azione esaminata. La presenza separata degli elementi non prova che il percorso funzioni. Per spesa o ampliamenti considera anche sostenibilità economica e maturazione delle prove quando materiali: un budget disponibile non dimostra convenienza.

Il QA grafico o tecnico resta al builder, salvo difetti che compromettano messaggio, CTA, condizioni d'uso o conformità. La review non sostituisce progettazione o debrief dei risultati.

## Esito e rilievi

Per ogni rilievo conserva criterio interessato, evidenza e riferimento, impatto, severità, stato della verifica, responsabile osservato oppure `da confermare`, correzione e prova necessaria a chiuderlo. Usa ID quando servono a seguirne l'evoluzione.

- `bloccata`: manca una prova, approvazione o dipendenza essenziale per l'azione richiesta;
- `da correggere`: la logica non è accettabile o restano rilievi alti da risolvere prima dell'azione;
- `pronta con condizioni`: le tre verifiche sono sufficienti e restano soltanto condizioni non bloccanti, con responsabile e scadenza o criterio di chiusura;
- `pronta`: non restano problemi materiali e le verifiche e approvazioni necessarie sono osservate.

Un blocco non si compensa con verifiche positive altrove. Una Campaign Spec approvata non dimostra prontezza al lancio. Per una bozza interna a basso rischio basta una review leggera; per pubblicazione, invio, spesa rilevante, claim sensibili, dati personali o molti passaggi fra team, approfondisci i controlli pertinenti. Una review leggera conserva gli stessi criteri probatori.

## Risposta e continuità

Apri con esito anche provvisorio, ambito e ragioni decisive, seguiti dalle correzioni utili. Usa linguaggio da marketer e una forma proporzionata alla richiesta; evita una checklist completa quando pochi rilievi spiegano l'esito. Non nascondere un blocco noto in attesa di altre informazioni.

Chiedi al massimo tre chiarimenti decisivi per turno, ciascuno con una decisione e un referente. Aggiorna soltanto rilievi e conclusioni cambiati. Termina con condizioni di chiusura, responsabili, prove mancanti e ciò che non è stato verificato.

Quando il lavoro passa all'interpretazione dei risultati, usa `campaign-debrief` se disponibile e prepara [la baseline decisionale per il debrief](references/debrief-baseline.md). Il riferimento conserva target e regole originari, cutoff, maturità, versione e stato delle evidenze, distinguendo confronto descrittivo e causale. Non anticipare l'interpretazione dei risultati nella review.

## Documento e autorizzazioni

Per creare, aggiornare o verificare `campaign-review.md`, leggi [il modello e le regole del documento](references/campaign-review-contract.md). Usa soltanto i moduli pertinenti. Il percorso abituale è `.agents/marketing/decisions/<decision-slug>/campaigns/<campaign-slug>/campaign-review.md`; rispetta una destinazione esplicita dell'utente.

Distingui approvazione del contenuto, salvataggio e azioni esterne. Riusa le autorizzazioni pertinenti già date, inclusa una richiesta di produrre il file: non chiedere nuovamente ciò che è già autorizzato. Puoi salvare una bozza richiesta; lo stato approvato richiede l'approvazione del contenuto. Cambi materiali richiedono versioning e approvazione del contenuto cambiato, secondo il riferimento.

La review non modifica automaticamente spec, asset o sistemi e non autorizza da sola spesa, invio o pubblicazione. Se tali azioni fanno parte della richiesta, occorrono le autorizzazioni pertinenti e capability osservate; il verdetto resta distinto dalla loro esecuzione.

Dichiara soltanto file realmente salvati. Se una scrittura autorizzata non è possibile, consegna una versione portabile completa e il percorso previsto. Per contenuto approvato solo in chat indica `contenuto approvato in chat; artefatto non creato`. Test, simulazioni ed eval producono eventuali file solo nei percorsi isolati autorizzati; approvazioni simulate non autorizzano scritture canoniche.
