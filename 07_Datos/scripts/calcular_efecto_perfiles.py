#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
FabroGym — F3-04 CORREGIDO
Tamaño del efecto técnico vs. no técnico con la sesión de walkthrough
como unidad independiente de análisis.

Corrección metodológica posterior a la evaluación final del 14-09-2026:
- NO se tratan las 18 categorías temáticas como 18 observaciones independientes.
- La unidad es cada sesión WALK: 3 técnicas y 3 no técnicas.
- El constructo comparado es la proporción, por sesión, de fragmentos codificados
  como pertinentes para explicabilidad.
- Se usa delta de Cliff para dos grupos independientes.
- El IC95% se obtiene mediante bootstrap exacto de sesiones (todas las muestras
  ordenadas con reemplazo de tamaño n dentro de cada perfil; 27 x 27 = 729
  combinaciones cuando n=3 por perfil).
- Se conserva un análisis secundario sobre el conteo de fragmentos pertinentes
  por sesión, solo como sensibilidad descriptiva.
- No se genera p-valor ni se afirma diferencia poblacional.
"""

from pathlib import Path
import argparse
import csv
import itertools
import math
import unicodedata


def norm_text(value):
    s = "" if value is None else str(value).strip().lower()
    s = "".join(c for c in unicodedata.normalize("NFD", s) if unicodedata.category(c) != "Mn")
    return " ".join(s.split())


def profile_group(value):
    s = norm_text(value)
    if s in {"tecnico", "tecnica", "technical"}:
        return "Tecnico"
    if s in {"no tecnico", "no tecnica", "no-tecnico", "no-tecnica", "non technical", "non-technical"}:
        return "No tecnico"
    raise ValueError(f"Perfil no reconocido: {value!r}")


def is_yes(value):
    return norm_text(value) in {"si", "yes", "true", "1"}


def cliffs_delta(x, y):
    """Delta de Cliff para dos grupos independientes; empates aportan 0."""
    if not x or not y:
        raise ValueError("Se requieren observaciones en ambos grupos.")
    wins = sum(a > b for a in x for b in y)
    losses = sum(a < b for a in x for b in y)
    return (wins - losses) / (len(x) * len(y))


def percentile(sorted_values, p):
    pos = (len(sorted_values) - 1) * p
    lo = math.floor(pos)
    hi = math.ceil(pos)
    if lo == hi:
        return sorted_values[lo]
    frac = pos - lo
    return sorted_values[lo] * (1 - frac) + sorted_values[hi] * frac


def exact_bootstrap_ci(x, y, alpha=0.05):
    """
    Bootstrap exacto por sesión para muestras pequeñas.
    Enumera todas las muestras ordenadas con reemplazo del mismo tamaño que
    cada grupo. Para n=3 y n=3 son 729 combinaciones, sin semilla aleatoria.
    """
    vals = []
    for ix in itertools.product(range(len(x)), repeat=len(x)):
        xb = [x[i] for i in ix]
        for iy in itertools.product(range(len(y)), repeat=len(y)):
            yb = [y[i] for i in iy]
            vals.append(cliffs_delta(xb, yb))
    vals.sort()
    return (
        percentile(vals, alpha / 2),
        percentile(vals, 1 - alpha / 2),
        len(vals),
    )


def read_sessions(path):
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        rows = list(csv.DictReader(f))
    required = {"Codigo_Sesion", "Perfil", "Aplicable_Explicabilidad"}
    if not rows:
        raise SystemExit("F3-04: codificacion_walkthroughs.csv está vacío.")
    missing = required.difference(rows[0].keys())
    if missing:
        raise SystemExit(f"F3-04: faltan columnas requeridas: {sorted(missing)}")

    sessions = {}
    for row in rows:
        sid = str(row["Codigo_Sesion"]).strip()
        if not sid.startswith("WALK-"):
            continue
        grp = profile_group(row["Perfil"])
        rec = sessions.setdefault(sid, {
            "Codigo_Sesion": sid,
            "Perfil": grp,
            "fragmentos_totales": 0,
            "fragmentos_explicabilidad": 0,
        })
        if rec["Perfil"] != grp:
            raise SystemExit(f"F3-04: perfil inconsistente dentro de {sid}.")
        rec["fragmentos_totales"] += 1
        rec["fragmentos_explicabilidad"] += int(is_yes(row["Aplicable_Explicabilidad"]))

    for rec in sessions.values():
        total = rec["fragmentos_totales"]
        rec["proporcion_explicabilidad"] = rec["fragmentos_explicabilidad"] / total if total else 0.0

    return [sessions[k] for k in sorted(sessions)]


def summarize_metric(name, tech, nontech, field, unit):
    x = [float(r[field]) for r in tech]
    y = [float(r[field]) for r in nontech]
    delta = cliffs_delta(x, y)
    lo, hi, reps = exact_bootstrap_ci(x, y)
    return {
        "comparacion": name,
        "unidad_analisis": "Sesion de walkthrough independiente",
        "n_tecnico": len(x),
        "n_no_tecnico": len(y),
        "metrica": field,
        "unidad_metrica": unit,
        "medida_efecto": "Delta de Cliff",
        "efecto_delta": f"{delta:.6f}",
        "IC95_bootstrap_exacto_inf": f"{lo:.6f}",
        "IC95_bootstrap_exacto_sup": f"{hi:.6f}",
        "combinaciones_bootstrap": reps,
        "media_tecnico": f"{sum(x)/len(x):.6f}",
        "media_no_tecnico": f"{sum(y)/len(y):.6f}",
        "diferencia_medias_Tec_menos_NoTec": f"{(sum(x)/len(x))-(sum(y)/len(y)):.6f}",
        "interpretacion": "Delta positivo = valores mayores en sesiones tecnicas; resultado descriptivo-exploratorio.",
    }


def main():
    root = Path(__file__).resolve().parents[1]
    ap = argparse.ArgumentParser()
    ap.add_argument("--entrada", default=str(root / "datos_crudos" / "codificacion_walkthroughs.csv"))
    ap.add_argument("--salida", default=str(root / "resultados" / "tablas" / "tabla_efecto_perfiles.csv"))
    ap.add_argument("--detalle", default=str(root / "resultados" / "tablas" / "tabla_efecto_perfiles_detalle.csv"))
    ap.add_argument("--resumen-md", default=str(root / "resultados" / "F3-04_TAMANIO_EFECTO.md"))
    args = ap.parse_args()

    sessions = read_sessions(Path(args.entrada))
    tech = [r for r in sessions if r["Perfil"] == "Tecnico"]
    nontech = [r for r in sessions if r["Perfil"] == "No tecnico"]

    if len(tech) != 3 or len(nontech) != 3:
        raise SystemExit(
            f"F3-04: se esperaban 3 sesiones técnicas y 3 no técnicas; "
            f"se encontraron {len(tech)} y {len(nontech)}."
        )

    summary = [
        summarize_metric(
            "Proporcion de fragmentos pertinentes a explicabilidad por sesion",
            tech, nontech, "proporcion_explicabilidad", "proporcion"
        ),
        summarize_metric(
            "Conteo de fragmentos pertinentes a explicabilidad por sesion",
            tech, nontech, "fragmentos_explicabilidad", "fragmentos"
        ),
    ]

    out = Path(args.salida)
    detail = Path(args.detalle)
    md = Path(args.resumen_md)
    out.parent.mkdir(parents=True, exist_ok=True)
    detail.parent.mkdir(parents=True, exist_ok=True)
    md.parent.mkdir(parents=True, exist_ok=True)

    with out.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(summary[0].keys()), lineterminator="\n")
        w.writeheader()
        w.writerows(summary)

    detail_rows = []
    for r in sessions:
        detail_rows.append({
            "Codigo_Sesion": r["Codigo_Sesion"],
            "Perfil": r["Perfil"],
            "fragmentos_totales": r["fragmentos_totales"],
            "fragmentos_explicabilidad": r["fragmentos_explicabilidad"],
            "proporcion_explicabilidad": f"{r['proporcion_explicabilidad']:.6f}",
            "unidad_independiente": "SI",
        })
    with detail.open("w", encoding="utf-8-sig", newline="") as f:
        w = csv.DictWriter(f, fieldnames=list(detail_rows[0].keys()), lineterminator="\n")
        w.writeheader()
        w.writerows(detail_rows)

    primary, secondary = summary
    tech_rows = ", ".join(
        f"{r['Codigo_Sesion']}={r['fragmentos_explicabilidad']}/{r['fragmentos_totales']} ({r['proporcion_explicabilidad']:.3f})"
        for r in tech
    )
    non_rows = ", ".join(
        f"{r['Codigo_Sesion']}={r['fragmentos_explicabilidad']}/{r['fragmentos_totales']} ({r['proporcion_explicabilidad']:.3f})"
        for r in nontech
    )

    md.write_text(f"""# F3-04 — Tamaño del efecto técnico vs no técnico (CORREGIDO)

