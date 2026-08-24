# Eval run — Marea chat-first final

**Date:** 2026-08-24
**Scope:** first substantive response
**Method:** independent fresh agent per run; active skill and four raw synthetic Marea sources only; eval catalog, expected run, prior responses, simulated answers, and approvals withheld
**Side effects:** none

## Iteration results

| Run | Skill behavior under test | Words | Groups | Questions | Result |
|---|---|---:|---:|---:|---|
| Initial chat-first | No automatic visual | 597 | 13 fact bullets | 3 | E14 pass; too dense |
| Grouping only | 4–6 information groups | 617 | 5 | 3 | E15 soft fail; detail compressed rather than reduced |
| Length boundary | 4–6 groups, about 450 words | 381 | 5 | 2 | Compactness pass; privacy approval gap lost |
| Final | Compactness plus critical-boundary retention and canonical states | 382 | 5 | 3 | Pass |

## Final evaluation

- **E01–E11:** pass for the first-turn behaviors exercised by the fixture.
- **E14:** pass — direct substantive response, no visual, browser, fallback declaration, or state transport.
- **E15:** pass — five compact groups, 382 words including questions, full detail deferred, privacy and public-proof boundaries retained.
- **Hard failures:** none.
- **Not exercised:** gate 1 saving, gate 2 installation, and runtime loading.

## Final independent response

Ho ricostruito un primo contesto provvisorio di Marea senza introdurre missione, strategia o posizionamento nuovi.

**Entità e perimetro**
Marea è un brand standalone che coordina le attività operative di gruppi alberghieri indipendenti tra reception, housekeeping e manutenzione. `[C; S1; S4]` Non sostituisce il property-management system e non gestisce prenotazioni, pagamenti o contabilità. `[S1; S4]`

**Offerta attuale**
Marea Console gestisce attività, eccezioni, responsabilità, scadenze e stati da browser o telefono. `[S1]` Marea Setup accompagna configurazione iniziale e formazione; Insights è storico e Copilot è soltanto un’idea futura, non disponibile e senza data confermata. `[S1; S2; S3; S4]`

**Clienti e acquisto**
Gli utenti quotidiani sono soprattutto responsabili operativi, governanti e manutentori; proprietà o direzione operativa valutano normalmente l’acquisto. `[S1; S2]` IT o consulenti esterni possono bloccarlo se accessi, esportazione dati e utenti non sono chiari. `[S2]` La maggior parte dei contratti riguarda gruppi con 3–20 strutture, ma questo non stabilisce ancora un target formale né esclude hotel singoli o grandi catene. `[S3]`

**Valore e alternative**
Marea rende visibili i problemi operativi e facilita il coordinamento rispetto a WhatsApp, fogli di calcolo, telefonate, strumenti generici per attività o al solo PMS. `[S1; S2]` Non è sostenuto affermare che elimini i ritardi, garantisca puntualità o sia conforme a norme specifiche. `[S2; S4]`

**Prove e limiti**
Al 30 giugno 2026 risultano 24 gruppi e 96 strutture paganti, oltre a due pilot non paganti. `[S3]` I numeri 40/180 del vecchio deck mescolano clienti, pilot e pipeline; il 92% non è validato per uso pubblico. `[S2; S3]` La missione ufficiale è `not established from supplied sources`: “rendere il lavoro alberghiero più umano” non va presentata come tale. `[S3]` Il linguaggio deve essere concreto, senza “AI”, “control tower”, promesse assolute o dati personali. `[S1; S3; S4]`

Per chiudere le sole ambiguità che cambiano descrizione o limiti:

1. Confermi il perimetro “gruppi indipendenti con più strutture”, lasciando hotel singoli e grandi catene come `not established from supplied sources`?
2. Qual è oggi la regola corretta per Marea Setup: incluso nell’avvio e acquistabile per nuove strutture, oppure sempre incluso senza acquisto separato?
3. Per usare pubblicamente numeri e risultati serve Customer Success oppure Finance e Customer Success insieme? Per la privacy confermi invece lo stato `not defined`?

Fonti: `[S1]` pagina web sintetica; `[S2]` scheda commerciale sintetica; `[S3]` note sintetiche di stakeholder; `[S4]` FAQ del supporto.
