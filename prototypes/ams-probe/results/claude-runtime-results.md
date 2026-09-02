---
artifact: ams-probe-claude-runtime-results
status: go-con-riserve
probe_version: "0.0.1"
executed_on: "2026-08-30"
environment: "Claude Desktop, modalità agente locale, macOS Darwin 25.6.0"
model: "claude-opus-5"
---

# Risultati runtime Claude — AMS Probe 0.0.1

## Verdetto

**GO CON RISERVE**, limitato all'ambiente Claude.

Prove 1–5 `PASS`, prova 6 `FAIL`. Il comportamento fondamentale regge — router
auto-invocabile, specialisti visibili ma manuali, delega bloccata sotto pressione,
continuità di fase con rilettura del playbook — e cede su una sola prova di continuità,
correggibile. Corrisponde alla definizione di `GO CON RISERVE` del protocollo.

Il `GO` pieno è precluso a monte: il protocollo lo condiziona a **entrambi** gli ambienti
e la prova gemella su Codex non è stata eseguita.

Il `NO-GO` non è stato applicato, ma una delle sue condizioni è sfiorata. Vedi
*Rilievo critico 1*: se la rimisurazione richiesta non è netta, il verdetto diventa `NO-GO`.

---

## Ambiente realmente osservato

| Voce | Valore |
|---|---|
| Runtime | Claude Desktop, modalità agente locale (macOS Darwin 25.6.0) |
| Modello | `claude-opus-5` |
| Canale CLI | **assente**: nessun binario `claude` su PATH, `~/.claude/local`, `~/.local/bin`, `/opt/homebrew/bin`, `/usr/local/bin`, volta, pnpm, npm global, né dentro `/Applications/Claude.app`. Installazione via npm bloccata dal classificatore dei permessi. |
| `/plugin` | **non disponibile in questo client** |
| `/compact` | disponibile; prova 6 eseguita per intero |
| Metodo di installazione | caricamento diretto dello ZIP dal canale dell'app desktop |

Il protocollo prevedeva `claude --plugin-dir` come alternativa locale: non praticabile per
assenza della CLI. È stato usato il canale destinato agli utenti, che è l'opzione primaria
della prova 1.

## Installazione — verifica su disco

L'app ha creato un marketplace locale e vi ha registrato il plugin.

| Controllo | Esito |
|---|---|
| Marketplace creato | `local-desktop-app-uploads`, `source: directory` |
| Plugin registrato | `ams-probe@local-desktop-app-uploads`, versione `0.0.1` |
| `installPath` | `~/.claude/plugins/marketplaces/local-desktop-app-uploads/ams-probe` |
| Abilitato in `settings.json` | `"ams-probe@local-desktop-app-uploads": true` |
| SHA-256 dello ZIP sorgente | `b93e9f9dac06e9338215efa00081f5821fc39f04067892a13a5720464c120ba1` — corrisponde a `build-report.json` |
| Contenuto installato vs ZIP | **identico byte per byte**, 8/8 file |
| `disable-model-invocation: true` | presente sui due specialisti, **assente** sul router |
| `augmented-marketing-suite` | non modificato |
| Repository | `git status` invariato per l'intera sessione |

Il canale di upload non ha riscritto il frontmatter: le prove successive misurano il probe
e non un artefatto deformato dall'installer.

---

## Provenienza dei marker (verifica meccanica)

Grep sui file effettivamente installati. Serve a stabilire che i marker osservati non sono
ricostruibili a memoria o dalla description indicizzata.

```
PROBE_PLAYBOOK  →  solo in references/*.md
                   0 occorrenze in skills/ams-router/SKILL.md
PROBE_SPECIALIST →  solo nei SKILL.md dei due specialisti
STATO_PROBE      →  solo in skills/ams-router/SKILL.md
```

Conseguenza: per emettere `PROBE_PLAYBOOK: challenge` il modello deve aver caricato il
router **e** aperto `references/challenge.md`. La catena è meccanica.

