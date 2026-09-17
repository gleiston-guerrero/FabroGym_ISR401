# FabroGym — Ingeniería de Requisitos (ISR-401)

Repositorio académico del proyecto **FabroGym**, desarrollado en la Universidad Técnica Estatal de Quevedo (UTEQ) para la Entrega 4 (2B / Defensa Final) de Ingeniería de Requisitos.

**Repositorio canónico de evaluación:** <https://github.com/gleiston-guerrero/FabroGym_ISR401>

> **Migración de propietario:** el repositorio fue transferido y la URL canónica vigente es la indicada arriba. Para un clon local existente, el remoto debe apuntar a esta dirección con `git remote set-url origin https://github.com/gleiston-guerrero/FabroGym_ISR401.git` y comprobarse posteriormente mediante `git remote -v`.

> **Líneas base de cierre:** `v2.0.0-final` a `v2.0.4-final` se conservan sin mover ni sobrescribir como etiquetas históricas. `v2.0.4-final` identifica la línea base evaluada en el informe del 17/09/2026 (`dc5a228`). Las correcciones posteriores se cerrarán con una nueva etiqueta anotada; por secuencia, corresponde `v2.0.5-final`, únicamente después de la verificación previa final y de regenerar/verificar ambos manifiestos SHA-256.

## Estado 2B

FabroGym documenta la ingeniería de requisitos de un sistema de gestión de gimnasio local. El componente empírico usa el **Enfoque 3: explicabilidad como Requisito No Funcional (RNF)** para estudiar necesidades de explicación asociadas a un **componente de recomendación de rutinas propuesto**. El recomendador/IA **no se presenta como implementado** en el MVP.

| Componente | Estado de cierre |
|---|---|
| ERS/SRS | `01_ERS/ERS_SRS_2B_v2.0.pdf` y fuente LaTeX |
| Trazabilidad | 25 RF, 23 RNF y 4 RD + 97 trazas históricas + 8 planes de verificación IA + 57 trazas de flujo de los 19 CU Must |
| MVP | cobertura C3 verificada: **16/19 RF Must (84,21 %)** |
| **Paquete de datos y análisis canónico** | **`07_Datos/` — ejecución oficial con `python scripts/run_all.py`** |
| Manuscrito | `07_Publicacion/manuscrito_final.pdf` + `.tex` |
| Zenodo | **PUBLICADO**, versión 2.0.0 — DOI `10.5281/zenodo.22237884` |
| OSF | **PUBLICADO** — DOI `10.17605/OSF.IO/62YSC` |
| Software Heritage | **SNAPSHOT ARCHIVADO** — `swh:1:snp:be5a4db361a11e5287ed1f925ed1b387cf73588e` |
| F-UJI / FAIR | **EJECUTADO** — **88 %**, FAIR **moderate**, F-UJI 4.0.0 / métrica 0.8 |

> **Regla de unicidad B1:** para la Entrega Final 2B existe un único paquete canónico ejecutable de datos y análisis: `07_Datos/`. Los archivos conservados en `06_Experimento/` documentan el protocolo, la procedencia y el desarrollo histórico del estudio; **no constituyen una segunda cadena canónica de ejecución**. Únicamente `06_Experimento/resultados/` se mantiene como espejo derivado byte-idéntico de `07_Datos/resultados/` para la verificación de cierre. Los artefactos de `07_Publicacion/` documentan la publicación/replicación histórica y tampoco sustituyen a `07_Datos/` para B1.

> **Nota de preservación:** Software Heritage muestra actualmente una revisión anterior del repositorio. Después del commit/tag final se debe ejecutar **Save again**.

## Evidencia FAIR y preservación

### F-UJI

El DOI `10.5281/zenodo.22237884` fue evaluado el 11 de septiembre de 2026:

- Resultado global: **88 %**
- FAIR level: **moderate**
- Findable: **7/7 — advanced**
- Accessible: **6/7 — moderate**
- Interoperable: **4/6 — moderate**
- Reusable: **6/6 — moderate**
- Evidencia: `fair_assessment.pdf`

### Software Heritage

- Snapshot SWHID: `swh:1:snp:be5a4db361a11e5287ed1f925ed1b387cf73588e`
- Revision archivada: `swh:1:rev:56ae64739c8dfcb93de77b9085afaf74b029e5fd`
- Directory SWHID: `swh:1:dir:864d5a537b9e2fa6931f7f2b3ad23a06275432fa`

## Equipo

### Autoría histórica y evidencia A2

FabroGym conserva la autoría histórica verificable de los cinco integrantes del proyecto. El informe del 17/09/2026 constató que, en la línea base evaluada `v2.0.4-final`, el trabajo posterior a la guía sobre los ítems de la rúbrica correspondía a **Mera Arias Erick Jhair** y **Ponce Rivera Mery Helenmey**.

| Integrante | Usuario Git | A2 vigente | Interpretación |
|---|---|---:|---|
| Erick Jhair Mera Arias | `Emeraxs` | 13 | Evidencia propia conservada |
| Mery Helenmey Ponce Rivera | `Mery-003` / `Mery` | 19 | Evidencia propia conservada |
| Alex José Mora Duarte | `amorad35` | 10 | Autoría histórica preservada |
| Alvia Villegas Erick Adalberto | `Erick-Alvia` | 3 | Evidencia histórica propia depositada personalmente el 17/09 |
| Vaca Romero David Octavio | `David-Bs1` | 3 | Evidencia histórica propia depositada personalmente el 17/09 |

