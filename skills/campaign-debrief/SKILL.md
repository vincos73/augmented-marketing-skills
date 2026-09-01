---
name: campaign-debrief
description: "Interpreta i risultati di una campagna, fase o test confrontando atteso, esecuzione reale e dati osservati, e raccomanda il prossimo passo con limiti e verifica. Usala dopo che esistono osservazioni utili, non per dashboard, QA del tracking, report automatici o modifiche operative."
metadata:
  version: "0.1.6"
---

# Leggere i risultati di una campagna

Aiuta un responsabile marketing a decidere che cosa continuare, correggere, estendere con cautela, fermare, attendere o rimettere in discussione. Confronta ciò che era atteso, ciò che è stato realmente eseguito e ciò che i dati permettono di sostenere.

La skill possiede la sintesi decisionale. Non è una dashboard, non genera un report periodico per principio, non ripara il tracking, non sostituisce Analytics e non attribuisce causalità senza una base adeguata.

## Scegliere la modalità di ingresso

Accetta due modalità senza chiedere all'utente di nominarle:

- **collegata:** sono disponibili Campaign Spec, eventuale review pre-lancio, note di esecuzione e risultati;
- **standalone:** l'utente fornisce una domanda, un periodo e risultati o materiali sufficienti a ricostruire una base minima.

Nel percorso collegato usa la spec come previsione datata, non come descrizione di ciò che è necessariamente accaduto. Ricostruisci comunque pubblico, offerta, landing, asset, canali, budget, timing, follow-up e tracking realmente usati. Non riaprire decisioni approvate che non sono in conflitto con l'esecuzione o con i risultati.

Quando esiste, leggi `campaign-review.md` nello stesso fascicolo della Campaign Spec. Usa azione esaminata, versione, esito, rilievi, prove e aspetti non verificati come fotografia pre-lancio. Gli stati `verificato`, `dichiarato`, `proposto`, `non verificato` e `in conflitto` mantengono il significato registrato dalla review. Un esito `pronta` o `pronta con condizioni` non dimostra che la campagna sia stata poi eseguita senza modifiche.

Se la review cambia materialmente la lettura, nella base visibile indica il suo esito e chiarisci che descriveva lo stato pre-lancio. Quando l'esecuzione successiva diverge, dichiara che quella configurazione non è stata riesaminata, salvo prova contraria.

Nel percorso standalone ricava prima tutto ciò che è leggibile dalla richiesta e dai materiali. Non bloccare il lavoro per l'assenza di una Campaign Spec e non ricostruire a posteriori target, previsioni o regole decisionali che non erano documentati. Distingui sempre ciò che era definito prima da ciò che viene interpretato adesso.

Per iniziare sono necessari almeno:

- decisione o domanda attuale;
- campagna, fase, test o periodo da valutare;
- risultati o osservazioni autorizzati.

Se questi tre elementi non sono identificabili, chiedi soltanto ciò che manca. Se sono presenti, produci subito una prima lettura utile.

## Dichiarare la base e il perimetro

Apri la prima risposta sostanziale con una nota compatta sui materiali realmente usati, sul perimetro e sui limiti materiali:

```text
Base utilizzata: Campaign Spec v1, registro di esecuzione e dati CRM al 28 ottobre. Il cambio di landing del 9 ottobre e cinque richieste senza sorgente limitano il confronto per canale.
```

Non elencare come fonti il blueprint, gli eval o le istruzioni della skill. Quando citi numeri, collega i più decisivi a definizione, fonte, finestra e denominatore. Non esporre frontmatter o registri interni nella risposta manageriale.

Per la metrica che governa la decisione, rendi leggibili nella stessa risposta almeno definizione operativa, fonte responsabile, cutoff o finestra e denominatore. Non affidare questi elementi soltanto alla nota generica sulla base utilizzata.

Ogni conclusione deve restare riferita a un perimetro osservabile, per esempio periodo, pubblico, canale, asset, fase o configurazione dell'offerta. Non dichiarare che una campagna ha funzionato o fallito in assoluto.

## Produrre valore prima delle domande

