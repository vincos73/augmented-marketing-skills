# Installare `campaign-review`

Questo pacchetto contiene solo la skill installabile. Non contiene Campaign Spec, asset, dati di campagna, autorizzazioni o file `AGENTS.md`/`CLAUDE.md` dell'organizzazione.

La versione corrente della sorgente è `0.1.3` ed è inclusa in Augmented Marketing Suite `0.1.0-beta.10`. La presenza nel repository non dimostra da sola installazione attiva o caricamento in una sessione: verifica sempre versione, checksum e destinazione del pacchetto effettivamente usato.

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
