# Augmented Marketing Suite v1.0.0

Augmented Marketing Suite 1.0.0 è la prima uscita stabile del prodotto. La Suite raccoglie skill installabili per rendere più chiari, verificabili e approvabili i passaggi delle decisioni di marketing.

## Assistant disponibile anche in Claude

Augmented Marketing Assistant v0.3.0 è incluso come normale skill in entrambi i plugin, Claude e OpenAI/Codex. Orienta l'utente verso una delle undici skill specialistiche quando il bisogno non è ancora definito. Una skill nominata direttamente viene usata senza passare dall'Assistant. Il bundle Claude non introduce agenti o subagenti.

## Contenuto

- Plugin Claude 1.0.0: dodici skill, Assistant compreso.
- Plugin OpenAI/Codex 1.0.0: dodici skill, Assistant compreso.
- `dist/1.0.0/agent-skills/`: undici ZIP portabili, uno per ciascuna skill specialistica.
- Le versioni delle undici skill specialistiche restano invariate rispetto alla distribuzione precedente.

La distribuzione complessiva comprende quindi dodici skill per ciascun plugin e undici archivi singoli specialistici.

## Verifica della build

Il controllo riproducibile della distribuzione è:

```sh
python3 scripts/build_suite.py --check
```

La build/check ha dato esito PASS; la suite di regressione del builder ha dato PASS con 11 test. Le verifiche coprono sorgenti, pacchetti, inventario, 13 archivi complessivi, manifest e `SHA256SUMS`. La distribuzione comprende due plugin completi da 12 skill e 11 ZIP specialistici; la validazione strict del bundle Claude e del marketplace locale ha dato PASS.

## Limiti dichiarati

- Due test conversazionali Claude non sono verificati perché l'autenticazione mancava; il rapporto eval non attribuisce loro un esito comportamentale.
- La presenza nei pacchetti non dimostra il caricamento in ogni sessione o runtime.
- Questa release non costituisce un pilot con marketer reali e non aggiunge nuove prove di efficacia.

## Asset della release

- `dist/1.0.0/claude/augmented-marketing-suite-claude-v1.0.0.zip`
- `dist/1.0.0/openai/augmented-marketing-suite-1.0.0.zip`
- `dist/1.0.0/agent-skills/` con gli undici ZIP singoli
- `dist/1.0.0/SHA256SUMS`
- `dist/1.0.0/manifest.json`

Pagina release: [augmented-marketing-suite-v1.0.0](https://github.com/vincos73/augmented-marketing-skills/releases/tag/augmented-marketing-suite-v1.0.0). Stato e dettagli delle verifiche: [`RELEASE-STATUS.md`](https://github.com/vincos73/augmented-marketing-skills/blob/main/RELEASE-STATUS.md) e [`evals/suite-1.0.0/README.md`](https://github.com/vincos73/augmented-marketing-skills/blob/main/evals/suite-1.0.0/README.md).
