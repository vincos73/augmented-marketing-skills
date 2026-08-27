# Audit statico del contratto di portabilità v1

**Data:** 2026-08-27
**Tipo:** audit statico delle sorgenti
**Perimetro:** cinque skill approvate nel repository
**Limite:** non è un forward test su ambienti differenti e non dimostra il caricamento runtime.

## Criteri

1. la skill non richiede connector per il risultato essenziale;
2. distingue salvataggio, installazione e caricamento quando pertinenti;
3. gestisce esplicitamente un workspace non scrivibile;
4. mantiene l'artefatto completo quando non può salvarlo;
5. non presume comandi, hook, subagenti o interfacce proprietarie;
6. conserva approvazioni e confini di autorità senza strumenti esterni.

## Esito

| Skill | Versione sorgente | Esito statico | Evidenza e gap |
|---|---:|---|---|
| `setup-business-context` | 0.6.2 | parziale forte | Prevede il fallback non scrivibile e distingue salvataggio, installazione e runtime. Il Gate 2 nomina Codex e Claude Code come host principali e deve essere generalizzato a instruction file equivalenti in una futura patch. |
| `setup-marketing-system` | 0.2.1 | conforme | Prevede artefatto completo senza scrittura, instruction file equivalenti, distinzione tra configurazione e runtime e nessuna dipendenza da connector. |
| `define-marketing-challenge` | 0.1.1 | parziale | Gestisce conferma senza autorizzazione al salvataggio, ma non distingue esplicitamente il rifiuto dell'utente dall'indisponibilità tecnica della scrittura. |
| `choose-marketing-direction` | 0.2.0 | parziale | Non richiede strumenti esterni e conserva i gate, ma manca un fallback esplicito per workspace non scrivibile. |
| `define-marketing-mix` | 0.1.1 | parziale | Non richiede strumenti esterni e conserva i gate, ma manca un fallback esplicito per workspace non scrivibile. |

## Decisione di manutenzione

Non modificare silenziosamente le skill già pubblicate durante questo audit. I quattro gap devono diventare patch comportamentali versionate, con aggiornamento delle relative reference, eval, installazioni e release solo dopo approvazione del contratto di portabilità.

## Forward test necessario

Per ogni skill aggiornata verificare almeno:

- un ambiente con scrittura nel workspace;
- un ambiente con lettura ma senza scrittura;
- una fonte necessaria non accessibile;
- una capability opzionale assente;
- una nuova sessione in cui la skill installata risulti effettivamente caricata.
