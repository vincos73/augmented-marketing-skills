---
target: skills/setup-business-context/SKILL.md
total_score: 34
max_score: 40
na_heuristics: 
p0_count: 0
p1_count: 3
timestamp: 2026-08-24T15-32-20Z
slug: skills-setup-business-context-skill-md
---
⚠️ DEGRADED: single-context (spawn_agent unavailable in this session)

# Review UX della skill `setup-business-context`

**Modalità valutata:** Operate/Read ibrida — onboarding conversazionale, gestione di fonti e approvazioni.
**Target:** `skills/setup-business-context/SKILL.md` e riferimenti operativi collegati.

## Design Health Score

| # | Euristica | Punteggio | Osservazione |
|---|---|---:|---|
| 1 | Visibilità dello stato del sistema | 3/4 | Fasi, gate e stati sono espliciti; manca una sintesi unica del percorso da mostrare al manager. |
| 2 | Corrispondenza con il mondo reale | 4/4 | Parla di fonti, ruoli, prove, approvazioni e limiti in termini utili a un manager. |
| 3 | Controllo e libertà dell'utente | 4/4 | Nessuna scrittura automatica; approvazione dell'identità e installazione sono separate. |
| 4 | Coerenza e standard | 3/4 | Le etichette canoniche sono ora italiane, ma il lessico interno resta misto e gli stati sono duplicati in più file. |
| 5 | Prevenzione degli errori | 4/4 | Protegge privacy, conflitti, fonti non attendibili, prove pubbliche e istruzioni incorporate. |
| 6 | Riconoscimento invece di memoria | 3/4 | Marker e template aiutano, ma la tassonomia degli stati richiede ancora spiegazione. |
| 7 | Flessibilità ed efficienza | 4/4 | Chat-first, massimo tre domande, quattro-sei gruppi e limite di circa 450 parole. |
| 8 | Design minimale | 3/4 | L'output previsto è compatto; la skill e il template restano densi per chi deve mantenerli. |
| 9 | Recupero dagli errori | 3/4 | Gestisce fonti parziali, conflitti e workspace non scrivibili; manca una procedura compatta per risolvere overflow e ambiguità linguistiche. |
| 10 | Aiuto e documentazione | 3/4 | Routing, template e installazione sono completi, ma distribuiti e parzialmente in inglese. |
| **Totale** |  | **34/40** | **Solido, con frizioni di coerenza e handoff.** |

## Design Specificity Verdict

La skill è chiaramente progettata per questo prodotto: chat-first, provenance markers, due gate, distinzione tra identità e strategia, protezione delle prove e divieto di trasporto visuale automatico. Non è un onboarding generico.

Il detector Impeccable ha restituito `[]`. È un risultato pulito ma limitato: il target è Markdown e non contiene markup o una superficie visuale da analizzare. Non sono applicabili browser inspection, overlay, live server o screenshot.

## Impressione complessiva

La direzione è corretta e molto più matura del questionario visuale originario. Il principale rischio residuo non è il flusso: è la possibilità che agenti diversi interpretino in modo diverso le etichette, gli stati e il grado di compattezza richiesto.

## Cosa funziona

- Il chat-first è una scelta netta: evita attese, stato tecnico e UI non affidabile.
- I due gate proteggono bene il confine tra “identità approvata” e “disponibilità per gli agenti”.
- Privacy, conflitti, fonti non attendibili e prove pubbliche sono trattati come vincoli operativi, non come note decorative.

## Priority Issues

### [P1] Localizzazione a due livelli

**Perché conta:** il manager-facing contract richiede italiano, ma la skill, il routing e le note operative contengono ancora etichette e descrizioni inglesi (`standalone brand`, `approved identity`, `known unknowns`). Un output può quindi risultare formalmente corretto ma linguisticamente ibrido.

**Fix:** definire una tabella unica “lessico manager-facing” e specificare quali termini restano tecnici o interni. Applicarla a SKILL, template, routing, eval e installazione.

**Suggested command:** `$impeccable clarify`

### [P1] Stati duplicati in più fonti

**Perché conta:** gli stati ora sono coerenti, ma vivono in SKILL.md, template, expert routing, catalogo eval e fixture. Alla prossima modifica possono divergere di nuovo.

**Fix:** mantenere un piccolo registro canonico degli stati con significato, esempio e regola d'uso; fare referenziare gli altri documenti a quel registro o verificarli con un eval strutturale.

**Suggested command:** `$impeccable harden`

### [P1] Compattezza dichiarata, non ancora vincolante

**Perché conta:** “circa 450 parole”, quattro-sei gruppi e due frasi per gruppo sono ottimi obiettivi, ma non definiscono cosa succede quando le fonti sono molto dense. Il rischio è tornare a comprimere troppo o perdere un vincolo critico.

**Fix:** aggiungere una procedura di overflow: prima comprimere descrizione, poi rinviare dettaglio, mai eliminare privacy/prove/approvazioni; aggiungere un controllo automatico su gruppi, domande, parole e token canonici.

**Suggested command:** `$impeccable distill` + `$impeccable harden`

### [P2] Handoff di installazione poco visibile

**Perché conta:** la skill separa correttamente l'installazione, ma chi scarica lo ZIP deve ancora capire il percorso minimo di installazione e il rapporto tra package, runtime locale e nuova sessione.

**Fix:** includere nel pacchetto una breve `INSTALL.md` con percorso supportato, verifica della versione e avvertenza sul riavvio della sessione.

**Suggested command:** `$impeccable onboard`

## Persona Red Flags

**Jordan — manager al primo utilizzo**

- Il primo output è breve, ma marker `[S1]`, stati canonici e due gate introducono tre nuovi concetti insieme.
- Le etichette italiane aiutano; le descrizioni inglesi rimaste nei riferimenti possono però riemergere nel template.
- Rischio: approvare correttamente il contenuto senza capire che l'installazione runtime è una decisione separata.

**Alex — power user / responsabile del sistema**

- Può verificare versioni, fonti e gate, ma deve ricostruire la regola degli stati da più file.
- Il package è scaricabile, ma manca una guida installativa breve direttamente nello ZIP.
- Rischio: modificare una copia locale e non sapere quale registro aggiornare per mantenere la coerenza.

**Marta — referente privacy/compliance**

- Trova buoni divieti su dati personali, prove e claims non approvati.
- La distinzione tra `non stabilito dalle fonti fornite` e `non definito` è corretta ma richiede una spiegazione orientata alla decisione.
- Rischio: interpretare un'assenza documentale come assenza organizzativa se l'agente non mostra sempre la spiegazione breve accanto allo stato.

## Osservazioni minori

- `non stabilito dalle fonti fornite` è semanticamente preciso ma lungo: va mantenuto come token canonico, accompagnandolo con una parafrasi breve quando serve.
- I nomi tecnici dei file e i marker `[S1]`/`[C]` devono restare invariati per compatibilità.
- La versione `0.4.1` e il package versionato sono un buon fondamento per verificare regressioni tra release.
- Il detector pulito non sostituisce un eval conversazionale: qui il comportamento reale va misurato con fixture e transcript.

## Questions to Consider

- Il prossimo intervento deve privilegiare **coerenza linguistica completa**, **compattezza verificabile** o **handoff di installazione**?
- Vuoi mantenere l'inglese nei documenti rivolti principalmente al modello, localizzando solo l'output manager-facing, oppure portare in italiano anche tutto il materiale operativo?
- Per la prossima versione preferisci correggere solo le priorità P1 oppure includere anche `INSTALL.md` e una verifica automatica degli stati?
