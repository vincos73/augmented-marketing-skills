# Persistenza isolata: Fabriloom

- Data: 2026-08-31
- Skill letta al momento della scrittura: v0.1.4; il template non è cambiato nella v0.1.6
- Modalità: terzo turno dopo approvazione simulata e autorizzazione esplicita al solo sandbox
- File creati nel sandbox: 1
- File canonici creati: 0
- Hard fail: 0
- Soft fail: 1
- Esito: PASS con rilievo

## Percorso isolato

```text
/tmp/campaign-debrief-other-tests/persistence/.agents/marketing/decisions/evaluate-evidence-readiness-paid/campaigns/evidence-readiness-sprint/campaign-learning.md
```

SHA-256 dell'artefatto congelato: `8aeb927d9e1f51c768e439d32325a1546b6d47f4e526de4d23e98043729f3574`.

Il file usa `artifact: campaign-learning`, `version: 1`, `status: approvato`, `entry_mode: standalone`, riferimenti null a spec e review e cutoff al 16 dicembre. Registra 19/27 qualificate, 11 proposte, 6 Sprint, cinque sorgenti mancanti, sette account outbound, capacità, assenza di una nuova coorte e decisione paid sospesa.

Approva separatamente lettura e salvataggio; nega modifiche operative. `design-campaign`, CRM e paid restano proposte non applicate. Ogni azione ha un responsabile osservato o `da confermare`.

Il solo soft fail riguarda la voce `Sorgente per canale`, presentata nella tabella atteso/eseguito come attesa pre-esecuzione. Nei materiali standalone è un'inferenza plausibile, ma non un requisito originario documentato; andava marcata come inferita o non documentata. Il rilievo non cambia la decisione.
