# Installare `setup-marketing-system`

Questo pacchetto contiene solo la skill installabile. Non contiene Business Identity, Fondamenti di marketing o file `AGENTS.md`/`CLAUDE.md` dell'organizzazione.

Questa è la versione stabile `0.3.0` della skill. Il pacchetto contiene solo la cartella installabile `setup-marketing-system`.

## Installazione da ZIP

1. Scarica uno ZIP ufficiale della versione che vuoi installare; la versione dichiarata in `SKILL.md` deve coincidere con la release scelta.
2. Verifica lo ZIP con il file `SHA256SUMS` della stessa release quando la verifica dell'integrità è richiesta.
3. Estrai lo ZIP. Deve contenere una sola cartella radice: `setup-marketing-system/`.
4. Copia quella cartella in `~/.codex/skills/`.

Il percorso finale deve essere:

```text
~/.codex/skills/setup-marketing-system/SKILL.md
```

Se esiste già una copia con lo stesso nome, conservala come backup prima di sostituirla. Non sovrascrivere una copia attiva senza aver verificato quale versione stai rimpiazzando.

## Verifica

Apri le prime righe di `SKILL.md` e verifica che riportino:

```yaml
name: setup-marketing-system
metadata:
  version: "0.3.0"
```

Per uno ZIP di release confronta la versione dichiarata dalla release e il checksum con il relativo file `SHA256SUMS`.

## Dopo l'installazione

La skill sarà disponibile per le attività successive. Avvia una nuova attività o sessione prima di testarla: l'installazione sul disco non dimostra che la sessione già aperta l'abbia caricata.

## Installazione dalla sorgente GitHub

Chi usa lo Skill Installer può installare la sorgente dal percorso `skills/setup-marketing-system`, fissando un commit o il tag `setup-marketing-system-v0.3.0` che contenga davvero la versione `0.3.0`. Questo metodo non sostituisce la verifica della versione e della destinazione locale.
