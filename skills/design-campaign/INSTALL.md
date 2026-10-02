# Installare `design-campaign`

Questo pacchetto contiene solo la skill installabile. Non contiene Business Identity, Marketing Foundations, artefatti Strategy, Campaign Spec aziendali, dati di campagne o autorizzazioni all'esecuzione.

La candidata locale della sorgente è `0.1.8-l10n.1`; non è una release pubblicata né un'installazione attiva. La presenza nel repository non implica che esistano già un tag o una release pubblica con la stessa versione.

## Installazione da ZIP

1. Per una release pubblicata, scarica uno ZIP ufficiale che dichiari in `SKILL.md` la versione scelta.
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

Il blocco seguente identifica **la sorgente candidata locale**. Per uno ZIP pubblicato, `metadata.version` deve invece coincidere con **la release scelta**, non necessariamente con questa candidata.

```yaml
name: design-campaign
metadata:
  version: "0.1.8-l10n.1"
```

L'installazione sul disco non dimostra che una sessione già aperta abbia caricato la skill. Avvia una nuova attività o sessione prima del test.

## Installazione dalla sorgente GitHub

Chi usa lo Skill Installer può installare la sorgente dal percorso `skills/design-campaign`, fissando un commit o un tag pubblicato che contenga davvero la versione scelta. Questo metodo non sostituisce la verifica della versione e della destinazione locale.
