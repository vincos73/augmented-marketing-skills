# Verifica del routing esteso di Augmented Marketing Assistant v0.2.0

## Perimetro

Verifica statica della definizione canonica, dell'adattatore OpenAI e degli scenari sintetici dopo l'aggiunta di Campaign Core e Content Director.

Questa verifica non è un test runtime e non dimostra che un ambiente effettui l'handoff tra skill.

## Casi verificati

| Richiesta | Routing atteso | Esito statico |
| --- | --- | --- |
| Progettare una campagna da un'esigenza, un brief o un marketing mix | `design-campaign` | PASS |
| Verificare campagna e asset prima del lancio | `campaign-review` | PASS |
| Interpretare risultati e decidere il passo successivo | `campaign-debrief` | PASS |
| Scegliere la strada editoriale per fonti o un'idea | `content-director` | PASS |
| Produrre un asset con obiettivo e formato già definiti | Nessun passaggio strategico obbligatorio | PASS |

## Controlli comuni

- La definizione canonica e l'adattatore OpenAI contengono le stesse nove destinazioni specialistiche.
- L'Assistant spiega il risultato prima del nome tecnico.
- La richiesta ambigua resta una sola domanda in linguaggio comune e non un catalogo di skill.
- La presenza della sorgente non viene trattata come prova di installazione, caricamento o handoff.
- Metodo, domande, artefatti e approvazioni restano posseduti dalle skill specialistiche.

## Verdetto

PASS statico, zero discrepanze tra definizione canonica, adattatore e scenari v0.2.

Restano da verificare in una sessione pulita: discovery della v0.2.0, selezione delle quattro nuove destinazioni e handoff osservabile.
