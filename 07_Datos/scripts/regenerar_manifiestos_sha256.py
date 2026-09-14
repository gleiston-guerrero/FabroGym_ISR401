#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""Regenera y valida los manifiestos SHA-256 terminales de FabroGym.

Uso (desde la raíz del repositorio):
    python 07_Datos/scripts/regenerar_manifiestos_sha256.py

Genera, en este orden:
1) 07_Datos/checksums_datos.sha256
   - rutas relativas a 07_Datos, para que funcione exactamente:
       cd 07_Datos
       sha256sum -c checksums_datos.sha256
2) checksums.sha256
   - rutas relativas a la raíz del repositorio;
   - para punteros Git LFS usa el oid sha256 del objeto materializado.

El script termina con código != 0 si alguna validación interna falla.
"""
from __future__ import annotations

from pathlib import Path
import hashlib
import re
import subprocess
import sys

REPO = Path(__file__).resolve().parents[2]
DATA = REPO / "07_Datos"
DATA_MANIFEST = DATA / "checksums_datos.sha256"
ROOT_MANIFEST = REPO / "checksums.sha256"
LFS_OID = re.compile(rb"^oid sha256:([0-9a-f]{64})$", re.MULTILINE)
TRANSIENT_SUFFIXES = {".aux", ".log", ".out", ".toc", ".lof", ".lot", ".blg", ".bbl", ".pyc"}


def sha256_file(path: Path) -> str:
    h = hashlib.sha256()
    with path.open("rb") as f:
        for block in iter(lambda: f.read(1024 * 1024), b""):
            h.update(block)
    return h.hexdigest()


def digest_root(path: Path) -> str:
    """SHA-256 real o, si es puntero LFS, oid SHA-256 del objeto."""
    if path.stat().st_size <= 4096:
        raw = path.read_bytes()
        if raw.startswith(b"version https://git-lfs.github.com/spec/v1"):
            m = LFS_OID.search(raw)
            if not m:
                raise ValueError(f"Puntero Git LFS sin oid válido: {path}")
            return m.group(1).decode("ascii")
    return sha256_file(path)


def is_transient(rel: Path) -> bool:
    return (
        ".git" in rel.parts
        or "__pycache__" in rel.parts
        or rel.suffix.lower() in TRANSIENT_SUFFIXES
        or rel.name.endswith("~")
    )


def tracked_files_or_fallback() -> list[Path]:
    """Prefiere archivos versionados; en un ZIP usa todos los archivos no temporales."""
    if (REPO / ".git").exists():
        proc = subprocess.run(
            ["git", "-C", str(REPO), "ls-files", "-z"],
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
            check=True,
        )
        items = [x for x in proc.stdout.decode("utf-8").split("\0") if x]
        return sorted((REPO / x for x in items if (REPO / x).is_file()), key=lambda p: p.relative_to(REPO).as_posix())

    return sorted(
        (p for p in REPO.rglob("*") if p.is_file() and not is_transient(p.relative_to(REPO))),
        key=lambda p: p.relative_to(REPO).as_posix(),
    )


def write_data_manifest() -> int:
    files = sorted(
        (
            p for p in DATA.rglob("*")
            if p.is_file()
            and p != DATA_MANIFEST
            and not is_transient(p.relative_to(REPO))
        ),
        key=lambda p: p.relative_to(DATA).as_posix(),
    )
    lines = [f"{sha256_file(p)}  {p.relative_to(DATA).as_posix()}" for p in files]
    DATA_MANIFEST.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return len(files)


def write_root_manifest() -> int:
    files = [p for p in tracked_files_or_fallback() if p != ROOT_MANIFEST]
    # El manifiesto de 07_Datos debe existir ya y queda cubierto por el manifiesto raíz.
    if DATA_MANIFEST not in files and DATA_MANIFEST.exists():
        files.append(DATA_MANIFEST)
    files = sorted(set(files), key=lambda p: p.relative_to(REPO).as_posix())
    lines = [f"{digest_root(p)}  {p.relative_to(REPO).as_posix()}" for p in files]
    ROOT_MANIFEST.write_text("\n".join(lines) + "\n", encoding="utf-8", newline="\n")
    return len(files)


def parse_manifest(path: Path) -> list[tuple[str, str]]:
    rows: list[tuple[str, str]] = []
    for n, line in enumerate(path.read_text(encoding="utf-8").splitlines(), 1):
        if not line.strip():
            continue
        if "  " not in line:
            raise ValueError(f"Formato inválido en {path}:{n}")
        digest, rel = line.split("  ", 1)
        if not re.fullmatch(r"[0-9a-f]{64}", digest):
            raise ValueError(f"SHA-256 inválido en {path}:{n}")
        rows.append((digest, rel))
    return rows


def validate_data() -> tuple[int, int]:
    ok = bad = 0
    for expected, rel in parse_manifest(DATA_MANIFEST):
        p = DATA / rel
        actual = sha256_file(p) if p.is_file() else ""
        if actual == expected:
            ok += 1
        else:
            bad += 1
            print(f"FALLO-DATOS {rel}")
    return ok, bad


def validate_root() -> tuple[int, int]:
    ok = bad = 0
    for expected, rel in parse_manifest(ROOT_MANIFEST):
        p = REPO / rel
        actual = digest_root(p) if p.is_file() else ""
        if actual == expected:
            ok += 1
        else:
            bad += 1
            print(f"FALLO-RAIZ {rel}")
    return ok, bad


def main() -> int:
    n_data = write_data_manifest()
    n_root = write_root_manifest()
    ok_data, bad_data = validate_data()
    ok_root, bad_root = validate_root()

    print(f"07_Datos: manifiesto generado con {n_data} archivos; {ok_data} OK; {bad_data} fallos")
    print(f"Repositorio: manifiesto generado con {n_root} archivos; {ok_root} OK; {bad_root} fallos")
    if bad_data or bad_root:
        return 2
    print("OK — manifiestos SHA-256 terminales regenerados y validados")
    return 0


if __name__ == "__main__":
    sys.exit(main())
