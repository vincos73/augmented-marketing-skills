# Sufficienza dei dati e routing delle domande

Leggi questa guida quando i risultati sono incompleti, le definizioni sono ambigue, l'esecuzione diverge dal piano o più lacune competono per l'attenzione del responsabile.

## Partire dalla decisione

Formula privatamente la decisione in questa forma:

```text
Dobbiamo decidere se [azione] per [perimetro] entro [momento], con un costo o rischio [basso/medio/alto].
```

Se l'utente chiede genericamente «com'è andata?», ricava una decisione provvisoria dai materiali e dichiarala. Chiedi conferma soltanto se decisioni plausibili diverse richiedono evidenze diverse.

## Evidenze che rendono verificabile la decisione

Per ogni elemento decisivo conserva:

- fonte e data;
- definizione;
- finestra e denominatore;
- stato: osservato, dichiarato, inferito, in conflitto o sconosciuto;
- conseguenza sulla decisione.

## Valutare la sufficienza in proporzione al rischio

Usa tre stati descrittivi, senza trasformarli in punteggi:

- **sufficiente per decidere:** le lacune residue non cambiano materialmente la scelta nel perimetro indicato;
- **indicativo per un passo reversibile:** esiste un segnale utile, ma la conclusione deve essere limitata e accompagnata da un nuovo controllo;
- **insufficiente per la scelta richiesta:** una lacuna può invertire la decisione o il costo dell'errore è sproporzionato.

Anche nell'ultimo caso identifica una decisione più piccola che i dati sostengono, se esiste.

### Casi tipici

| Situazione | Cosa si può sostenere | Comportamento prudente |
|---|---|---|
| Finestra immatura per ricavi o pipeline | Output e comportamenti già maturi | Attendere la finestra e fissare il controllo |
| Tracking cambiato a metà periodo | Risultati entro ciascuna definizione | Non aggregare; ricostruire periodi comparabili |
| Pubblico o landing modificati | Esito della configurazione realmente usata | Non attribuire il risultato al piano originario |
| Campione piccolo ma test reversibile | Segnale indicativo | Limitare esposizione e definire criterio di stop |
| Baseline non comparabile | Andamento assoluto nel perimetro corrente | Cercare confronto pertinente o dichiararne l'assenza |
| Capacità Sales saturata | Domanda osservata e collo di bottiglia | Non aumentare distribuzione prima della decisione operativa |

## Scegliere i chiarimenti

Entro il limite di tre domande, dai priorità alle lacune che cambiano la decisione:

1. decisione, perimetro e costo dell'errore;
2. divergenza di esecuzione capace di invalidare il confronto;
3. definizione, fonte, finestra o denominatore di una metrica decisiva;
4. fattore alternativo che può invertire la raccomandazione;
5. responsabile e momento del prossimo controllo.

Non chiedere un inventario di KPI, tutte le esportazioni o ogni dettaglio operativo. Non ripetere ciò che è già leggibile.

## Formulare le domande

Ogni domanda deve richiedere una sola informazione o decisione principale e avere un solo referente plausibile. Esempi:

- «La decisione da prendere ora è se estendere il test a tutto il segmento oppure se correggere prima la landing?»
- «Le 18 richieste qualificate usano la stessa definizione per tutte le sei settimane?»
- «Il cambio di landing del 9 ottobre ha interessato tutto il traffico o solo LinkedIn?»
- «Chi può autorizzare il limite del prossimo test?»

Se il referente non conosce la risposta, registra il limite. Non indurlo a inventare una definizione retroattiva.

## Scegliere la prossima osservazione

Preferisci l'osservazione che distingue due spiegazioni capaci di produrre decisioni diverse. Specifica:

- cosa osservare;
- per quale perimetro;
- con quale definizione e fonte;
- fino a quando;
- quale decisione cambierà.

Una richiesta generica di «più dati» non è una prossima verifica utilizzabile.

## Paid, scala e ampliamenti

La raccomandazione deve separare il destino del perimetro corrente dalla possibilità di aumentare esposizione o spesa. Prima di sostenere un'estensione considera le condizioni materiali del caso: tracking stabile, consenso e uso dei dati compatibili, follow-up e backlog sotto controllo, capacità disponibile e configurazione approvata. Collega la capacità a limite e carico osservati, senza inventare responsabili o soglie.

La convenienza economica richiede la base pertinente, per esempio costi completi, qualità e maturazione degli esiti, margini o una soglia di test concordata con Finance. Un costo per lead favorevole, un budget disponibile o una qualifica commerciale non bastano da soli a raccomandare scala o ROI. Se la prova manca, limita la conclusione e identifica chi può definirla; non trasformare questo controllo in una richiesta universale di conto economico per ogni debrief.

Quando una prova decisiva è immatura, distingui:

- **controllo intermedio di prontezza:** chiusura dei pendenti, verifica di tracking, backlog, capacità o configurazione;
- **riesame della decisione:** confronto su osservazioni abbastanza mature per paid, scala o ampliamento.

Non fissare il riesame prima della maturazione delle prove dichiarate necessarie. Se serve una nuova coorte comparabile per distinguere le spiegazioni, il riesame dipende dal fatto che sia stata realmente eseguita con definizione, configurazione e tracking stabili, poi chiusa e osservata. La sola prontezza della nuova configurazione non basta, né basta elencare la coorte come attività parallela.

Indica ciò che conviene fare nel frattempo, il responsabile osservato o `da confermare`, l'osservazione attesa e quando controllarla. La decisione di test e il nuovo controllo devono avere ciascuno un responsabile identificabile. L'approvazione dell'analisi o di un budget non equivale all'autorizzazione al lancio.
