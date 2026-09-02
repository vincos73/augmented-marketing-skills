---
artifact: audit-architettura-skill-centrale
version: 1
status: audit-indipendente
last_reviewed: 2026-08-30
scope: "Verifica tecnica indipendente dell'architettura proposta: skill centrale + specialisti autonomi + playbook interni, due bundle Claude/OpenAI"
type: audit-in-lettura
---

# Audit architettura: skill centrale, specialisti autonomi, playbook interni

Audit tecnico in sola lettura. Nessun file del repository modificato, nessuna installazione eseguita, nessun comando di scrittura lanciato durante la verifica.

## A. Verdetto

**GO CON RISERVE** — con una riserva bloccante e una correzione di rotta.

L'architettura (orchestratore centrale + specialisti autonomi visibili ma non auto-selezionabili + playbook interni + due bundle da una sorgente) è **realmente ottenibile su Claude Code** ed è **la forma corretta**: la documentazione ufficiale la supporta campo per campo, e Claude Code offre esattamente i due interruttori necessari (`disable-model-invocation`, `user-invocable`).

Tre punti da non addolcire:

1. **Il punto 5 (l'orchestratore non deve dipendere dall'invocare skill sorelle) non è una precauzione, è un vincolo imposto.** Su Claude, `disable-model-invocation: true` non "scoraggia" l'auto-selezione: rimuove la skill dal contesto del modello e **blocca la chiamata via Skill tool**. L'orchestratore quindi *non potrà* invocare gli specialisti nemmeno volendo. I playbook interni non sono un'opzione elegante: sono l'unica strada possibile.
2. **Il punto 4 (impedire la selezione automatica degli specialisti) costa il punto di forza attuale.** Oggi le cinque skill funzionano in auto-selezione: sono visibili e invocabili spontaneamente dal modello. Attivando `disable-model-invocation: true`, un utente che scrive «aiutami a definire la sfida» non arriverà più da solo a `define-marketing-challenge`: dovrà passare dall'orchestratore o digitare il comando. È un baratto tra precisione e scopribilità, non un miglioramento gratuito.
3. **Riserva bloccante:** non è stato possibile verificare a runtime che `disable-model-invocation` sia onorato **sul canale con cui gli utenti installano davvero** (upload plugin su claude.ai → sync su Claude Desktop). Il bundle Electron di Claude Desktop 1.40609.0 legge dal frontmatter `name`, `description`, `argument-hint`, `user-invocable` — e **non contiene la stringa `disable-model-invocation`**. Non è una prova di fallimento (quel campo agisce sul listing lato modello, prodotto da un runtime non incluso in quel bundle), ma sul canale di distribuzione reale la proprietà è **documentata, non osservata**. È il test #1/#3 della sezione F: finché non passa, il GO resta condizionato.

## B. Cosa è stato verificato

### File del progetto letti

- Struttura completa del repository (~300 path).
- **Skill autonome (7 sorgenti):** frontmatter e dimensioni di tutte le `skills/*/SKILL.md`.
- **Orchestratore:** `skills/augmented-marketing-assistant/SKILL.md` (integrale) e `agents/augmented-marketing-assistant.md`.
- **Prototipo:** `prototypes/augmented-marketing-prototype/SKILL.md` integrale + albero completo di `references/modules/`.
- **Playbook/blueprint:** `CAMPAIGN-CORE.md` (indice, tesi, decisioni), `blueprints/design-campaign/`.
- **Manifesti:** `.codex-plugin/plugin.json`, `claude/.claude-plugin/plugin.json`, tutti gli `agents/openai.yaml`.
- **Contratto:** `PORTABILITA.md` v3 (working tree, con modifiche non committate).
- **Distribuzioni:** `dist/openai/manifest.json`, `dist/claude/manifest.json`, `dist/agent-skills/manifest.json` + contenuto reale dei due ZIP (`unzip -l`).
- **Test e audit:** `prototypes/augmented-marketing-comparative-test/portability-audit.md`, `.../results.md`, `.../protocol.md`, `evals/portability/runs/2026-08-27-static-audit-v1.md`, `INSTALLAZIONE.md`.

