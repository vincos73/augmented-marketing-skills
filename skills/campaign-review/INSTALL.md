# Installare `campaign-review`

Questo pacchetto contiene solo la skill installabile. Non contiene Campaign Spec, asset, dati di campagna, autorizzazioni o file `AGENTS.md`/`CLAUDE.md` dell'organizzazione.

La versione candidata corrente della sorgente è `0.1.3`. La presenza nel repository non implica che esista già un pacchetto, un tag, una release pubblica o un'installazione attiva con la stessa versione. La distribuzione beta.9 può quindi restare a `0.1.2` finché non viene svolto un workflow di release separato.

## Installazione da ZIP

1. Scarica lo ZIP ufficiale della versione scelta; `SKILL.md` deve dichiarare esattamente la versione del pacchetto.
2. Verifica lo ZIP con `SHA256SUMS` della stessa distribuzione quando previsto.
3. Estrai lo ZIP. Deve contenere una sola cartella radice: `campaign-review/`.
4. Copia la cartella in `~/.codex/skills/` o nella destinazione prevista dall'ambiente.

Il percorso finale abituale è:

```text
~/.codex/skills/campaign-review/SKILL.md
```

Se esiste una copia precedente, conserva il backup e verifica quale versione stai sostituendo.

## Verifica

Controlla il frontmatter:

```yaml
name: campaign-review
metadata:
  version: "0.1.3"
```

Controlla inoltre che il pacchetto contenga `references/campaign-review-contract.md` e non contenga fixture, eval, asset di campagne o file di istruzioni dell'organizzazione.

L'installazione sul disco non dimostra che una sessione già aperta abbia caricato la skill. Avvia una nuova attività o sessione e verifica che `campaign-review` sia visibile o invocabile.

## Installazione dalla sorgente GitHub

Chi usa uno Skill Installer può installare `skills/campaign-review`, fissando un commit o un tag che contenga davvero la versione desiderata. Questo metodo non sostituisce la verifica della versione, della destinazione e del checksum del pacchetto quando si usa uno ZIP.
