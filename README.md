# AGID Accessibilita Kit (bozze)

Generatore di **bozze** per:
- pagina "Dichiarazione di accessibilita"
- pagina "Feedback accessibilita" (segnalazioni)
- snippet footer pronto da incollare
- checklist operativa

Obiettivo: aiutare PMI/agenzie a partire in modo rapido e ordinato. Non sostituisce obblighi e procedure ufficiali (ne' consulenza legale).

## Installazione (npm)
```bash
npm i -g @germanocosti/agid-accessibilita-kit
agid-accessibilita-kit --help
```

Oppure (npx, senza installare):
```bash
npx -y @germanocosti/agid-accessibilita-kit --help
```

## Uso rapido
Genera i file in una cartella `./accessibilita/`:
```bash
agid-accessibilita-kit init
```

Puoi anche indicare una cartella diversa:
```bash
agid-accessibilita-kit init --out-dir .\\public\\accessibilita
```

## Output generati
- `dichiarazione-accessibilita.html`
- `feedback-accessibilita.html`
- `footer-snippet.html`
- `CHECKLIST.md`
- `agid-accessibilita.config.json` (config salvata)

## Versione Python (GUI)
Se vuoi una interfaccia grafica:
```powershell
cd python-app
python -m pip install -e .
agid-accessibilita-gui
```

## Supporto / Donazioni
Se ti e' utile:
- `docs/sostieni-il-progetto.md`

## Licenza
MIT
