# Revisione beta.11 — evidenze locali

Questa cartella conserva la fonte fornita dall’utente, le versioni locali d’ingresso e i loro hash, le misure della revisione, i controlli e le prove sintetiche. Il rapporto autorevole della sessione è [SUITE-REVIEW-BETA11.md](../../SUITE-REVIEW-BETA11.md).

Le note dei tre editor sono progressive e possono descrivere una versione intermedia. `metrics.json`, il rapporto finale e il manifest in `dist/beta.11` identificano la candidata finale.

`behavior/` contiene copie byte per byte dei prompt, risposte e file realmente prodotti nell’area temporanea autorizzata. I percorsi temporanei dentro quei testi sono conservati per fedeltà; i corrispondenti file sono disponibili anche qui. `behavior-manifest.json` ne registra gli hash.

Sono prove incrociate: ciascun caso finale è svolto da un editor che non ha modificato quella skill, nello stesso ambiente e con contesto precedente condiviso. Non sono blind, isolate a livello di runtime, prove con utenti reali o receipt di provenance host. I due casi `voice-response` e `mix-response` documentano candidati intermedi; i cinque casi finali sono copy A, content B, debrief, voice-conditions e mix-final.

I JSON `legacy-runner-*` mantengono separati il PASS delle otto verifiche statiche sulla baseline congelata e il rifiuto della candidata da parte dei controlli vincolati a hash/versioni beta.10. Non sono un nuovo BEHAVIOR_PASS della suite storica.
