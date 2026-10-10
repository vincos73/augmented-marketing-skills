# Guida alla voce del brand

Il risultato deve essere leggibile dal responsabile e abbastanza concreto da orientare un altro autore. Usa i moduli utili, senza compilare un brandbook per obbligo.

## Scegli il risultato proporzionato

**Guida esistente adeguata.** Il documento approvato resta il riferimento. Restituisci ciò che hai recepito, il suo perimetro e gli eventuali chiarimenti. Non crearne una seconda versione abbreviata che perda eccezioni o introduca regole nuove. Se viene richiesto un file operativo, può bastare una nota che punti al riferimento accessibile, conservi versione e perimetro, e contenga solo precisazioni approvate. Se è richiesta una formalizzazione autonoma, preserva tutte le decisioni sostanziali, segnala le parti non trasferibili e non dichiarare la conversione completa finché non lo è. Quando la richiesta è recepire una sezione approvata in una nota autonoma, restituisci la sezione completa come unità utilizzabile: includi regola, perimetro, condizioni o limiti ed esempio approvato pertinenti, invece di isolare il solo esempio. Questo vale per il contenuto che la nota deve incorporare; non trasforma una correzione locale in una guida completa né richiede di compilare tutti i moduli sotto.

**Guida nuova.** Riunisci le scelte emerse da materiali, dialogo e prove. Separa le regole approvate dalle proposte e dalle parti ancora da definire. Non presentare la descrizione dei testi osservati come approvazione implicita.

**Integrazione o revisione.** Mostra cosa cambia, perché e dove vale. Riusa la guida valida per il resto. Mantieni riconoscibili eventuali parti approvate accanto a proposte nuove: l'approvazione di una sezione non si estende al documento intero.

## Contenuto da rendere disponibile

Adatta titoli e profondità. Questi sono moduli, non un indice obbligatorio:

1. **A chi appartiene e dove vale.** Azienda, brand o persona, relazione con eventuale gruppo, pubblici, lingue e situazioni coperte. Indica le esclusioni che evitano un uso sbagliato.
2. **La voce in poche righe.** Relazione desiderata con il lettore e scelte espressive riconoscibili. Evita sequenze di aggettivi intercambiabili. Non riscrivere posizionamento o promessa di marca.
3. **Come si scrive.** Principi traducibili in azioni, con un esempio e le condizioni d'uso quando servono. Lessico, ritmo, punto di vista, pronomi, tecnicismi, struttura dell'argomentazione o umorismo solo dove orientano davvero il lavoro.
4. **Come cambia il tono.** Adattamenti per situazioni, pubblici e lingue pertinenti. Preserva il nucleo comune senza imporre identità tra brand diversi o equivalenze letterali tra lingue.
5. **Preferenze e limiti.** Distingui preferenze flessibili da vincoli esplicitamente approvati; chiarisci ambito ed eccezioni. Un limite stilistico non sostituisce un controllo dei fatti o un vincolo legale.
6. **Esempi.** Frasi reali autorizzate, loro eventuali riscritture e casi di prova chiaramente distinti. I controesempi illustrano uno scarto specifico, non una scrittura intenzionalmente ridicola. Non attribuire esempi inventati a clienti o persone reali. Se un esempio contiene impegni o condizioni, applica il controllo in [example-review.md](example-review.md).
7. **Decisioni, fonti e parti aperte.** Riferimenti leggibili, versione delle guide usate quando nota, osservazioni significative e scelte confermate nel dialogo. Segnala limiti del materiale o aspetti esclusi dall'approvazione, senza riportare tutta la conversazione.

Una tabella «principio / come applicarlo / esempio / limite» può essere utile per una guida nuova; evita una seconda rappresentazione equivalente in prosa. Per recepimenti semplici basta meno. Non imporre un numero di principi, canali, parole vietate o esempi.

## Provenienza delle scelte

Nel documento deve essere possibile distinguere:

- ciò che dice una fonte approvata, con riferimento;
- ciò che è osservato nei campioni, con esempio e limiti di rappresentatività;
- ciò che il responsabile ha deciso, con perimetro della conferma;
- ciò che l'agente propone o che resta aperto.

Puoi usare note brevi o una tabella compatta. Non esporre un codice di classificazione in ogni frase della chat. Non inventare nomi di approvatori, date di documenti, versioni o accessi. Se la data di un'approvazione è ignota, indica «confermato in questa conversazione» senza fabbricare uno storico.

## Intestazione per un file nuovo

Quando crei un file riutilizzabile, un'intestazione YAML minima aiuta a distinguerne perimetro e stato. I valori seguenti sono segnaposto del modello: sostituiscili con dati noti, ometti campi non pertinenti e non presentarli come un profilo reale.

```yaml
---
artifact: brand-voice-guide
version: "0.1"
status: bozza
entity: "Nome dell'entità"
voice_scope: "Perimetro della voce"
languages: [it]
kind: guida
---
```

`kind` può essere `guida`, `riferimento` o `integrazione`. Usa `status: approvato` soltanto per le decisioni approvate nel perimetro dichiarato; una bozza di revisione può citare la versione approvata che resta valida. Se il file contiene sezioni con stati diversi, lascialo in bozza e indica localmente le parti già approvate, oppure separa un'integrazione quando è più chiaro. Non marcare globalmente approvato un insieme con scelte sostanziali irrisolte.

L'intestazione non sostituisce la guida né dimostra che un altro sistema l'abbia caricata. Per la conservazione leggi [persistence-and-reuse.md](persistence-and-reuse.md).