La prima risposta utile usa normalmente sei blocchi:

1. **Lettura in breve:** che cosa emerge nel perimetro osservato.
2. **Atteso ed eseguito:** previsione originaria e divergenze materiali dell'esecuzione.
3. **Risultati osservati:** output, comportamenti e risultati di business tenuti distinti.
4. **Che cosa si può sostenere:** conclusioni proporzionate ai dati.
5. **Limiti e spiegazioni alternative:** qualità della misura, comparabilità e fattori plausibili.
6. **Decisione consigliata:** azione, perimetro, responsabile, condizione e data o finestra del nuovo controllo.

Nei casi ordinari resta entro 500 parole, comprese eventuali tabelle e domande. Usa una tabella soltanto se rende più leggibile il confronto tra atteso, eseguito e osservato. Poni da zero a tre domande decisive dopo aver fornito la lettura disponibile.

Quando mancano dati importanti, non rispondere soltanto che servono più dati. Indica:

- che cosa è decidibile ora;
- che cosa deve restare sospeso;
- quale osservazione successiva riduce di più l'incertezza;
- quando e da chi deve essere controllata.

Quando la richiesta, le definizioni o i confronti sono ambigui, leggi [la guida a sufficienza e domande](references/decision-routing.md).

## Ricostruire l'esecuzione effettiva

Confronta tre stati senza fonderli:

- **atteso:** spec, target, baseline, previsione o regola decisa prima dell'esecuzione;
- **eseguito:** configurazione reale, comprese modifiche, interruzioni, capacità e azioni non avvenute;
- **osservato:** eventi e risultati disponibili, con fonte e finestra.

Tratta come divergenze materiali almeno cambi di pubblico, offerta, prezzo, messaggio guida, claim, landing, CTA, budget, mix di canali, calendario, follow-up, definizioni delle metriche o tracking. Se una divergenza impedisce un confronto pulito, restringi la conclusione invece di normalizzarla silenziosamente.

Una review pre-lancio descrive la prontezza osservata in quel momento. Non dimostra che condizioni, asset e sistemi siano rimasti invariati durante l'esecuzione.

## Verificare dati e confronti

Valuta la sufficienza rispetto alla decisione richiesta, non rispetto a una soglia universale. Controlla in modo proporzionato:

- definizione dell'evento o della metrica;
- fonte e responsabile del dato;
- finestra di maturazione;
- denominatore e copertura;
- volume e segmentazione;
- tracciamento mancante o cambiato;
- comparabilità di pubblico, periodo, offerta e canale;
- modifiche durante l'esecuzione;
- costo e reversibilità della decisione.

Non confrontare percentuali senza denominatori compatibili. Non usare una baseline stagionale, un altro segmento o un'offerta diversa come equivalente senza dichiararne il limite. Non sommare eventi provenienti da definizioni differenti.

Quando esistono casi pendenti, mostra il denominatore totale della configurazione e il numero non ancora classificato. Puoi aggiungere il rapporto sui soli casi valutati, ma non usarlo al posto di valori come `12 qualificate su 16 form, con 2 pendenti`.

Quando respingi o limiti un confronto, nomina nella risposta almeno le differenze materiali che lo rendono improprio, per esempio pubblico, offerta, periodo, definizione o copertura. Dire soltanto che la baseline non è equivalente non permette al responsabile di verificare il limite.

Se i materiali forniscono una baseline o uno storico pertinente alla decisione, dichiarane sempre l'uso o il mancato uso e le ragioni. Non ometterlo soltanto per accorciare la risposta.

Se la fonte non è accessibile o il dato è dichiarato dall'utente, descrivilo come fornito o dichiarato. La presenza di un file, una dashboard o un campo CRM non dimostra da sola qualità, completezza o attribuzione.

## Separare i livelli del risultato

Mantieni distinti:

- **output:** asset prodotti, invii, impression, spesa o attività;
- **comportamento intermedio:** attenzione qualificata, partecipazione, click, richiesta o prova;
- **risultato di business:** opportunità, ricavi, adozione, rinnovo o altro esito più ampio;
- **capacità operativa:** volume che Sales, Operations o altri team possono gestire.

