# Referto di prontezza pre-produzione AMS

Data: 31 agosto 2026

## Sintesi per decisione

Il confronto Codex è completo. La Vertical Slice v0.1.2 supera sia CURRENT sia GENERALIST sul
compito Fabriloom per copertura, coerenza delle quattro P, allineamento dell'asset e minore rework.
GENERALIST resta competitivo: completa 8/8, è leggibile e non presenta hard fail. CURRENT si
ferma a 4/8 perché il bundle pubblicato non contiene Campaign Core o Content Core.

La conclusione multipiattaforma non è completa. Il Mac si è bloccato prima dei due nuovi run
Claude e richiede sblocco manuale. Inoltre il baseline Codex v0.1.2 non registra nei materiali
pubblicabili il modello usato, quindi il matching stretto del modello non è dimostrabile senza
ripetere una prova già congelata.

## Evidenze riutilizzate

- Vertical Slice v0.1.2 completa su Codex e Claude;
- router e specialisti manuali verificati;
- continuità dopo ripresa e compattazione verificata;
- sorgenti, bundle e hash verificati;
- referto precedente `GO CON RISERVE` mantenuto immutato.

Non è stata eseguita una nuova Vertical Slice: esistono già risposte complete con gli stessi
materiali, compito e condizioni. Il limite del modello Codex resta dichiarato invece di produrre
automaticamente una nuova baseline.

## Nuove evidenze

| Harness | CURRENT | GENERALIST | Confronto cieco |
|---|---|---|---|
| Codex | completo, 4/8 e arresto controllato | completo, 8/8 | completo |
| Claude | non eseguito: sblocco manuale richiesto | non eseguito: sblocco manuale richiesto | non eseguibile senza le due risposte |

## Lettura del confronto Codex

### Vertical Slice

- 8/8 fasi;
- nessun hard fail o claim materiale inventato;
- nessuna domanda ripetuta;
- rework basso;
- vantaggio osservabile rispetto al generalista nella governance decisionale.

### CURRENT

- 4/8 fasi;
- un hard fail strutturale di copertura;
- cinque invocazioni tecniche nel percorso;
- nessun vantaggio end-to-end rispetto al generalista;
- non richiede una semplice correzione editoriale, ma una capacità aggiuntiva.

### GENERALIST

- 8/8 fasi e nessun hard fail;
- due riconferme ripetute;
- un claim qualitativo eccessivo, corretto nella review;
- rework medio su mix e collocazione dell'asset;
- calendario di campagna più immediatamente leggibile.

## Vantaggio provato e vantaggio non provato

È provato, in una singola esecuzione Codex, che la Vertical Slice produce un percorso più coerente
e richiede meno revisione sostanziale del GENERALIST.

Non è ancora provato che:

- il vantaggio si replichi su Claude nelle condizioni matched;
- il vantaggio sia stabile tra run;
- marketer reali lo percepiscano o lavorino meglio;
- il tempo reale risparmiato sia positivo;
- la Suite sia pronta per una release pubblica.

Non vengono presentate stime del modello come tempo risparmiato.

## Azioni richieste

1. Sbloccare manualmente il Mac.
2. Eseguire CURRENT e GENERALIST su Claude Opus 5 con impegno alto seguendo
   `CLAUDE-COMPLETION-RUNBOOK.md`.
3. Congelare e valutare in cieco le tre risposte Claude.
4. Solo dopo un confronto multipiattaforma non ambiguo, avviare un pilot con marketer seguendo
   `MARKETER-PILOT-RUNBOOK.md`.

Confidenza sulla classifica Codex: **85%**. Il campione è singolo, ma la distanza di copertura e
rework è netta. Confidenza sullo stato complessivo incompleto: **oltre 95%**, perché mancano due
prove Claude esplicitamente richieste.

## Verdetto

INCOMPLETE — ACTION REQUIRED
