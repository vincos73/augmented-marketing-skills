# Standard per progettare le skill

Questo documento definisce il contratto di authoring comune per le nuove skill dell'Augmented Marketing Suite e per le revisioni sostanziali di quelle esistenti.

Lo scopo non è uniformare ogni conversazione, ma ridurre carico cognitivo, ripetizioni e tempo di revisione senza perdere decisioni, provenienza, rischi o limiti di autorità. Una skill è riuscita quando aiuta il responsabile ad avanzare e approvare, non quando produce il documento più lungo possibile.

## Come si applica

- Il blueprint di una nuova skill deve dichiarare come applica questo standard e motivare le eventuali eccezioni.
- Le regole necessarie durante l'uso devono essere incorporate in `SKILL.md` o nei riferimenti inclusi nel pacchetto. Il file comune non è una dipendenza runtime implicita.
- Le regole specifiche del dominio restano nella singola skill; non vanno trasformate in principi generali senza evidenze trasversali.
- Authoring, installazione locale e distribuzione pubblica sono tre gate distinti.

## Linguaggio di dominio, non di implementazione

Prima di progettare l'interfaccia conversazionale, identifica il ruolo che userà la skill e il lessico che adopera nel lavoro. La chat e i documenti destinati al responsabile devono parlare la lingua del dominio; i termini di authoring, orchestrazione e implementazione restano nelle istruzioni interne.

- Preferire termini già riconoscibili nel mestiere, purché siano pertinenti e non introdotti per esibire il framework.
- Tradurre etichette interne come `gate`, `routing`, `artefatto canonico`, `schema`, `handoff`, `owner` e `runtime` in azioni o concetti comprensibili al destinatario.
- Non vietare un termine tecnico quando è davvero standard nel dominio: per esempio `brief`, `claim`, `trade-off`, `funnel`, `awareness`, `consideration`, `conversion`, `nurturing`, `Product`, `Price`, `Place` e `Promotion` possono essere naturali per un marketer.
- Non imporre una tassonomia standard se non descrive il caso reale. Le fasi del funnel entrano soltanto quando corrispondono al percorso effettivo del pubblico; possono essere adattate, accorpate o omesse.
- Se un termine interno deve comparire per ragioni operative, spiegarlo prima in linguaggio naturale e mostrarlo solo dove serve.

Ogni skill deve indicare quali etichette sono soltanto interne e quali titoli o termini usare nelle risposte rivolte al responsabile. Gli eval devono trattare il gergo di implementazione esposto senza necessità come rework linguistico, anche quando il contenuto è formalmente corretto.

## 1. Prima risposta utile

La prima risposta sostanziale deve dare valore prima di chiedere altro:

1. mostrare una comprensione o una proposta provvisoria utile;
2. rendere visibili soltanto i vincoli che cambiano la decisione;
3. porre al massimo tre domande ad alta conseguenza;
4. usare una sola rappresentazione dominante, evitando di ripetere la stessa struttura in prosa e tabella;
5. rinviare esempi, procedure e campi secondari finché non servono.

Ogni skill deve definire un budget proporzionato. Per una decisione o un piano semplice, il riferimento è 250-350 parole e il tetto ordinario è 450-500. Una riconciliazione di fonti complessa può arrivare a 650 parole se deve conservare conflitti, provenienza o vincoli critici. I limiti sono tetti, non obiettivi.

## 2. Progressione per differenza

Dopo ogni risposta dell'utente:

- confermare solo le decisioni appena chiuse;
- aggiornare solo le parti cambiate;
- non ripresentare il documento o l'architettura completi a ogni turno;
- non richiedere informazioni già presenti o già classificate;
- passare al gate appena il risultato è approvabile.

Ogni turno dovrebbe avere una decisione dominante. Domande con responsabili, rischi o percorsi diversi non vanno accorpate artificialmente.

## 3. Fonti e autorità

La skill deve distinguere almeno:

- fonti di business e decisioni approvate;
- affermazioni dell'utente autorizzato;
- inferenze e ipotesi;
- gap e conflitti;
- materiali metodologici della skill.

Blueprint, template, eval, run e documenti del framework spiegano il metodo: non sono prove del business e non devono comparire tra le fonti usate per prendere la decisione, salvo audit espliciti del framework.

Privacy, conformità, uso pubblico delle prove, sicurezza e limiti di autorizzazione non si eliminano per comprimere il testo.

## 4. Gate di revisione

Il gate deve offrire al responsabile una rappresentazione compatta ma completa di ciò che sta approvando:

- decisione o proposta principale;
- elementi ancora aperti che possono cambiarla;
- rischi, dipendenze e responsabilità rilevanti;
- stato e destinazione dell'eventuale artefatto.

Non deve essere un inventario di campi né duplicare una versione sintetica e una estesa della stessa proposta. La bozza tecnica completa si mostra quando serve alla revisione, quando viene richiesta o quando una scrittura autorizzata non è possibile.

L'approvazione del contenuto e l'autorizzazione al salvataggio o all'esecuzione restano decisioni distinte. Possono essere richieste nello stesso turno, purché la distinzione sia inequivocabile.

## 5. Template modulari

Un template è una libreria di campi, non l'indice obbligatorio dell'output.

- Definire un nucleo compatto sempre necessario.
- Rendere opzionali sezioni, righe e tabelle che non aggiungono decisioni, responsabili, rischi o limiti.
- Assegnare ogni informazione a una destinazione principale, senza ripeterla in più sezioni.
- Evitare di esporre in chat JSON, YAML, nomi di campi interni o altri dettagli di implementazione.
- Usare etichette comprensibili a un responsabile che non conosce il framework.

## 6. Modalità test e scritture

Una prova dichiarata come test, simulazione o eval non autorizza scritture nei percorsi canonici, anche se nel copione compaiono risposte come “approvo” o “salva”. Un eventuale artefatto di prova deve essere richiesto esplicitamente e restare isolato in una destinazione non canonica.

Fuori dalla modalità test:

- non scrivere prima dell'autorizzazione esplicita;
- se la scrittura autorizzata fallisce, spiegare il limite e fornire una sola versione portabile dell'artefatto;
- non interpretare l'approvazione del contenuto come permesso per pubblicare, acquistare, inviare o modificare sistemi esterni.

## 7. Verifica comportamentale

Ogni nuova skill deve avere almeno:

1. una fixture coerente, composta da materiali realistici;
2. un catalogo di eval con hard fail e osservazioni qualitative;
3. una prova standalone quando la skill può essere usata senza il percorso precedente;
4. una regressione collegata agli artefatti a monte quando esistono;
5. un test del dialogo completo, non soltanto del documento finale.

La verifica deve osservare almeno: parole per turno, numero e qualità delle domande, decisioni ripetute, provenienza, comportamento al gate, scritture non autorizzate e minuti di revisione o rework richiesti al responsabile. Un checker formale non sostituisce la revisione umana della perdita di significato.

## 8. Definizione di pronto

Una nuova skill è pronta per il gate successivo solo se:

- il primo turno è utile e proporzionato;
- i turni successivi avanzano per differenza;
- il gate è approvabile senza leggere due volte la stessa proposta;
- fonti, inferenze e materiali metodologici restano separati;
- template e output sono modulari;
- modalità test, approvazioni e scritture rispettano i confini di autorità;
- validazione strutturale, controllo del diff e test comportamentale sono documentati;
- versione sorgente, versione installata e versione pubblicata non vengono confuse.

Le eccezioni sono ammesse quando proteggono comprensione, rischio o completezza decisionale. Devono essere esplicite nel blueprint e coperte dagli eval.
