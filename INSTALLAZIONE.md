# Installazione di Augmented Marketing Suite 1.0.0

> La versione stabile 1.0.0 contiene dodici skill in entrambi i plugin: undici specialistiche e Augmented Marketing Assistant v0.3.0. La pubblicazione GitHub e i controlli live restano indicati in [`RELEASE-STATUS.md`](RELEASE-STATUS.md).

La Suite offre tre formati separati:

- `dist/1.0.0/claude/augmented-marketing-suite-claude-v1.0.0.zip`: plugin Claude con dodici skill, Assistant compreso;
- `dist/1.0.0/agent-skills/`: undici ZIP individuali e portabili, uno per skill specialistica;
- `dist/1.0.0/openai/augmented-marketing-suite-1.0.0.zip`: plugin OpenAI/Codex con il manifesto `.codex-plugin`, le undici skill e Augmented Marketing Assistant.

**Regola di scelta:** per una sola skill usa uno ZIP in `dist/1.0.0/agent-skills/`; per il bundle completo usa il plugin dedicato alla piattaforma. Non caricare lo ZIP OpenAI/Codex in Claude, né lo ZIP Claude in ChatGPT/Codex.

## Quale archivio scegliere

| Se usi | Scegli | Contiene |
| --- | --- | --- |
| Claude, Suite completa | `dist/1.0.0/claude/augmented-marketing-suite-claude-v1.0.0.zip` | Plugin Claude con dodici skill, Assistant compreso. |
| Claude, una sola skill | Uno ZIP in `dist/1.0.0/agent-skills/` | Una skill specialistica con i suoi riferimenti. |
| ChatGPT con caricamento diretto delle skill | Uno ZIP in `dist/1.0.0/agent-skills/` | La stessa skill portabile. |
| ChatGPT o Codex con Plugin Creator/catalogo plugin | `dist/1.0.0/openai/augmented-marketing-suite-1.0.0.zip` | Le undici skill più Augmented Marketing Assistant. |
| Claude Projects senza custom skill | I file estratti, come contesto di progetto | Alternativa statica, non installazione di skill. |

Augmented Marketing Assistant è incluso nei plugin Claude e OpenAI/Codex. Gli undici ZIP portabili rimangono dedicati alle singole skill specialistiche.

## Claude: plugin con tutte le skill