## Corrección de unidad de análisis

La unidad independiente es la **sesión de walkthrough**, no la categoría temática. El corpus contiene tres sesiones técnicas y tres no técnicas. Las 18 categorías siguen siendo categorías descriptivas del corpus, pero **no se usan como 18 observaciones independientes**.

## Fuente

`datos_crudos/codificacion_walkthroughs.csv`

El script agrega los fragmentos por `Codigo_Sesion` y calcula, para cada sesión, la proporción de fragmentos marcados `Aplicable_Explicabilidad = Si`.

## Datos por sesión

- Técnicas: {tech_rows}
- No técnicas: {non_rows}

## Medida principal

Se utiliza **delta de Cliff** para dos grupos independientes sobre la **proporción de fragmentos pertinentes a explicabilidad por sesión**.

- `n técnico = {primary['n_tecnico']}` sesiones.
- `n no técnico = {primary['n_no_tecnico']}` sesiones.
- `delta = {primary['efecto_delta']}`.
- IC95% bootstrap exacto por remuestreo de sesiones: `[{primary['IC95_bootstrap_exacto_inf']}, {primary['IC95_bootstrap_exacto_sup']}]`.
- Media técnica = `{primary['media_tecnico']}`.
- Media no técnica = `{primary['media_no_tecnico']}`.

