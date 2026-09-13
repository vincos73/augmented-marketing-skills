# Sorgente del bundle Claude

Questo perimetro contiene il manifesto Claude. Il pacchetto generato combina `.claude-plugin/plugin.json` con le dodici skill canoniche in `skills/`: Augmented Marketing Assistant v0.3.0 e undici specialistiche. Non duplica né modifica le loro istruzioni.

Nella Suite 1.0.0 l’Assistant è il punto di ingresso conversazionale anche per Claude. È una skill di orientamento nella conversazione corrente: in Claude Code usa `Skill` con `augmented-marketing-suite:<nome-skill>`; negli altri ambienti legge il `SKILL.md` pertinente. Se l’utente nomina già una skill, questa viene usata direttamente senza passare dall’Assistant.

Il bundle non include `agents/openai.yaml`, directory di agenti, subagenti, MCP o hook. Il pacchetto OpenAI/Codex conserva invece i suoi metadati di interfaccia. L’archivio locale è [`dist/1.0.0/claude/augmented-marketing-suite-claude-v1.0.0.zip`](../dist/1.0.0/claude/augmented-marketing-suite-claude-v1.0.0.zip); il plugin è disponibile anche dal [marketplace GitHub](https://github.com/vincos73/augmented-marketing-skills).

Le verifiche locali e i limiti dei due test conversazionali Claude non verificati per autenticazione mancante sono nel [rapporto Suite 1.0.0](../evals/suite-1.0.0/README.md).
