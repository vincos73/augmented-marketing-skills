# Installare `define-marketing-mix`

Questo pacchetto contiene solo la skill installabile. Non contiene Business Identity, Fondamenti di marketing, Brief della sfida, Direzioni di marketing, Marketing Mix o file `AGENTS.md`/`CLAUDE.md` dell'organizzazione.

La versione corrente della sorgente è `0.1.10`. Una modifica della sorgente non implica che esistano già un tag o una release pubblica con la stessa versione.

## Installazione da ZIP

1. Se installi da uno ZIP pubblicato, verifica che la versione dichiarata nel suo `SKILL.md` corrisponda a quella che hai scelto.
2. Verifica lo ZIP con il relativo `SHA256SUMS` quando previsto dalla release.
3. Estrai lo ZIP. Deve contenere una sola cartella radice: `define-marketing-mix/`.
4. Copia la cartella in `~/.codex/skills/`.

Il percorso finale deve essere:

```text
~/.codex/skills/define-marketing-mix/SKILL.md
```

Se esiste già una copia con lo stesso nome, conservala come backup prima di sostituirla e verifica quale versione stai rimpiazzando.

## Verifica

Apri le prime righe di `SKILL.md` e verifica:

```yaml
name: define-marketing-mix
metadata:
  version: "0.1.10"
```

L'installazione sul disco non dimostra che una sessione già aperta abbia caricato la skill. Avvia una nuova attività o sessione prima del test.

## Installazione dalla sorgente GitHub

Chi usa lo Skill Installer può installare la sorgente dal percorso `skills/define-marketing-mix`, fissando un commit o un tag pubblicato che contenga davvero la versione richiesta. Verifica la versione effettiva e la destinazione locale.
