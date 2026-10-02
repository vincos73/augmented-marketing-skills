# Localization core — candidata locale

**Stato:** sorgenti in valutazione, versione `1.0.1-l10n.1`. Nessuna release, installazione o verifica in una nuova sessione applicativa è implicita. La distribuzione pubblica `1.0.0` resta il riferimento stabile.

## Base e provenienza

- Base: `main` al commit `cd250d3657370715ad07197ba09757fcecadced2`.
- Origine della proposta linguistica: commit `a39dc30` del ramo locale `codex/suite-localization-close`.
- Questa candidata ha un identificatore distinto dalle prove `rc.1`–`rc.7` del ramo d'origine, perché ne contiene solo una selezione.

## Cosa contiene

- Guida inglese al prodotto, all'installazione e agli esempi (`README.en.md`, `INSTALLATION.md`, `docs/en/`).
- Descrizioni inglesi per le dodici skill, metadati delle interfacce OpenAI e manifest dei plugin.
- Una regola comune: risposta nella lingua dell'utente e documento nella lingua esplicitamente richiesta, anche con fonti in altre lingue; conservazione di voce, citazioni, testi protetti e identificatori tecnici.
- Rimozione delle istruzioni che imponevano l'italiano per impostazione predefinita nei tre punti in cui avrebbero contraddetto la nuova regola.
- Quattro template allineati alla lingua del documento richiesto. Il metodo operativo delle skill e i riferimenti restano in italiano.

## Cosa resta separato

Le successive modifiche comportamentali a `design-campaign` e `write-marketing-copy`, le valutazioni e gli archivi di prova del ramo d'origine non sono inclusi. In particolare la revisione `design-campaign` rc7 non è stata accettata per promozione nei rapporti esistenti. Questa candidata non ne eredita lo stato né ne dichiara risolti i problemi. Nessun contenuto dei worktree di salvataggio iMac o MacBook è stato trasferito.

## Verifiche e decisione successiva

Il 2 ottobre 2026, nel worktree isolato:

- `git diff --check`: superato;
- 11 test del builder: superati;
- 12 frontmatter, 12 file YAML dell'interfaccia, regola linguistica comune e versioni dei manifest: validati con il parser YAML di Ruby;
- 13 archivi costruiti in una directory temporanea, con controllo di integrità, corrispondenza esatta alle sorgenti e byte deterministici: superato;
- link locali dei dieci documenti di ingresso e guida: nessun collegamento mancante;
- `dist/` ed `evals/`: nessuna modifica inclusa nella candidata.

Il validatore standard `quick_validate.py` non ha potuto avviarsi perché l'interprete Python disponibile non ha `PyYAML`; la verifica YAML sopra copre la struttura rilevante, non l'intera logica di quel validatore. Servono prove in nuove sessioni Codex, ChatGPT e Claude con richieste italiane, inglesi e miste, controllando attivazione, lingua del documento, citazioni e testi protetti. I limiti di autenticazione Claude o dell'interfaccia vanno dichiarati se impediscono una prova. La pubblicazione su GitHub, il merge, l'installazione e la promozione a release sono decisioni separate.