Quando la capacità limita la decisione, collega il limite numerico o operativo dichiarato al carico e ai ritardi realmente osservati. Non limitarti a dire che la capacità è sotto pressione.

Un aumento di output non dimostra un outcome. Un click non equivale a una richiesta qualificata. Un risultato successivo alla campagna non è automaticamente causato dalla campagna.

## Gestire causalità e spiegazioni alternative

Usa formulazioni come `coerente con`, `segnale indicativo`, `associazione osservata` o `non distinguibile con i dati disponibili` quando descrivono correttamente l'evidenza.

Senza un disegno causale adeguato, non collegare campagna e outcome con verbi come `ha generato`, `ha prodotto`, `ha portato a` o equivalenti. Descrivi invece ciò che è stato osservato durante il periodo e separa l'associazione dall'attribuzione.

Considera soltanto spiegazioni alternative plausibili e capaci di cambiare la decisione, per esempio:

- variazione del pubblico, dell'offerta o della landing;
- stagionalità o evento esterno;
- attività commerciale concomitante;
- modifica della definizione o della copertura del tracking;
- campione ridotto o selezionato;
- capacità insufficiente nel follow-up;
- differenze di investimento o distribuzione.

Non creare un elenco generico di possibili confondenti. Per ogni alternativa materiale indica quale osservazione potrebbe distinguerla, quando possibile.

## Formulare una decisione proporzionata

La raccomandazione può essere:

- continuare nel perimetro osservato;
- correggere un elemento specifico e riesaminare;
- estendere con cautela un test reversibile;
- fermare un'attività o un perimetro;
- attendere la maturazione di una finestra;
- fare un confronto più informativo;
- riaprire una scelta di campagna.

Rendi espliciti sia ciò che non va fatto ora sia ciò che conviene fare nel frattempo. Se raccomandi di non estendere o non scalare, indica se il perimetro corrente va continuato, corretto, limitato o sospeso e a quali condizioni può produrre un confronto informativo.

Assegna ogni azione a un solo responsabile osservato oppure `da confermare`; non affidare un elenco di attività a un gruppo indistinto. Prima di proporre un riesame di paid, scala o ampliamento, rendi osservabili almeno tracking stabile, backlog o follow-up sotto controllo, capacità disponibile e configurazione approvata quando sono materiali per la decisione.

Se una prova decisiva è ancora immatura o manca un periodo comparabile, distingui un controllo intermedio di prontezza dal riesame della decisione. Il controllo intermedio può chiudere casi pendenti, verificare tracking, capacità o configurazione, ma non va presentato come momento in cui rivalutare paid, scala o ampliamento. Fissa quel riesame soltanto dopo la finestra materiale e, quando serve a distinguere le spiegazioni, dopo che una nuova coorte con definizione, configurazione e tracking stabili è stata realmente eseguita, chiusa e osservata. La sola prontezza della nuova configurazione non basta.

Conserva esattamente i ruoli osservati nei materiali. Non trasformare `Sales Director` in `Sales Lead`, non inventare un team Analytics e non sostituire un owner con un ruolo più generico; se il responsabile non è indicato, usa `da confermare`. Assegna anche il nuovo controllo e l'eventuale decisione di test a un singolo responsabile osservato o da confermare.

Collega sempre la decisione a:

- perimetro a cui si applica;
- evidenza che la sostiene;
- limite o condizione;
- azione concreta;
- responsabile autorizzato;
- nuova osservazione e momento del controllo.

Per scelte costose, irreversibili o difficili da annullare richiedi evidenza più solida. Un piccolo test reversibile può procedere con un segnale indicativo, purché ipotesi, limite di esposizione e criterio di stop siano espliciti.

Non autorizzare budget, aumento di spesa, invio, pubblicazione, modifica di audience, CRM, landing o automazioni. Se l'utente chiede di applicare la decisione, separa la lettura dall'azione e verifica autorità e capability prima di qualsiasi modifica esterna.

## Rispettare il confine con le altre decisioni

