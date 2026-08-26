# Installare `setup-business-context`

Questo pacchetto contiene solo la skill installabile. Non contiene identità aziendali, brand profile o file `AGENTS.md`/`CLAUDE.md`.

La versione della sorgente e della copia attualmente installata è `0.6.2`. Una modifica della sorgente non implica che esistano già un tag o una release pubblica con la stessa versione.

## Installazione da ZIP

1. Scarica uno ZIP ufficiale della versione che vuoi installare oppure usa la sorgente verificata; la copia attualmente installata deve dichiarare `0.6.2` in `SKILL.md`.
2. Verifica lo ZIP con il file `SHA256SUMS` della stessa release quando la verifica dell'integrità è richiesta.
3. Estrai lo ZIP. Deve contenere una sola cartella radice: `setup-business-context/`.
4. Copia quella cartella in `~/.codex/skills/`.

Il percorso finale deve essere:

```text
~/.codex/skills/setup-business-context/SKILL.md
```

Se esiste già una copia con lo stesso nome, conservala come backup prima di sostituirla. Non sovrascrivere una copia attiva senza aver verificato quale versione stai rimpiazzando.

## Verifica

Apri le prime righe di `SKILL.md` e verifica che riportino:

```yaml
name: setup-business-context
metadata:
  version: "0.6.2"
```

Per verificare la parità del pacchetto puoi confrontare il checksum dello ZIP con il file `SHA256SUMS` della release.

## Dopo l'installazione

La skill sarà disponibile per le attività successive. Avvia una nuova attività o sessione prima di testarla: l'installazione sul disco non dimostra che la sessione già aperta l'abbia caricata.

## Installazione dalla sorgente GitHub

Chi usa lo Skill Installer può installare la sorgente dal percorso `skills/setup-business-context`, fissando un commit o un tag che contenga davvero la versione `0.6.2`. Non indicare `v0.6.2` finché quel tag non è stato creato e verificato. Questo metodo non sostituisce la verifica della versione e della destinazione locale.
