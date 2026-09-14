#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from __future__ import annotations

import argparse
import csv
from collections import Counter
from pathlib import Path

from validar_entradas import validar_codificacion


def norm_profile(v):
    v = (v or "").strip().lower()
    if v in {"t", "tecnico", "técnico"}:
        return "Técnico"
    if v in {"nt", "no tecnico", "no técnico"}:
        return "No técnico"
    if not v or v in {"no_verificable", "no verificable"}:
        return "No verificable"
    return v


def write_counter(path, header1, counter):
    with path.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow([header1, "Conteo"])
        for key, count in sorted(counter.items(), key=lambda x: str(x[0])):
            w.writerow([key, count])


def procesar(entrada: Path, salida: Path):
    rows = validar_codificacion(entrada)
    salida.mkdir(parents=True, exist_ok=True)
    if not rows:
        print("La matriz de codificación no contiene datos. No se generan resultados empíricos.")
        return

    terminal = "Aplicable_Explicabilidad" in rows[0]
    applicability_col = "Aplicable_Explicabilidad" if terminal else "Necesidad_Explicabilidad"
    dimension_col = "Dimension_Explicabilidad" if terminal else "Dimension"

    perfiles = Counter()
    aplicabilidad = Counter()
    dimensiones = Counter()
    perfil_dimension = Counter()
    processed = []

    for r in rows:
        perfil = norm_profile(r.get("Perfil"))
        aplic = (r.get(applicability_col) or "").strip()
        dim_raw = (r.get(dimension_col) or "").strip()

        perfiles[perfil] += 1
        if aplic:
            aplicabilidad[aplic] += 1

        dims = [d.strip() for d in dim_raw.split("/") if d.strip()] if dim_raw else []
        for dim in dims:
            dimensiones[dim] += 1
            perfil_dimension[(perfil, dim)] += 1

        rr = dict(r)
        rr["Perfil_Normalizado"] = perfil
        processed.append(rr)

    fields = list(rows[0].keys())
    if "Perfil_Normalizado" not in fields:
        fields.append("Perfil_Normalizado")

    with (salida / "codificacion_walkthroughs_procesada.csv").open(
        "w", encoding="utf-8-sig", newline=""
    ) as f:
        w = csv.DictWriter(f, fieldnames=fields, lineterminator="\n")
        w.writeheader()
        w.writerows(processed)

    # Se conservan los nombres históricos de salida para compatibilidad.
    write_counter(salida / "resumen_necesidades.csv", applicability_col, aplicabilidad)
    write_counter(salida / "resumen_dimensiones.csv", dimension_col, dimensiones)

    with (salida / "resumen_necesidades_por_perfil.csv").open(
        "w", encoding="utf-8-sig", newline=""
    ) as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["Perfil", "Unidades_Codificadas"])
        for k, v in sorted(perfiles.items()):
            w.writerow([k, v])

    with (salida / "resumen_perfil_dimension.csv").open(
        "w", encoding="utf-8-sig", newline=""
    ) as f:
        w = csv.writer(f, lineterminator="\n")
        w.writerow(["Perfil", "Dimension", "Conteo"])
        for (perfil, dim), v in sorted(perfil_dimension.items()):
            w.writerow([perfil, dim, v])

    print(f"Unidades codificadas procesadas: {len(rows)}")
    print(
        f"Esquema: {'terminal' if terminal else 'histórico'}; "
        f"dimensiones observadas: {sum(dimensiones.values())}"
    )


def main():
    p = argparse.ArgumentParser(
        description="Resume la codificación de walkthroughs de FabroGym."
    )
    p.add_argument("--entrada", required=True, type=Path)
    p.add_argument("--salida", required=True, type=Path)
    a = p.parse_args()
    procesar(a.entrada, a.salida)


if __name__ == "__main__":
    main()