Por instrucción directa del docente del 17/09/2026, Alvia y Vaca realizan y suben personalmente sus capturas. Los commits usados para depositarlas se clasifican como **depósito de evidencia histórica A2** y no como nuevos aportes técnicos a la fase de corrección.

La solicitud del 15/09/2026 sobre composición evaluada se conserva sin modificar como antecedente; la incorporación personal de A2 no se documenta como modificación de esa solicitud. Consulte `10_Autoria/EQUIPO_EXAMEN_FINAL.md` y `04_Trazabilidad/ACLARACION_ALCANCE_CAPTURAS_ALVIA_VACA_20260917.md`.

## Compilar el ERS/SRS

### Compilador

- `pdflatex` (distribución TeX Live o MiKTeX compatible con los paquetes utilizados por el documento).

### Archivo principal

- `01_ERS/ERS_SRS_2B_v2.0.tex`

### Dependencias versionadas

- `01_ERS/referencias.bib`
- `01_ERS/figuras_2B/`
- `01_ERS/modelado_final/`
- `03_Modelado/Diagramas_UML/` como ubicación canónica del modelado UML

### Directorio de ejecución

Desde la raíz del repositorio:

```bash
cd 01_ERS
```

### Orden exacta de compilación

Ejecutar tres veces:

```bash
pdflatex -interaction=nonstopmode -halt-on-error ERS_SRS_2B_v2.0.tex
pdflatex -interaction=nonstopmode -halt-on-error ERS_SRS_2B_v2.0.tex
pdflatex -interaction=nonstopmode -halt-on-error ERS_SRS_2B_v2.0.tex
```

### PDF esperado

- `01_ERS/ERS_SRS_2B_v2.0.pdf`

## Reproducir el análisis — cadena oficial B1

Desde la raíz del repositorio:

```bash
cd 07_Datos
python -m pip install -r scripts/requirements.txt
python scripts/run_all.py
```

Esta es la **única cadena canónica de reproducción para la Entrega 4 (2B)**. No se debe ejecutar `06_Experimento/scripts_analisis/run_all.py` como cadena oficial de B1. El pipeline declara `SEED = 401` y, dentro del repositorio completo, sincroniza al finalizar un espejo byte-idéntico en `06_Experimento/resultados/`.

## Relación con `06_Experimento/`

`06_Experimento/` conserva el protocolo, el prerregistro OSF, instrumentos, matrices y scripts históricos que documentan la procedencia del estudio. Se mantienen por trazabilidad y no-retroceso, pero la cadena consolidada y evaluable se encuentra únicamente en `07_Datos/`. La subcarpeta `06_Experimento/resultados/` es únicamente un espejo derivado de las salidas canónicas y debe mantener los mismos archivos y hashes que `07_Datos/resultados/`.

## Paquete FAIR

Zenodo 2.0.0: https://doi.org/10.5281/zenodo.22237884. La evaluación F-UJI real se conserva como `fair_assessment.pdf`. Consulte también `FAIR_CHECKLIST.md` y `CITATION.cff`.

## Licencias

- Código del MVP y scripts: **MIT**.
- Documentación y dataset anonimizado: **CC BY 4.0**.
- Evidencia identificable: sujeta a las reglas de la capa restringida/cifrada definidas en `08_Etica/`.

### Verificación integral de cierre

Antes de regenerar los manifiestos SHA-256 terminales debe incorporarse `10_Autoria/verificacion_previa.pdf`, firmada por **Mera Arias Erick Jhair** y **Ponce Rivera Mery Helenmey**, responsables del cierre posterior a la guía, sobre el corte de contenido congelado. Después de integrar esa verificación firmada, los manifiestos terminales se regeneran una sola vez y la nueva etiqueta anotada se crea únicamente sobre el último commit de integridad. `v2.0.4-final` permanece como línea base histórica del corte evaluado el 17/09/2026 y no se mueve ni se sobrescribe; por secuencia, el nuevo cierre corresponde a `v2.0.5-final`.

Los manifiestos terminales se regeneran únicamente después de cerrar todo el contenido versionado. Para el cierre final se usa el procedimiento manual con `sha256sum`, alineado con la guía de evaluación y sin depender de scripts auxiliares.

Desde `07_Datos`:

```bash
find . -path './checksums_datos.sha256' -prune -o -type f -print0 | sort -z | xargs -0 sha256sum > checksums_datos.sha256
sha256sum -c checksums_datos.sha256 --quiet
```

Desde la raíz del repositorio:

```bash
find . -path './.git' -prune -o -path './checksums.sha256' -prune -o -type f -print0 | sort -z | xargs -0 sha256sum > checksums.sha256
sha256sum -c checksums.sha256 --quiet
```

Para el paquete empírico canónico, la reproducción se comprueba además con:

```bash
cd 07_Datos
python scripts/run_all.py
sha256sum -c checksums_datos.sha256 --quiet
```

`07_Datos/checksums_datos.sha256` contiene rutas relativas a `07_Datos/`; por ello no duplica el prefijo `07_Datos/`. El manifiesto global calcula SHA-256 sobre los bytes físicamente presentes en la entrega. Si una exportación contiene un puntero Git LFS, `sha256sum` verifica el archivo de puntero tal como fue entregado; su `oid sha256` documenta por separado la identidad del objeto LFS no materializado. Cada manifiesto excluye únicamente su propio archivo para evitar una referencia hash circular.
