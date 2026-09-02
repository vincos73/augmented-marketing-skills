# Che cosa deve dimostrare la beta.11

Piano di review della Augmented Marketing Suite alla beta.10, preparato il 1 settembre 2026 sul commit `5c5a39f` (tag `augmented-marketing-suite-v0.1.0-beta.10`).

## Tesi

La beta.10 ha reso la Suite verificabile. Non ha ancora reso verificabile che serva a un marketer più di un buon prompt. Il rischio principale non è un comportamento sbagliato: è un investimento sproporzionato in governance della prova rispetto alla prova stessa, su una base utenti che oggi non esiste. Questa review misura l'utilità marginale, non la conformità.

Tre conseguenze pratiche per il disegno della review:

- **Ogni lente ha un confronto.** Nessun test misura la skill in isolamento: sempre skill contro prompt disciplinato, sempre stessa fixture, stesso modello.
- **Persone prima delle receipt.** Almeno due marketer esterni e un caso reale anonimizzato entrano nel campione. La provenance host è opzionale per questa review.
- **Fixture nuove.** Fabriloom è usata da sei eval diversi ed è ormai un caso su cui le skill sono state affinate. Serve materiale mai visto.

## 1. Fotografia della beta.10

Osservato sul repository allineato a `origin/main`:

| Misura | Valore |
|---|---|
| Skill nel sorgente | 10 (9 nel bundle Claude, 10 in quello OpenAI/Codex) |
| Parole di istruzioni (SKILL.md + references) | 38.251 |
| Righe Python di checker e self-test in `evals/` | 5.902 |
| Righe aggiunte da beta.9 a beta.10 | 9.304, di cui 24 nelle skill |
| Test con un utente reale | 1 (il proprietario, `design-campaign` v0.1.2) |
| Pilot con marketer esterni | 0 |
| Stelle sul repository / download per beta | 0 / ~14 |

La beta.10 aggiunge quasi esclusivamente infrastruttura di prova: contratto di stato comune, lineage di campagna, ledger di autorizzazione, provenance comportamentale con receipt SHA-256 e una matrice di readiness a cinque stati. L'unica modifica di comportamento è la baseline decisionale di `campaign-review` v0.1.3. Il runner statico passa in locale; il gate comportamentale è progettato per fallire senza una capture host esterna, e infatti fallisce.

Le evidenze di valore per l'utente sono più vecchie e più deboli dell'infrastruttura. Il retest cieco del 27 agosto ha misurato un vantaggio quasi nullo delle skill di fondazione rispetto a una baseline disciplinata (+0,06 su 5), con `setup-marketing-system` in negativo. Il forward test successivo ha confrontato solo vecchia e nuova versione, non skill contro assenza di skill. I valutatori sono sempre stati modelli con una persona assegnata, mai marketer.

## 2. Rilievi già emersi dall'ispezione

Da correggere o decidere prima o durante la review.

**R1 — Il report di readiness pubblicato contraddice la release.**
Al tag della beta.10 il repository dichiara `candidate_ready: false` e `package_state: not_built`, mentre la release è pubblicata lo stesso giorno. Il report è per disegno una vista pre-package, ma chi legge il tag vede una candidata non pronta distribuita come beta. Va aggiunto uno stato post-release o il report va datato e chiuso.
*File: `evals/robustness/runtime-readiness/READINESS-REPORT.md`, `candidate-readiness.json`*

**R2 — Il README della provenance è fermo alla beta.9.**
Il documento vincola il run comportamentale al commit `561dc93` e parla di «nove invocazioni reali delle skill beta.9»; l'allowlist canonica punta invece a `2bed5fb`. Chi prepara una capture seguendo il README produce un run che il checker respinge.
*File: `evals/behavioral-provenance/README.md` righe 3, 11, 133, 140; `runtime-allowlist.json`*

**R3 — Il commit vincolato non è il commit del tag.**
L'allowlist accetta solo `2bed5fb` mentre il tag punta a `5c5a39f`. Il vincolo è sul commit e non sui digest delle directory skill, quindi una capture eseguita sul tag pubblicato fallirebbe pur usando byte identici. Verificare se il checker confronta anche i digest e, in tal caso, rilassare il vincolo sul commit.
*File: `evals/behavioral-provenance/runtime-allowlist.json`, `scripts/check_provenance.py`*

