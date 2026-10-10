# Augmented Marketing Suite 1.0.2 — pacchetto OpenAI

Questo è il pacchetto esatto caricato nel portale OpenAI l'8 ottobre 2026. Contiene 12 skill in inglese, due manifest, il listing inglese con traduzione italiana e due PNG del logo approvato. Il caricamento ha superato i controlli automatici del portale ed è in review; non risulta ancora pubblicato nel catalogo ChatGPT.

- [ZIP installabile](augmented-marketing-suite-public-1.0.2.zip)
- [Sorgente completo](source/)
- [SHA256SUMS](SHA256SUMS)
- [Stato della release](../../../RELEASE-STATUS-1.0.2.md)

Lo SHA-256 dello ZIP è `8e68e50f92a8aca57786cbf27cf7e3281672a224607d095232fe4d3f75c07da5`. Lo ZIP comprende 58 file: 56 file testuali e due PNG. Le skill italiane in `skills/`, il plugin Claude e gli ZIP portabili restano alla versione 1.0.0.

Per verificare l'archivio dalla radice del repository:

```sh
shasum -a 256 -c releases/1.0.2/openai/SHA256SUMS
python3 scripts/verify_openai_1_0_2.py
```
