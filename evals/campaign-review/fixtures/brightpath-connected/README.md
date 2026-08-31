# Regressione sintetica collegata

Questa fixture verifica che la review riusi una base strategica già approvata senza rifare `design-campaign` né riaprire la scelta del mix.

- `marketing-mix.md`: componente Promotion approvata;
- `campaign-spec.md`: spec v1 che la referenzia;
- `asset-email.md`: asset con una deviazione materiale di pubblico;
- `operations-readiness.md`: unica dipendenza operativa non verificata;
- `user-request.md`: richiesta di controllo prima dell'invio.

La fixture è sintetica e non autorizza scritture o azioni esterne.
