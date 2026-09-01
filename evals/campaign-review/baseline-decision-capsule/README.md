# Baseline decisionale Campaign Review → Campaign Debrief

Questa regressione sintetica e pubblicabile verifica il passaggio minimo tra una review pre-lancio e il debrief. Non esegue le skill, non contiene receipt e non viene presentata come prova comportamentale. Un forward test indipendente separato ha confermato che il debrief sa usare la capsule, ma i file di quella run non sono inclusi qui.

Il checker confronta oggetti semantici strutturati, non formulazioni letterali. Verifica che il passaggio conservi identità e stato della Campaign Spec, metrica o obiettivo, definizione operativa, target, finestra, cutoff, maturità, baseline, asset, esito, rilievi, autorizzazione, esecuzione, evidenze e unknowns.

I tre casi positivi coprono:

1. target di 20 richieste qualificate, finestra di sei settimane e definizione operativa disponibili al debrief anche quando riceve solo il passaggio della review;
2. target assente conservato come `missing`, senza ricostruzione;
3. regola di successo qualitativa con cutoff e maturità conservati senza semplificazione numerica.

Le regressioni negative cambiano il target, ne inventano uno assente, semplificano la regola qualitativa, usano una decisione di autorizzazione come prova di esecuzione, bloccano il confronto descrittivo per la sola assenza di baseline e predispongono un confronto causale senza base. Gli ID di errore devono coincidere esattamente.

Il caso con target 20 conserva due stati distinti: il confronto descrittivo è `prepared` e richiede risultati osservati maturi; il confronto incrementale o causale resta `unavailable` perché baseline e comparatore sono assenti.

```text
python3 evals/campaign-review/baseline-decision-capsule/scripts/check_capsule.py
```