**R4 — Le superfici Claude non sono mai state provate sulla candidata.**
La matrice segna `not_run` Claude Code, Claude Desktop e Claude Cloud. Il bundle Claude non contiene l'Assistant, quindi il routing dipende solo dalle description delle skill: nessun test verifica che una richiesta naturale attivi la skill giusta in Claude.
*File: `READINESS-REPORT.md` tabella superfici; `claude/README.md`; `dist/claude/`*

**R5 — Nessuna skill è stata riconfrontata con una baseline dopo le correzioni.**
Il retest cieco ha trovato `setup-marketing-system` sotto la baseline disciplinata. La v0.3.0 è stata poi confrontata solo con la v0.2.1. Per Campaign Core esiste un solo confronto matched-input (debrief, «vantaggio stretto sul buon generalista»). Il claim di utilità della Suite è oggi sostenuto da un test del 27 agosto su due skill.
*File: `evals/comparative-blind/2026-08-27-retest/report.md`, `2026-08-27-forward-v2/report.md`*

**R6 — Prolissità e ridondanza osservate, corrette, mai riverificate sul dialogo intero.**
L'unico test con utente reale ha rilevato piano riscritto a ogni turno, gate troppo esteso e tentativo di scrittura canonica in modalità test. I retest successivi valutano solo la prima risposta standalone.
*File: `evals/design-campaign/runs/2026-08-29-vincos-guide-user-test-v0.1.2.md`, retest v0.1.4*

**R7 — Regole comuni duplicate in ogni SKILL.md.**
Lo standard di progettazione non è caricato a runtime, quindi ogni skill ripete linguaggio, gate, test mode e fallback. La frase sui percorsi canonici compare in 8 file su 10, il tetto delle tre domande in 9. Ogni patch allo standard richiede dieci modifiche coordinate e una release per ciascuna.
*File: `STANDARD-PROGETTAZIONE-SKILL.md`; `skills/*/SKILL.md`*

**R8 — Carico di istruzioni molto disomogeneo.**
Da 857 parole dell'Assistant a 3.141 di `setup-business-context`, più references. Non esiste un budget di parole per SKILL.md analogo a quello imposto alle risposte, né una misura dell'effetto della lunghezza sulla qualità.
*File: `skills/setup-business-context/SKILL.md`, `skills/campaign-debrief/SKILL.md`*

**R9 — Residui di manutenzione.**
La PR #3 è aperta dal 25 agosto su un branch già unito. `CAMPAIGN-CORE-STATUS.md` descrive ancora branch di lavoro e prossimi passi già eseguiti. `MARKETING-AGENT-SYSTEM.md` è a 80 KB e mescola architettura, registro decisioni e stato.
*File: PR #3; `CAMPAIGN-CORE-STATUS.md`*

## 3. Le cinque lenti

Ogni lente ha una domanda, un metodo, un'evidenza e un criterio di esito.

### A — Utilità marginale per il marketer

**Domanda:** su un caso mai visto, la skill batte un prompt disciplinato di 80 parole?

**Metodo:** per ciascuna delle nove skill, due fixture nuove e sintetiche più un caso reale anonimizzato. Tre condizioni sullo stesso input e stesso modello: baseline libera, baseline disciplinata (tracciabilità, gap, fonti, tre domande), skill. Giudizio cieco pairwise con ordine invertito.

**Giudici:** Vincenzo più due marketer esterni per il caso reale; un giudice modello con la rubrica esistente per le fixture sintetiche. I due giudizi restano separati nel report.

**Misure:** gap medio su 5 per dimensione (rubrica del retest, riusata); preferenza cieca in percentuale; minuti di correzione stimati dal giudice umano prima di poter approvare.

**Esito:** una skill è **confermata** se supera la baseline disciplinata in almeno 2 fixture su 3 senza hard fail; **da rivedere** se pareggia; **da congelare** se è sotto in 2 su 3.

### B — Esperienza del dialogo completo

**Domanda:** dal primo turno al gate, quante parole, domande e ripetizioni costa arrivare a un documento approvabile?

