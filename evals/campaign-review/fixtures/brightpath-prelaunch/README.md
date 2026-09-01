# Fixture sintetica: Brightpath, review pre-lancio

Questa fixture è interamente sintetica e pubblicabile. Brightpath è un'azienda immaginaria che vende `FlowLens`, un servizio B2B per aiutare team Operations a rendere visibili i colli di bottiglia nelle richieste di assistenza.

La richiesta simula una review completa prima di una campagna webinar. I materiali contengono volutamente:

- un claim più ampio delle prove disponibili;
- una differenza tra il pubblico della Campaign Spec e un asset;
- una lista email più ampia dei contatti classificati e autorizzati;
- tracking, assegnazione e follow-up dichiarati ma non verificati;
- paid media e approvazione Legal ancora aperti.

La fixture serve a verificare che la skill separi le tre lenti, non dichiari il lancio pronto e non applichi correzioni o azioni esterne.

## Materiali

- `user-request.md`: richiesta del responsabile;
- `campaign-spec.md`: Campaign Spec v2 approvata per la singola iniziativa;
- `asset-linkedin.md`: asset coerente nel tema ma con claim non sostenuto;
- `asset-email.md`: asset con pubblico e consenso non allineati;
- `evidence-register.md`: registro sintetico delle prove e delle autorizzazioni;
- `operations-readiness.md`: stato dichiarato del percorso tecnico e operativo.

La baseline dell'autore è separata dagli input in [`../../oracles/brightpath-prelaunch-expected-review.md`](../../oracles/brightpath-prelaunch-expected-review.md). Non va fornita al generatore durante il forward test.
