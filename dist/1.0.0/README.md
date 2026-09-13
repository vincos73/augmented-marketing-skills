# Augmented Marketing Suite 1.0.0

Questo artefatto locale della release stabile contiene 13 archivi: due plugin completi da dodici skill e undici skill specialistiche portabili. L'Assistant resta incluso solo nei plugin completi e mantiene la versione `0.3.0`.

## Pacchetti

- [OpenAI/Codex](openai/augmented-marketing-suite-1.0.0.zip): 12 skill, con metadati OpenAI.
- [Claude](claude/augmented-marketing-suite-claude-v1.0.0.zip): 12 skill, senza directory `agents`.
- [Skill singole](agent-skills/): 11 archivi, uno per ogni skill specialistica.
- [Manifest](manifest.json) e [SHA256SUMS](SHA256SUMS): inventario e digest verificabili.

L'archivio Claude ha SHA-256 `f5791493d384d8ad798c0d8fca2fd6dddbfb9a976e254a3c5a2491eb80ae147d`. Il marketplace Claude indirizza alla [release GitHub pubblicata `augmented-marketing-suite-v1.0.0`](https://github.com/vincos73/augmented-marketing-skills/releases/tag/augmented-marketing-suite-v1.0.0); questo artefatto locale mantiene la stessa struttura della distribuzione.

## Riproduzione e verifica

```sh
python3 scripts/build_suite.py
python3 scripts/build_suite.py --check
```

Il manifest usa lo stato neutro `built`: descrive il completamento della build, senza fare affermazioni sull'installazione. `--check` conserva il commit di provenienza registrato e confronta ogni byte di sorgenti, archivi, manifest e checksum.

Gli asset di una release GitHub sono distribuiti in una directory piatta, mentre `SHA256SUMS` conserva i percorsi relativi di `dist/1.0.0`. Per una verifica automatica dopo il download, ricolloca i file nelle directory indicate dal [manifest](manifest.json); in alternativa confronta il digest del singolo archivio con il valore riportato nel manifest o nel marketplace.
