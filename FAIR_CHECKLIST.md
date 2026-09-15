# FAIR_CHECKLIST — FabroGym 2B

**Proyecto:** FabroGym — ISR-401  
**Estado documental:** cierre PRE-CHECKSUM posterior a `v2.0.2-final`; esa etiqueta ya publicada se conserva intacta como línea base histórica  
**Repositorio:** `https://github.com/gleiston-guerrero/FabroGym_ISR401`

Este archivo documenta el estado FAIR y de preservación verificable posterior a la etiqueta ya publicada `v2.0.2-final`. El identificador terminal declarado para esta entrega es `v2.0.3-final`; se crea únicamente después de cerrar contenido y verificar los manifiestos SHA-256 finales. No se mueve ni se sobrescribe ninguna etiqueta existente.

## Estado actual

| Área | Comprobación | Evidencia | Estado |
|---|---|---|---|
| Findable | Identificador persistente del paquete | Zenodo v2.0.0 — DOI `10.5281/zenodo.22237884` | **VERIFICADO** |
| Findable | Registro del protocolo | OSF — DOI `10.17605/OSF.IO/62YSC` | **VERIFICADO** |
| Findable | Título, descripción, autores y palabras clave | Zenodo + `CITATION.cff` | **VERIFICADO** |
| Findable | Citación legible por máquina | `CITATION.cff` | **DISPONIBLE** |
| Accessible | Paquete público | Zenodo / GitHub | **DISPONIBLE** |
| Accessible | Separación público/restringido | `08_Etica/` + auditor de privacidad | **VERIFICADA** |
| Accessible | Auditoría de privacidad | `07_Datos/resultados/REVISION_PRIVACIDAD_PUBLICA.md` | **0 BLOQUEOS / B6 MANUAL CERRADO** |
| Interoperable | Formatos abiertos/estructurados | CSV, JSON, TXT, MD, SVG | **DISPONIBLE** |
| Interoperable | Identificadores estables | ENTR, WALK, MC, RF, RNF y RD | **DISPONIBLE** |
| Interoperable | Diccionario de datos | `07_Datos/diccionario_datos.csv` | **DISPONIBLE** |
| Reusable | Licencias | CC BY 4.0 datos/documentación; MIT código | **DISPONIBLE** |
| Reusable | Proveniencia | `07_Datos/datos_crudos/PROVENIENCIA_FUENTES.md` + OSF | **DISPONIBLE** |
| Reusable | Reproducibilidad | `07_Datos/scripts/run_all.py` + `requirements.txt` | **VERIFICADA** |
| Reusable | Versionado | Git + `CHANGELOG.md` + Zenodo 2.0.0 | **DISPONIBLE** |
| Reusable | Evaluación FAIR externa | `fair_assessment.pdf` | **88 % — FAIR moderate** |
| Preservación | Software Heritage | Snapshot real previo al tag final | **VERIFICADO; la preservación definitiva se asocia al tag final publicado** |

## F-UJI

**Recurso evaluado:** *Replication package for Explainability Requirements for Fitness Routine Recommendations: A Field Case Study in Ecuador*  
**PID:** `10.5281/zenodo.22237884`  
**Fecha de evaluación:** 2026-09-11  
**F-UJI:** 4.0.0  
**Versión de métrica:** 0.8  
**Resultado global:** **88 % — FAIR level: moderate**

| Dimensión | Puntaje | Nivel |
|---|---:|---|
| Findable | 7/7 | advanced |
| Accessible | 6/7 | moderate |
| Interoperable | 4/6 | moderate |
| Reusable | 6/6 | moderate |

La evidencia se conserva como `fair_assessment.pdf`.

## Software Heritage

Snapshot archivado actualmente:

```text
swh:1:snp:be5a4db361a11e5287ed1f925ed1b387cf73588e
```

Revision archivada:

```text
swh:1:rev:56ae64739c8dfcb93de77b9085afaf74b029e5fd
```

Directory SWHID:

```text
swh:1:dir:864d5a537b9e2fa6931f7f2b3ad23a06275432fa
```

Este snapshot es real y verificable. Corresponde al estado anterior al tag final; después de publicar el tag de entrega se ejecutará **Software Heritage → Save again** para preservar el estado congelado. Esta operación corresponde a preservación posterior al tag y no altera el contenido académico congelado.

## Reproducibilidad canónica B1

La cadena canónica del cierre es:

```bash
cd 07_Datos
python -m pip install -r scripts/requirements.txt
python scripts/run_all.py
```

`06_Experimento/` se conserva como procedencia/historial metodológico y no sustituye a `07_Datos/`.

## Privacidad

El reporte `07_Datos/resultados/REVISION_PRIVACIDAD_PUBLICA.md` documenta:

- **0 hallazgos automáticos bloqueantes**;
- capa restringida documentada;
- 5 fotografías A6 con EXIF técnicamente válido;
- límites de verificación manual documentados sin hallazgos automáticos bloqueantes;
- ausencia de claves expuestas detectables en las rutas públicas inspeccionadas.

## Estado de cierre FAIR

Evidencias disponibles antes del tag:

- [x] Zenodo v2.0.0 con DOI real.
- [x] OSF con DOI real.
- [x] `fair_assessment.pdf`.
- [x] F-UJI ejecutado: 88 %.
- [x] SWHID real archivado.
- [x] `07_Datos/` declarado como paquete canónico.
- [x] Auditoría automática de privacidad con 0 bloqueos.
- [x] Control B6 documentado con 0 hallazgos automáticos bloqueantes y límites de inspección explícitos.
- [x] README raíz y `CHANGELOG.md` normalizados para A5/B1.

La comprobación desde clon limpio y la verificación de checksums
se ejecutan sobre el commit final inmediatamente antes del tag
final y quedan documentadas en la verificación de cierre.

Procedimiento de congelamiento/post-tag:

El commit final de entrega se congela mediante un **tag anotado publicado en GitHub**; una vez visible el tag remoto, se solicita **Software Heritage → Save again** sobre ese estado. Estas acciones pertenecen al proceso de publicación posterior a la integración del presente corte y no representan contenido académico incompleto dentro del repositorio.

> No se debe realizar un nuevo commit únicamente para perseguir un SWHID posterior: primero se congela con el tag y luego se solicita la nueva preservación.