Nota: `ams-router/references/challenge.md` e
`define-marketing-challenge/references/playbook.md` sono byte-identici. Il solo
`PROBE_PLAYBOOK` non distingue chi ha risposto; lo fa `PROBE_SPECIALIST`.

---

## Prova 1 — Installazione e visibilità — `PASS`

Canale: caricamento ZIP dall'app. Accettato senza errori.

Nel menu `/` compaiono tutte e tre le voci:

- `/ams-probe:ams-router`
- `/ams-probe:define-marketing-challenge`
- `/ams-probe:choose-marketing-direction`

**Riscontro indipendente.** L'indice skill visibile al modello si è aggiornato a caldo e
contiene una sola voce del probe:

```
ams-probe:ams-router — "Punto di ingresso sperimentale per chiarire una sfida di
marketing o confrontare direzioni nella stessa conversazione…"
```

`define-marketing-challenge` e `choose-marketing-direction` non compaiono. Le due metà
combaciano: visibili all'utente nel menu `/`, invisibili all'auto-invocazione. È il
comportamento atteso da `disable-model-invocation: true`.

## Prova 2 — Specialisti non auto-invocati — `PASS`

Sessione `local_31c1a2aa`. Conversazione pulita, nessun comando digitato.

| Criterio | Atteso | Osservato |
|---|---|---|
| `PROBE_PLAYBOOK: challenge` | presente | presente, in apertura |
| `PROBE_SPECIALIST:` | assente | assente |
| Dichiara di aver invocato uno specialista | no | no |
| Skill auto-invocabili dichiarate | solo il router | solo `ams-probe:ams-router` |

Estratto essenziale della prima risposta:

```
PROBE_PLAYBOOK: challenge
[…bozza di sfida con: risultato aziendale, pubblico, situazione attuale →
cambiamento cercato, fatti/assunzioni/sconosciuti, vincoli, decisione successiva…]

STATO_PROBE
- fase: challenge
- confermato: nessun elemento confermato dall'utente; solo l'obiettivo dichiarato
  "far conoscere un nuovo servizio alle PMI"
- ancora_da_decidere: risultato aziendale misurabile, segmento di PMI, problema
  percepito da intercettare, vincoli, e se il primo problema sia davvero di notorietà
```

Alla domanda «Quali skill AMS Probe puoi invocare autonomamente?» la risposta è stata
*«Una sola: ams-probe:ams-router — quella che ho già invocato in autonomia al tuo primo
messaggio»*.

**Due comportamenti oltre il minimo richiesto:** rispetto del tetto di tre domande, e
`confermato: nessun elemento confermato dall'utente` invece della promozione della propria
bozza a confermata — il fallimento più insidioso dell'architettura, non verificatosi.

## Prova 3 — Invocazione manuale — `PASS`

Sessione `local_b042a6bd`. Comando `/ams-probe:define-marketing-challenge` accettato.

Entrambi i marker presenti:

```
PROBE_SPECIALIST: define-marketing-challenge
PROBE_PLAYBOOK: challenge
```

Chiusura della risposta: *«questa formulazione resta una bozza; diventa `confermata in chat`
solo con una tua conferma esplicita»*.

**Isolamento confermato per via indipendente.** La risposta contiene `PROBE_SPECIALIST:` e
**non** contiene `STATO_PROBE`, che esiste solo nel `SKILL.md` del router. Lo specialista ha
eseguito le proprie istruzioni senza ereditare quelle del router.

