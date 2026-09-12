# setup-brand-voice 0.1.1

## Riepilogo

La versione 0.1.1 aiuta a definire, recepire o aggiornare una voce di brand a partire da materiali e decisioni disponibili. È la candidata `0.1.1-receipt` rinominata per la promozione, senza ulteriori modifiche comportamentali.

La modifica rende più esplicito il riferimento alla guida approvata quando viene preparata una nota autonoma riutilizzabile. La nota deve recepire la sezione pertinente con regola, perimetro, condizioni ed esempio. Restano proporzionati il lavoro richiesto e il risultato: non vengono compilati moduli non necessari e una correzione locale non aggiorna automaticamente la guida.

La skill include anche un controllo condizionale degli esempi. Quando un esempio contiene impegni o condizioni, il controllo verifica stato delle azioni, condizioni necessarie, scadenze, garanzie, ambito e formulazioni che potrebbero implicare fatti non documentati. Il controllo può essere delegato a un nuovo agente soltanto con autorizzazione; altrimenti viene dichiarato non indipendente.

Per il comportamento completo, consultare la [skill sorgente](../../skills/setup-brand-voice/SKILL.md).

## Cosa mostrano le prove

Nei piloti del 12 settembre 2026:

- il controllo condizionale ha corretto i tre errori seminati negli esempi pertinenti in tutte e sei le revisioni, su due repliche, e ha lasciato identici i sei testi già corretti;
- una replica ha conservato un dettaglio già presente nella bozza ma non documentato nella scheda di consegna, quindi resta una riserva sulla completezza del controllo;
- nel confronto sul recepimento, le note sono risultate complete in 2/2 casi sia per il predecessore sia per la candidata;
- una candidata ha mantenuto una riserva locale e la revisione separata ha modificato un esempio in modo non richiesto;
- la riproduzione di un errore storico ha confermato il difetto originario, ma due nuove esecuzioni del predecessore lo hanno evitato; la candidata non ha quindi dimostrato un vantaggio stabile.

Le prove sostengono una modifica circoscritta e utilizzabile, non una superiorità generale della versione. I casi erano sintetici, con poche esecuzioni e giudizi limitati: non misurano affidabilità generale, riconoscibilità della voce per lettori umani, valore commerciale, costi, latenza o attivazione spontanea della revisione. Non costituiscono una certificazione.

## Stato di rilascio

L'uso, l'installazione e la pubblicazione sono autorizzati dall'utente. La sorgente promossa e l'installazione locale 0.1.1 in `~/.codex/skills/setup-brand-voice` sono verificate e coincidono; il backup 0.1.0 è conservato fuori dalla directory della skill. La versione sorgente è identificata dal commit Git che contiene questi file. ZIP e checksum restano artefatti locali esclusi dal commit.

La prova su casi reali sarà svolta dall'utente e resta separata dai risultati dei piloti.
