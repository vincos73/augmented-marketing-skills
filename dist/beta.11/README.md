# Augmented Marketing Suite beta.11

Undici skill specialistiche e Augmented Marketing Assistant per OpenAI/Codex. Sono incluse per la prima volta nella Suite `setup-brand-voice` e `write-marketing-copy`; tutte le skill hanno ricevuto la revisione Astra.

## Pacchetti

- [OpenAI/Codex](openai/augmented-marketing-suite-0.1.0-beta.11.zip): 12 skill, Assistant compreso, con metadati OpenAI.
- [Claude](claude/augmented-marketing-suite-claude-v0.1.0-beta.11.zip): 11 skill specialistiche, senza Assistant né metadati OpenAI.
- [Skill singole](agent-skills/): 11 ZIP portabili, ciascuno con una cartella radice, `SKILL.md` e riferimenti.
- [Manifest di sorgenti e pacchetti](manifest.json) e [SHA256SUMS](SHA256SUMS).

La release beta.11 è pubblicata con i suoi archivi e checksum. La copia OpenAI/Codex è installata localmente e verificata contro l’archivio; ciò non dimostra il caricamento in una sessione già aperta. Usa il pacchetto corrispondente all'ambiente e il flusso di installazione supportato; allegare un archivio a una chat non ne dimostra l'installazione.

## Riproduzione

Dalla radice del repository:

```sh
python3 scripts/build_suite.py
python3 scripts/build_suite.py --check
```

Il builder controlla inventario e versioni, esclude file di sistema e risorse non portabili, verifica ogni contenuto nello ZIP e produce archivi deterministici. `--check` non scrive e rileva pacchetti mancanti o diversi dalla sorgente corrente. Il commit nel manifest è la base del lavoro; gli hash dei singoli file identificano le modifiche locali effettivamente impacchettate.

[Rapporto di revisione e limiti delle prove](../../SUITE-REVIEW-BETA11.md).
