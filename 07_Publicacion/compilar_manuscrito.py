#!/usr/bin/env python3
"""Compilación reproducible del manuscrito final de FabroGym.

El fuente canónico `manuscrito_final.tex` conserva el encabezado destinado a
Springer Nature (`sn-jnl`). Para que la entrega académica pueda recompilarse
incluso cuando esa clase editorial externa no esté instalada, este script genera
transitoriamente una vista LaTeX estándar, sin alterar el contenido científico,
y produce `manuscrito_final.pdf`.

No modifica `manuscrito_final.tex`, no descarga dependencias y elimina todos los
archivos temporales al terminar.
"""
from __future__ import annotations

import os
import re
import shutil
import subprocess
import sys
from pathlib import Path

HERE = Path(__file__).resolve().parent
SRC = HERE / "manuscrito_final.tex"
OUT = HERE / "manuscrito_final.pdf"
TMP_STEM = "manuscrito_final_render_tmp"
TMP_TEX = HERE / f"{TMP_STEM}.tex"

# Fecha fija de construcción para que dos compilaciones equivalentes produzcan
# exactamente los mismos bytes PDF. 2026-09-14 00:00:00 UTC.
SOURCE_DATE_EPOCH = "1789344000"


def balanced_arg(text: str, command: str) -> str:
    """Devuelve el argumento {...} balanceado de un comando LaTeX."""
    pos = text.find(command)
    if pos < 0:
        raise RuntimeError(f"No se encontró {command} en {SRC.name}")
    brace = text.find("{", pos + len(command))
    if brace < 0:
        raise RuntimeError(f"{command} no tiene argumento entre llaves")
    depth = 0
    for i in range(brace, len(text)):
        ch = text[i]
        if ch == "{" and (i == 0 or text[i - 1] != "\\"):
            depth += 1
        elif ch == "}" and (i == 0 or text[i - 1] != "\\"):
            depth -= 1
            if depth == 0:
                return text[brace + 1 : i]
    raise RuntimeError(f"Argumento no balanceado en {command}")


def build_render_source(source: str) -> str:
    if r"\documentclass[pdflatex,sn-basic]{sn-jnl}" not in source:
        raise RuntimeError(
            "El encabezado esperado de manuscrito_final.tex cambió; "
            "revise el compilador antes de continuar."
        )

    title = balanced_arg(source, r"\title")
    abstract = balanced_arg(source, r"\abstract")
    keywords = balanced_arg(source, r"\keywords")

    rendered = source.replace(
        r"\documentclass[pdflatex,sn-basic]{sn-jnl}",
        r"""\documentclass[10pt,a4paper]{article}
\pdfinfoomitdate=1
\pdftrailerid{}
\pdfsuppressptexinfo=15
\usepackage[T1]{fontenc}
\usepackage[utf8]{inputenc}
\usepackage{natbib}
\usepackage[a4paper,top=26mm,bottom=26mm,left=38mm,right=38mm]{geometry}
\usepackage{setspace}
\setstretch{1.0}
\setlength{\parindent}{1em}
\setlength{\parskip}{0pt}""",
        1,
    )

    front_start = rendered.find(r"\title[")
    intro_start = rendered.find(r"\section{Introduction}")
    if front_start < 0 or intro_start < 0 or intro_start <= front_start:
        raise RuntimeError("No se pudo delimitar el bloque de portada del manuscrito")

    front = rf"""\title{{{title}}}
\author{{Erick Adalberto Alvia Villegas\\
Erick Jhair Mera Arias\\
Alex Jos{{\'e}} Mora Duarte\\
Mery Helenmey Ponce Rivera\\
David Octavio Vaca Romero\\[0.7em]
\small Facultad de Ciencias de la Computaci{{\'o}}n, Universidad T{{\'e}}cnica Estatal de Quevedo\\
\small Quevedo, Los R{{\'i}}os, Ecuador}}
\date{{}}
\maketitle

\begin{{abstract}}
{abstract}
\end{{abstract}}

\noindent\textbf{{Keywords:}} {keywords.replace(',', ';')}

\vspace{{1em}}
"""
    rendered = rendered[:front_start] + front + rendered[intro_start:]

    if r"\bibliographystyle{" not in rendered:
        rendered = rendered.replace(
            r"\bibliography{referencias}",
            "\\bibliographystyle{plainnat}\n\\bibliography{referencias}",
            1,
        )
    return rendered


def run(cmd: list[str], log_name: str) -> None:
    log = HERE / log_name
    with log.open("w", encoding="utf-8", errors="replace") as fh:
        env = os.environ.copy()
        env["SOURCE_DATE_EPOCH"] = SOURCE_DATE_EPOCH
        env["FORCE_SOURCE_DATE"] = "1"
        proc = subprocess.run(
            cmd, cwd=HERE, stdout=fh, stderr=subprocess.STDOUT, env=env
        )
    if proc.returncode != 0:
        tail = log.read_text(encoding="utf-8", errors="replace")[-6000:]
        raise RuntimeError(f"Falló {' '.join(cmd)}\n--- log ---\n{tail}")


def cleanup() -> None:
    for ext in ("tex", "aux", "log", "out", "toc", "lof", "lot", "bbl", "blg", "pdf"):
        p = HERE / f"{TMP_STEM}.{ext}"
        if p.exists():
            p.unlink()
    for name in ("compile1_tmp.txt", "compile2_tmp.txt", "compile3_tmp.txt", "bibtex_tmp.txt"):
        p = HERE / name
        if p.exists():
            p.unlink()


def main() -> int:
    cleanup()
    try:
        source = SRC.read_text(encoding="utf-8")
        TMP_TEX.write_text(build_render_source(source), encoding="utf-8")

        pdflatex = shutil.which("pdflatex")
        bibtex = shutil.which("bibtex") or shutil.which("bibtex8") or shutil.which("bibtexu")
        if not pdflatex:
            raise RuntimeError("No se encontró pdflatex en PATH")
        if not bibtex:
            raise RuntimeError("No se encontró bibtex/bibtex8/bibtexu en PATH")

        run([pdflatex, "-interaction=nonstopmode", "-halt-on-error", TMP_TEX.name], "compile1_tmp.txt")
        run([bibtex, TMP_STEM], "bibtex_tmp.txt")
        run([pdflatex, "-interaction=nonstopmode", "-halt-on-error", TMP_TEX.name], "compile2_tmp.txt")
        run([pdflatex, "-interaction=nonstopmode", "-halt-on-error", TMP_TEX.name], "compile3_tmp.txt")

        final_log = (HERE / "compile3_tmp.txt").read_text(encoding="utf-8", errors="replace")
        bad = re.findall(
            r"(?:undefined references|undefined citations|Citation .* undefined|Reference .* undefined)",
            final_log,
            flags=re.IGNORECASE,
        )
        if bad:
            raise RuntimeError("La compilación terminó con referencias/citas indefinidas")

        tmp_pdf = HERE / f"{TMP_STEM}.pdf"
        if not tmp_pdf.exists() or tmp_pdf.stat().st_size < 10000:
            raise RuntimeError("No se produjo un PDF válido")
        tmp_pdf.replace(OUT)
        print(f"OK: {OUT.relative_to(HERE)} generado correctamente")
        return 0
    finally:
        # OUT ya fue movido fuera del nombre temporal, por lo que no se elimina.
        cleanup()


if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except Exception as exc:
        print(f"ERROR: {exc}", file=sys.stderr)
        raise SystemExit(1)
