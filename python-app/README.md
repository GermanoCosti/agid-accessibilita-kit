# AGID Accessibilita Kit (Python)

Questa cartella contiene la versione Python con:
- CLI
- Interfaccia grafica (Tkinter)

## Installazione (locale, sviluppo)
```powershell
cd python-app
python -m pip install -e .
```

## Uso CLI
```powershell
agid-accessibilita-kit-py init --out-dir .\\accessibilita
```

## Uso GUI
```powershell
agid-accessibilita-gui
```

## Build EXE (Windows)
```powershell
python -m pip install -r requirements-dev.txt
python -m PyInstaller --onefile --windowed --name agid-accessibilita-gui .\\agid_accessibilita_kit\\gui.py
```

