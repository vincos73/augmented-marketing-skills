# Run statico P0: Fabriloom Evidence Readiness lineage

Data: 1 settembre 2026
Checkout base: commit `561dc93`, tag `augmented-marketing-suite-v0.1.0-beta.9`, detached HEAD; modifiche eval locali non committate durante il test
Skill verificate: `campaign-review` v0.1.2, `campaign-debrief` v0.1.6
Tipo di prova: validazione statica della fixture e dei casi negativi

## Comando

```bash
python3 evals/campaign-lineage/fabriloom-evidence-readiness/scripts/check_lineage.py
```

## Esito osservato

```text
PASS manifest positivo: FABRILOOM-ERS-LINEAGE-1
PASS caso negativo respinto: asset v0 riferito al file v1
PASS caso negativo respinto: lineage completa promossa a asset v0 mentre il file resta v1
PASS caso negativo respinto: resolution review non risolta
PASS caso negativo respinto: versione mancante
PASS caso negativo respinto: rilievo bloccante non chiuso
PASS caso negativo respinto: scope paid non autorizzato
PASS caso negativo respinto: execution log con review superata
PASS caso negativo respinto: asset diverso da quello revisionato
```

Il controllo ricalcola i digest, confronta identità, versione e riferimenti semantici del front matter con il manifest e usa `check_files: true` per le regressioni di versione.

## Copertura hard osservata

- ID, versione, percorso e SHA-256 per gli artefatti materiali della catena;
- Campaign Spec approvata comune ad asset e review;
- v0 difettoso e review v1 bloccata con criterio di chiusura;
- v1 distinto, fornito dalla fixture e osservato direttamente dalla review v2;
- chiusura del rilievo legata a ID, versione e digest di v1;
- autorizzazione sintetica post-review riferita esattamente ad asset v1 e review v2;
- execution log coerente con la coppia approvata e non superata;
- debrief riferito a atteso, eseguito e osservato, con causalità non attribuita;
- debrief effettivo distinto dall'oracolo expected, con path e digest propri;
- claim vietato confinato a spec, asset v0, rilievo e oracle;
- testimonianza anonima, paid non attivato, tracking e capacità espliciti.

## Casi negativi osservati

| Caso | Classe | Esito |
|---|---|---|
| reference senza versione | hard | respinto per versione mancante |
| execution con asset v0 ma review v2 | hard | respinto per asset diverso da quello revisionato |
| review v2 procedibile con blocco aperto | hard | respinto per rilievo bloccante non chiuso |
| execution con review v1 | hard | respinto perché la review è superata |
| lineage completa asset v0 con file v1 | hard | respinta dal confronto tra front matter e manifest |

## Limiti

Questo run valida struttura, coerenza interna e regressioni statiche. Non è un forward test indipendente delle risposte generate dalle skill, non misura la qualità con marketer reali e non prova package, installazione, caricamento o runtime. I controlli soft FLG10-FLG14 sono definiti per un successivo run comportamentale, ma non possono risultare PASS in base al solo checker statico.
