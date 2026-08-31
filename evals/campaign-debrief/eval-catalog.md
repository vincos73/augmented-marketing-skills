# Eval catalog: `campaign-debrief`

Questi eval verificano il blueprint prima di creare una sorgente installabile. L'obiettivo è osservare se il responsabile riceve una lettura proporzionata e una decisione utile senza causalità inventata, richieste ridondanti o scritture non autorizzate.

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

La fixture e gli eval devono restare fuori dai percorsi canonici e non autorizzano pubblicazione o azioni esterne. Il valore va confrontato con un buon agente generalista, il workflow abituale del responsabile e uno specialista Analytics.
