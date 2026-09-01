# Installare `content-director`

Questo pacchetto contiene solo la skill installabile. Non contiene Business Identity, Marketing Foundations, Campaign Spec aziendali, dati editoriali o autorizzazioni alla produzione e alla pubblicazione.

La versione stabile corrente è `0.1.1`, pubblicata nella release [`content-director-v0.1.1`](https://github.com/vincos73/augmented-marketing-skills/releases/tag/content-director-v0.1.1). La presenza nel repository o il download della release non dimostrano che una sessione già aperta abbia caricato la skill.

## Installazione da ZIP

1. Scarica uno ZIP ufficiale che dichiari `0.1.1` in `SKILL.md`.
2. Verifica lo ZIP con il relativo `SHA256SUMS` quando previsto dalla release.
3. Estrai lo ZIP. Deve contenere una sola cartella radice: `content-director/`.
4. Copia la cartella in `~/.codex/skills/`.

Il percorso finale deve essere:

```text
~/.codex/skills/content-director/SKILL.md
```

Se esiste già una copia con lo stesso nome, conservala come backup prima di sostituirla e verifica quale versione stai rimpiazzando.

## Verifica

Apri le prime righe di `SKILL.md` e verifica:

```yaml
name: content-director
metadata:
  version: "0.1.1"
```

L'installazione sul disco non dimostra che una sessione già aperta abbia caricato la skill. Avvia una nuova attività o sessione prima del test.

## Installazione dalla sorgente GitHub

Chi usa lo Skill Installer può installare la sorgente dal percorso `skills/content-director`, fissando il tag `content-director-v0.1.1`. Questo metodo non sostituisce la verifica della versione e della destinazione locale.
