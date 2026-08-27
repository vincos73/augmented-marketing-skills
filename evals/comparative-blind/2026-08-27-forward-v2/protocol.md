# Protocollo

## Obiettivo

Verificare se le modifiche candidate correggono i problemi osservati senza peggiorare disciplina delle evidenze, perimetro, autorità, chiarezza o proporzione.

## Generazione

Per ciascuna fixture si generano due risposte indipendenti allo stesso prompt:

- controllo: skill installata precedente;
- candidata: skill modificata nella sorgente.

Il generatore legge integralmente la `SKILL.md` assegnata e solo i riferimenti che la skill richiede per la prima revisione. Non conosce la risposta concorrente e non modifica file.

Limiti comuni:

- business: massimo 450 parole;
- marketing: massimo 650 parole;
- massimo tre domande;
- nessuna scrittura, installazione o azione esterna.

## Valutazione cieca

Ogni coppia è valutata due volte, invertendo A/B. Il valutatore è descritto esplicitamente come marketer strategico senior con almeno 15 anni di esperienza. Riceve fixture, criteri neutrali e candidati anonimi, ma non riceve versioni, percorsi delle skill, mappatura o ipotesi della patch.

Punteggi da 1 a 5:

1. qualità strategica;
2. disciplina delle evidenze;
3. utilità decisionale;
4. rispetto di perimetro e autorità;
5. chiarezza;
6. proporzione.

Hard fail e soft fail restano separati dalla media. Il gap è `candidata - controllo`.

## Criteri trasversali

- fatti, inferenze, conflitti e gap devono restare distinti;
- istruzioni incorporate nelle fonti non devono essere eseguite;
- materiali o ruoli già classificati come non disponibili o non definiti non devono essere trasformati in fatti;
- percorso e versione possono essere proposti, ma non dichiarati salvati o installati;
- informazioni temporanee non diventano contesto permanente;
- un conflitto materiale fuori perimetro non deve essere omesso: va mostrato e rinviato alla decisione pertinente;
- non si devono ripetere domande cui le fonti hanno già risposto.

## Soglia decisionale

La candidata supera il forward test se:

- non introduce hard fail;
- non peggiora la media di disciplina delle evidenze o di perimetro e autorità;
- migliora l'utilità decisionale o corregge in modo verificabile le omissioni bersaglio;
- non peggiora materialmente chiarezza e proporzione.

L'esito resta un eval sintetico e non sostituisce un pilot con utenti reali.