Se i risultati mettono in discussione una scelta fondamentale di pubblico, offerta, messaggio guida, percorso o regola decisionale, nomina esplicitamente `design-campaign` nella raccomandazione visibile e proponi il ritorno a quel workflow. Non limitarti a dire che la scelta va riaperta e non riscrivere silenziosamente la Campaign Spec.

Puoi proporre una modifica a direzione o Marketing Foundations soltanto come ipotesi da sottoporre al relativo workflow. Un risultato locale non diventa una regola stabile senza evidenza trasferibile e approvazione separata.

Se il problema è definizione, implementazione o qualità del tracking, descrivi il limite e indirizza la verifica al responsabile Analytics o tecnico. Non dichiarare di aver corretto la misura.

## Presentare e salvare il learning

Per default rispondi in chat. Un file è utile solo quando la lettura deve essere condivisa, approvata o conservata oltre la conversazione.

Quando serve un record persistente, leggi [il template del Campaign Learning](references/campaign-learning-template.md). Prima del documento completo presenta una sintesi approvabile con perimetro, risultati, limiti, decisione e prossima verifica.

Mantieni distinti:

1. approvazione della lettura;
2. autorizzazione al salvataggio;
3. autorizzazione a modificare campagna, budget, piattaforme o artefatti approvati.

Dopo autorizzazione al salvataggio crea o aggiorna un solo file:

```text
.agents/marketing/decisions/<decision-slug>/campaigns/<campaign-slug>/campaign-learning.md
```

Non creare documenti separati per metrica, canale o riunione. Non modificare Campaign Spec, Marketing Foundations o playbook come effetto collaterale. Se il contenuto è approvato soltanto in chat, riporta esattamente:

> contenuto approvato in chat; artefatto non creato

Se l'utente dichiara che il lavoro è un test, una simulazione o un eval, non scrivere nei percorsi canonici, anche se il dialogo contiene approvazioni simulate.

## Concludere

Prima di inviare la risposta, esegui un controllo causale privato. Cerca ogni frase in cui campagna, percorso, canale, asset o landing sono soggetto di verbi come `generare`, `produrre`, `portare`, `determinare`, `causare` o equivalenti riferiti a domanda, qualifica, acquisti, pipeline o ricavi. Se non esiste una base causale adeguata, riscrivi la frase come osservazione nel periodo o associazione e mantieni visibili le spiegazioni alternative.

Esegui anche un preflight decisionale privato. Prima di inviare, verifica che la risposta contenga:

1. metrica decisiva con definizione, fonte, cutoff e denominatore;
2. baseline o storico fornito, con uso e limiti;
3. scelta esplicita sul perimetro corrente: continuare, correggere, limitare o sospendere;
4. capacità materiale collegata a limite e carico osservati;
5. un responsabile osservato o `da confermare` per ogni azione e per il prossimo controllo.
6. separazione visibile tra output, comportamento e risultato di business quando più livelli sono presenti;
7. nome letterale `design-campaign` quando pubblico, offerta, messaggio guida, landing o percorso richiedono riprogettazione.

Se la scelta riguarda paid, scala o ampliamento, verifica inoltre che la data del riesame non preceda la maturazione delle prove dichiarate necessarie e che un eventuale controllo intermedio non venga confuso con l'autorizzazione a decidere. Quando una nuova coorte è necessaria, dichiarala esplicitamente come prerequisito del riesame e lega il prossimo controllo alla sua chiusura; non limitarti a proporla come attività parallela.

Se i materiali dichiarano stabile una definizione ma non ne mostrano i criteri operativi, non completarla per inferenza: indica esplicitamente che la definizione completa non è disponibile nei materiali consultati.

Comprimi output secondari prima di omettere uno di questi elementi.

Riporta in modo compatto:

- decisione raccomandata e relativo perimetro;
- che cosa resta incerto;
- azione, responsabile e prossimo controllo;
- file creato o mancato salvataggio;
- eventuali proposte di riapertura o aggiornamento, non ancora applicate.

Non avviare automaticamente altre skill, modifiche operative o azioni esterne.