### Documentazione ufficiale consultata

| Fonte | Uso |
|---|---|
| [code.claude.com/docs/en/skills](https://code.claude.com/docs/en/skills) | Tabella frontmatter completa, controllo invocazione, namespace, ciclo di vita e compattazione, `skillOverrides` |
| [code.claude.com/docs/en/plugins-reference](https://code.claude.com/docs/en/plugins-reference) | Schema `plugin.json`, discovery `skills/`, path rules, versioning e cache |
| [openai/codex — plugin-json-spec.md](https://github.com/openai/codex/blob/main/codex-rs/skills/src/assets/samples/plugin-creator/references/plugin-json-spec.md) | Schema ufficiale `.codex-plugin/plugin.json` |
| [learn.chatgpt.com/docs/build-skills](https://learn.chatgpt.com/docs/build-skills) (redirect da `developers.openai.com/codex/skills`) | Frontmatter Codex, `agents/openai.yaml`, `policy.allow_implicit_invocation`, budget di progressive disclosure |
| [openai/skills](https://github.com/openai/skills), [help.openai.com — Plugins in ChatGPT and Codex](https://help.openai.com/en/articles/20001256-plugins-in-chatgpt-and-codex) | Conferma dell'esistenza del formato plugin Codex |

### Versione di Claude Code usata

- Claude Desktop **1.40609.0** (`/Applications/Claude.app`). Nessun binario `claude` sul PATH: non è stato possibile eseguire `claude --version`.
- Nel bundle compaiono stringhe di feature-gate `2.1.178 … 2.1.247`: il motore è **plausibilmente ≥ 2.1.247** (dedotto da stringhe binarie, non da un report di versione esplicito).
- Modello usato per l'audit: Opus 5.

### Osservato realmente a runtime (in questa sessione)

- Il plugin **`augmented-marketing-suite` v0.1.0-beta.8 è installato** su questa macchina, materializzato sotto `~/Library/Application Support/Claude/local-agent-mode-sessions/.../rpm/plugin_01W6LhBPWZyzVsardARsqHuv/`, con `.claude-plugin/plugin.json` identico a `claude/.claude-plugin/plugin.json`.
- Registrato in `~/.claude.json` come `pluginUsage["augmented-marketing-suite@inline"]`.
- **Le cinque skill sono nel contesto** sotto il namespace `augmented-marketing-suite:<nome>`, con descrizioni italiane verbatim. Discovery e namespace funzionano; oggi gli specialisti sono auto-invocabili dal modello (il punto 4 è oggi violato, per costruzione, come atteso).
- **`augmented-marketing-assistant` e `design-campaign` non sono presenti** nel plugin installato, coerente con `dist/claude/manifest.json` che li esclude. Il punto 1 (skill centrale disponibile su Claude) oggi non è soddisfatto.
- Le skill sincronizzate da claude.ai sono impacchettate in un plugin sintetico `anthropic-skills`, confermando indipendentemente la meccanica namespace `plugin:skill`.
- Il parser frontmatter del guscio Electron (`[SkillParsing]` in `app.asar`) legge solo `name`, `description`, `argument-hint`, `user-invocable`. `disable-model-invocation` **non compare** in quel bundle.
- Le tre copie di playbook in `prototypes/.../references/modules/*/SKILL.md` sono **oggi byte-identiche** alle sorgenti in `skills/` (verificato con `diff`). Nessuna deriva ancora, ma nessun meccanismo che la impedisca.

### Non verificabile

1. Se il **validatore di upload plugin di claude.ai** accetta `disable-model-invocation` nel frontmatter di una skill di plugin. La doc dichiara errore rigido per skill upload / Skills API / `package_skill.py`, non esplicitamente per i plugin — ma il canale reale passa da claude.ai. Da testare.
2. Se il runtime dell'agente in Desktop 1.40609.0 onora il campo (il runtime non è nel bundle su disco).
3. Comportamento reale post-compattazione con questo pacchetto specifico (nessuna sessione lunga eseguita).
4. Se un `SKILL.md` annidato a `references/modules/<x>/SKILL.md` venga mai raccolto da uno scanner di plugin come skill autonoma. Dedotto sicuro dalla doc (scansione a un livello sotto `skills/`), non provato.
5. Tutto ciò che riguarda ChatGPT Web (non Codex CLI): nessun ambiente disponibile per osservarlo direttamente. L'handoff fallito riportato in `PORTABILITA.md` v3 è preso come osservazione del progetto, non come verifica indipendente.

## C. Comportamento su Claude Code

### Scoperta e visualizzazione

- Le skill vivono in `<plugin>/skills/<nome>/SKILL.md`. Il campo manifest `skills` **si aggiunge** allo scan di default (a differenza di `commands`/`agents` che lo **sostituiscono**). `claude/.claude-plugin/plugin.json` non dichiara `skills` — corretto, lo scan di default basta.
- In sessione normale **solo le descrizioni** entrano nel contesto del modello; il corpo si carica all'invocazione. Descrizione + `when_to_use` sono **troncate a 1.536 caratteri** nel listing. Le descrizioni della suite vanno da 152 a 341 caratteri: ampiamente sotto soglia.
- Il campo `metadata:` usato per la versione è supportato e ignorato da Claude Code (free-form map), ed è uno dei sei campi ammessi dallo spec Agent Skills: sopravvive a tutti i canali.

### Invocazione manuale

- Comando: `/augmented-marketing-suite:define-marketing-challenge`. Il nome nudo `/define-marketing-challenge` funziona anch'esso, salvo collisione con un altro comando.
- Il frontmatter `name` di una skill di plugin **determina l'ultimo segmento del comando** (diverso dalle skill personali/progetto, dove conta la directory). I `name` attuali coincidono con le directory: nessuna sorpresa.
- `argument-hint` è disponibile per l'autocomplete e non è oggi utilizzato.

### Come si impedisce l'invocazione automatica

| Frontmatter | L'utente può invocare | Claude può invocare | Quando entra in contesto |
|---|---|---|---|
| *(default)* | Sì | Sì | Descrizione sempre in contesto |
| `disable-model-invocation: true` | **Sì** | **No** | **Descrizione NON in contesto**; corpo solo su invocazione utente |
| `user-invocable: false` | No | Sì | Descrizione sempre in contesto |

Conseguenze da mettere a bilancio:

1. La skill viene rimossa dal contesto del modello **interamente**. Ottimo per il rumore, ma l'orchestratore non "vede" più gli specialisti: la sua tabella di instradamento deve essere autosufficiente (lo è già).
2. Se Claude prova comunque a chiamarla, **Claude Code blocca la chiamata** e intima di non riprodurre i passi in altro modo. Nessuna simulazione silenziosa del metodo.
3. **`skillOverrides` non si applica alle skill di plugin.** Gli stati intermedi (`name-only`, `user-invocable-only`) sono fuori portata: per il plugin esistono solo i due campi frontmatter. L'utente non può riattivare l'auto-invocazione senza un aggiornamento del plugin.

Leve aggiuntive esistenti e non usate: `disallowed-tools`, `paths`, `context: fork` + `agent`, `model`, `effort`, `hooks`. Tutte Claude-only: se usate, diventano adattatore, non nucleo.

### Namespace e nomi dei comandi

- Namespace `plugin-name:skill-name`: nessun conflitto con skill personali/progetto/enterprise.
- Trappola versione-dipendente: scrivere `name: augmented-marketing-suite:design-campaign` non raddoppia il prefisso da **v2.1.246**, ma lo raddoppiava da v2.1.216 a v2.1.245. Regola operativa: mai prefissare a mano il `name`.
- Il nome di plugin `augmented-marketing-suite` è lungo: i comandi namespaced sono scomodi da digitare. Attrito UX reale, non difetto tecnico.

### Contesto, compattazione, conflitti

Rischio architetturale più concreto. Dalla documentazione:

> L'auto-compattazione riporta avanti le skill invocate entro un budget: i primi 5.000 token di ciascuna, con budget combinato 25.000 token, riempito partendo dalla più recente. Le più vecchie possono essere eliminate del tutto.

Applicato al caso concreto:

- `setup-business-context/SKILL.md` = 22.396 byte ≈ 5.600 token → **verrà troncato** al riaggancio. È l'unica sopra soglia, ma anche quella con i gate più densi.
- **Più serio:** i playbook che l'orchestratore carica con `Read` **non sono contenuto di skill**. Sono risultati di tool. La compattazione **non li riaggancia**: li riassume o li perde. Il prototipo ha ~69 KB di reference (~17k token) letti in questo modo.

Paradosso da considerare: l'architettura "una skill + playbook interni" è, dopo la compattazione, **più fragile** di tre skill sorelle invocate davvero, perché le skill invocate godono del riaggancio e i file letti no. Non è motivo per cambiare rotta — l'invocazione tra sorelle resta preclusa dal punto 4 e non è portabile — ma impone un requisito di progetto oggi assente dal prototipo: l'orchestratore deve mantenere un **blocco di stato breve** (sfida confermata / direzione approvata / decisioni e autorità) rigenerato a ogni passaggio, e **rileggere il playbook attivo** invece di assumerlo in contesto.

Conflitti tra descrizioni: nessuno rilevato. Le sei descrizioni sommano 1.716 caratteri e sono già scritte con confini negativi espliciti («non usarla per…»).

## D. Confronto con Codex

### Realmente comune

| Elemento | Claude Code | Codex/ChatGPT |
|---|---|---|
| Cartella skill + `SKILL.md` | `skills/<nome>/SKILL.md` | `skills/<nome>/SKILL.md` |
| Frontmatter minimo | `name`, `description` | `name`, `description` (gli unici due richiesti) |
| Progressive disclosure | Descrizione in contesto, corpo su invocazione | Idem |
| Reference relative nella cartella | Sì | Sì |
| Formato plugin con manifesto + `skills/` | `.claude-plugin/plugin.json` | `.codex-plugin/plugin.json` |
| Manifesto: `name`, `version`, `description`, `author`, `keywords`, `skills`, `hooks`, `mcpServers` | Sì | Sì (quasi identici) |
| **Controllo dell'invocazione automatica** | `disable-model-invocation: true` | `policy: allow_implicit_invocation: false` |

Il controllo dell'invocazione automatica ha **parità funzionale su entrambi gli harness**. Codex espone `allow_implicit_invocation` in `agents/openai.yaml`, sezione `policy`. Questo campo **non è oggi usato**: i sette `agents/openai.yaml` esistenti contengono solo `interface:`.

### Richiede adattatori differenti

| Elemento | Claude | Codex | Conseguenza |
|---|---|---|---|
| Manifesto | `.claude-plugin/plugin.json` | `.codex-plugin/plugin.json` | Due file, incomprimibili |
| Metadata UI | Nessun campo (usa `displayName`) | Blocco `interface:` in `agents/openai.yaml` (`display_name`, `brand_color`, `default_prompt`, icone, screenshot) | `agents/` deve restare fuori dal bundle Claude (oggi lo è) |
| Blocco auto-invocazione | Frontmatter del `SKILL.md` | `agents/openai.yaml` → `policy` | Lo stesso `SKILL.md` non può portare entrambi |
| Sintassi invocazione utente | `/nome` o `/plugin:nome` | `$nome` in CLI/IDE, `@` in ChatGPT, `/skills` | L'orchestratore non deve mai hard-codare la sintassi |
| Namespace | `plugin:skill`, isolamento garantito | Nomi globali, priorità per scope (`.agents/skills` → `$HOME/.agents/skills` → `/etc/codex/skills` → built-in) | Rischio collisione diverso |
| Budget listing | 1.536 caratteri per skill | ~2% della context window o 8.000 caratteri per l'intero roster, con avviso se qualcosa viene omesso | Codex penalizza chi installa molte skill: la suite compete con le altre dell'utente |

### Non rendibile equivalente

- **`disable-model-invocation` non è portabile come campo.** Un `SKILL.md` con quel campo, se caricato via upload skill claude.ai / Skills API / `package_skill.py`, **fallisce con errore rigido**: quei canali ammettono solo `name`, `description`, `license`, `compatibility`, `metadata`, `allowed-tools`. Colpisce direttamente il formato `dist/agent-skills/`: la build deve strippare il campo per quel target.
- **Handoff tra skill sorelle**: precluso su Claude per costruzione (col flag attivo) e già osservato fallire su ChatGPT Web in `PORTABILITA.md` v3. Non è equivalente da nessuna parte — è l'argomento più forte a favore dei playbook interni.
- **Metadata UI ricchi** (colore, icone, prompt di partenza, screenshot): esistono solo su Codex. Claude ha solo `displayName`.
- **Leve di contesto** (`context: fork`, `paths`, `disallowed-tools`, `hooks`, `model`, `effort`): solo Claude. Se il metodo dipendesse da queste, la portabilità finirebbe.
- **Semantica di compattazione**: la regola 5.000/25.000 token è documentata solo da Anthropic. Nessuna regola equivalente pubblicata per Codex: progettare per il caso peggiore.

### Rischio di dipendere da comportamenti specifici di un harness

1. **Fidarsi che l'orchestratore venga scelto.** Con gli specialisti spenti, tutto passa dalla descrizione dell'orchestratore. Se non triggera, l'utente non ha percorso, e non ha nemmeno più il fallback dell'auto-selezione degli specialisti. Single point of failure comportamentale su entrambi gli harness.
2. **Fidarsi che il flag sia onorato sul canale di distribuzione reale.** Vedi riserva bloccante in A.
3. **Fidarsi del riaggancio post-compattazione.** Numeri documentati ma versione-dipendenti e non contrattuali.

## E. Valutazione dell'architettura proposta

**Skill autonome + playbook interni: corretto.** `portability-audit.md` era già arrivato a questa conclusione, e la documentazione la conferma per una ragione più forte di quella disponibile in precedenza: non è solo che l'handoff *potrebbe* non funzionare — è che il punto 4 lo rende **impossibile per costruzione** su Claude.

**L'orchestratore può evitare di chiamare skill sorelle: sì, e deve.** Il prototipo lo fa già correttamente (legge integralmente un solo playbook per turno). Va aggiunta la disciplina anti-compattazione descritta in C (blocco di stato + rilettura del playbook attivo).

**Gli specialisti restano visibili e usabili singolarmente: sì.** `disable-model-invocation: true` li lascia nel menu `/` e invocabili a mano; su Codex `allow_implicit_invocation: false` fa lo stesso con `$nome`. Nessuna perdita di questa proprietà, ma la scopribilità cala: chi non conosce il nome non li trova, e su Claude si perde lo stato intermedio `name-only` perché `skillOverrides` non tocca i plugin.

**Una sorgente → due bundle affidabili: sì in teoria, non con l'attuale processo.** Oggi esistono tre formati costruiti a mano e già disallineati:

- `dist/claude` esclude l'orchestratore → punto 1 non soddisfatto su Claude;
- `design-campaign` v0.1.4 non è in nessun bundle, pur essendo sorgente candidata;
- le versioni nei manifest (`@0.6.4`, `@0.1.3`…) sono indietro rispetto alle sorgenti (`0.6.5`, `0.1.4`…): i pacchetti pubblicati non corrispondono al repo;
- i playbook del prototipo sono copie (oggi identiche, ma senza meccanismo che impedisca la deriva);
- `.agents/skills/setup-business-context/` è una directory vuota residua.

Il salto architetturale mancante non è concettuale, è **un build**: una sorgente unica dei playbook, e uno script che generi (a) le skill autonome, (b) l'orchestratore con i playbook incorporati come reference rinominate (`challenge.md`, `direction.md`, `mix.md`, non `SKILL.md` annidati), (c) i tre target con i campi giusti aggiunti o rimossi. Finché il processo è manuale, "una sola base concettuale" resta un'intenzione, non una proprietà osservata.

**Sul non compromettere il lavoro fatto:** l'architettura non lo compromette, ma l'ordine sì. Attivare `disable-model-invocation` **prima** di avere un orchestratore che triggera in modo affidabile su Claude peggiorerebbe l'esperienza attuale: oggi le cinque skill si attivano da sole e funzionano (verificato in questa sessione). Il flag va acceso **dopo** aver dimostrato l'affidabilità dell'orchestratore, non prima.

## F. Test minimo decisivo

Isolato, reversibile, ~45 minuti, senza toccare il repository né il plugin installato.

**Setup.** Copiare il bundle beta.8 in una cartella temporanea, rinominare il plugin `ams-probe` (namespace diverso, nessuna collisione con `augmented-marketing-suite` installato), ridurre a due skill specialistiche (`define-marketing-challenge`, `choose-marketing-direction`) più un orchestratore minimo `ams-router` con i due playbook come `references/challenge.md` e `references/direction.md`.

Frontmatter da provare:

```yaml
# skills/ams-router/SKILL.md
name: ams-router
description: "Punto di accesso al Marketing Agent System..."
# nessun flag: model-invocabile per default

# skills/define-marketing-challenge/SKILL.md
name: define-marketing-challenge
disable-model-invocation: true
argument-hint: "[obiettivo, problema o idea tattica]"
```

| # | Prova | Come | Passa se |
|---|---|---|---|
| 1 | Installazione sul canale reale | Carica lo ZIP `ams-probe` con lo stesso flusso degli utenti (Personalizza → Plugin su Desktop). **Test bloccante:** verifica che l'upload non rifiuti `disable-model-invocation` | Nessun errore di validazione |
| 2 | Visibilità | Nuova chat, digita `/ams` | Compaiono `/ams-probe:ams-router` e `/ams-probe:define-marketing-challenge` |
| 3 | Mancata attivazione automatica | Nuova chat: «Ho l'obiettivo di far conoscere un nuovo servizio ma non so quale problema affrontare». Poi: «elenca le skill che vedi disponibili» | Claude non invoca lo specialista e non lo elenca (descrizione fuori contesto). Se lo elenca, il flag non è onorato → NO-GO |
| 4 | Invocazione manuale | `/ams-probe:define-marketing-challenge` con un brief | Il metodo parte con gate e domande corrette |
| 5 | Orchestratore | Nuova chat, stessa frase del test 3 | `ams-router` si attiva da solo, legge un solo playbook, non simula l'altro (verificare una sola `Read` nel transcript) |
| 6 | Blocco delegazione | Chiedere esplicitamente «passa la mano alla skill specialistica» | Claude Code blocca la chiamata e propone il comando manuale, confermando che i playbook interni sono obbligatori |
| 7 | Continuità multi-turno | 4 turni: sfida → conferma → direzione → approvazione, senza reinvocare nulla | Nessuna richiesta di ripetere informazioni, gate rispettati |
| 8 | Compattazione | Riempire il contesto fino all'auto-compact (o `/compact`), poi chiedere di riassumere sfida confermata e direzione approvata con le rispettive autorità | Le decisioni sopravvivono. Se fallisce la prima volta, la correzione è nell'orchestratore (blocco di stato + rilettura), non nell'architettura |
| 9 | Aggiornamento | Bump a `0.0.2`, cambio di una frase osservabile, ricarica, `/reload-plugins` o riavvio | La nuova frase compare e i flag sopravvivono all'update |
| 10 | Rimozione | Disinstallare `ams-probe` | Sparisce da `/`, `augmented-marketing-suite` originale resta intatto |

**Prova gemella su Codex** (stesso nucleo, adattatore diverso): ripetere 2/3/4/5 con `agents/openai.yaml` contenente `policy: allow_implicit_invocation: false`, invocazione `$define-marketing-challenge`.

**Reversibilità:** tutto vive in una cartella temporanea e in un plugin con nome distinto. Disinstallare `ams-probe` riporta lo stato esatto di partenza.

## G. Condizioni di rinuncia

Abbandonare questa architettura (non il progetto) se:

1. **Test 1 fallisce** — il canale di distribuzione reale rifiuta o ignora `disable-model-invocation`. I punti 3 e 4 diventano incompatibili su Claude: scegliere tra specialisti auto-invocabili senza orchestratore centrale, oppure orchestratore unico che contiene tutto e specialisti non distribuiti su Claude.
2. **Test 3 fallisce** — il flag è accettato ma il modello continua a vedere o invocare gli specialisti. Stesso bivio del punto 1.
3. **Test 5 fallisce in modo persistente** — l'orchestratore non viene selezionato in modo affidabile su richieste di marketing plausibili. Con gli specialisti spenti non c'è rete di sicurezza: l'utente resta senza percorso. In quel caso non spegnere gli specialisti, mantenendo l'auto-selezione distribuita che oggi funziona.
4. **Test 8 fallisce anche dopo la correzione** — se le decisioni approvate non sopravvivono alla compattazione nemmeno con blocco di stato e rilettura, la promessa di continuità multi-turno (unico vantaggio misurato dell'orchestratore in `results.md`) evapora. Le skill autonome tornano superiori.
5. **Test 6 mostra simulazione** — se, bloccata la delega, Claude riproduce il metodo dello specialista a memoria invece di fermarsi, i confini di autorità sono compromessi. Per un prodotto che vende approvazioni verificabili, è un difetto fatale.
6. **Test 9 fallisce** — se un aggiornamento resetta i flag o cambia il namespace, ogni release rischia una regressione silenziosa su installazioni di terzi.
7. **Deriva strutturale** — se dopo tre release i playbook dell'orchestratore e le skill autonome sono ancora copie manuali, il problema non è l'harness: è la manutenzione di due prodotti chiamandoli uno.
8. **Il vantaggio non sopravvive al test umano** — `results.md` dichiara esplicitamente che non è un test con un marketer reale. Se con utenti veri il carico di digitare `/augmented-marketing-suite:...` supera il beneficio di continuità, il valore netto è negativo.

## Risposta alla domanda: affiderei questa architettura a un plugin per utenti Claude e OpenAI?

**Sì, ma non come un solo plugin curato a mano, e non prima del test 1+3.**

Tre condizioni non negoziabili:

1. **Un nucleo, tre build generate**, mai tre pacchetti curati a mano. I target divergono su campi che si escludono a vicenda (`disable-model-invocation` obbligatorio per il plugin Claude, vietato per l'upload skill claude.ai/OpenAI): la divergenza va gestita da uno script, non dalla memoria.
2. **Il test 1+3 prima di qualsiasi altra cosa.** È l'unico punto in cui l'intera premessa può crollare, e costa circa un'ora.
3. **Accendere il flag `disable-model-invocation` per ultimo.** Rimuove una capacità che oggi funziona davvero (verificata in questa sessione: le cinque skill si auto-selezionano correttamente). Va sostituita da un orchestratore affidabile prima di essere tolta, non contemporaneamente.

`prototypes/augmented-marketing-comparative-test/portability-audit.md` era già arrivato alla conclusione corretta (NO-GO per un orchestratore che dipende dall'handoff runtime) senza avere questa prova documentale. Questo audit non la smentisce: la rende più stringente, perché su Claude quell'handoff non è incerto — è bloccato dal meccanismo stesso richiesto per il punto 4.
