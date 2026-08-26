# Installare `setup-marketing-system`

Questo pacchetto contiene solo la skill installabile. Non contiene Business Identity, Fondamenti di marketing o file `AGENTS.md`/`CLAUDE.md` dell'organizzazione.

La versione di questa sorgente è `0.2.0`. Una modifica della sorgente non implica che esistano già un tag o una release pubblica con la stessa versione.

## Installazione da ZIP

1. Scarica uno ZIP ufficiale della versione che vuoi installare; per questa release deve dichiarare `0.2.0` in `SKILL.md`.
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
  version: "0.2.0"
```

Per verificare la parità del pacchetto puoi confrontare il checksum dello ZIP con il file `SHA256SUMS` della release.

## Dopo l'installazione

La skill sarà disponibile per le attività successive. Avvia una nuova attività o sessione prima di testarla: l'installazione sul disco non dimostra che la sessione già aperta l'abbia caricata.

## Installazione dalla sorgente GitHub

Chi usa lo Skill Installer può installare la sorgente dal percorso `skills/setup-marketing-system`, fissando un commit o il tag `setup-marketing-system-v0.2.0` che contenga davvero la versione `0.2.0`. Questo metodo non sostituisce la verifica della versione e della destinazione locale.