**Metodo:** conversazione intera fino all'approvazione su una fixture per skill, con risposte del responsabile predefinite. Copre il turno di follow-up, il gate e il comportamento in modalità test. Non solo la prima risposta.

**Misure:** parole per turno e per intero dialogo; numero di domande e domande che chiedono cose già fornite; decisioni ripresentate senza cambiamento; tentativi di scrittura fuori autorizzazione; turni fino al gate.

**Esito:** confronto con i budget dello standard (250-350 parole, tetto 500, tre domande). Ogni scostamento diventa un rilievo con severità, non un fail automatico.

### C — Portabilità reale sui runtime

**Domanda:** il pacchetto si installa, si carica e si attiva con una richiesta naturale in Claude, ChatGPT e Codex?

**Metodo:** matrice a quattro superfici: Claude Desktop con il plugin, Claude Code con la cartella skills, ChatGPT con uno ZIP singolo, Codex CLI con il bundle OpenAI. Per ciascuna: installazione, visibilità in sessione nuova, dieci richieste naturali in italiano e verifica di quale skill si attiva.

**Misure:** installato / caricato / attivato per superficie; precisione del routing per description (Claude) e per Assistant (OpenAI); fallback su workspace non scrivibile osservato.

**Esito:** aggiorna la matrice di readiness con stati `runtime_loaded_verified` reali. Chiude R4. Se il routing per description in Claude è sotto 8 su 10, le description vanno riscritte prima della beta.11.

### D — Sorgente e manutenibilità

**Domanda:** quanto costa cambiare una regola comune, e quanto della documentazione è ancora vera?

**Metodo:** audit statico — mappa delle sezioni duplicate tra SKILL.md, budget di parole per skill, coerenza tra README, INSTALLAZIONE, PORTABILITA, CAMPAIGN-CORE-STATUS e readiness report. Prova pratica: applicare una modifica allo standard e contare i file da toccare.

**Misure:** percentuale di testo comune per skill; parole per SKILL.md e per references; affermazioni di stato non più vere nei documenti.

**Esito:** decidere tra tre modelli — mantenere la duplicazione, estrarre un `references/common.md` incluso in ogni pacchetto, oppure comprimere le sezioni comuni a un paragrafo con rimando. Chiude R1, R2, R7, R8, R9.

### E — Proporzione dell'infrastruttura di prova

**Domanda:** quale decisione ha cambiato, finora, ciascun checker? Quale ne cambierà una nei prossimi tre mesi?

**Metodo:** per ogni gate (provenance, readiness, ledger, lineage, cross-core, raw-to-snapshot, state contract) — chi lo esegue, quando, quale errore reale ha intercettato, quante righe costa mantenere. Confronto con la spesa in test comportamentali e con persone.

**Misure:** righe di codice e self-test per gate; errori reali intercettati dal gate (non dai self-test); ore stimate per adattarlo a una nuova beta.

**Esito:** classificare ogni gate come **core**, **congelato** (resta ma non evolve) o **archiviato**. Obiettivo esplicito: nella beta.11 le righe aggiunte alle skill superino quelle aggiunte ai checker.

## 4. Protocollo in tre settimane

Le lenti statiche prima, le persone dopo, la decisione alla fine.

**Settimana 1 — Lenti D ed E, più correzioni immediate.**
Chiudere R1, R2, R3 e R9 con una PR di manutenzione. Produrre la mappa delle duplicazioni e l'inventario dei gate. Preparare le nove coppie di fixture nuove e i tre prompt baseline. Nessuna modifica alle skill in questa fase: la review misura la beta.10 così com'è.

**Settimana 2 — Lenti A, B e C.**
Generazione delle tre condizioni per skill, giudizio cieco con modello, dialoghi completi, matrice runtime a quattro superfici. In parallelo, coinvolgere i due marketer esterni: brief di 30 minuti, un caso ciascuno, giudizio su coppie anonime.

**Settimana 3 — Sintesi e decisione.**
Report unico con esito per skill e per gate, applicazione delle regole di decisione, backlog della beta.11 ordinato per impatto sull'utilità misurata. Aggiornamento dei documenti di stato e del readiness report con gli stati realmente verificati.

### Regole di condotta della review

