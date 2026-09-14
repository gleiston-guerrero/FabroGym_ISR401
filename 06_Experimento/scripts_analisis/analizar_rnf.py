#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path

from validar_entradas import validar_rnf


def norm_profile(v):
    v = (v or "").strip().lower()
    if v in {"t", "tecnico", "técnico"}:
        return "Técnico"
    if v in {"nt", "no tecnico", "no técnico"}:
        return "No técnico"
    if not v or v in {"no_verificable", "no verificable"}:
        return "No verificable"
    return v


def procesar(entrada: Path, salida: Path, total_dimensiones: int | None = None):
    rows = validar_rnf(entrada)
    salida.mkdir(parents=True, exist_ok=True)
    if not rows:
        print("La matriz de candidatos RNF no contiene datos. No se generan resultados empíricos.")
        return

    terminal = "ID_RNF" in rows[0]
    id_col = "ID_RNF" if terminal else "ID"

    if terminal:
        complete_cols = [
            "Enunciado_RNF", "Metrica", "Umbral",
            "Metodo_Comprobacion", "Fuentes",
        ]
    else:
        complete_cols = ["Enunciado_RNF", "Fuente", "Criterio_Aceptacion"]

    verificables = [
        r for r in rows if all((r.get(c) or "").strip() for c in complete_cols)
    ]

    with (salida / "resumen_candidatos_rnf.csv").open(
        "w", encoding="utf-8-sig", newline=""
    ) as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["Metrica", "Valor"])
        w.writerow(["Candidatos_registrados", len(rows)])
        w.writerow(["Candidatos_operacionalizados", len(verificables)])
        w.writerow(["Esquema_fuente", "terminal" if terminal else "historico"])

    if terminal:
        decisions = Counter((r.get("Decision_Final") or "").strip() for r in rows)
        states = Counter((r.get("Estado") or "").strip() for r in rows)

        with (salida / "candidatos_por_perfil.csv").open(
            "w", encoding="utf-8-sig", newline=""
        ) as f:
            w = csv.writer(f, lineterminator="\n")
            w.writerow(["Perfil", "Conteo", "Estado"])
            w.writerow([
                "NO_REGISTRADO_EN_FUENTE_TERMINAL", "",
                "NO CALCULABLE sin inventar perfil por candidato",
            ])

        with (salida / "candidatos_por_dimension.csv").open(
            "w", encoding="utf-8-sig", newline=""
        ) as f:
            w = csv.writer(f, lineterminator="\n")
            w.writerow(["Dimension", "Conteo", "Estado"])
            w.writerow([
                "NO_REGISTRADA_COMO_CAMPO_NORMALIZADO", "",
                "NO CALCULABLE sin inventar dimensión por candidato",
            ])

        with (salida / "cobertura_dimensiones.csv").open(
            "w", encoding="utf-8-sig", newline=""
        ) as f:
            w = csv.writer(f, lineterminator="\n")
            w.writerow(["Metrica", "Valor", "Estado"])
            w.writerow([
                "Proporcion_cobertura", "",
                "No calculable: la fuente terminal no define un universo cerrado de dimensiones por candidato",
            ])

        with (salida / "candidatos_por_decision.csv").open(
            "w", encoding="utf-8-sig", newline=""
        ) as f:
            w = csv.writer(f, lineterminator="\n")
            w.writerow(["Decision_Final", "Conteo"])
            for k, v in sorted(decisions.items()):
                w.writerow([k, v])

        with (salida / "candidatos_por_estado.csv").open(
            "w", encoding="utf-8-sig", newline=""
        ) as f:
            w = csv.writer(f, lineterminator="\n")
            w.writerow(["Estado", "Conteo"])
            for k, v in sorted(states.items()):
                w.writerow([k, v])

    else:
        perfil = Counter()
        dim = Counter()
        for r in rows:
            perfil[norm_profile(r.get("Perfil"))] += 1
            d = (r.get("Dimension") or "").strip()
            if d:
                dim[d] += 1

        with (salida / "candidatos_por_perfil.csv").open(
            "w", encoding="utf-8-sig", newline=""
        ) as f:
            w = csv.writer(f, lineterminator="\n")
            w.writerow(["Perfil", "Conteo"])
            for k, v in sorted(perfil.items()):
                w.writerow([k, v])

        with (salida / "candidatos_por_dimension.csv").open(
            "w", encoding="utf-8-sig", newline=""
        ) as f:
            w = csv.writer(f, lineterminator="\n")
            w.writerow(["Dimension", "Conteo"])
            for k, v in sorted(dim.items()):
                w.writerow([k, v])

        with (salida / "cobertura_dimensiones.csv").open(
            "w", encoding="utf-8-sig", newline=""
        ) as f:
            w = csv.writer(f, lineterminator="\n")
            w.writerow(["Metrica", "Valor", "Estado"])
            covered = len({
                (r.get("Dimension") or "").strip()
                for r in verificables
                if (r.get("Dimension") or "").strip()
            })
            if total_dimensiones and total_dimensiones > 0:
                w.writerow(["Dimensiones_cubiertas", covered, "Calculable"])
                w.writerow(["Total_dimensiones_evaluadas", total_dimensiones, "Calculable"])
                w.writerow(["Proporcion_cobertura", covered / total_dimensiones, "Calculable"])
            else:
                w.writerow(["Dimensiones_cubiertas", covered, "Descriptivo"])
                w.writerow([
                    "Proporcion_cobertura", "",
                    "No calculable: no se proporcionó un denominador verificable",
                ])

    print(f"Candidatos RNF procesados: {len(rows)}")
    print(f"Esquema: {'terminal' if terminal else 'histórico'}; IDs válidos: {id_col}")


def main():
    p = argparse.ArgumentParser(description="Resume candidatos RNF de explicabilidad.")
    p.add_argument("--entrada", required=True, type=Path)
    p.add_argument("--salida", required=True, type=Path)
    p.add_argument(
        "--total-dimensiones", type=int, default=None,
        help="Denominador verificable; omitir si no está establecido.",
    )
    a = p.parse_args()
    procesar(a.entrada, a.salida, a.total_dimensiones)


if __name__ == "__main__":
    main()
