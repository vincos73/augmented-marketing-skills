# Installazione di Augmented Marketing Suite beta.11

> La release beta.11 contiene undici skill specialistiche e Augmented Marketing Assistant per OpenAI/Codex. Scarica gli archivi dalla [release GitHub](https://github.com/vincos73/augmented-marketing-skills/releases/tag/augmented-marketing-suite-v0.1.0-beta.11), poi confrontali con i checksum allegati.

La beta `0.1.0-beta.11` offre tre formati separati:

- `dist/beta.11/claude/augmented-marketing-suite-claude-v0.1.0-beta.11.zip`: plugin Claude con undici skill specialistiche;
- `dist/beta.11/agent-skills/`: undici ZIP individuali e portabili, uno per skill specialistica;
- `dist/beta.11/openai/augmented-marketing-suite-0.1.0-beta.11.zip`: pacchetto OpenAI/Codex con il manifesto `.codex-plugin`, le undici skill e Augmented Marketing Assistant.

**Regola di scelta:** per una sola skill usa uno ZIP in `dist/agent-skills/`; per il bundle completo usa il plugin dedicato alla piattaforma. Non caricare lo ZIP OpenAI/Codex in Claude, né lo ZIP Claude in ChatGPT/Codex.

## Quale archivio scegliere

| Se usi | Scegli | Contiene |
| --- | --- | --- |
| Claude, tutte le skill specialistiche | `dist/beta.11/claude/augmented-marketing-suite-claude-v0.1.0-beta.11.zip` | Plugin Claude con undici skill specialistiche. |
| Claude, una sola skill | Uno ZIP in `dist/beta.11/agent-skills/` | Una skill specialistica con i suoi riferimenti. |
| ChatGPT con caricamento diretto delle skill | Uno ZIP in `dist/beta.11/agent-skills/` | La stessa skill portabile. |
| ChatGPT o Codex con Plugin Creator/catalogo plugin | `dist/beta.11/openai/augmented-marketing-suite-0.1.0-beta.11.zip` | Le undici skill più Augmented Marketing Assistant. |
| Claude Projects senza custom skill | I file estratti, come contesto di progetto | Alternativa statica, non installazione di skill. |

Gli archivi Claude e portabili non includono Augmented Marketing Assistant: il suo testo dichiara esplicitamente di essere un adattatore per ChatGPT e Codex.

## Claude: plugin con tutte le skill

1. Scarica `augmented-marketing-suite-claude-v0.1.0-beta.11.zip` dalla release beta.11.
2. In Claude apri **Personalizza → Plugin** e scegli il caricamento di un plugin.
3. Seleziona quello ZIP, non `augmented-marketing-suite-0.1.0-beta.11.zip`: quest'ultimo è il pacchetto OpenAI/Codex e contiene `.codex-plugin`, non `.claude-plugin`.
4. Dopo l'installazione, apri una nuova chat e usa `/` o il pulsante `+` per vedere le undici skill del plugin.

Il plugin Claude contiene `.claude-plugin/plugin.json` alla radice e le skill in `skills/<nome>/SKILL.md`, senza MCP, connector, hook o subagenti.

## Claude: caricamento di una custom skill

1. Apri Claude e crea o apri uno spazio in cui le custom skill sono disponibili nel tuo piano o workspace.
2. Apri le impostazioni o il pannello delle skill, scegli di caricare una skill e seleziona uno ZIP da `dist/agent-skills/`.
3. Verifica che Claude mostri il nome tecnico della skill, per esempio `define-marketing-challenge`.
4. Avvia una nuova chat e fai una richiesta pertinente, per esempio: “Ho l'obiettivo di far conoscere un nuovo servizio ma non so ancora quale problema di marketing affrontare.”

Una custom skill Claude richiede un archivio con una sola cartella radice e un file `SKILL.md`; gli archivi portabili rispettano questa struttura. Se il tuo workspace non mostra il caricamento delle skill, non allegare lo ZIP a una chat normale aspettandoti che resti installato: chiedi all'amministratore se sono abilitate le custom skill o usa un Project come alternativa documentale.

### Claude Code e Claude Desktop

Se il tuo ambiente Claude consente skill locali, estrai uno ZIP in una cartella di skill del progetto o dell'utente, senza rinominare la cartella radice. Verifica prima la documentazione e il percorso mostrato dalla tua versione di Claude Code/Desktop: i percorsi e le funzioni disponibili possono dipendere da piano, amministratore e canale di rilascio.

L'installazione sul disco non dimostra che una sessione già aperta abbia caricato la skill. Apri una nuova sessione e controlla che il nome sia visibile o invocabile secondo l'interfaccia disponibile.

### Claude Projects come alternativa

Un Project può conservare i file come istruzioni o conoscenza di progetto, ma non equivale a una custom skill selezionata automaticamente. Carica soltanto il contenuto della skill scelta, mantieni `SKILL.md` e la cartella `references/` insieme e descrivi nella chat quale skill vuoi applicare. Questa strada non offre una prova di discovery, invocazione o aggiornamento automatico.

## ChatGPT: caricamento diretto di una skill

1. Apri il flusso **Skills** disponibile nel tuo account o workspace.
2. Crea o carica una skill e seleziona lo ZIP portabile desiderato da `dist/beta.11/agent-skills/`.
3. Controlla nome e versione dichiarati in `SKILL.md`.
4. Apri una nuova chat e prova una richiesta coerente con quella skill.

La disponibilità del caricamento diretto dipende da prodotto, piano e amministratore. Le skill seguono lo standard Agent Skills e il formato portabile è intenzionalmente separato dal pacchetto plugin OpenAI/Codex.

## ChatGPT e Codex: Suite completa come plugin

Usa `dist/beta.11/openai/augmented-marketing-suite-0.1.0-beta.11.zip` solo in un ambiente che mostra Plugin Creator, un catalogo plugin o un marketplace compatibile. Non è un file da caricare in Claude.

1. Apri una nuova chat o sessione.
2. Carica l'archivio nel flusso di creazione o aggiornamento plugin disponibile.
3. Verifica che la radice dell'archivio contenga `.codex-plugin/plugin.json` e `skills/`.
4. Controlla che il manifesto dichiari versione `0.1.0-beta.11` e che `skills` sia la directory delle skill.
5. Installa o aggiorna il plugin nel marketplace consentito dal tuo ambiente, poi avvia una nuova chat.

Se usi un flusso che chiede un prompt di registrazione, puoi usare questo testo:

````text
Crea o aggiorna il plugin personale dal pacchetto allegato Augmented Marketing Suite 0.1.0-beta.11.

Verifica che la radice contenga .codex-plugin/plugin.json e che il manifesto dichiari skills/ come directory delle skill. Mantieni intatte le dodici skill incluse. Non aggiungere MCP, connector, hook o altri componenti.

Al termine, indica come installarlo dal catalogo disponibile e ricorda di provarlo in una nuova chat.
````

## Contenuto e versioni della beta.11

| Componente | Versione beta.11 |
| --- | --- |
| Plugin Claude Augmented Marketing Suite | `0.1.0-beta.11` |
| Plugin OpenAI/Codex Augmented Marketing Suite (`augmented-marketing-suite`) | `0.1.0-beta.11` |
| Augmented Marketing Assistant, solo pacchetto OpenAI/Codex | `0.2.1` |
| Setup Business Context | `0.6.7` |
| Setup Marketing System | `0.3.4` |
| Setup Brand Voice | `0.1.2` |
| Define Marketing Challenge | `0.1.8` |
| Choose Marketing Direction | `0.2.8` |
| Define Marketing Mix | `0.1.9` |
| Design Campaign | `0.1.7` |
| Campaign Review | `0.1.4` |
| Campaign Debrief | `0.1.7` |
| Content Director | `0.1.2` |
| Write Marketing Copy | `0.1.5` |

Questa documentazione corrisponde alla [release GitHub della Suite beta.11](https://github.com/vincos73/augmented-marketing-skills/releases/tag/augmented-marketing-suite-v0.1.0-beta.11). Le singole skill non richiedono necessariamente un tag separato quando sono distribuite insieme alla Suite.

## Verifica prima del test

1. Confronta lo SHA-256 dello ZIP con `SHA256SUMS` nella stessa cartella di distribuzione.
2. Estrai in una cartella temporanea e controlla che ogni ZIP portabile abbia una sola cartella radice, `SKILL.md` e gli eventuali `references/`.
3. Per il pacchetto OpenAI/Codex, controlla che `.codex-plugin/plugin.json` sia alla radice dell'archivio.
4. Dopo l'installazione, apri una nuova chat e chiedi un risultato che appartenga chiaramente alla skill scelta.

La verifica strutturale non sostituisce la prova in un account reale. Restano manuali la disponibilità dell'interfaccia nel piano dell'utente, l'upload effettivo, la discovery nella nuova chat e la comprensibilità per tester esterni.
