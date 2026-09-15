---
name: vincos-editorial-diagrams
description: "Create or edit Vincos-branded editorial infographics and strategic diagrams for AI/IA, work, task analysis, consulting frameworks, newsletters, blog visuals, training materials, and social graphics. Use for raster or export-ready diagrams that need the Vincos palette, Barlow-led typography, lightweight technical grammar, matrices, task-brick sequences, value/control flows, or intentional clipped-corner boxes. Apply together with $vincos-brand-guidelines; use $imagegen when bitmap generation or editing is needed."
metadata:
  version: "1.7.0"
---

# Vincos Editorial Diagrams

Versione 1.7.0

## Purpose

Use this skill to produce the editorial diagram style developed for Vincos AI/work essays: professional, sparse, analytical, and readable on social, blog, consulting, and training formats.

Apply `$vincos-brand-guidelines` as the source of truth for identity, logo, typography, and palette. Use this skill only to add the diagram grammar. If the two skills conflict, follow the brand guidelines.

Use `$imagegen` for bitmap generation or image editing. Do not rely on image generation alone when exact typography or an official logo is required.

Per scegliere la struttura, parti da ciò che il lettore deve capire e usa il selettore compatto in [references/structure-selector.md](references/structure-selector.md). Prima di disegnare fissa sempre destinazione e dimensione, livello di dettaglio e pubblico. Se il contenuto viene ridotto, consegna una breve ricevuta delle semplificazioni effettuate.

Per geometria, testi, frecce, chamfer e logo usa SVG o altro layout deterministico come base. `$imagegen` è un supporto soltanto quando serve una componente illustrata o bitmap; non sostituisce il controllo deterministico del layout.

Quando serve un punto di partenza riproducibile, leggi [references/canonical-examples.md](references/canonical-examples.md) e adatta il template della famiglia scelta. Gli esempi sono strutturali: prima della consegna inserisci sempre il lockup ufficiale e completa il controllo del render.

Usa [references/design-system.md](references/design-system.md) per applicare token, primitive e ruoli visivi comuni. Leggi la sezione `Stack operativo con orchestratore laterale` quando il diagramma rappresenta una suite, un sistema operativo professionale o un punto di ingresso che orienta verso più livelli. Non trattare rettangoli, cerchi, chamfer, retini e frecce come decorazioni intercambiabili: ciascuno deve rappresentare un ruolo analitico.

## Core Style

- Default to a clean paper-white background: `#FEFDFB`.
- Use navy for rules, outlines, arrows, icons, and technical marks: `#072743`.
- Use dark gray for primary text where needed: `#323232`.
- Use pale blue highlight fills only for AI-affected elements, value shifts, selected task bricks, or system nodes: `#E3F4FF`.
- Use Barlow as the primary editorial voice: Barlow Bold for titles and central entities, Barlow Medium for labels, and Barlow Regular for explanations. IBM Plex Mono is the documented secondary exception for short functional metadata only: sequence numbers, states, measurements, timestamps, input/output labels, file names, and connector annotations. Keep mono text below 15% of visible copy; never use it for titles, conclusions, paragraphs, or the logo. Use the bundled Regular/Medium files in `assets/fonts/ibm-plex-mono/` and preserve `OFL.txt` when distributing them.
- Use navy backgrounds or panels only when they create a deliberate section or hierarchy. Use `#FEFDFB` text and verify contrast on navy.
- Prefer landscape editorial/social composition unless the user asks otherwise.
- Keep the visual calm, precise, sparse, and consulting-grade.
- Prefer leggerezza percettiva: fai emergere la gerarchia con spazio, scala, contrasto e posizione prima che con linee spesse.
- Usa una scala di tratti leggera e intenzionale: struttura quieta, relazioni primarie appena più presenti, relazioni secondarie sottili o tratteggiate. Non rinforzare tutti i bordi per rendere il diagramma più chiaro.
- Tratta guide, assi e contenitori come supporto: grigio attenuato o navy a bassa intensità quando il contesto lo consente; il navy pieno resta per il fuoco, il testo e le relazioni che devono guidare la lettura.
- Lascia respirare i nodi: aumenta il padding e riduci cornici, riempimenti e separatori quando non aggiungono una distinzione semantica.
- Usa `OpenFrame` quando basta suggerire un campo o un sistema: quattro segni angolari possono sostituire una cornice completa. Non usarlo come decorazione attorno a ogni modulo.
- Usa un `TechnicalField` puntinato o quadrettato soltanto dietro un nucleo operativo e a intensità molto bassa. Non estendere la griglia all'intero canvas.
- Usa un retino obliquo leggero soltanto per distinguere la natura di un ruolo o di una superficie, non per dichiararne automaticamente l'importanza. Negli stack con orchestratore esterno può riempire il box dell'orchestratore; mantieni testo, bordo e chamfer pienamente leggibili e non ripeterlo sui livelli interni.
- Put the official Vincos lockup on every final diagram, including article figures. Reserve a quiet footer zone before laying out the diagram and place the lockup in the lower-right corner, without covering data, labels, or captions. Treat the reserved footer as a no-draw area: no box, border, arrow, connector, caption, baseline, or other diagram element may enter it.
- Use the correct official master from `$vincos-brand-guidelines`: `vincos-lockup-navy.svg` on white, cream, or pale-blue backgrounds; `vincos-lockup-white.svg` on navy or dark backgrounds; use the black master only for monochrome output. Never generate, redraw, or retype the logo.
- Use the complete lockup, not the isolated symbol. Keep clear space around it at least equal to the main stroke width, preserve its proportions, and size it discreetly but legibly (normally 7–10% of the canvas width).
- Build every composition around one focal object. At thumbnail size, this object must remain the first element perceived; the pale-blue fill, a larger scale, or a local density contrast may establish it, but only one mechanism should dominate.
- Use a deliberate visual hierarchy for connectors: structural boundaries are quiet, primary flows are clear, and secondary or feedback relationships are lighter or dashed. Do not give every relationship the same visual weight.
- Keep a consistent series frame while varying one structural metaphor per diagram. Do not repeat the same row of equal cards when the reader needs a map, a hierarchy, a comparison, or a trajectory.

