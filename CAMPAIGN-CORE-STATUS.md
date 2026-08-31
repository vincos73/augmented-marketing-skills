# Campaign Core — punto della situazione

Aggiornato: 31 agosto 2026

## Dove siamo

Il Campaign Core è definito come proposta di progettazione in [`CAMPAIGN-CORE.md`](CAMPAIGN-CORE.md).

La prima skill candidata è `design-campaign`. Trasforma un'esigenza di campagna, un brief o un marketing mix approvato in una Campaign Spec con:

- obiettivo, pubblico e cambiamento cercato;
- funnel o sequenza della campagna;
- messaggi, prove e limiti dei claim;
- ruolo dei canali e matrice degli asset;
- responsabilità, dipendenze, approvazioni e capacità;
- percorso di risposta, conversione e follow-up;
- misurazione, assunzioni e condizioni per continuare, correggere o fermare.

La skill non produce gli asset finali, non pubblica, non acquista media, non modifica CRM o piattaforme e non autorizza budget.

## Versione candidata

- Sorgente: [`skills/design-campaign/`](skills/design-campaign/)
- Versione: `0.1.4`
- Stato: candidata, installata localmente con parità verificata rispetto alla sorgente
- Pubblicazione: non ancora inclusa nella Suite pubblicata

La v0.1.4 deriva dai test della v0.1.3 e corregge il linguaggio visibile verso termini comprensibili a marketer e manager: brief, funnel, revisione finale e passaggio alla produzione.

## Evidenze disponibili

- La v0.1.2 ha superato il retest indipendente su Fabriloom con zero hard fail e due soft fail non bloccanti.
- Il test utente della v0.1.3 ha confermato il valore della progressione, ma ha evidenziato prolissità multi-turn e lessico ancora troppo tecnico.
- La v0.1.4 richiede ancora un retest comportamentale indipendente.

I test esistenti non provano ancora il percorso completo con marketer esterni, la produzione reale di asset, la review pre-lancio o l'efficacia di una campagna.

## Prossimo passaggio

1. Eseguire un retest indipendente della v0.1.4 usando la fixture Fabriloom, senza leggere prima catalogo, run precedenti o baseline.
2. Registrare hard fail, soft fail, limiti e materiali letti.
3. Correggere la skill solo se il retest lo richiede.
4. Verificare installazione/parità e decidere se proporre la pubblicazione.

`campaign-review` e `learn-from-results` restano skill successive: non vanno implementate in parallelo al retest di `design-campaign`.

## Contesto Git

- Branch: `codex/campaign-core-skill-candidates`
- Commit di base: `a9b8364 feat: add Campaign Core candidate and align skill UX`
- Remoto: `https://github.com/vincos73/augmented-marketing-skills.git`
- Il branch contiene il lavoro del Campaign Core; il worktree locale ha anche modifiche non pertinenti che non devono essere incluse automaticamente.

## Come continuare sul portatile

```bash
git clone https://github.com/vincos73/augmented-marketing-skills.git
cd augmented-marketing-skills
git fetch origin
git switch --track origin/codex/campaign-core-skill-candidates
sed -n '1,240p' CAMPAIGN-CORE-STATUS.md
```

Dopo aver letto questo file, il riferimento progettuale completo è [`CAMPAIGN-CORE.md`](CAMPAIGN-CORE.md); la skill candidata e i materiali di test sono nella cartella [`skills/design-campaign/`](skills/design-campaign/) e in [`evals/design-campaign/`](evals/design-campaign/).

