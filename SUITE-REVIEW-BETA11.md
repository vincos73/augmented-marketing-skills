# Augmented Marketing Suite — revisione beta.11

Aggiornato il 12 settembre 2026. **Esito: beta.11 integrata, installata localmente e pubblicata nel perimetro documentato.**

## Risultato

La Suite passa da nove a **undici skill specialistiche**, con `setup-brand-voice` e `write-marketing-copy`. Il plugin OpenAI/Codex contiene anche Augmented Marketing Assistant, per un totale di dodici; Claude e gli ZIP singoli conservano soltanto le specialistiche.

Tutte le dodici skill sono state revisionate applicando il documento allegato dall’utente, [Rethinking skills and prompts for GPT-6 Astra](evals/suite-beta11/astra-guidelines.md), e il `skill-creator` locale aggiornato. Non è stata necessaria ricerca web per applicare il materiale fornito.

## Sorgenti riconciliate

La base Git locale è `82688f5` e i manifesti del progetto erano alla beta.10. `setup-brand-voice` era già nel repository, ma esclusa dai pacchetti; `write-marketing-copy` è stata importata dalla copia locale installata 0.1.4.

Il confronto con le installazioni ha individuato revisioni più recenti di sette skill: contesto aziendale, sistema di marketing, sfida, direzione, mix, progettazione campagna e voce. Le correzioni successive sono state integrate nelle riscritture e le versioni incrementate oltre quelle installate. Fra queste: validità temporale delle fonti, continuità dei punti aperti, distinzione tra decisione rinviata e dato ignoto, soglie economiche richieste solo quando pertinenti, condizioni congiunte e impegni negli esempi di voce.

[Inventario e hash delle sorgenti d’ingresso](evals/suite-beta11/input-sources.json). Le installazioni sono state soltanto lette. Le modifiche preesistenti a `MARKETING-AGENT-SYSTEM.md`, `PROPOSTE-MIGLIORAMENTO-SUITE.md` e i materiali locali non pertinenti sono stati conservati. Nessun commit, push, modifica del marketplace pubblico o installazione è stato eseguito.

## Cambiamenti applicati

- **Scelta della skill:** description più corte e discriminanti; distinzione fra definire una voce, scegliere un contenuto e scrivere il testo. Il router include le due nuove skill e non impone onboarding a un incarico già chiaro.
- **Caricamento delle istruzioni:** entrypoint centrati su risultato, criteri e confini; modelli, installazione e casi specialistici sono consultati quando pertinenti. Rimosse ricette duplicate, conteggi rigidi di sezioni/parole e checklist generiche. I riferimenti stessi sono stati rivisti: il testo eliminato non è stato semplicemente spostato in un file da leggere comunque.
- **Continuità:** una richiesta di preparare un documento viene completata; una scrittura già autorizzata non richiede una conferma rituale. Le scelte non approvate restano in bozza. Salvataggio, installazione, produzione e azioni esterne conservano perimetri distinti.
- **Istruzioni del progetto:** aggiornati standard e portabilità. Non è presente un `AGENTS.md` applicabile nel repository da ripulire. Nei modelli che le skill usano per configurare AGENTS/CLAUDE, le letture diventano contestuali e gli import globali non sono più il default, preservando eventuali scelte esplicite dell’utente.
- **Distribuzione:** manifesti beta.11, archivio per ciascun ambiente, undici ZIP portabili, inventario e checksum. Nuovo builder riproducibile; la copia OpenAI/Codex installata localmente corrisponde all'archivio. I pacchetti beta.10 restano riferimenti storici.

Restano espliciti gli invarianti di dominio: fonti e ipotesi distinguibili; guida di voce non usata come prova dei claim; testi protetti conservati; un solo stato per ogni P; Place separato da Promotion; decisioni di CEO/Finance non assorbite dal marketing; review distinta da esecuzione; target, pendenti e maturazione conservati nel debrief; causalità non dedotta da un confronto descrittivo. Le skill rimangono utilizzabili anche su ambienti diversi da Astra, senza dipendenze nuove da subagent o connector.

## Versioni e misura del testo

Il confronto usa la sorgente locale più recente trovata per ogni skill, non soltanto le vecchie copie della beta.10. Il totale degli entrypoint passa da **22.500 a 9.942 parole (−55,8%)**. Entrypoint e riferimenti insieme passano da **46.546 a 32.070 parole (−31,1%)**.

Sono conteggi di parole con `str.split()`, frontmatter incluso, non token misurati, tempi di esecuzione o prova di maggiore efficacia. [Metriche riproducibili](evals/suite-beta11/metrics.json).

