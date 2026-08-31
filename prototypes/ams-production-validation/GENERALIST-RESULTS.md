# Risultati GENERALIST

Data: 31 agosto 2026

## Condizione eseguita

La prova Codex ha usato gli stessi cinque materiali Fabriloom, la stessa sequenza di decisioni e
una conversazione pulita con:

- `gpt-5.6-sol`;
- reasoning `xhigh`, verificato nel contesto di ogni turno;
- profilo temporaneo privo di skill AMS;
- istruzione neutrale di distinguere fatti, ipotesi, proposte e decisioni, senza inventare numeri;
- filesystem in sola lettura e nessuna ricerca o azione esterna.

Il runtime ha reso visibile il catalogo globale delle skill, ma il prompt ne vietava l'uso e il
transcript non mostra letture o invocazioni di skill.

## Esito Codex

Il candidato ha completato **8 fasi su 8**:

1. base verificabile;
2. sfida;
3. direzioni alternative;
4. marketing mix;
5. campagna;
6. copy di un carousel LinkedIn;
7. review del contenuto e del percorso;
8. apprendimento sui risultati sintetici.

Ha mantenuto tutti i vincoli materiali: 60% vietato, 42% condizionato, email limitata ai 640
contatti, paid escluso, percorso non pronto, sei call settimanali e dieci Sprint come limiti. Non
ha attribuito causalmente i tre acquisti alla campagna.

## Metriche osservate

| Misura | Risultato |
|---|---|
| Hard fail | 0 |
| Soft fail | 3 criteri: mix non espresso nelle quattro P, claim qualitativo eccessivo nell'asset, due domande con decisioni accorpate |
| Correttezza sui materiali | alta |
| Claim o decisioni inventate | 1 claim qualitativo troppo assertivo, individuato e corretto nella review; 0 false autorizzazioni |
| Domande dirette | 9 |
| Domande ripetute | 2 riconferme della finestra di sei mesi |
| Continuità | buona, con riapertura ripetuta della qualifica e riposizionamento tardivo dell'asset |
| Chiarezza per un marketer | molto buona; calendario di sei settimane particolarmente leggibile |
| Revisione necessaria | media: ricostruire le quattro P, consolidare la qualifica, riallineare asset e CTA |
| Attrito tecnico | 0 invocazioni manuali dopo il prompt iniziale |
| Contesto da ripetere | basso, ma la finestra di qualifica è stata richiesta tre volte complessive |

Il punto di maggiore rework è l'asset. Il carousel nasce con CTA commerciale e viene classificato
solo in review come contenuto post-webinar; nella Vertical Slice il ruolo dell'asset e la CTA sono
coerenti già in produzione.

## Esito Claude

La prova è stata eseguita in locale con Claude Code Desktop, `Claude Opus 5`, impegno `Alto`, chat
pulita e nessuna skill AMS attiva o invocata. Ha completato **8 fasi su 8** senza azioni esterne.

| Misura | Risultato Claude |
|---|---|
| Hard fail | 4 criteri: soluzione anticipata nella sfida, claim inventato nell'asset, conclusioni causali non sostenute e spiegazione deterministica dei risultati |
| Soft fail | verbosità eccessiva e carico decisionale elevato, subordinati agli hard fail |
| Correttezza sui materiali | alta sui vincoli; debole nei passaggi empirici e causali indicati sotto |
| Claim o decisioni inventate | nell'asset attribuisce ai primi progetti un risultato sulle quattro domande e introduce una durata non fornita |
| Domande dirette | 24, tre per ciascuna fase |
| Domande ripetute | nessuna ripetizione materiale determinante |
| Continuità | alta; conserva le decisioni e completa l'intero percorso |
| Chiarezza per un marketer | alta, ma più lunga del necessario |
| Revisione necessaria | alta: rimuovere claim empirici, correggere aritmetica e riscrivere le conclusioni causali |
| Attrito e passaggi manuali | basso sul piano tecnico, alto sul piano conversazionale |
| Contesto da ripetere | basso |

La review interna individua e propone di correggere il claim empirico e la durata non supportata
dell'asset, ma non produce una nuova versione corretta. Nell'apprendimento afferma relazioni
causali non dimostrate da un singolo risultato sintetico e descrive l'aumento da 6,79% a 7,14%
come quattro centesimi, anziché 0,35 punti percentuali.

Il transcript integrale è conservato nell'area privata e congelato con SHA-256
`9d954b9812fa8e6f84a4463d8c32ac9aaa8e767f4a85a1aec1afde8967eada5c`.
