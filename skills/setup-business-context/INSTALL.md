# Installare `setup-business-context`

Questo pacchetto contiene solo la skill installabile. Non contiene identità aziendali, brand profile o file `AGENTS.md`/`CLAUDE.md`.

Questa sorgente candidata dichiara `0.6.3`. La release stabile e la copia locale osservata al momento di questa modifica restano `0.6.2`: la presenza della candidata nella sorgente non dimostra che sia stata pubblicata o installata.

## Installazione da ZIP

1. Scarica uno ZIP ufficiale della versione che vuoi installare oppure usa la sorgente verificata; la versione dichiarata in `SKILL.md` deve coincidere con la versione che hai scelto.
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
  version: "0.6.3"
```

Il valore sopra descrive questa sorgente candidata. Per uno ZIP di release verifica invece la versione dichiarata dalla release e confronta il checksum con il relativo file `SHA256SUMS`.

## Dopo l'installazione

La skill sarà disponibile per le attività successive. Avvia una nuova attività o sessione prima di testarla: l'installazione sul disco non dimostra che la sessione già aperta l'abbia caricata.

## Installazione dalla sorgente GitHub

Chi usa lo Skill Installer può installare la sorgente dal percorso `skills/setup-business-context`, fissando il tag `setup-business-context-v0.6.2` che contiene la versione `0.6.2`. Questo metodo non sostituisce la verifica della versione e della destinazione locale.