| Skill | Ingresso locale | Candidata | Parole entrypoint |
| --- | --- | --- | --- |
| `augmented-marketing-assistant` | 0.2.0 | 0.2.1 | 857 → 499 |
| `campaign-debrief` | 0.1.6 | 0.1.7 | 2312 → 989 |
| `campaign-review` | 0.1.3 | 0.1.4 | 1771 → 868 |
| `choose-marketing-direction` | 0.2.7 | 0.2.8 | 2234 → 939 |
| `content-director` | 0.1.1 | 0.1.2 | 1241 → 649 |
| `define-marketing-challenge` | 0.1.7 | 0.1.8 | 2053 → 905 |
| `define-marketing-mix` | 0.1.8 | 0.1.9 | 1705 → 969 |
| `design-campaign` | 0.1.6 | 0.1.7 | 2290 → 1109 |
| `setup-brand-voice` | 0.1.1 | 0.1.2 | 1512 → 692 |
| `setup-business-context` | 0.6.6 | 0.6.7 | 3292 → 820 |
| `setup-marketing-system` | 0.3.3 | 0.3.4 | 2087 → 900 |
| `write-marketing-copy` | 0.1.4 | 0.1.5 | 1146 → 603 |

## Verifica

**Struttura e pacchetti:** validatore `skill-creator` passato su 12/12 skill; YAML UI valido; riferimenti Markdown locali risolti. I 13 archivi superano integrità ZIP, confronto byte per byte con i sorgenti inclusi e rigenerazione deterministica nello stesso ambiente. `git diff --check` pulito. [Risultati strutturali](evals/suite-beta11/validation.json), [manifest e checksum](dist/beta.11/manifest.json).

**Prove sintetiche finali:** cinque casi eseguiti e letti dal coordinatore, senza problemi materiali rilevati sui criteri indicati. Due esecuzioni intermedie sono conservate separatamente; mix e voce sono stati riprovati dopo il recupero delle revisioni installate.

| Caso finale | Risultato osservato |
| --- | --- |
| [Copy con voce abituale inaccessibile](evals/suite-beta11/behavior/copy-a-response.md) | Copy utile e dichiarato provvisorio; richiesta di riferimento per la voce; nessun prezzo o promessa inventati. |
| [Content Brief richiesto su file](evals/suite-beta11/behavior/content-brief.md) | Documento completo realmente salvato in bozza senza nuova conferma; campione sintetico non generalizzato; nessuna produzione avviata. |
| [Sezione di voce con condizioni e impegno](evals/suite-beta11/behavior/voice-conditions.md) | Nota autonoma completa, condizioni entrambe necessarie, testo approvato identico, verifica non iniziata e impegno entro venerdì conservati; nuovo esempio in bozza. |
| [Marketing mix finale](evals/suite-beta11/behavior/mix-final-response.md) | Product/Price restano decisioni esterne, accesso distinto dalla comunicazione, webinar non promosso a scelta, capacità e confronto fra ruoli preservati. |
| [Debrief con pendenti e proposta di scala](evals/suite-beta11/behavior/debrief-response.md) | Target non retrodatato né dichiarato raggiunto; totale e pendenti visibili; storico non comparabile escluso; nessuna causalità attribuita; ampliamento sospeso e lavoro sul perimetro corrente indicato. |

Sono prove incrociate tra autori, svolte nello stesso ambiente, con prompt e output conservati e scritture di prova solo nell’area temporanea autorizzata. Non sono prove blind, receipt host verificate, una campagna end-to-end su tutte le skill o test su Claude/ChatGPT. Le cinque prove non misurano efficacia con marketer reali né tutte le modalità delle dodici skill.

**Runner storico:** sulla baseline Git estratta in un’area temporanea passa tutte le otto verifiche statiche. Sulla candidata, i primi cinque gruppi passano; adapter/provenance/readiness rifiutano hash e versioni diversi da quelli congelati per beta.10 (`P003`, `M026`, con errori derivati nei self-test). Il rifiuto è stato verificato, non aggirato aggiornando prove storiche. Non si dichiara il runner interamente verde sulla beta.11 né un nuovo `BEHAVIOR_PASS`. [Output baseline](evals/suite-beta11/legacy-runner-on-baseline.json), [output candidata finale](evals/suite-beta11/legacy-runner-on-candidate.json).

## Organizzazione del lavoro

Tre subagent riutilizzati, senza ulteriori delegazioni: fondazione/strategia; campagne; voce/copy/contenuti. Ogni editor ha modificato solo i percorsi assegnati. Il coordinatore ha gestito fonti e versioni, Assistant, standard, pacchetti e controlli. Le prove sono state assegnate a un autore diverso da quello della skill, con materiale circoscritto. Le letture dei diff installati hanno evitato di rifare la progettazione o rieseguire tutti gli eval storici.

## Ripresa e distribuzione

- [Pacchetti beta.11](dist/beta.11/README.md).
- [Builder](scripts/build_suite.py): `python3 scripts/build_suite.py`; controllo senza scrittura: `python3 scripts/build_suite.py --check`.
- [Evidenze della sessione](evals/suite-beta11/README.md).

La beta.11 è pubblicata e la copia OpenAI/Codex è installata localmente. Caricamento in una nuova sessione, prove su altri runtime e pilot restano non eseguiti. Se si richiede la certificazione end-to-end del runner storico sulla nuova Suite, occorre creare un nuovo perimetro di capture/readiness per beta.11 e acquisire prove effettive, senza promuovere le fixture precedenti a evidenza del nuovo comportamento.
