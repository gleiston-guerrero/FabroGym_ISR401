#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Validadores de entrada para la cadena empírica de FabroGym.

Acepta la estructura terminal vigente y, cuando corresponde, la estructura
histórica conservada en 06_Experimento. El objetivo es fallar temprano ante
columnas incompatibles, IDs duplicados o valores fuera de dominio.
"""
from __future__ import annotations

import argparse
import csv
from pathlib import Path

CODIFICACION_CURRENT = [
    "ID_Registro", "Codigo_Sesion", "Perfil", "Fuente", "Fragmento",
    "Codigo_Normalizado", "Categoria", "Aplicable_Explicabilidad",
    "Dimension_Explicabilidad", "ID_Evidencia", "Estado_Analisis",
]
CODIFICACION_LEGACY = [
    "ID_Registro", "Codigo_Sesion", "Codigo_Participante", "Perfil",
    "Fuente_Evidencia", "Ubicacion_Evidencia", "Fragmento_Anonimizado",
    "Necesidad_Explicabilidad", "Dimension", "Candidato_RNF_Relacionado",
    "Observaciones",
]

RNF_CURRENT = [
    "ID_RNF", "Enunciado_RNF", "Metrica", "Umbral", "Metodo_Comprobacion",
    "Fuentes", "Resultado_Member_Checking", "Decision_Final",
    "Fecha_Member_Checking",
]
RNF_LEGACY = [
    "ID", "Enunciado_RNF", "Fuente", "Perfil", "Dimension",
    "Criterio_Aceptacion", "Observaciones",
]

MC_COLUMNS = [
    "Codigo_Participante", "Fecha", "ID", "Resultado",
    "Observaciones", "Ajuste_Propuesto",
]

PERFILES = {
    "T", "NT", "Tecnico", "Técnico", "No tecnico", "No técnico",
    "No_verificable", "No verificable", "",
}
APLICABILIDAD = {"Si", "Sí", "No", ""}
MC_RESULTADOS = {"Confirmado", "Ajustado", "No confirmado", ""}


def read_rows(path: Path):
    if not path.exists():
        raise FileNotFoundError(f"No existe el archivo: {path}")
    with path.open("r", encoding="utf-8-sig", newline="") as f:
        reader = csv.DictReader(f)
        return reader.fieldnames or [], list(reader)


def detect_schema(fields, current, legacy, label):
    s = set(fields)
    if set(current).issubset(s):
        return "terminal"
    if set(legacy).issubset(s):
        return "historico"
    missing_current = [c for c in current if c not in s]
    missing_legacy = [c for c in legacy if c not in s]
    raise ValueError(
        f"{label}: estructura no reconocida. "
        f"Faltan en esquema terminal: {', '.join(missing_current) or 'ninguna'}; "
        f"faltan en esquema histórico: {', '.join(missing_legacy) or 'ninguna'}."
    )


def require_nonempty(row, cols, path, rownum):
    empty = [c for c in cols if not (row.get(c) or "").strip()]
    if empty:
        raise ValueError(
            f"{path.name}: campos obligatorios vacíos en fila {rownum}: "
            + ", ".join(empty)
        )


def validar_codificacion(path: Path):
    fields, rows = read_rows(path)
    schema = detect_schema(fields, CODIFICACION_CURRENT, CODIFICACION_LEGACY, path.name)
    ids = set()

    for n, row in enumerate(rows, start=2):
        rid = (row.get("ID_Registro") or "").strip()
        if not rid:
            raise ValueError(f"{path.name}: ID_Registro vacío en fila {n}")
        if rid in ids:
            raise ValueError(f"{path.name}: ID_Registro duplicado {rid!r} en fila {n}")
        ids.add(rid)

        perfil = (row.get("Perfil") or "").strip()
        if perfil not in PERFILES:
            raise ValueError(f"{path.name}: perfil no reconocido {perfil!r} en fila {n}")

        sesion = (row.get("Codigo_Sesion") or "").strip()
        if not sesion.startswith("WALK-"):
            raise ValueError(
                f"{path.name}: Codigo_Sesion no corresponde a WALK en fila {n}: {sesion!r}"
            )

        if schema == "terminal":
            require_nonempty(
                row,
                ["Codigo_Sesion", "Perfil", "Fuente", "Fragmento",
                 "Codigo_Normalizado", "Categoria", "ID_Evidencia"],
                path, n,
            )
            aplic = (row.get("Aplicable_Explicabilidad") or "").strip()
            if aplic not in APLICABILIDAD:
                raise ValueError(
                    f"{path.name}: Aplicable_Explicabilidad no reconocido "
                    f"{aplic!r} en fila {n}"
                )
            if aplic in {"Si", "Sí"} and not (row.get("Dimension_Explicabilidad") or "").strip():
                raise ValueError(
                    f"{path.name}: fragmento marcado aplicable sin "
                    f"Dimension_Explicabilidad en fila {n}"
                )
        else:
            require_nonempty(row, ["Codigo_Sesion", "Perfil"], path, n)

    return rows


def validar_rnf(path: Path):
    fields, rows = read_rows(path)
    schema = detect_schema(fields, RNF_CURRENT, RNF_LEGACY, path.name)
    id_col = "ID_RNF" if schema == "terminal" else "ID"
    ids = set()

    for n, row in enumerate(rows, start=2):
        rid = (row.get(id_col) or "").strip()
        if not rid:
            raise ValueError(f"{path.name}: {id_col} vacío en fila {n}")
        if rid in ids:
            raise ValueError(f"{path.name}: ID duplicado {rid!r} en fila {n}")
        ids.add(rid)

        if schema == "terminal":
            require_nonempty(
                row,
                ["Enunciado_RNF", "Metrica", "Umbral", "Metodo_Comprobacion",
                 "Fuentes", "Resultado_Member_Checking", "Decision_Final",
                 "Fecha_Member_Checking"],
                path, n,
            )
        else:
            perfil = (row.get("Perfil") or "").strip()
            if perfil not in PERFILES:
                raise ValueError(f"{path.name}: perfil no reconocido {perfil!r} en fila {n}")

    return rows


def validar_member_checking(path: Path):
    fields, rows = read_rows(path)
    missing = [c for c in MC_COLUMNS if c not in fields]
    if missing:
        raise ValueError(
            f"{path.name}: faltan columnas de member checking: {', '.join(missing)}"
        )

    seen = set()
    for n, row in enumerate(rows, start=2):
        require_nonempty(row, ["Codigo_Participante", "Fecha", "ID", "Resultado"], path, n)
        result = (row.get("Resultado") or "").strip()
        if result not in MC_RESULTADOS:
            raise ValueError(
                f"{path.name}: resultado no reconocido {result!r} en fila {n}"
            )
        key = (
            (row.get("Codigo_Participante") or "").strip(),
            (row.get("ID") or "").strip(),
        )
        if key in seen:
            raise ValueError(
                f"{path.name}: decisión duplicada participante/RNF {key!r} en fila {n}"
            )
        seen.add(key)

    return rows


def main():
    p = argparse.ArgumentParser(description="Valida matrices del Enfoque 3 de FabroGym.")
    p.add_argument("--codificacion", type=Path)
    p.add_argument("--rnf", type=Path)
    p.add_argument("--member-checking", type=Path)
    a = p.parse_args()

    if not any([a.codificacion, a.rnf, a.member_checking]):
        p.error("Indique al menos un archivo.")

    rnf_ids = None
    if a.codificacion:
        print(f"Codificación válida: {len(validar_codificacion(a.codificacion))} filas.")
    if a.rnf:
        rows = validar_rnf(a.rnf)
        id_col = "ID_RNF" if "ID_RNF" in rows[0] else "ID"
        rnf_ids = {(r.get(id_col) or "").strip() for r in rows}
        print(f"Matriz RNF válida: {len(rows)} filas.")
    if a.member_checking:
        rows = validar_member_checking(a.member_checking)
        if rnf_ids is not None:
            mc_ids = {(r.get("ID") or "").strip() for r in rows}
            unknown = sorted(mc_ids - rnf_ids)
            if unknown:
                raise ValueError(
                    "Member checking referencia RNF no presentes en la matriz: "
                    + ", ".join(unknown)
                )
        print(f"Member checking válido: {len(rows)} filas.")


if __name__ == "__main__":
    main()
