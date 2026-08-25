# Installare `setup-business-context`

Questo pacchetto contiene solo la skill installabile. Non contiene identità aziendali, brand profile o file `AGENTS.md`/`CLAUDE.md`.

## Installazione da ZIP

1. Scarica `setup-business-context-v0.5.0.zip` dalla [release GitHub v0.5.0](https://github.com/vincos73/augmented-marketing-skills/releases/tag/v0.5.0).
2. Verifica il file con `setup-business-context-v0.5.0.SHA256SUMS` quando la verifica dell'integrità è richiesta.
3. Estrai lo ZIP. Deve contenere una sola cartella radice: `setup-business-context/`.
4. Copia quella cartella in `~/.codex/skills/`.

Il percorso finale deve essere:

```text
~/.codex/skills/setup-business-context/SKILL.md
```

Se esiste già una copia con lo stesso nome, conservala come backup prima di sostituirla. Non sovrascrivere una copia attiva senza aver verificato quale versione stai rimpiazzando.

## Verifica

Apri le prime righe di `SKILL.md` e verifica che riportino:

```text
name: setup-business-context
version: 0.5.0
```

Per verificare la parità del pacchetto puoi confrontare il checksum dello ZIP con il file `SHA256SUMS` della release.

## Dopo l'installazione

La skill sarà disponibile per le attività successive. Avvia una nuova attività o sessione prima di testarla: l'installazione sul disco non dimostra che la sessione già aperta l'abbia caricata.

## Installazione dalla sorgente GitHub

Chi usa l'helper ufficiale dello Skill Installer può installare la sorgente dal percorso `skills/setup-business-context` fissando il riferimento `v0.5.0`. Questo metodo installa la stessa struttura della release, ma non sostituisce la verifica della versione e della destinazione locale.
