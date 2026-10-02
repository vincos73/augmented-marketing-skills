# Installare `choose-marketing-direction`

Questo pacchetto contiene solo la skill installabile. Non contiene Business Identity, Fondamenti di marketing, Brief della sfida, Direzioni di marketing o file `AGENTS.md`/`CLAUDE.md` dell'organizzazione.

La candidata locale della sorgente è `0.2.9-l10n.1`; non è una release pubblicata né un'installazione attiva. Una modifica della sorgente non implica che esistano già un tag o una release pubblica con la stessa versione.

## Installazione da ZIP

1. Per una release pubblicata, scarica lo ZIP ufficiale della versione che vuoi installare; deve dichiarare quella versione in `SKILL.md`.
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

Il blocco seguente identifica **la sorgente candidata locale**. Per uno ZIP pubblicato, `metadata.version` deve invece coincidere con **la release scelta**, non necessariamente con questa candidata.

```yaml
name: choose-marketing-direction
metadata:
  version: "0.2.9-l10n.1"
```

L'installazione sul disco non dimostra che una sessione già aperta abbia caricato la skill. Avvia una nuova attività o sessione prima del test.

## Installazione dalla sorgente GitHub

Chi usa lo Skill Installer può installare la sorgente dal percorso `skills/choose-marketing-direction`, fissando un commit o un tag pubblicato che contenga davvero la versione scelta. Questo metodo non sostituisce la verifica della versione e della destinazione locale.
