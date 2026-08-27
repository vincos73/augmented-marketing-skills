# Sorgente del bundle Claude

Questo perimetro contiene soltanto il manifesto Claude. Il pacchetto generato combina `.claude-plugin/plugin.json` con le cinque skill specialistiche canoniche in `skills/`; non duplica né modifica le loro istruzioni. È il bundle da caricare in Claude, non negli ambienti OpenAI/Codex.

Non include Augmented Marketing Assistant: è l'adattatore del pacchetto OpenAI/Codex e non è coerente con il namespace delle skill Claude.
