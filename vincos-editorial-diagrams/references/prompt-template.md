# Prompt Template

Use this as a compact starting point with `$imagegen`, after applying `$vincos-brand-guidelines`. Treat generation as an intermediate step when the final asset requires exact Barlow typography or an official logo.

```text
Use case: infographic-diagram
Asset type: editorial social/blog visual
Primary request: Create a Vincos-style infographic that represents: <concept>.
Reader need / structure family: <what the reader must understand> / <system map | flow | cycle | hierarchy | comparison | evolution>.
Parameters before drawing: destination/size=<...>; detail level=<overview | operational | analytical>; audience=<...>.
Complexity budget: keep within 7 main nodes/panels, 9 labels, 10 connections and 2 hierarchy levels; if exceeded, provide an overview plus a detail view and a short simplification receipt.
Composition contract: focal object=<...>; primary relationship=<...>; secondary relationship=<... or none>. Preserve the shared frame, title block and footer, then vary one structural metaphor only. Use distinct visual roles for boundary, primary flow, secondary/feedback flow, card and focal card.

Scene/backdrop: clean #FEFDFB paper-white background, no global grid or texture. A faint local technical field is allowed only behind one operational nucleus when it clarifies alignment, processing, or scale. Use a navy panel only if it creates a deliberate section or hierarchy.
Subject: <framework/scenario/process>.
Composition/framing: landscape infographic, title normally aligned to the left content grid and kept on one line whenever size, margins, and readability allow. Center it only when the whole composition is genuinely symmetric. A short descriptive line is optional only when it explains how to read the diagram; it must not restate the title or repeat a conclusion already visible. Use a clean structured layout with a quiet lower-right footer zone reserved for the official Vincos lockup. Reserve the footer before placing any diagram element: treat at least the bottom 12% of the canvas and a horizontal area extending one logo width to the left of the logo as a no-draw safe zone, with clear space around the lockup. Keep every box, border, arrow, connector, baseline, and caption outside this zone and at least 24 px from its boundary at final raster size, or 2× the main stroke width when larger. If the composition does not fit, reflow it, increase the canvas, or move footer content; never let the diagram enter the safe zone. Default to hybrid techprint: combine a precise schematic structure with at least one restrained line illustration that explains a mechanism, scale, role, or relationship. Use explanatory techprint when drawings can carry the argument. Use an analytical schematic without illustrations when drawings would reduce precision, legibility, or data fidelity. Choose only the necessary elements among matrices, task-brick sequences, simple arrows, dashed paths, plus markers, schematic circles or nodes, and explanatory techprint illustrations. If clipped-corner boxes are used, each corner must be a clearly recognizable chamfer made of two visible diagonal edges, fully inside the canvas, unobstructed by other elements and safely separated from the viewport edge, footer, and neighboring shapes. The cut must remain legible at 100% final-size viewing, normally at least 4× the main stroke width and never less than 16 px in the final raster export. A partial, hidden, hairline, or off-canvas cut is invalid; enlarge it or use a regular rectangle if it cannot remain visible. Keep geometry and navy stroke width consistent.
For every chamfer, use an explicit filled-and-stroked polygon/path with the same visible diagonal in the fill and outline, such as `M24 0 H... L... 0 V24 ...`; do not use a nearly rectangular box, thin overlay, mask, crop, or zero-length corner alteration.
Render the box fill first, any internal header or band with the same chamfered path second, and the complete navy outline last. Never overlay a plain rectangle, mask, or background on top of the outlined box if it can cover either diagonal.
Style/medium: precise editorial technical diagram, calm, analytical, human-aware consulting and training visual language. Use SVG or another deterministic layout for geometry, text, arrows, chamfers and the official logo; use imagegen only for an illustrated or bitmap component.
Color palette: #FEFDFB background, #072743 navy lines and rules, #323232 dark gray text, #E3F4FF pale blue highlights/fills. Use pale blue only for the focal AI/value-affected component. Give structural boundaries, primary flows and secondary/feedback flows distinct line weights or treatments; do not give all connectors equal visual weight. Terminate connectors on visible node boundaries and resume them as explicit segments on the opposite side; no connector may cross or remain hidden under an opaque card. Use an open frame made of four corner marks when a full boundary would add unnecessary weight.
Typography: Barlow Bold for the readable title and central entities, Barlow Medium for labels, Barlow Regular for explanations. Use IBM Plex Mono Regular or Medium only for short sequence numbers, states, measurements, input/output labels, file names, timestamps, and connector annotations; keep it below 15% of visible copy. Never use mono for titles, paragraphs, conclusions, or the logo. Default to sentence case; reserve all caps for acronyms, numbering, and technical micro-labels. Build hierarchy through size and weight. If exact fonts cannot be produced, leave clean text areas for later typesetting instead of approximating them.
Text (verbatim):
Title: "<title>"
Labels: "<label 1>", "<label 2>", "<label 3>", "<label 4>"
Constraints: no descriptive line unless it adds a genuine reading rule, no paragraph text, no watermark, no working numbers, section codes, or editorial notes unless explicitly intended for readers, all text exactly spelled, generous whitespace, high legibility. Remove verbal conclusions already communicated by the drawing. Every illustration must explain a mechanism, scale, role, or relationship rather than decorate. Do not generate, redraw, or retype the Vincos logo; leave the reserved lower-right footer zone clear so the official `vincos-lockup-navy.svg` or `vincos-lockup-white.svg` master can be inserted after generation.
Avoid: cluttered microtext, illegible labels, red/orange annotations, cyberpunk, neon, gradients, glossy UI, stock imagery, generic decorative people silhouettes, punched-card holes, perforated paper, competing navy areas, inconsistent line weights, mixed corner treatments, decorative technical marks without analytical meaning.
```

## Common Patterns

Hybrid techprint:
- Start from the analytical structure: flow, comparison, sequence, stack, or system map.
- Add at least one line illustration only after assigning it a specific explanatory function.
- Use the drawing to reveal a mechanism, scale, role, or relationship that abstract boxes alone would communicate less clearly.
- Omit the drawing and use an analytical schematic when it would be merely decorative.

Four-scenario matrix:
- Use a 2x2 matrix with one consistent box per scenario.
- If clipped corners clarify the system, use the same clearly recognizable chamfer on every box, with two visible diagonal edges and consistent stroke width. Keep all cuts inside the canvas with clear space around them; never let a cut touch or disappear behind the canvas edge or another element. At final size, a barely visible diagonal is a failed cut and must be enlarged or removed.
- Put one short sentence-case label in each box; use all caps only when it functions as a technical micro-label.
- Make each box visually distinct through the schematic, not through extra text.

Task impact:
- Use a horizontal sequence of rectangular task bricks.
- Fill only the impacted task or AI system node in `#E3F4FF`.
- Show replacement, acceleration, threshold lowering, or new tasks through arrows and dashed branches.

Value/control shift:
- Use currency/value nodes, worker nodes, system circles, and stepped value lines.
- Use dashed paths for knowledge/data transfer into a system.
- Use pale blue to show where value, control, or capability changes.
