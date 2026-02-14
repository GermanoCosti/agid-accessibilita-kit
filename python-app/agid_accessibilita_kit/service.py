from __future__ import annotations

import json
import pathlib
from dataclasses import dataclass

from agid_accessibilita_kit.templates import (
    render_checklist_md,
    render_dichiarazione_html,
    render_feedback_html,
    render_footer_snippet,
)
from agid_accessibilita_kit.export import export_docx, export_html_from_docx, export_pdf_from_docx


@dataclass(frozen=True)
class Config:
    ente: str
    sito: str
    email: str
    base_path: str
    out_dir: str


def write_project(cfg: Config) -> dict[str, str]:
    out_dir = pathlib.Path(cfg.out_dir).resolve()
    out_dir.mkdir(parents=True, exist_ok=True)

    files: dict[str, str] = {}
    p = out_dir / "dichiarazione-accessibilita.html"
    p.write_text(render_dichiarazione_html(cfg.ente, cfg.sito, cfg.email, cfg.base_path), encoding="utf-8")
    files["dichiarazione-accessibilita.html"] = str(p)

    p = out_dir / "feedback-accessibilita.html"
    p.write_text(render_feedback_html(cfg.ente, cfg.sito, cfg.email), encoding="utf-8")
    files["feedback-accessibilita.html"] = str(p)

    p = out_dir / "footer-snippet.html"
    p.write_text(render_footer_snippet(cfg.base_path), encoding="utf-8")
    files["footer-snippet.html"] = str(p)

    p = out_dir / "CHECKLIST.md"
    p.write_text(render_checklist_md(), encoding="utf-8")
    files["CHECKLIST.md"] = str(p)

    config_path = pathlib.Path("agid-accessibilita.config.json").resolve()
    config_path.write_text(
        json.dumps(
            {
                "ente": cfg.ente,
                "sito": cfg.sito,
                "email": cfg.email,
                "basePath": cfg.base_path,
                "outDir": str(out_dir),
            },
            indent=2,
            ensure_ascii=False,
        ),
        encoding="utf-8",
    )
    files["agid-accessibilita.config.json"] = str(config_path)

    # Output "ufficio": DOCX + export HTML/PDF (opzionali).
    # Nota: PDF richiede Microsoft Word se usi docx2pdf.
    docx_path = out_dir / "accessibilita-bozze.docx"
    files["accessibilita-bozze.docx"] = str(export_docx(
        {
            "ente": cfg.ente,
            "sito": cfg.sito,
            "email": cfg.email,
            "basePath": cfg.base_path,
        },
        str(docx_path),
    ))

    html_path = out_dir / "accessibilita-bozze.html"
    files["accessibilita-bozze.html"] = str(export_html_from_docx(str(docx_path), str(html_path)))

    # PDF: se fallisce, non bloccare la generazione.
    try:
        pdf_path = out_dir / "accessibilita-bozze.pdf"
        files["accessibilita-bozze.pdf"] = str(export_pdf_from_docx(str(docx_path), str(pdf_path)))
    except Exception as exc:  # noqa: BLE001
        files["accessibilita-bozze.pdf"] = f"NON CREATO: {exc}"
    return files
