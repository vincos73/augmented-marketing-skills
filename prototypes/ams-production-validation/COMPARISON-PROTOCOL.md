# Protocollo di confronto pre-produzione AMS

Data di congelamento: 31 agosto 2026
Branch: `codex/ams-production-validation`
Baseline: AMS Vertical Slice v0.1.2

## Scopo

Completare soltanto le condizioni mancanti del collaudo Fabriloom e confrontare:

1. `VERTICAL`: AMS Vertical Slice v0.1.2, evidenza già congelata;
2. `CURRENT`: Augmented Marketing Suite rilasciata v0.1.0-beta.8;
3. `GENERALIST`: lo stesso modello senza skill AMS e con istruzioni neutrali.

Il confronto misura errori, ripetizioni, continuità, copertura, rework osservabile e attrito. Non
misura tempo reale risparmiato e non sostituisce un test con marketer.

## Evidenza Vertical Slice riutilizzata

Si riutilizzano senza modificarli:

- `prototypes/ams-vertical-slice/results/v0.1.2-final-verdict.md`;
- i risultati runtime Codex e Claude v0.1.2;
- i transcript e le valutazioni v0.1.2;
- `prototypes/ams-vertical-slice/EVAL-RUBRIC.md`;
- `prototypes/ams-vertical-slice/TEST-PROTOCOL.md`;
- i cinque materiali Fabriloom, lo script di decisioni e i risultati simulati congelati.

Il baseline contiene una esecuzione completa per harness. La nuova numerosità iniziale è quindi
una esecuzione per candidato e harness. Si aggiungono prove soltanto se una risposta è ambigua,
incompleta per un errore di harness o molto variabile rispetto alle decisioni controllate.

## Comparabilità

| Dimensione | Codex | Claude |
|---|---|---|
| Materiali | identici, verificati con `materials.sha256` | identici, verificati con `materials.sha256` |
| Compito e decisioni | stessi otto prompt e stesso script | stessi otto prompt e stesso script |
| Numerosità baseline | una esecuzione completa | una esecuzione completa |
| Modello baseline | non registrato nei risultati pubblicabili v0.1.2 | Claude Opus 5, impegno alto |
| Nuove prove | `gpt-5.6-sol`, reasoning `xhigh` | Claude Opus 5, impegno alto, se accessibile |
| Continuità | stessa conversazione per candidato | stessa conversazione per candidato |

La risposta Vertical Slice Codex resta confrontabile per materiali, compito e condizioni, ma il
confronto strettamente matched sul modello non è dimostrabile dai metadati pubblicabili esistenti.
Non si ripete automaticamente la Vertical Slice: la risposta completa esiste ed è congelata; il
limite viene mantenuto nell'interpretazione.

## Definizione delle condizioni

### CURRENT

Usa il bundle rilasciato `augmented-marketing-suite-0.1.0-beta.8.zip`, hash dichiarato nel
repository `27f2f650f24ff306d8a4f21256a49f0a196a0061a717603ab64e31d2953f379d`.

L'adattatore OpenAI contiene l'Assistant conversazionale e cinque specialisti: contesto,
fondamenti, sfida, direzione e marketing mix. L'adattatore Claude contiene i cinque specialisti,
ma non l'Assistant. Le skill candidate presenti nel branch ma assenti dai bundle rilasciati non
appartengono a CURRENT. Per ogni passaggio disponibile si usa una vera invocazione runtime. Le
capacità assenti non vengono simulate né sostituite con lavoro generalista.

### GENERALIST

Usa una directory e un profilo puliti senza skill AMS. Riceve i materiali, il compito comune e
questa sola istruzione neutrale:

> Non usare, cercare o leggere skill, plugin, playbook o documenti di Augmented Marketing Suite.
> Distingui fatti, ipotesi, proposte e decisioni confermate; non superare le autorità indicate;
> non inventare numeri; procedi un passaggio alla volta e poni al massimo tre domande per turno.

## Sequenza congelata

1. Verificare gli hash dei cinque materiali.
2. Creare una conversazione pulita per ciascun candidato e harness.
3. Fornire soltanto i cinque materiali e il prompt iniziale comune.
4. Inviare, senza adattamenti sostanziali, i turni 2-7 già congelati.
5. Al turno 8 fornire integralmente `fixture/simulated-results.md`; non usare il percorso errato
   documentato nel primo run Claude.
6. Salvare la risposta dopo ogni turno e il transcript integrale prima della valutazione.
7. Non correggere retroattivamente nessuna risposta congelata.

Per CURRENT le invocazioni tecniche necessarie vengono aggiunte al turno corrispondente e
conteggiate come attrito. Per GENERALIST non si aggiungono istruzioni di metodo specifiche della
Suite.

## Isolamento Codex

- modello: `gpt-5.6-sol`;
- reasoning: `xhigh`;
- profilo temporaneo distinto per CURRENT e GENERALIST;
- directory di lavoro in sola lettura contenente soltanto i materiali consentiti;
- nessuna memoria di altre esecuzioni;
- nessuna scrittura canonica, ricerca o azione esterna.

Il modello e il livello di reasoning sono verificati nei metadati del runtime, non dedotti dal
solo comando.

## Isolamento Claude

- modello: Claude Opus 5;
- impegno: alto;
- esecuzione locale in Claude Code Desktop, perché la modalità cloud non esponeva in modo
  osservabile le skill locali in sequenza;
- chat pulita per CURRENT e GENERALIST;
- Vertical Slice disattivata durante CURRENT e GENERALIST;
- suite corrente attiva solo durante CURRENT;
- per GENERALIST nessuna skill AMS deve essere attiva o invocata;
- nessuna simulazione di Claude da Codex.

I tentativi cloud nei quali le skill locali non erano richiamabili sono esclusi dal campione. I
due run validi sono quelli locali, con modello, impegno, disponibilità delle skill e sequenza
verificati nell'interfaccia e nei transcript congelati.

## Valutazione cieca

Le risposte congelate vengono copiate in file con identificatori casuali. La chiave resta in
`private/blind-key.md`, ignorata da Git. Un valutatore separato riceve soltanto:

- le tre risposte anonime;
- i cinque materiali Fabriloom;
- lo script di decisioni e i risultati simulati;
- la rubrica congelata, senza nomi di candidato o tracce di skill.

Misure:

- hard fail e soft fail;
- correttezza rispetto ai materiali;
- claim o decisioni inventate;
- domande ripetute;
- continuità delle decisioni confermate;
- chiarezza per un marketer;
- correzioni sostanziali necessarie;
- passaggi e invocazioni manuali;
- contesto ripetuto dall'utente;
- lunghezza o complessità non giustificate;
- fasi completate su otto;
- vantaggio osservabile rispetto al generalista.

Le metriche automatiche, le valutazioni simulate del modello e le osservazioni di utenti reali
restano categorie separate.

## Soglia del verdetto

Il referto termina con uno solo fra:

- `NO-GO`;
- `NEEDS REDESIGN`;
- `READY FOR MARKETER PILOT`;
- `INCOMPLETE — ACTION REQUIRED`.

Senza test con marketer reali non è consentito dichiarare `READY FOR RELEASE`.