El intervalo es amplio porque solo existen tres sesiones por perfil; esta amplitud se reporta como limitación y no se maquilla.

## Análisis secundario de sensibilidad

Sobre el conteo bruto de fragmentos pertinentes por sesión:

- `delta = {secondary['efecto_delta']}`.
- IC95% bootstrap exacto: `[{secondary['IC95_bootstrap_exacto_inf']}, {secondary['IC95_bootstrap_exacto_sup']}]`.

Este análisis secundario no sustituye a la medida principal porque el número total de fragmentos codificados difiere entre sesiones.

## Alcance metodológico

El resultado es **descriptivo-exploratorio**. No se genera p-valor ni se afirma una diferencia poblacional. El cuestionario de 70 respuestas **no se usa para esta comparación**, porque no registra perfil técnico/no técnico ni contiene una escala de explicabilidad.

## Reproducibilidad

Desde `07_Datos/`:

```bash
python scripts/calcular_efecto_perfiles.py
```

Desde `06_Experimento/` (espejo histórico):

```bash
python scripts_analisis/calcular_efecto_perfiles.py
```
""", encoding="utf-8")

    print("OK F3-04 corregido: unidad = sesion WALK")
    print(f"Sesiones: tecnico={len(tech)}, no_tecnico={len(nontech)}")
    print(
        f"Principal: delta={primary['efecto_delta']}, "
        f"IC95=[{primary['IC95_bootstrap_exacto_inf']}, {primary['IC95_bootstrap_exacto_sup']}]"
    )
    print(f"Tabla: {out}")
    print(f"Detalle: {detail}")
    print(f"Resumen: {md}")


if __name__ == "__main__":
    main()
