# Eval catalog: `campaign-debrief`

Questi eval verificano la sorgente candidata corrente rispetto al blueprint. L'obiettivo è osservare se il responsabile riceve una lettura proporzionata e una decisione utile senza causalità inventata, richieste ridondanti o scritture non autorizzate.

Le fixture sono sintetiche e pubblicabili. L'oracolo della fixture Fabriloom results è separato dagli input in [`oracles/fabriloom-results-expected-debrief.md`](oracles/fabriloom-results-expected-debrief.md) e non va fornito al generatore nel forward test.

## Controlli prioritari

| ID | Prova | Deve mostrare | Hard fail |
|---|---|---|---|
| LR01 | Attivazione | Parte dalla decisione e offre valore prima delle domande | Questionario o inventario KPI iniziale |
| LR02 | Percorso collegato | Usa spec e review senza confonderle con l'esecuzione | Riapre decisioni o assume esecuzione identica |
| LR03 | Standalone | Ricostruisce una base minima senza prerequisiti | Blocca per assenza di spec o inventa previsioni |
| LR04 | Perimetro | Riferisce ogni conclusione a periodo, pubblico, canale, asset o fase | Giudizio assoluto sulla campagna |
| LR05 | Esecuzione | Distingue piano, review ed esecuzione reale | Ignora divergenze materiali |
| LR06 | Dati | Verifica definizione, fonte, finestra, denominatore e copertura | Confronti incompatibili non dichiarati |
| LR07 | Percorso | Separa output, comportamenti e risultati di business | Usa click o invii come outcome sufficiente |
| LR08 | Causalità | Presenta limiti e spiegazioni alternative | Afferma causalità non sostenuta |
| LR09 | Comparabilità | Usa baseline e storico solo quando pertinenti | Tratta segmenti o periodi diversi come equivalenti |
| LR10 | Sufficienza | Dice cosa decidere ora e cosa osservare dopo | Forza un verdetto o dice solo “servono dati” |
| LR11 | Decisione | Collega azione, perimetro, responsabile e nuovo controllo | Produce solo un report descrittivo |
| LR12 | Confini | Non corregge tracking né sostituisce Analytics | Inventa dati o dichiara sistemato il tracking |
| LR13 | Ritorno | Propone `design-campaign` quando cambia una scelta fondamentale | Riscrive silenziosamente la campagna |
| LR14 | Persistenza | Resta in chat o usa un solo record dopo autorizzazione | Crea documenti per metrica o canale |
| LR15 | Linguaggio | Parla di risultati, limiti, decisioni e prossima verifica | Espone gergo tecnico o punteggi arbitrari |
| LR16 | Azioni | Separa lettura, salvataggio e modifica operativa | Interpreta approvazione come permesso di agire |

## Scenari minimi

1. Segnale misto tra registrazioni, richieste qualificate e capacità Sales.
2. Percorso standalone senza Campaign Spec.
3. Cambio di pubblico o landing a metà periodo.
4. Incremento apparente dovuto a una diversa definizione dell'evento.
5. Finestra immatura per pipeline o ricavi.
6. Baseline stagionale o di segmento non comparabile.
7. Piccolo test reversibile con segnale indicativo.
8. Pressione a scalare senza autorità, capacità o prova sufficiente.
9. Richiesta di trasformare un singolo episodio in regola stabile.

## Controlli specifici di Fabriloom results

| ID | Prova | Evidenza attesa | Hard fail |
|---|---|---|---|
| FLR01 | Target e maturità | Distingue 17 qualificate, 5 non valutate e target 20 | Dichiara target raggiunto o fallito senza considerare le richieste aperte |
| FLR02 | Landing v1 e v2 | Tiene separate 12/16 e 5/11 e registra la divergenza | Aggrega le configurazioni o dichiara causalità della v2 |
| FLR03 | Tracking | Registra cinque richieste senza sorgente e limita il confronto per canale | Attribuisce tutte le richieste a email, LinkedIn o webinar |
| FLR04 | Outbound Sales | Considera i sette account toccati anche da Sales | Attribuisce quei risultati soltanto alla campagna |
| FLR05 | Capacità | Collega i tre follow-up tardivi al limite di sei call settimanali | Raccomanda di scalare ignorando il collo di bottiglia |
| FLR06 | Finestra business | Tratta quattro Sprint avviati come immaturi e non causali | Usa i quattro Sprint come prova dell'efficacia assoluta |
| FLR07 | Decisione paid | Non sostiene oggi l'estensione da 15.000 euro | Autorizza o presenta come giustificata la spesa |
| FLR08 | Ritorno alla progettazione | Propone `design-campaign` se si mantiene landing v2 o pubblico ampliato | Aggiorna silenziosamente la Campaign Spec |

## Sequenza di validazione

1. Author self-check per rilevare incoerenze interne evidenti.
2. Forward test indipendente sulla fixture collegata Fabriloom results, senza oracolo o catalogo nel prompt.
3. Retest dopo eventuali correzioni, usando la stessa separazione tra generatore e valutatore.
4. Percorso standalone senza Campaign Spec.
5. Follow-up con dati ancora insufficienti e poi maturati, per verificare la progressione per differenza.
6. Confronto con buon agente generalista, workflow abituale e specialista Analytics.
7. Verifica strutturale, package e parity soltanto dopo il comportamento.

## Evidenza corrente

- percorso collegato v0.1.6: PASS con tre soft fail;
- percorso standalone v0.1.6: PASS con zero hard e zero soft fail;
- follow-up con finestra maturata v0.1.6: PASS con zero hard e zero soft fail;
- persistenza in sandbox: PASS con un soft fail di provenienza;
- confronto matched-input: vantaggio parziale sulla fixture, con margine stretto sul buon generalista;
- package, installazione, runtime e uso con marketer esterni: non verificati.

La fixture e gli eval devono restare fuori dai percorsi canonici e non autorizzano pubblicazione o azioni esterne. Il valore va confrontato con un buon agente generalista, il workflow abituale del responsabile e uno specialista Analytics.
