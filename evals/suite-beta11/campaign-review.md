# Campaign Core: revisione Astra

Ambito modificato: solo `skills/design-campaign`, `skills/campaign-review`, `skills/campaign-debrief`.

Versioni sorgenti e INSTALL: design-campaign 0.1.5; campaign-review 0.1.4; campaign-debrief 0.1.7. campaign-review INSTALL indica destinazione beta.11, senza dichiarare installazione o release.

## Risultato

Entrypoint ridotti da 6.182 a 2.841 parole (-54,0%; conteggio whitespace, non token):

| Skill | Prima | Dopo |
|---|---:|---:|
| design-campaign | 2099 | 984 |
| campaign-review | 1771 | 868 |
| campaign-debrief | 2312 | 989 |

Description: 169, 161 e 171 caratteri. Rimosse strutture di risposta obbligate, tetti di parole, funnel a 3-5 fasi, registri privati prescrittivi e preflight duplicati. Conservato il limite di tre domande decisive, una decisione e un referente, come scelta della suite.

Riferimenti: semplificato question-routing; spostata la baseline review→debrief in un solo nuovo riferimento `campaign-review/references/debrief-baseline.md`; nel decision-routing del debrief concentrati prerequisiti di paid/scala, maturazione, nuova coorte e controllo intermedio. Template riallineati su richiesta di file come autorizzazione al salvataggio di una bozza, approvazione del contenuto distinta e riuso delle autorizzazioni già presenti.

## Invarianti conservate

- Fonti business separate da istruzioni/eval; osservato, dichiarato, inferito e sconosciuto restano distinti.
- Claim vincolati a prove, contesto, limiti e autorizzazione; nessun trasferimento di certificazioni dei fornitori.
- Spec approvata distinta da readiness, autorizzazione e osservazione dell'esecuzione.
- Tre lenti di review e quattro esiti; un blocco non si compensa con altri esiti positivi.
- Debrief confronta atteso, eseguito e osservato; preserva regole qualitative, cutoff, maturità e unknowns.
- Confronto descrittivo col target possibile senza baseline; incremento/causalità/ROI richiedono base adeguata.
- Definizione, fonte, cutoff e denominatore leggibili; pendenti e limiti dello storico non spariscono.
- Decisione esplicita sul perimetro corrente; capacità collegata a carico e ritardi; ruoli osservati conservati.
- Per paid/scala: tracking, consenso pertinente, follow-up, capacità, configurazione, maturazione ed evidenza economica proporzionati; nuova coorte realmente eseguita/chiusa/osservata quando necessaria.
- Test/simulazioni/eval fuori dai percorsi canonici; analisi e approvazione di budget non sono lancio.

## Scelte da conoscere

La review accetta una base approvata equivalente sufficiente alla spec: evita di bloccare una campagna soltanto per il nome/formato del documento, mantenendo il divieto di dichiararla pronta senza una base sufficiente. I requisiti economici sono condizionali alla decisione di spesa/scala; nessun conto economico universale imposto. Le richieste di produrre un file completano una bozza autorizzata senza chiedere una seconda autorizzazione al salvataggio; lo stato approvato richiede ancora l'approvazione del contenuto.

## Verifica

- quick_validate: 3/3 validi con `/private/tmp/ams-beta11-venv/bin/python`.
- Link Markdown locali: nessun riferimento mancante nei tre pacchetti.
- `git diff --check -- skills/design-campaign skills/campaign-review skills/campaign-debrief`: pulito.
- Lettura editoriale incrociata dei riferimenti modificati e dei confini conservati. Nessun nuovo test comportamentale eseguito da questo editor: non costituisce un audit indipendente.
- Nessuna modifica a fixture/eval, nessun commit, installazione o pubblicazione.

Il python3 di sistema mancava di PyYAML; la verifica definitiva sopra è stata eseguita nel venv comune, senza installazioni da parte dell'editor.

## Riconciliazione finale con copie installate

Confrontato soltanto il diff fra baseline repo e installazioni. `design-campaign` installata era 0.1.6: recepite la riconciliazione preliminare di date/fatti, la distinzione fra sconosciuto/rinviato/scelta esplicita, le domande economiche solo quando cambiano la campagna, il rispetto di scelte senza numero o nuova spesa e la validità del salvataggio per oggetto/destinazione/perimetro. Aggiunto il corrispondente criterio nel template. Versione finale design-campaign **0.1.7**, con INSTALL coerente: supera la versione 0.1.5 riportata nella fotografia iniziale sopra.

`campaign-review` e `campaign-debrief` installate sono identiche alle rispettive baseline in tutti i file (`diff -qr`, exit 0): nessuna correzione aggiuntiva da importare. Nessuna copia installata modificata, nessuna nuova prova eseguita; validazione finale centralizzata dal coordinatore.
