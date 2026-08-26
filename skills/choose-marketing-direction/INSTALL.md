# Installare `choose-marketing-direction`

Questo pacchetto contiene solo la skill installabile. Non contiene Business Identity, Fondamenti di marketing, Brief della sfida, Direzioni di marketing o file `AGENTS.md`/`CLAUDE.md` dell'organizzazione.

La versione di questa sorgente è `0.2.0`. Una modifica della sorgente non implica che esistano già un tag o una release pubblica con la stessa versione.

## Installazione da ZIP

1. Scarica lo ZIP ufficiale della versione che vuoi installare; per questa release deve dichiarare `0.2.0` in `SKILL.md`.
2. Verifica lo ZIP con il relativo `SHA256SUMS` quando previsto dalla release.
3. Estrai lo ZIP. Deve contenere una sola cartella radice: `choose-marketing-direction/`.
4. Copia la cartella in `~/.codex/skills/`.

Il percorso finale deve essere:

```text
~/.codex/skills/choose-marketing-direction/SKILL.md
```

Se esiste già una copia con lo stesso nome, conservala come backup prima di sostituirla e verifica quale versione stai rimpiazzando.

## Verifica

Apri le prime righe di `SKILL.md` e verifica:

```yaml
name: choose-marketing-direction
metadata:
  version: "0.2.0"
```

L'installazione sul disco non dimostra che una sessione già aperta abbia caricato la skill. Avvia una nuova attività o sessione prima del test.

## Installazione dalla sorgente GitHub

Chi usa lo Skill Installer può installare la sorgente dal percorso `skills/choose-marketing-direction`, fissando il tag `choose-marketing-direction-v0.2.0` che contiene la versione `0.2.0`. Questo metodo non sostituisce la verifica della versione e della destinazione locale.
