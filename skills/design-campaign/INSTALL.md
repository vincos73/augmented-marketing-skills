# Installare `design-campaign`

Questo pacchetto contiene solo la skill installabile. Non contiene Business Identity, Marketing Foundations, artefatti Strategy, Campaign Spec aziendali, dati di campagne o autorizzazioni all'esecuzione.

La versione corrente della sorgente è `0.1.4`. La presenza nel repository non implica che esistano già un tag, una release pubblica o un'installazione attiva con la stessa versione.

## Installazione da ZIP

1. Scarica uno ZIP ufficiale che dichiari `0.1.4` in `SKILL.md`.
2. Verifica lo ZIP con il relativo `SHA256SUMS` quando previsto dalla release.
3. Estrai lo ZIP. Deve contenere una sola cartella radice: `design-campaign/`.
4. Copia la cartella in `~/.codex/skills/`.

Il percorso finale deve essere:

```text
~/.codex/skills/design-campaign/SKILL.md
```

Se esiste già una copia con lo stesso nome, conservala come backup prima di sostituirla e verifica quale versione stai rimpiazzando.

## Verifica

Apri le prime righe di `SKILL.md` e verifica:

```yaml
name: design-campaign
metadata:
  version: "0.1.4"
```

L'installazione sul disco non dimostra che una sessione già aperta abbia caricato la skill. Avvia una nuova attività o sessione prima del test.

## Installazione dalla sorgente GitHub

Chi usa lo Skill Installer può installare la sorgente dal percorso `skills/design-campaign`, fissando un commit o un tag pubblicato che contenga davvero la versione `0.1.4`. Questo metodo non sostituisce la verifica della versione e della destinazione locale.