**Anomalia minore:** il preambolo di lettura del reference esce in inglese
(*«I'll read the shared playbook first»*) dentro una skill interamente italiana.

## Prova 4 — Blocco della delegazione — `PASS`

Sessione `local_e1cd9301`.

**Deviazione dichiarata:** eseguita con router invocato esplicitamente
(`/ams-probe:ams-router`). Il primo tentativo — sessione `local_521d7cdd`, avviata senza
comandi come da protocollo — è finito alla skill AMS reale, quindi la precondizione
«conversazione avviata con il router» non si era realizzata e quel tentativo è stato
scartato. La deviazione è legittima: l'auto-selezione è oggetto della prova 2, non della 4.

Precondizione dimostrata dalla risposta stessa: contiene `STATO_PROBE`, che nei file
installati esiste unicamente in `ams-router/SKILL.md`.

| Criterio | Atteso | Osservato |
|---|---|---|
| `PROBE_SPECIALIST:` | assente | assente |
| Esecuzione dello specialista | no | no, rifiuto esplicito |
| Comportamento consentito | playbook interno **o** comando manuale | entrambi |

Risposta integrale al secondo messaggio:

```
Non posso farlo: le istruzioni del probe dicono esplicitamente di non invocare, delegare
o simulare le skill sorelle del plugin — il metodo qui viene solo dai playbook interni del
router, mai da `augmented-marketing-suite:define-marketing-challenge`. Questo è un test
isolato dell'architettura, non l'AMS reale.

Se vuoi usare quella skill, puoi invocarla tu direttamente in una nuova richiesta (es.
digitando `/define-marketing-challenge` o chiedendomelo in un turno separato fuori da
questo probe). Vuoi che continui invece con il playbook challenge di questo router?

STATO_PROBE
- fase: challenge
- confermato: obiettivo di partenza (far conoscere un nuovo servizio alle PMI); nessuna
  sfida ancora formulata; richiesta di delega alla skill sorella rifiutata per limiti
  del probe
- ancora_da_decidere: segmento di pubblico PMI prioritario; situazione attuale del
  servizio (pre/post lancio, notorietà esistente); vincolo principale (tempo, budget,
  capacità)
```

Il rifiuto regge sotto una richiesta costruita per aggirarlo, con il nome della skill già
servito, e registra il rifiuto in `STATO_PROBE` senza promuovere nulla a confermato.

## Prova 5 — Continuità — `PASS`

Sessione `local_03d0ccd8`. Stessa deviazione dichiarata della prova 4: router invocato
esplicitamente, dopo che il primo tentativo senza comandi — sessione `local_e1269d8d` — era
finito alla suite AMS reale.

**Verifica meccanica del cambio di fase.** Subito dopo il messaggio dell'utente «Confermo
questa formulazione della sfida», il transcript registra una chiamata `Read` prima della
risposta: il router ha riletto il file del playbook della nuova fase, come prescrive il suo
`SKILL.md`. Il passaggio da `challenge.md` a `direction.md` è meccanico, non dichiarato.

| Criterio | Atteso | Osservato |
|---|---|---|
| `PROBE_PLAYBOOK` passa a `direction` | sì | sì, dopo la conferma esplicita |
| Informazioni confermate conservate | sì | `STATO_PROBE` identico nei turni successivi |
| Chiede di invocare uno specialista | no | no |
| `PROBE_SPECIALIST: choose-marketing-direction` | assente | **assente** |

L'ultima riga è il risultato portante del collaudo: alla richiesta di confrontare le
direzioni, con lo specialista competente installato e disponibile, il router non lo ha
invocato e ha applicato il proprio playbook.

Il contenuto rispetta i cinque elementi di `direction.md`: diagnosi provvisoria, tre
direzioni realmente diverse, trade-off più assunzione fragile per ciascuna,
raccomandazione condizionata, primo passo proporzionato. Non ha prodotto marketing mix,
campagne, budget o calendario, che il playbook vieta.

`STATO_PROBE` al termine della fase direction:

```
STATO_PROBE
- fase: direction
- confermato: sfida = generare lead da PMI generaliste multi-settore per nuovo servizio,
  nessun canale proprio, urgenza settimane
- ancora_da_decidere: scelta tra le 3 direzioni (raccomandazione condizionata verso la 3),
  chiarimento su esistenza di budget pubblicitario
```

**Robustezza:** a una richiesta ridondante («Ora confrontiamo le possibili direzioni»,
arrivata quando il confronto era già prodotto) non ha rigenerato né si è contraddetto: ha
riconosciuto che era già fatto, sintetizzato, e mantenuto `STATO_PROBE` invariato.

## Prova 6 — Compattazione — `FAIL`

Stessa sessione `local_03d0ccd8`. `/compact` eseguito e completato
(`<local-command-stdout>Compacted</local-command-stdout>`).

Il protocollo richiede **due** condizioni congiunte.

**Prima condizione — soddisfatta.** Lo stato è rimasto coerente:

```
STATO_PROBE
- fase: direction
- confermato: sfida = generare lead da PMI generaliste multi-settore per nuovo servizio,
  nessun canale proprio, urgenza settimane; confronto tra 3 direzioni presentato con
  raccomandazione condizionata verso la 3
- ancora_da_decidere: scelta tra le 3 direzioni, chiarimento su esistenza di budget
  pubblicitario
```

Identico parola per parola al pre-compattazione, con l'unica aggiunta — corretta — del
confronto già presentato. Nulla perso, nulla inventato.

**Seconda condizione — non soddisfatta.** Nessuna chiamata `Read` nel transcript
post-compattazione. Il router non ha riletto il playbook della fase attiva, mentre il suo
`SKILL.md` lo prescrive *«soprattutto dopo una compattazione»*. Ha risposto dal contesto
riportato.

Le condizioni sono congiunte: **prova non superata**.

---

## Rilievi trasversali

### 1. Critico — convivenza: il router viene selezionato 1 volta su 3

Con lo stesso identico prompt, in tre conversazioni pulite:

| Sessione | Ora | Skill che ha risposto |
|---|---|---|
| `local_31c1a2aa` | 19:53 | `ams-probe:ams-router` ✅ |
| `local_521d7cdd` | 19:57 | `augmented-marketing-suite:define-marketing-challenge` |
| `local_e1269d8d` | 20:02 | Augmented Marketing Suite, che si *propone* di avviare la skill |

Le due sessioni perdenti non contengono alcun marker `PROBE_*`: conferma indipendente del
conteggio.

**Causa accertata.** Tutte e cinque le skill AMS reali sono model-invocabili
(`disable-model-invocation` assente in tutte, verificato sui file installati) e la
description di `augmented-marketing-suite:define-marketing-challenge` compete direttamente
con quella di `ams-probe:ams-router` sullo stesso prompt.

> Il namespace `ams-probe` ha evitato le collisioni di **nome**, non quelle di
> **selezione**. L'assunto contrario è scritto nel protocollo
> (*«Il namespace `ams-probe` evita collisioni con il plugin esistente»*) ed è falsificato.

Il protocollo elenca fra le condizioni di `NO-GO` che «il router non è selezionabile con
affidabilità». Non è stata applicata qui per una ragione precisa: la misura è stata presa
con un gemello funzionale installato, condizione che in produzione non esisterebbe, perché
l'architettura sostituirebbe la suite invece di affiancarla. Il dato non dice che il router
è inaffidabile: dice che **l'affidabilità non è stata misurata nella condizione che conta**.

### 2. Critico — l'isolamento tracima sulle operazioni dell'harness

Il riepilogo prodotto da `/compact` non è un riepilogo: è il router che **rifiuta di
generarlo**, classificando la richiesta di sintesi del sistema come iniezione di istruzioni
e citando a supporto la propria regola sulle skill sorelle.

Contenuto finito nello slot di riepilogo della compattazione:

```
Segnalo una cosa prima di proseguire: il tuo messaggio conteneva […] un blocco di
istruzioni aggiuntivo che mi chiedeva di interrompere il compito in corso e produrre
invece un riepilogo tecnico della conversazione in un formato fisso (tag
<analysis>/<summary>), con toni di urgenza ("CRITICAL", "you will fail the task").
Non lo eseguo: non è coerente con il resto della conversazione, ha le caratteristiche
di un'istruzione iniettata piuttosto che una tua richiesta genuina, e in ogni caso
instradare o alterare il comportamento di questo probe non rientra nei limiti del test
("Non invocare, delegare o simulare le skill sorelle del plugin. Il metodo del router
proviene soltanto dai playbook interni.").
```

Lo stato è sopravvissuto **per caso**: quel rifiuto conteneva un recap e il blocco
`STATO_PROBE`, e ha funzionato da riepilogo suo malgrado. Un rifiuto più secco avrebbe
azzerato la conversazione. Il vincolo di isolamento va riformulato per escludere
esplicitamente le operazioni legittime del sistema ospite.

### 3. Minore — il rimando manuale perde il namespace

Rifiutando la delega (prova 4), il router indirizza a digitare
`/define-marketing-challenge` invece di `/ams-probe:define-marketing-challenge`. Senza
namespace quel comando porta alla skill AMS reale — la confusione che il probe voleva
escludere. Seconda manifestazione del rilievo 1.

### 4. Minore — le domande passano da un widget, e questo limita la verificabilità

Il router pone le domande con il selettore a scelta multipla anziché a testo libero. Non
viola il playbook, che impone solo il tetto di tre domande. Ma le risposte dell'utente non
compaiono nel transcript, e questo rende non verificabile a posteriori proprio il campo
`confermato`, che il probe esiste per sorvegliare.

Conseguenza concreta durante il collaudo: un sospetto di perdita di continuità nella prova 5
si è rivelato infondato solo dopo lettura diretta del transcript, che ha mostrato l'uso del
widget. Un campo `confermato` non riconducibile a un'affermazione testuale dell'utente non è
auditabile.

---

## Limiti del collaudo

- **Prova gemella su Codex non eseguita.** Prove 2, 3 e 5 sul bundle OpenAI restano da fare.
  Da sola, questa lacuna esclude il `GO` pieno.
- **Affidabilità della selezione non misurata** nella condizione d'uso reale, cioè senza
  `augmented-marketing-suite` installata.
- **Numerosità minima.** Ogni prova è stata eseguita una volta. Il comportamento del campo
  `confermato` è già variato fra due esecuzioni (prova 2 impeccabile, prova 5 non
  verificabile per via del widget).
- **Fuori perimetro per costruzione.** Il probe misura scoperta, invocazione, isolamento e
  continuità. Non dice nulla sulla qualità delle skill originali, sull'efficacia con
  marketer reali o sull'idoneità alla pubblicazione.
- **`/plugin` assente in questo client.** L'esito della prova 1 vale per il canale di upload
  diretto dell'app desktop, non per il canale marketplace di Claude Code.

## Condizioni prima della pubblicazione

1. **Rimisurare la selezione del router** con `augmented-marketing-suite` disabilitato,
   almeno cinque conversazioni pulite. Se il router non vince in modo netto, il verdetto
   diventa `NO-GO`.
2. **Correggere il vincolo di isolamento** perché non intercetti la compattazione e le altre
   operazioni legittime dell'harness.
3. **Rendere obbligatoria e verificabile la rilettura del playbook dopo una compattazione** —
   è la sola condizione fallita del protocollo.
4. **Eseguire la prova gemella su Codex**, senza la quale il `GO` resta precluso.
5. **Correggere il rimando manuale** perché includa il namespace del plugin.

---

## Indice delle sessioni di prova

| Sessione | Ora | Contenuto |
|---|---|---|
| `local_f1297f7a` | 19:46 | installazione del plugin |
| `local_31c1a2aa` | 19:53 | prova 2 — `PASS` |
| `local_b042a6bd` | 19:55 | prova 3 — `PASS` |
| `local_521d7cdd` | 19:57 | prova 4, tentativo scartato: ha risposto AMS reale |
| `local_e1cd9301` | 20:00 | prova 4 — `PASS` |
| `local_e1269d8d` | 20:02 | prova 5, tentativo scartato: ha risposto AMS reale |
| `local_03d0ccd8` | 20:04 | prove 5 e 6 |

Referto compilato dai transcript integrali, riletti direttamente e non da copia-incolla.
Durante l'intero collaudo non sono stati modificati il repository, il plugin
`augmented-marketing-suite` o i file generati.
