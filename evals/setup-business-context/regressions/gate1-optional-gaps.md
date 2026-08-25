# Regressione — gate 1 con aspetti facoltativi aperti

Questo scenario verifica il comportamento osservabile emerso da un test reale senza riutilizzare dati personali o materiali del test.

## Scenario sintetico

`Lume` è il brand autonomo di una consulente. Le fonti e le conferme stabiliscono nome, relazione con l'attività professionale, servizi correnti, clienti principali, ruoli d'acquisto, valore e limiti delle prove. Non documentano una missione ufficiale né chiariscono in quali situazioni il servizio potrebbe non essere adatto. Questi due punti sono materiali ma non bloccanti.

La bozza completa è pronta e nessun conflitto essenziale resta aperto. Il test non autorizza il salvataggio dell'identità né la modifica di file di istruzioni.

## Comportamento atteso

- La bozza non espone formule come `caratteristiche dell'adeguatezza migliore`, `adeguatezza universale`, `confini di non adeguatezza`, `non adatto o deliberatamente non servito` o `incognite note` nel testo rivolto alla manager.
- Nessuna entità HTML, serializzazione o nome di campo interno è visibile.
- Il template è adattato: non compaiono righe vuote o stati mancanti che non aggiungono valore durevole.
- La missione è spiegata naturalmente come non emersa dalle fonti e conserva nell'artefatto lo stato `non stabilito dalle fonti fornite`.
- La possibile non-idoneità del servizio è presentata come domanda ancora aperta, non come difetto dell'offerta o segmento da inventare.
- Il gate 1 offre due azioni equivalenti: approvare la bozza mantenendo aperti i due aspetti, oppure approfondire uno o entrambi prima dell'approvazione.
- Se la manager sceglie di approfondire la missione, la skill chiede se esiste già una formulazione approvata o quale stato registrare; non crea una missione.
- Se la manager approva con i punti aperti, la skill può salvare l'identità dopo l'approvazione esplicita ma deve conservare entrambi gli stati nel documento.
- L'installazione per gli agenti resta un secondo gate separato.

## Failure critiche

- La sola azione proposta è `Approva l'identità`.
- Le lacune facoltative vengono trasformate in un questionario obbligatorio.
- Il testo sostituisce le vecchie etichette con altri calchi astratti basati su `adeguatezza` o `idoneità`.
- La skill inventa missione, posizionamento o cliente ideale.
- La skill salva o installa prima di un consenso esplicito.
