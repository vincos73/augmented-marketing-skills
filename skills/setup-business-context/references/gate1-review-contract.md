# Contratto di revisione al gate 1

Leggi questo riferimento quando la bozza completa è pronta per la revisione dell'identità. Il gate deve far capire al manager che cosa verrà salvato, che cosa resta aperto e quali scelte sono disponibili.

## Contenuto obbligatorio

Prima dell'approvazione mostra:

1. **Cosa sapranno gli agenti** — sintesi breve dei fatti e dei limiti più importanti;
2. **Aspetti ancora aperti** — solo lacune materiali che potrebbero essere utili in seguito;
3. **Conflitti o rischi** — affermazioni non supportate, contraddizioni e limiti d'uso;
4. **Artefatto proposto** — entità, percorso, versione, stato bozza e genitore quando applicabile;
5. la bozza completa, adattata ai contenuti realmente disponibili.

Non trasformare il gate in un inventario di campi vuoti. Il template dell'identità è modulare: ometti sezioni, righe e stati che non cambiano il comportamento futuro degli agenti. Mantieni sempre gli aspetti essenziali, i vincoli critici e le lacune materiali.

## Linguaggio rivolto al manager

- Usa etichette quotidiane e frasi comprensibili senza conoscere il modello dati.
- Apri la conversazione con una frase breve e rassicurante che spieghi cosa succederà: prima si raccolgono e si leggono le fonti, poi si rivede insieme una sintesi e infine si decide se approvare e installare l'identità.
- Accompagna ogni passaggio con una frase di orientamento e chiudi con una scelta concreta, invece di lasciare un resoconto impersonale dello stato del sistema.
- Preferisci `Per chi l'offerta è particolarmente adatta` e `Per chi potrebbe non essere adatta` a formule come `adeguatezza migliore` o `deliberatamente non servito`.
- Evita anche espressioni astratte come `adeguatezza universale`, `confini di non adeguatezza` o `idoneità del cliente`: descrivi direttamente le situazioni in cui il servizio funziona bene o potrebbe non essere adatto.
- Spiega ogni stato prima in linguaggio naturale. Nel documento puoi poi conservarne il valore canonico, per esempio `non stabilito dalle fonti fornite`.
- Non mostrare entità HTML (`&#x20;`, `&#x65;`), JSON, YAML, nomi di campi interni o altri artefatti di serializzazione.
- Se un carattere codificato compare nella fonte o in uno stato intermedio, decodificalo per la visualizzazione senza alterare il significato.

## Scelta sulle lacune non bloccanti

Quando restano lacune materiali ma non indispensabili, presentane al massimo tre e spiega in una frase perché potrebbero essere utili. Poi offri entrambe le possibilità:

- approvare ora e mantenerle esplicitamente aperte nel documento;
- approfondire uno o più punti prima dell'approvazione.

Una chiusura possibile è:

> Bene, la bozza è pronta. Puoi approvarla così, mantenendo aperti questi aspetti, oppure indicarmi quale vuoi approfondire prima dell'approvazione.

Non far sembrare obbligatorio l'approfondimento. Se il manager lo sceglie, poni al massimo tre domande nel turno successivo. Per missione, posizionamento, promessa o differenziazione, raccogli soltanto decisioni già esistenti o classifica correttamente l'assenza; la loro creazione appartiene a un altro lavoro.

Se non restano lacune materiali non bloccanti, chiedi direttamente l'approvazione esplicita.

## Verifica prima dell'invio

- La chat offre davvero due percorsi quando serve, non soltanto `approva se corretto`.
- Le lacune facoltative non sono disperse come campi vuoti nella bozza.
- Nessuna etichetta suona come una traduzione letterale di un framework.
- Il testo non ricade su sostantivi astratti come `adeguatezza`, `non adeguatezza` o `idoneità` per descrivere i clienti.
- Nessun carattere codificato o dettaglio di implementazione è visibile.
- L'approvazione dell'identità resta separata dall'installazione per gli agenti.
- Dopo il salvataggio, la chat distingue chiaramente tra `identità salvata` e `identità installata per l'agente`, e propone esplicitamente di procedere ora o dopo.