## Composition Modes

Choose one mode deliberately:

- **Hybrid techprint, default:** combine a precise schematic structure with at least one restrained line illustration that clarifies a mechanism, scale, role, or relationship. Use this mode for most conceptual editorial visuals.
- **Explanatory techprint:** make distinct line illustrations carry the explanation when the subject concerns people, organizations, systems, tools, or changes of scale. Keep labels short and let the drawings do analytical work.
- **Analytical schematic:** use matrices, charts, sequences, flows, or comparisons without illustrations when a drawing would reduce precision, legibility, or data fidelity.

Do not add a techprint illustration merely to satisfy the default. If it cannot be assigned a specific explanatory function, switch to the analytical schematic mode.

## Diagram Grammar

Select only the elements that clarify the conceptual structure:

- Use clipped-corner technical boxes only when the treatment is intentional. The corner must read immediately as a real chamfer, not as an almost-rectangular box: draw two clearly visible diagonal edges that interrupt the horizontal and vertical borders. Every cut must be fully visible: keep each clipped corner entirely inside the canvas, outside the footer safe area, and unobstructed by adjacent shapes, lines, text, masks, or the viewport edge. Make the diagonal cut long enough to remain legible at final size, normally at least 4× the main stroke width and never less than 16 px in the final raster export. Keep every cut geometrically consistent and draw it with the same navy stroke width. A clipped, partial, hidden, hairline, or off-canvas cut is invalid; if the diagonal is not immediately recognizable at 100% final-size viewing, enlarge it or use a regular rectangle instead.
- Construct the chamfer explicitly as a polygon/path with a visible diagonal from the top edge to the side edge, for example `M24 0 H... L... 0 V24 ...`; do not simulate it with a thin overlay, a mask, a crop, or a nearly zero-length corner modification. The fill must follow the same chamfered path as the outline so the diagonal is not lost against the box fill.
- Render order is part of the geometry: draw the box fill first, draw any internal header or band with the same chamfered path, and draw the complete navy outline last. Never place a rectangular header, background, mask, or overlay on top of the outlined box if it can cover either diagonal.
- Four-quadrant matrices for frameworks with four scenarios or modes.
- Horizontal task-brick sequences to represent work as bundles of activities.
- Pale-blue filled brick or node to show where AI intervenes.
- Dashed navy or pale-blue paths for data, learning, handoff, or future migration.
- Thin arrows for acceleration, value movement, or process flow.
- Small plus signs only when they act as meaningful technical markers.
- Simple circles for systems, control points, worker/value nodes, or feedback loops.
- Minimal currency/value markers only when the concept needs remuneration or value capture.
- Integrate line illustrations in a restrained techprint style when they explain scale, mechanisms, roles, or relationships better than abstract boxes alone.
- Give every illustration a distinct analytical function. Keep the palette limited, use consistent navy strokes, preserve generous whitespace, and match the level of detail across the composition.
- For the lightweight direction, prefer open geometry, pochi punti di contatto e linee che terminano nello spazio; evita contorni doppi, bordi sovrapposti e campiture che trasformano una relazione in una massa.
- Termina ogni connettore sul perimetro visibile del nodo e fallo ripartire dal lato opposto. Non disegnare una linea continua sotto un blocco opaco: segmenta la geometria e mantieni un piccolo `connector-clearance` quando la relazione non deve entrare nel nodo.
- Apply the primitive contracts in [references/design-system.md](references/design-system.md): `Frame`, `TitleBlock`, `Card`, `FocalCard`, `Node`, `Connector`, `Boundary`, and `Trajectory`.

