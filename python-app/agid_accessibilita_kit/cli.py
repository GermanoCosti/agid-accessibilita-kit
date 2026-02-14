from __future__ import annotations

import argparse
import sys

try:
    from agid_accessibilita_kit.service import Config, write_project
except ModuleNotFoundError:
    # Permette esecuzione anche come file diretto: `python agid_accessibilita_kit/cli.py ...`
    import pathlib

    ROOT = pathlib.Path(__file__).resolve().parents[1]
    if str(ROOT) not in sys.path:
        sys.path.insert(0, str(ROOT))
    from agid_accessibilita_kit.service import Config, write_project


def main() -> int:
    parser = argparse.ArgumentParser(prog="agid-accessibilita-kit-py", description="Generatore bozze accessibilita (AGID).")
    sub = parser.add_subparsers(dest="cmd", required=True)

    init = sub.add_parser("init", help="Genera pagine + snippet + checklist")
    init.add_argument("--out-dir", default="accessibilita", help="Cartella output")
    init.add_argument("--ente", default="Nome organizzazione", help="Nome organizzazione")
    init.add_argument("--sito", default="https://www.esempio.it", help="URL sito (https://...)")
    init.add_argument("--email", default="accessibilita@esempio.it", help="Email accessibilita")
    init.add_argument("--base-path", default="/accessibilita", help="Percorso pubblico (es. /accessibilita)")

    args = parser.parse_args()

    if args.cmd != "init":
        parser.print_help()
        return 1

    try:
        files = write_project(
            Config(
                ente=args.ente,
                sito=args.sito,
                email=args.email,
                base_path=args.base_path,
                out_dir=args.out_dir,
            )
        )
    except Exception as exc:  # noqa: BLE001
        print(f"Errore: {exc}", file=sys.stderr)
        return 1

    print("OK. File generati:")
    for k, v in files.items():
        print(f"- {k}: {v}")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
