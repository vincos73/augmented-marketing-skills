# Revisione Astra: voce, copy e direzione editoriale

Modificati soltanto i tre percorsi assegnati. Versioni: setup-brand-voice 0.1.1; write-marketing-copy 0.1.5; content-director 0.1.2. INSTALL.md portabili aggiornati o creati; nessuna attestazione di release della nuova versione.

## Cambiamenti
- Description brevi e selettive, distinguendo voce durevole, testo singolo e decisione sul contenuto.
- Entrypoint: voce 1467 → 658 parole; copy 1146 → 603; content 1241 → 649 (conteggio whitespace, baseline fornita). Totale 3854 → 1910, circa -50%.
- Eliminati menu interni, quote editoriali e ripetizioni; riferimenti caricati per esigenze concrete.
- Content-director: niente arresto imposto prima di un brief completo richiesto; possibile bozza con decisioni aperte. Conservato schema portabile e approvazione editoriale distinta dal salvataggio.
- Editorial-routing trasformato da itinerario/checklist a criteri, classificazioni e dipendenze pertinenti. Conservata scelta dell'ottimo editoriale prima della fattibilità.

## Invarianti preservati
- Nessun setup/artefatto/skill a monte obbligatorio.
- Una voce espressamente richiesta senza riferimento utilizzabile richiede un chiarimento effettivo, anche se accompagnato da bozza provvisoria.
- Fonti, osservazioni, proposte, approvazioni e fatti restano distinti. Una guida di voce non prova risultati/offerta.
- Nessun rafforzamento di claim non sostenuto; qualificazioni e testi protetti preservati, anche nei raccordi e formule di cortesia.
- Le approvazioni sono circoscritte; una correzione locale non riscrive la guida.
- Scritture richieste già autorizzate non richiedono conferma rituale; stati aperti rimangono in bozza.
- Test in area isolata; produzione/pubblicazione/salvataggio distinti; nessuna affermazione di caricamento o operazione non verificata.
- Trasformare distinto da produrre-con-vincoli in base alla differenza dalla richiesta iniziale; non produzione non genera brief positivo.

## Verifiche
- Link Markdown locali: nessun target mancante nei tre pacchetti.
- git diff --check: passato sui tre percorsi.
- quick_validate.py invocato: runtime python3 privo di PyYAML; comunicato al coordinatore per validazione comune. Non è un esito di test positivo.
- Riesame manuale dei riferimenti condizionali e delle clausole di salvataggio/approvazione; corretto il template che subordinava impropriamente l'approvazione editoriale al salvataggio.

Nessun test comportamentale indipendente eseguito da questo agente. I conteggi non misurano token effettivi né qualità del comportamento.
