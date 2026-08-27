# Installazione di Augmented Marketing Suite beta.7

La beta `0.1.0-beta.7` separa deliberatamente due formati:

- `dist/agent-skills/`: cinque ZIP individuali e portabili, uno per skill specialistica, per Claude o altri ambienti che caricano una skill alla volta;
- `dist/openai/augmented-marketing-suite-0.1.0-beta.7.zip`: pacchetto OpenAI/Codex con il manifesto `.codex-plugin`, le cinque skill e Augmented Marketing Assistant.

Non chiamare il primo formato "plugin Claude": per un utente Claude la via più lineare è caricare una singola custom skill. Claude dispone anche di plugin, ma non sono necessari a queste cinque skill, che non richiedono strumenti, MCP, hook o automazioni.

## Quale archivio scegliere

| Se usi | Scegli | Contiene |
| --- | --- | --- |
| Claude | Uno ZIP in `dist/agent-skills/` | Una skill specialistica con i suoi riferimenti. |
| ChatGPT con caricamento diretto delle skill | Uno ZIP in `dist/agent-skills/` | La stessa skill portabile. |
| ChatGPT o Codex con Plugin Creator/catalogo plugin | `dist/openai/augmented-marketing-suite-0.1.0-beta.7.zip` | Le cinque skill più Augmented Marketing Assistant. |
| Claude Projects senza custom skill | I file estratti, come contesto di progetto | Alternativa statica, non installazione di skill. |

Gli ZIP portabili non includono Augmented Marketing Assistant: il suo testo dichiara esplicitamente di essere un adattatore per ChatGPT e Codex. In Claude scegli direttamente la skill dal bisogno, oppure consulta la tabella nel README.

## Claude: caricamento di una custom skill

1. Apri Claude e crea o apri uno spazio in cui le custom skill sono disponibili nel tuo piano o workspace.
2. Apri le impostazioni o il pannello delle skill, scegli di caricare una skill e seleziona uno ZIP da `dist/agent-skills/`.
3. Verifica che Claude mostri il nome tecnico della skill, per esempio `define-marketing-challenge`.
4. Avvia una nuova chat e fai una richiesta pertinente, per esempio: “Ho l'obiettivo di far conoscere un nuovo servizio ma non so ancora quale problema di marketing affrontare.”

Una custom skill Claude richiede un archivio con una sola cartella radice e un file `SKILL.md`; gli archivi beta.7 rispettano questa struttura. Se il tuo workspace non mostra il caricamento delle skill, non allegare lo ZIP a una chat normale aspettandoti che resti installato: chiedi all'amministratore se sono abilitate le custom skill o usa un Project come alternativa documentale.

### Claude Code e Claude Desktop

Se il tuo ambiente Claude consente skill locali, estrai uno ZIP in una cartella di skill del progetto o dell'utente, senza rinominare la cartella radice. Verifica prima la documentazione e il percorso mostrato dalla tua versione di Claude Code/Desktop: i percorsi e le funzioni disponibili possono dipendere da piano, amministratore e canale di rilascio.

L'installazione sul disco non dimostra che una sessione già aperta abbia caricato la skill. Apri una nuova sessione e controlla che il nome sia visibile o invocabile secondo l'interfaccia disponibile.

### Claude Projects come alternativa

Un Project può conservare i file come istruzioni o conoscenza di progetto, ma non equivale a una custom skill selezionata automaticamente. Carica soltanto il contenuto della skill scelta, mantieni `SKILL.md` e la cartella `references/` insieme e descrivi nella chat quale skill vuoi applicare. Questa strada non offre una prova di discovery, invocazione o aggiornamento automatico.

## ChatGPT: caricamento diretto di una skill

1. Apri il flusso **Skills** disponibile nel tuo account o workspace.
2. Crea o carica una skill e seleziona lo ZIP portabile desiderato da `dist/agent-skills/`.
3. Controlla nome e versione dichiarati in `SKILL.md`.
4. Apri una nuova chat e prova una richiesta coerente con quella skill.

La disponibilità del caricamento diretto dipende da prodotto, piano e amministratore. Le skill seguono lo standard Agent Skills e il formato portabile è intenzionalmente separato dal pacchetto plugin OpenAI/Codex.

## ChatGPT e Codex: Suite completa come plugin

Usa `dist/openai/augmented-marketing-suite-0.1.0-beta.7.zip` solo in un ambiente che mostra Plugin Creator, un catalogo plugin o un marketplace compatibile.

1. Apri una nuova chat o sessione.
2. Carica l'archivio nel flusso di creazione o aggiornamento plugin disponibile.
3. Verifica che la radice dell'archivio contenga `.codex-plugin/plugin.json` e `skills/`.
4. Controlla che il manifesto dichiari versione `0.1.0-beta.7` e che `skills` sia la directory delle skill.
5. Installa o aggiorna il plugin nel marketplace consentito dal tuo ambiente, poi avvia una nuova chat.

Se usi un flusso che chiede un prompt di registrazione, puoi usare questo testo:

````text
Crea o aggiorna il plugin personale dal pacchetto allegato Augmented Marketing Suite 0.1.0-beta.7.

Verifica che la radice contenga .codex-plugin/plugin.json e che il manifesto dichiari skills/ come directory delle skill. Mantieni intatte le sei skill incluse. Non aggiungere MCP, connector, hook o altri componenti.

Al termine, indica come installarlo dal catalogo disponibile e ricorda di provarlo in una nuova chat.
````

## Contenuto e versioni della beta.7

| Componente | Versione beta.7 |
| --- | --- |
| Plugin Augmented Marketing Suite (`augmented-marketing-suite`) | `0.1.0-beta.7` |
| Augmented Marketing Assistant, solo pacchetto OpenAI/Codex | `0.1.0` |
| Setup Business Context | `0.6.4` |
| Setup Marketing System | `0.3.1` |
| Define Marketing Challenge | `0.1.3` |
| Choose Marketing Direction | `0.2.2` |
| Define Marketing Mix | `0.1.3` |

Questa documentazione corrisponde alla [release GitHub della Suite beta.7](https://github.com/vincos73/augmented-marketing-skills/releases/tag/augmented-marketing-suite-v0.1.0-beta.7). Le singole skill non richiedono necessariamente un tag separato quando sono distribuite insieme alla Suite.

## Verifica prima del test

1. Confronta lo SHA-256 dello ZIP con `SHA256SUMS` nella stessa cartella di distribuzione.
2. Estrai in una cartella temporanea e controlla che ogni ZIP portabile abbia una sola cartella radice, `SKILL.md` e gli eventuali `references/`.
3. Per il pacchetto OpenAI/Codex, controlla che `.codex-plugin/plugin.json` sia alla radice dell'archivio.
4. Dopo l'installazione, apri una nuova chat e chiedi un risultato che appartenga chiaramente alla skill scelta.

La verifica strutturale non sostituisce la prova in un account reale. Restano manuali la disponibilità dell'interfaccia nel piano dell'utente, l'upload effettivo, la discovery nella nuova chat e la comprensibilità per tester esterni.