- Le fixture della review non entrano in `evals/` finché la review non è chiusa, per evitare che le correzioni si adattino ai casi di prova.
- I giudizi umani e quelli del modello non si sommano. Se divergono, prevale l'umano e la divergenza è un rilievo sulla rubrica.
- Nessuna scrittura nei percorsi canonici, nessuna release, nessuna modifica di versione durante la review.
- Ogni run registra modello, data, versione della skill e commit, in un file per run come già avviene.

## 5. Regole di decisione

Concordate prima di vedere i risultati.

1. **Skill sotto la baseline disciplinata in 2 fixture su 3:** congelata alla versione corrente, esclusa dalla beta.11 o unita a una skill adiacente. Candidate naturali all'unione: `setup-business-context` e `setup-marketing-system`, che condividono onboarding, gate e installazione.
2. **Skill che pareggia:** resta, ma la beta.11 deve portare una modifica mirata alla dimensione più debole, riverificata con lo stesso protocollo.
3. **Routing per description in Claude sotto 8 su 10:** riscrittura delle description prima di qualsiasi altra modifica; il bundle Claude non viene ripubblicato finché non passa.
4. **Gate senza errori reali intercettati:** congelato. Non riceve nuove regole né self-test nella beta.11.
5. **Dialogo che supera del 50% il budget di parole in 2 skill su 3:** la sezione «prima risposta utile» dello standard viene riscritta come istruzione comune, non rattoppata skill per skill.
6. **Nessun marketer esterno disponibile entro la settimana 2:** la review si chiude comunque, ma il report dichiara che le lenti A e B restano sintetiche e la beta.11 non può usare la parola «validata».

## 6. Ipotesi da mettere alla prova

Non decisioni. Ogni ipotesi ha una lente che la conferma o la smentisce.

| Ipotesi | Se vera, cosa cambia | Lente |
|---|---|---|
| Il valore della Suite è concentrato in Campaign Core (spec, review, debrief), dove il metodo è meno ovvio per un generalista. | La beta.11 si presenta a partire dalla campagna; le fondazioni diventano opzionali e più corte. | A |
| Un prompt disciplinato eguaglia le due skill di fondazione. | Le due skill si uniscono in un solo onboarding da 1.500 parole con un unico gate. | A, D |
| Metà di ogni SKILL.md è regola comune ripetuta. | Un file comune incluso in ogni pacchetto; SKILL.md sotto le 1.200 parole. | D |
| La prolissità nasce al gate, non al primo turno. | Il contratto di revisione compatta diventa unico e condiviso, con un tetto proprio. | B |
| In Claude le richieste naturali in italiano non attivano la skill giusta senza l'Assistant. | Description riscritte con i termini che un marketer usa davvero; eventuale skill di orientamento anche per Claude. | C |
| Nessun gate di provenance ha mai intercettato un errore che un diff e un run letto da una persona non avrebbero visto. | Provenance e readiness congelati; il tempo va ai pilot. | E |
| Chi scarica la beta non riesce a installarla al primo tentativo. | Un percorso di dieci minuti in cima al README, una superficie alla volta; il resto scende in INSTALLAZIONE. | C |

## 7. Output attesi

- **Report della review** in `evals/suite-review/2026-09/`: esito per skill sulle lenti A e B, matrice runtime aggiornata, inventario dei gate, rilievi R1–R9 chiusi o riassegnati.
- **Backlog della beta.11** ordinato per impatto sull'utilità misurata, con le regole di decisione applicate e motivate.
- **Documenti di stato corretti**: readiness report con stati verificati, `CAMPAIGN-CORE-STATUS.md` chiuso o aggiornato, README della provenance allineato al commit corretto.
- **Due giudizi umani esterni** archiviati come prima evidenza non sintetica della Suite.

Ciò che la review non produce: nuove versioni delle skill, release, claim pubblici di efficacia. Quelli vengono dopo, sulla base di quello che la review avrà misurato.

---

*Piano preparato il 1 settembre 2026 sul repository `vincos73/augmented-marketing-skills` al commit `5c5a39f`. I numeri della fotografia derivano da conteggi diretti sul sorgente e dalle API GitHub; le valutazioni comparative citate sono quelle già archiviate in `evals/comparative-blind/`.*
