# Smoke test runtime Codex di Augmented Marketing Assistant beta.4

**Data:** 2026-08-27

**Versione verificata:** 0.1.0-beta.4

**Ambiente:** tre processi Codex effimeri separati, fuori dal repository e con sandbox in sola lettura

**Modello:** configurazione predefinita dell'ambiente, non fissata dal test

**Vincoli comuni:** nessun uso di memorie, file di progetto o Internet; sole skill installate pertinenti

## Risultati

| Caso | Skill effettivamente lette | Comportamento osservato | Esito |
| --- | --- | --- | --- |
| Richiesta ambigua: “Dobbiamo sistemare il marketing.” | `augmented-marketing-assistant` | Ha posto una sola domanda con opzioni comprensibili, ma ha omesso il caso di un'attività già definita | SOFT FAIL |
| Richiesta specialistica esplicita | `choose-marketing-direction` | Ha selezionato direttamente la skill richiesta senza caricare l'Assistant e ha chiesto il contenuto del brief non accessibile | PASS |
| Prerequisito mancante | `augmented-marketing-assistant`, poi `define-marketing-challenge` e la reference pertinente | Ha riconosciuto che abbonamento e corso erano soluzioni premature; la skill specialistica ha assunto il workflow e formulato la sfida provvisoria | PASS |

## Evidenza dell'handoff

Il caricamento non è stato dedotto dalla risposta. I log runtime mostrano la lettura di:

- `skills/augmented-marketing-assistant/SKILL.md` per la richiesta ambigua;
- `skills/choose-marketing-direction/SKILL.md` per l'invocazione diretta;
- `skills/augmented-marketing-assistant/SKILL.md`, poi `skills/define-marketing-challenge/SKILL.md` e `references/question-routing.md` per il prerequisito mancante.

Questo dimostra che, nell'ambiente Codex testato, l'Assistant può passare realmente il lavoro a una skill specialistica. Non dimostra che il routing sia deterministico in ogni configurazione o con ogni catalogo di skill.

## Soft fail da correggere

La domanda per la richiesta completamente generica ha distinto contesto, regole stabili, sfida, direzione e marketing mix, ma non ha offerto l'alternativa di un'attività esecutiva già definita. Il contratto richiede invece di distinguere almeno:

1. contesto dell'organizzazione;
2. regole stabili;
3. decisione specifica;
4. attività già definita.

La correzione dovrebbe restare circoscritta alla formulazione della domanda ambigua. Non serve introdurre un agente Strategist né modificare il routing specialistico, che nei due casi pertinenti ha funzionato.

## Condizioni osservate

Il runtime ha avvertito che, a causa dell'ampiezza del catalogo installato, alcune descrizioni delle skill erano state abbreviate pur restando visibili. Ha inoltre ignorato metadati non validi appartenenti a skill esterne alla Suite. Questi warning non hanno impedito i tre test, ma possono aumentare la variabilità della selezione automatica e vanno distinti dal comportamento di Augmented Marketing Suite.

## Verdetto

Il routing reale in Codex è dimostrato nei casi di invocazione diretta e prerequisito mancante. La beta.4 non supera ancora completamente lo smoke test: resta un soft fail nella gestione delle richieste totalmente generiche.