Avoid:

- Dense microtext, paragraphs inside boxes, long captions, or tiny labels.
- Gradients, neon/cyberpunk, glossy UI, red/orange annotations, or large navy areas that compete with the information.
- Stock imagery, generic human silhouettes, decorative icons, punched-card holes, perforated paper.
- Overly literal illustrations when a schematic can communicate the point more clearly.
- Mixed corner treatments, inconsistent line weights, or technical decoration without an analytical function.

## Workflow

1. Apply `$vincos-brand-guidelines`, identify the destination format and final dimensions, choose the matching official logo master, and reserve its lower-right footer area before placing any diagram element. Define a visible no-draw footer safe zone around the logo: reserve at least the bottom 12% of the canvas height and a horizontal area extending at least one logo width to the left of the logo, plus clear space around the lockup. Keep the lowest diagram baseline, box, border, arrow, connector, and caption above this boundary with a minimum gap of 24 px at final raster size, or 2× the main stroke width when that is larger. If the composition does not fit, reduce or reflow the diagram, increase the canvas, or move the footer content; never let the diagram enter the reserved zone.
2. Fissa destinazione/dimensione, livello di dettaglio e pubblico; poi scegli la famiglia strutturale dal selector e il composition mode. Default a hybrid techprint, ma passa a explanatory techprint o analytical schematic quando migliora comprensione e precisione.
3. Rispetta i budget prudenti della reference: se un budget viene superato, passa a una panoramica più un dettaglio invece di comprimere microtesto e relazioni.
4. Riduci il testo a titolo e label brevi. Se semplifichi, annota cosa hai tolto, raggruppato o spostato fuori immagine.
5. Scegli una sola metafora e gli elementi necessari. In hybrid mode assegna una funzione analitica a ogni illustrazione; in analytical mode omettila se sarebbe decorativa.
6. Evidenzia soltanto l'elemento analiticamente importante in `#E3F4FF`.
7. Costruisci geometria, testo, frecce, chamfer e logo con SVG o layout deterministico; usa `$imagegen` solo per l'eventuale componente illustrata o bitmap.
8. Valida gli invarianti SVG con `scripts/validate_svg.py`; usa gli attributi documentati nella reference, inclusi nodi e connettori verificabili quando il flusso usa linee o polilinee. Quando modifichi validator o template, esegui anche `python3 tests/run_tests.py`.
9. Renderizza il PNG finale e ispezionalo a dimensione piena e ridotta, verificando comprensione, collisioni, chamfer, logo, contrasto, margini e footer. Se emerge un difetto, correggi, renderizza di nuovo e ripeti.
10. Salva gli asset finali nel workspace `outputs/`, non solo nella directory delle immagini generate.

## Text Rules

- Keep Italian text exact and verify accents manually.
- Default to sentence case. Reserve all caps for acronyms, numbering, and short technical micro-labels.
- Keep the title on one line whenever it retains adequate size, margins, and readability. Break it only when the composition requires it.
- Prefer short, autonomous labels such as `Persona`, `Impresa`, `Economia`.
- Give central entities greater emphasis through Barlow Bold and size. Remove verdicts, captions, or repeated conclusions already communicated visually.
- Use `IA`, not `AI`, for Italian diagrams unless the user asks otherwise.
- Spell words with accents in the prompt explicitly, for example `ATTIVITÀ` with final `À`.
- If imagegen misspells a label, iterate with a targeted edit that changes only that label. If the error persists or the font is not Barlow, typeset the label outside imagegen.

## Prompt Template

Read [references/prompt-template.md](references/prompt-template.md) when creating a new image from scratch or when adapting an existing diagram to this style.
