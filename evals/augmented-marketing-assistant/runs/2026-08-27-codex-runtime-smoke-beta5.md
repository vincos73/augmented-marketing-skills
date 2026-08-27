# Regression test runtime Codex di Augmented Marketing Assistant beta.5

**Data:** 2026-08-27

**Versione verificata:** 0.1.0-beta.5

**Ambiente:** tre processi Codex effimeri separati, fuori dal repository e con sandbox in sola lettura

**Modello:** configurazione predefinita dell'ambiente, non fissata dal test

**Vincoli comuni:** nessun uso di memorie, file di progetto o Internet; sole skill installate pertinenti

## Risultati

| Caso | Skill effettivamente lette | Comportamento osservato | Esito |
| --- | --- | --- | --- |
| Richiesta ambigua: “Dobbiamo sistemare il marketing.” | `augmented-marketing-assistant` | Ha posto una sola domanda con le quattro categorie richieste, inclusa l'attività già definita, senza esporre i passaggi interni dello Strategy Core | PASS |
| Richiesta specialistica esplicita | `choose-marketing-direction` | Ha selezionato direttamente la skill richiesta senza caricare l'Assistant e ha chiesto il contenuto del brief non accessibile | PASS |
| Prerequisito mancante | `augmented-marketing-assistant`, poi `define-marketing-challenge` e le reference pertinenti | Ha riconosciuto che abbonamento e corso erano soluzioni premature; la skill specialistica ha assunto il workflow e formulato la sfida provvisoria | PASS |

## Evidenza del caricamento

I log runtime mostrano la lettura di:

- `skills/augmented-marketing-assistant/SKILL.md` per la richiesta ambigua;
- `skills/choose-marketing-direction/SKILL.md` per l'invocazione diretta;
- `skills/augmented-marketing-assistant/SKILL.md`, poi `skills/define-marketing-challenge/SKILL.md` e le reference necessarie per il prerequisito mancante.

La regressione non si limita quindi alla conformità del testo: verifica selezione diretta e handoff effettivo nell'ambiente Codex testato.

## Condizioni osservate

Il runtime ha avvertito che alcune descrizioni delle skill erano state abbreviate per il budget del catalogo e ha ignorato metadati non validi appartenenti a skill esterne alla Suite. Questi warning non hanno impedito i tre PASS, ma il test non dimostra comportamento deterministico in ogni catalogo o ambiente.

## Verdetto

La beta.5 supera lo smoke test con tre PASS e nessun hard o soft fail. Il comportamento può essere promosso come Augmented Marketing Assistant v0.1.0, mantenendo separata la maturità ancora beta di Augmented Marketing Suite.
