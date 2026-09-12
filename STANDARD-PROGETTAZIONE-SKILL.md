# Standard per progettare le skill

Revisione del 12 settembre 2026, applicata alla candidata locale beta.11. Integra il documento fornito dall'utente, *Rethinking skills and prompts for GPT-6 Astra*, e la versione locale aggiornata di `skill-creator`.

Una skill aggiunge conoscenza di dominio e criteri decisionali utili a un agente già capace. La riuscita si misura dal lavoro che permette di completare, dalla qualità delle decisioni e dal rework richiesto al responsabile. La lunghezza delle istruzioni non è una misura di robustezza.

## Scoperta e letture pertinenti

La description dichiara in poche parole cosa fa la skill e quando usarla. Aggiunge esclusioni solo per ambiguità probabili con capacità adiacenti. Evita elenchi esaustivi, superlativi e trigger generici che attirano ogni richiesta di marketing.

`SKILL.md` contiene risultato, criteri essenziali, confini di autorità e indicazioni su quali riferimenti consultare. Procedure di salvataggio, template, modalità specialistiche ed esempi sostanziali vanno nei riferimenti quando servono solo a una parte dei compiti. Non spostare l'intera vecchia ricetta in un file da leggere comunque ogni volta.

Una skill semplice può restare autonoma. Le istruzioni necessarie sono incluse nella sua cartella: questo standard, blueprint, storia delle prove e altre skill non sono dipendenze operative implicite. Un eventuale `AGENTS.md` del progetto indirizza alle letture pertinenti al cambiamento, senza imporre una mappa completa del repository prima di ogni modifica.

## Risultato e dialogo

Dichiara cosa significa aver finito: per esempio copy completo, proposta decidibile, guida revisionata o documento salvato quando richiesto. Continua fino a completare il lavoro autorizzato e risolvere i problemi causati dal cambiamento, fermandoti su una decisione effettivamente mancante o un limite dimostrato.

Mostra una proposta utile con le informazioni disponibili. Chiedi solo ciò che può cambiare significato, utilità, correttezza o autorizzazione; riusa le risposte già date. Tre domande ad alta conseguenza sono il limite ordinario di un turno, non una quota da raggiungere. Un incarico chiaro può non richiedere domande.

Adatta lunghezza e forma alla decisione. Una correzione semplice richiede una risposta breve; una riconciliazione complessa conserva conflitti e vincoli senza comprimere artificialmente l'evidenza. Dopo un feedback aggiorna ciò che cambia; ripresenta il documento completo quando serve alla consegna o alla revisione.

Il template è una risorsa per non perdere informazioni, non un indice obbligatorio. Evita duplicazioni tra testo e tabelle e campi privi di utilità. Usa il lessico del destinatario: termini interni come routing, gate e artefatto canonico restano nelle istruzioni, salvo necessità operativa spiegata.

## Evidenze e decisioni

Distingui fatti documentati, dichiarazioni dell'utente, decisioni approvate, inferenze, ipotesi, lacune e conflitti quando incidono sul lavoro. Blueprint, template e casi sintetici spiegano il metodo e non provano fatti dell'organizzazione.

Mantieni gli invarianti specifici della skill: per esempio una guida di voce non prova una promessa commerciale; Place e Promotion risolvono problemi diversi; un risultato osservato non dimostra da solo causalità. Non trasformare ogni errore storico in una regola universale.

## Autorizzazioni e completamento

Prima di un'approvazione necessaria rendi concreta la decisione: proposta, questioni aperte, dipendenze e destinazione dell'eventuale documento. Contenuto approvato, salvataggio, installazione ed esecuzione esterna sono ambiti distinti; un mandato può autorizzarne più di uno quando è inequivocabile.

Le autorizzazioni pertinenti persistono nella conversazione. Non richiederle di nuovo per lo stesso ambito; chiedi soltanto ciò che manca o cambia. Non dedurre dalla sola approvazione di un testo il permesso di inviare, pubblicare, acquistare o modificare sistemi esterni.

Una simulazione non autorizza scritture aziendali reali. Gli artefatti di prova richiesti restano in destinazioni isolate. Se una scrittura autorizzata fallisce, restituisci una versione portabile e dichiara che il file non è stato creato. Non confondere sorgente, pacchetto, installazione e caricamento in sessione.

## Verifica proporzionata

Per revisioni sostanziali conserva una baseline e verifica scenari realistici che potrebbero cambiare comportamento: uso autonomo, riuso di decisioni, ambiguità, provenienza e autorizzazioni. Scegli prove mirate alle modifiche, con input minimi e output conservati; una correzione locale non richiede l'intera storia degli eval.

I controlli strutturali verificano metadati, riferimenti e pacchetti. Le prove comportamentali verificano decisioni e risultati osservati, non la presenza di formule o titoli. Quando utile, un subagent indipendente riceve richiesta, skill e materiali essenziali senza l'esito atteso. Distingui revisione statica, prova sintetica e uso reale; non estendere il risultato a modelli o ambienti non provati.

Una skill è pronta per il passo dichiarato quando il risultato è completo per quel perimetro, le verifiche pertinenti sono documentate e i limiti restano espliciti. Authoring, installazione locale e pubblicazione conservano stati separati.
