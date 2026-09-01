# Installare `campaign-debrief`

Questo pacchetto contiene solo la skill installabile. Non contiene Campaign Spec aziendali, dati di campagne, accessi Analytics o autorizzazioni operative.

La versione corrente della sorgente è `0.1.6`. La presenza nel repository non implica che esistano già un tag, una release pubblica o un'installazione attiva con la stessa versione.

## Installazione da ZIP

1. Scarica uno ZIP ufficiale che dichiari `0.1.6` in `SKILL.md`.
2. Verifica lo ZIP con il relativo `SHA256SUMS` quando previsto dalla release.
3. Estrai lo ZIP. Deve contenere una sola cartella radice: `campaign-debrief/`.
4. Copia la cartella in `~/.codex/skills/`.

Il percorso finale deve essere:

```text
~/.codex/skills/campaign-debrief/SKILL.md
```

Se esiste già una copia con lo stesso nome, conservala come backup prima di sostituirla e verifica quale versione stai rimpiazzando.

## Verifica

Apri le prime righe di `SKILL.md` e verifica:

```yaml
name: campaign-debrief
metadata:
  version: "0.1.6"
```

L'installazione sul disco non dimostra che una sessione già aperta abbia caricato la skill. Avvia una nuova attività o sessione prima del test.

## Installazione dalla sorgente GitHub

Chi usa lo Skill Installer può installare la sorgente dal percorso `skills/campaign-debrief`, fissando un commit o un tag pubblicato che contenga davvero la versione `0.1.6`. Questo metodo non sostituisce la verifica della versione e della destinazione locale.