1. Dopo la pubblicazione, scarica `augmented-marketing-suite-claude-v1.0.0.zip` dalla [release GitHub v1.0.0](https://github.com/vincos73/augmented-marketing-skills/releases/tag/augmented-marketing-suite-v1.0.0), oppure usa il file locale in `dist/1.0.0/claude/`.
2. In Claude apri **Personalizza → Plugin** e scegli il caricamento di un plugin.
3. Seleziona lo ZIP Claude. Il pacchetto ha `.claude-plugin/plugin.json`, include dodici skill e non contiene agenti o subagenti.
4. Dopo l'installazione, apri una nuova chat e usa `/` o il pulsante `+` per vedere le skill del plugin.

Il plugin Claude contiene le skill in `skills/<nome>/SKILL.md`, senza MCP, connector, hook o subagenti.

## Claude: caricamento di una custom skill

1. Apri Claude e crea o apri uno spazio in cui le custom skill sono disponibili nel tuo piano o workspace.
2. Apri le impostazioni o il pannello delle skill, scegli di caricare una skill e seleziona uno ZIP da `dist/1.0.0/agent-skills/` oppure dalla release GitHub.
3. Verifica che Claude mostri il nome tecnico della skill.
4. Avvia una nuova chat e fai una richiesta pertinente.

Una custom skill Claude richiede un archivio con una sola cartella radice e un file `SKILL.md`; gli archivi portabili rispettano questa struttura. La disponibilità del caricamento dipende da piano e workspace. Se non è disponibile, usa un Project come alternativa documentale.

### Claude Code e Claude Desktop

Per Claude Code, estrai il bundle completo e verifica `claude plugin validate --strict <bundle-estratto>`. Dopo la pubblicazione, aggiungi il marketplace GitHub remoto:

```sh
claude plugin marketplace add vincos73/augmented-marketing-skills
claude plugin install augmented-marketing-suite@augmented-marketing-skills
```

Se devi validare una copia locale del marketplace, il percorso deve essere scritto `./` (non `.`): la CLI 2.1.266 rifiuta `claude plugin marketplace add .` con `Invalid marketplace source format`. La validazione locale non dimostra la disponibilità del marketplace remoto o l'installazione nell'account personale.

In una nuova sessione, una richiesta come “Ho un negozio e le vendite online calano, non so cosa fare” dovrebbe attivare l'Assistant e portare a `define-marketing-challenge` quando il meccanismo dell'ambiente lo consente. La richiesta “Usa define-marketing-challenge per chiarire il calo delle vendite online del mio negozio” usa direttamente la specialistica senza passare dall'Assistant. In Claude Code l'Assistant richiama la specialistica con `Skill` usando `augmented-marketing-suite:<nome-skill>`; negli altri ambienti legge `SKILL.md` con il meccanismo disponibile.

Se il tuo ambiente Claude consente skill locali, estrai uno ZIP in una cartella di skill del progetto o dell'utente, senza rinominare la cartella radice. L'installazione sul disco non dimostra che una sessione già aperta abbia caricato la skill: apri una nuova sessione e controlla che il nome sia visibile o invocabile.

### Claude Projects come alternativa

Un Project può conservare i file come istruzioni o conoscenza di progetto, ma non equivale a una custom skill selezionata automaticamente. Carica soltanto il contenuto della skill scelta, mantieni `SKILL.md` e la cartella `references/` insieme e descrivi nella chat quale skill vuoi applicare.

## ChatGPT: caricamento diretto di una skill

1. Apri il flusso **Skills** disponibile nel tuo account o workspace.
2. Crea o carica una skill e seleziona lo ZIP portabile desiderato da `dist/1.0.0/agent-skills/`.
3. Controlla nome e versione dichiarati in `SKILL.md`.
4. Apri una nuova chat e prova una richiesta coerente con quella skill.

La disponibilità del caricamento diretto dipende da prodotto, piano e amministratore. Il formato portabile è separato dal pacchetto plugin OpenAI/Codex.

## ChatGPT e Codex: Suite completa come plugin

Usa `dist/1.0.0/openai/augmented-marketing-suite-1.0.0.zip` solo in un ambiente che mostra Plugin Creator, un catalogo plugin o un marketplace compatibile. Non è un file da caricare in Claude.

1. Apri una nuova chat o sessione.
2. Carica l'archivio nel flusso di creazione o aggiornamento plugin disponibile.
3. Verifica che la radice dell'archivio contenga `.codex-plugin/plugin.json` e `skills/`.
4. Controlla che il manifesto dichiari versione `1.0.0` e che `skills` sia la directory delle skill.
5. Installa o aggiorna il plugin nel marketplace consentito dal tuo ambiente, poi avvia una nuova chat.

## Contenuto e versioni

| Componente | Versione nella Suite 1.0.0 |
| --- | --- |
| Plugin Claude Augmented Marketing Suite | `1.0.0` |
| Plugin OpenAI/Codex Augmented Marketing Suite (`augmented-marketing-suite`) | `1.0.0` |
| Augmented Marketing Assistant, plugin Claude e OpenAI/Codex | `0.3.0` |
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

Le singole versioni delle skill restano invariate. Gli archivi, i manifest e i checksum della build locale sono riepilogati in [`dist/1.0.0/README.md`](dist/1.0.0/README.md).

## Verifica prima del test

1. Confronta lo SHA-256 di ogni ZIP con `SHA256SUMS` nella stessa cartella di distribuzione.
2. Estrai in una cartella temporanea e controlla che ogni ZIP portabile abbia una sola cartella radice, `SKILL.md` e gli eventuali `references/`.
3. Per il pacchetto Claude, controlla `.claude-plugin/plugin.json`; per OpenAI/Codex, controlla `.codex-plugin/plugin.json` alla radice dell'archivio.
4. Verifica che ciascun plugin contenga dodici skill e che `agent-skills/` contenga undici ZIP specialistici.
5. Dopo l'installazione, apri una nuova chat e chiedi un risultato che appartenga chiaramente alla skill scelta.

Il rapporto [`evals/suite-1.0.0/README.md`](evals/suite-1.0.0/README.md) separa i controlli strutturali dalle prove comportamentali. Due test conversazionali Claude restano non verificati per autenticazione mancante. La verifica strutturale non dimostra la discovery in ogni account, il caricamento nella sessione o la comprensibilità per tester esterni.
