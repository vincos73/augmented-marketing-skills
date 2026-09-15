# Vincos Editorial Diagrams

Skill per creare e modificare infografiche editoriali e diagrammi strategici nello stile Vincos.

È pensata per visualizzazioni dedicate a intelligenza artificiale, lavoro, analisi delle attività, consulenza, newsletter, formazione e contenuti social.

## Contenuto

- `SKILL.md`: grammatica visiva, regole tipografiche e flusso operativo
- `agents/openai.yaml`: metadati per l’integrazione con Codex
- `assets/icon.svg`: icona della skill
- `assets/fonts/ibm-plex-mono/`: IBM Plex Mono Regular/Medium e licenza OFL per metadati tecnici
- `references/prompt-template.md`: modello di prompt per produrre nuovi diagrammi
- `references/structure-selector.md`: selezione della struttura, budget e invarianti SVG
- `references/canonical-examples.md`: scelta e anti-pattern delle sei famiglie
- `references/design-system.md`: token, primitive e gerarchia visiva condivisi
- `assets/examples/`: sei template SVG canonici e accessibili
- `scripts/validate_svg.py`: validatore senza dipendenze per safe zone, gap e chamfer
- `tests/run_tests.py`: verifica automatica di fixture e template

## Principi essenziali

- mantenere una composizione editoriale pulita, analitica e leggibile
- usare la palette navy, azzurro chiaro, grigio scuro e bianco panna
- usare Barlow come font principale e IBM Plex Mono soltanto per metadati tecnici brevi
- usare di default una composizione ibrida techprint, salvo i casi in cui riduca precisione o leggibilità
- evidenziare soltanto gli elementi rilevanti per l’analisi
- inserire il lockup ufficiale Vincos nell’area inferiore destra
- verificare il PNG finale sia a dimensione piena sia ridotta prima della consegna
- evitare gradienti, estetica cyberpunk, decorazioni tecniche prive di funzione e testi troppo densi

## Skill collegate

Usare questa skill insieme a `$vincos-brand-guidelines`, che rimane la fonte di riferimento per logo, tipografia e palette.

Quando occorre generare o modificare immagini bitmap, usare anche `$imagegen`. Testi e logo ufficiale devono essere inseriti con un metodo di impaginazione deterministico.

## Installazione

Il repository è pubblico e può essere clonato direttamente da GitHub.

```bash
gh repo clone vincos73/vincos-editorial-diagrams
cd vincos-editorial-diagrams
mkdir -p ~/.codex/skills/vincos-editorial-diagrams
rsync -a SKILL.md agents assets references scripts ~/.codex/skills/vincos-editorial-diagrams/
```

La skill viene rilevata da Codex dal turno successivo all’installazione.

Per verificare validator e template dal repository:

```bash
python3 tests/run_tests.py
python3 ~/.codex/skills/.system/skill-creator/scripts/quick_validate.py .
```

## Utilizzo

È possibile richiamarla esplicitamente con `$vincos-editorial-diagrams`.

```text
Usa $vincos-brand-guidelines e $vincos-editorial-diagrams per trasformare questo framework in un diagramma editoriale Vincos.
```

```text
Usa $vincos-editorial-diagrams per creare una matrice a quattro quadranti leggibile anche sui social.
```

## Versione

Release corrente: `v1.7.0`.
