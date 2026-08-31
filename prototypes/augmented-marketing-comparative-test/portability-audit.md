# Audit di portabilità — orchestrazione multi-harness

Data: 2026-08-30

## Verdetto

La forma più promettente non è una skill centrale che invoca altre skill installate. È **una singola skill portabile che seleziona playbook interni**, distribuita attraverso adattatori distinti per ogni harness.

Il nucleo può essere comune; il plugin installabile non può essere letteralmente lo stesso artefatto su ogni piattaforma perché manifest, namespace, discovery e controlli di invocazione differiscono.

## Evidenze osservate

1. Claude Code dichiara che le skill seguono lo standard aperto Agent Skills e usa cartelle con `SKILL.md` e risorse di supporto. Estende però lo standard con controlli di invocazione, subagenti, contesto e namespace del plugin. [Documentazione Claude sulle skill](https://code.claude.com/docs/en/slash-commands)
2. Un plugin Claude usa `.claude-plugin/plugin.json`; le skill del plugin vivono sotto `skills/` e sono invocate con namespace del plugin. [Documentazione Claude sui plugin](https://code.claude.com/docs/en/plugins), [riferimento tecnico](https://code.claude.com/docs/en/plugins-reference)
3. OpenAI accetta skill come directory o archivio ZIP e gestisce versioni immutabili tramite la Skills API. Questo conferma la portabilità del pacchetto di skill, non l'identità del manifest del plugin. [OpenAI Skills API](https://developers.openai.com/api/reference/python/resources/skills/methods/create)
4. Nel repository corrente il bundle OpenAI usa [`.codex-plugin/plugin.json`](../../.codex-plugin/plugin.json), mentre quello Claude usa [`.claude-plugin/plugin.json`](../../claude/.claude-plugin/plugin.json). Il bundle Claude beta.8 esclude già l'Assistant centrale.
5. Il [contratto di portabilità esistente](../../PORTABILITA.md) separa correttamente nucleo e adattatori e richiede forward test distinti. Il nuovo confronto non lo smentisce; rende più precisa la forma del possibile orchestratore.

## Perché il prototipo funziona in Codex

Il prototipo non effettua un handoff reale verso tre skill installate. Carica un solo `SKILL.md` e legge il playbook pertinente da file inclusi nella propria cartella. Il successo osservato è quindi quello di una **skill composita a caricamento progressivo**, non la prova di un router universale fra skill.

Questa distinzione è decisiva. Un harness può:

- non consentire a una skill di attivarne un'altra;
- esporre nomi o namespace differenti;
- scegliere autonomamente di non caricare una skill che ritiene non necessaria;
- perdere parte del contesto caricato dopo compaction;
- avere strumenti, permessi e sintassi di invocazione differenti.

Il prototipo attuale è quindi una prova comportamentale, non ancora il nucleo neutro definitivo. Prima di un bundle Claude andrebbero risolti tre dettagli senza toccare il metodo:

- `agents/openai.yaml` deve restare esclusivo dell'adattatore OpenAI;
- versione e metadata devono essere espressi nei campi effettivamente supportati dal singolo harness, senza affidare al nucleo decisioni di caricamento;
- i file annidati chiamati `SKILL.md` dovrebbero diventare reference neutrali come `challenge.md`, `direction.md` e `marketing-mix.md`, evitando che uno scanner li interpreti come skill autonome o che il pacchetto sembri dipendere da un handoff.

## Architettura consigliata

```text
marketing-decision-path/
├── SKILL.md
└── references/
    └── playbooks/
        ├── challenge.md
        ├── direction.md
        └── marketing-mix.md

adapters/
├── openai/
│   └── .codex-plugin/plugin.json
└── claude/
    └── .claude-plugin/plugin.json
```

Principi:

- un solo nucleo provider-neutral;
- playbook nominati come reference, non come skill annidate;
- nessuna dipendenza dal comando usato per invocare un'altra skill;
- percorsi relativi risolti dalla cartella della skill;
- output, autorità e approvazioni identici nei due adattatori;
- metadata UI, manifest, permessi e namespace confinati nell'adattatore;
- due bundle generati dalla stessa sorgente e verificati separatamente.

## Rapporto con il lavoro esistente

Le skill autonome non vanno eliminate. Restano:

- unità di authoring e test del metodo;
- ingressi diretti quando l'utente sa già che cosa gli serve;
- fallback per harness che gestiscono male la skill composita;
- base di confronto per regressioni.

Per evitare deriva, il passo futuro non dovrebbe mantenere copie manuali indipendenti dei tre `SKILL.md`. Prima di migrare occorre scegliere una fonte unica dei playbook e generare o assemblare da quella sia le skill autonome sia la skill composita. Questa è una migrazione architetturale e non è stata applicata in questo test.

## Matrice di rischio

| Elemento | Portabilità attesa | Rischio |
|---|---|---|
| `SKILL.md` con istruzioni neutrali | Alta | Differenze di interpretazione del modello |
| Reference relative incluse nella stessa skill | Alta | Percorsi o caricamento progressivo da verificare |
| Invocazione automatica basata sulla description | Media | Trigger e budget delle descrizioni variano |
| Skill centrale che invoca skill sorelle | Bassa | Dipendenza forte dall'harness |
| Manifest unico per tutti gli harness | Bassa | Formati e namespace incompatibili |
| Sorgente unica con due adattatori e due bundle | Alta | Richiede build e QA separati |
| Hook, subagenti, UI o MCP come requisito del metodo | Bassa | Capability non uniformi |

## Test runtime ancora necessario su Claude

Il runtime `claude` non era disponibile nell'ambiente di questa prova. Restano da verificare in una nuova sessione Claude:

1. discovery del plugin e della skill composita;
2. caricamento di un solo playbook per turno;
3. continuità sfida → direzione → mix senza nuove invocazioni;
4. mantenimento delle decisioni dopo compaction;
5. fallback quando una reference non è accessibile;
6. assenza di attivazione concorrente delle skill autonome;
7. comportamento con invocazione esplicita e automatica.

Finché questo forward test non viene eseguito, la portabilità verso Claude resta **architetturalmente plausibile ma non provata**.
