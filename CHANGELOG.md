# Changelog

## 2026-09-15 - Cierre documental §15: alcance A1/A5 e inventario EXIF completo

- Se separa explícitamente el alcance de A1 y A5: `10_Autoria/bitacora_sesiones.csv` contiene **28 sesiones internas de trabajo del equipo**, mientras las notas de campo se contrastan únicamente contra las **16 sesiones empíricas** de `07_Datos/datos_crudos/sesiones_multimedia_desde_ficha_v3_1.csv` (10 entrevistas + 3 WALK-TEC + 3 WALK-NTEC).
- Se incorpora `10_Autoria/notas_campo/inventario_notas_campo.csv` y su README de trazabilidad. El corte contiene **13 notas contemporáneas asociables a 13/16 sesiones empíricas**: 10/10 entrevistas y 3/3 walkthroughs técnicos; no están depositadas notas para `WALK-NTEC-01`, `WALK-NTEC-02` y `WALK-NTEC-03`.
- Se documentan, sin alterar la evidencia, dos discrepancias históricas en las notas técnicas: un archivo cuyo nombre indica `WALK-TEC-03` pero cuyo manuscrito identifica `WALK-TEC-01`, y la fecha manuscrita de `WALK-TEC-02` frente a la fecha del inventario multimedia canónico.
- `10_Autoria/exif_inventario.csv` se amplía de 11 a **25 fotografías reales**: 2 de equipo, 18 de entorno y 5 de aplicación del cuestionario. Se registran 20 con fecha de captura recuperable, 2 `EXIF_PARCIAL` y 5 `SIN_EXIF`, sin inventar metadatos.
- Se documenta la discrepancia entre las **26 fotografías** mencionadas por la guía y las **25 físicamente presentes** en el árbol actual: la guía presupone 3 fotos de equipo y el repositorio verificable contiene 2.
- Se mantiene como equipo actual de cierre a Mera, Mora y Ponce; los aportes históricos de Alvia y Vaca se conservan sin fabricar capturas nuevas.
- Se restituye en la documentación la exigencia de la guía vigente de producir `10_Autoria/verificacion_previa.pdf` **firmada** sobre el corte final. Ese PDF se genera al final de §15, antes de los manifiestos terminales y de `v2.0.3-final`, para que no certifique un estado intermedio.

## 2026-09-15 - Cierre §12 del examen suspenso: determinismo y carpeta canónica de resultados

- Se explicita `SEED = 401` en `07_Datos/scripts/run_all.py` y se utiliza esa constante en el bootstrap pseudoaleatorio del cuestionario.
- Se mantiene `07_Datos/resultados/` como única fuente canónica de resultados; `06_Experimento/resultados/` pasa a ser un espejo derivado byte-idéntico sincronizado por el orquestador oficial.
- Se documenta la regla de espejo en `README.md`, `07_Datos/README_datos.md` y `06_Experimento/README.md`.
- Se reejecuta dos veces la cadena canónica y se comprueba identidad SHA-256 de `datos_procesados/` y `resultados/` entre ejecuciones equivalentes.
- Los manifiestos terminales `07_Datos/checksums_datos.sha256` y `checksums.sha256` **no se regeneran todavía**; se reservan para el penúltimo paso, después de cerrar §15 y §16.

## 2026-09-15 - Cierre §4 del examen suspenso: especificación textual de casos de uso

- Se especifican textualmente los **19 casos de uso Must** del ERS con actor principal, disparador, precondiciones, flujo principal numerado, flujo alternativo con condición, excepción con condición y poscondiciones.
- Cada caso de uso conserva su vínculo vigente con RF, HU, CA, evidencia, componente y mockups; la corrección refina comportamiento existente y **no crea requisitos nuevos**.
- Se incorpora la convención de identificadores `CU-xx-FP`, `CU-xx-FA-01` y `CU-xx-EX-01`.
- `04_Trazabilidad/matriz_trazabilidad.csv` añade las columnas `ID_Flujo` y `Descripcion_Flujo` y 57 trazas explícitas de flujo, manteniendo las 105 trazas previas; el total queda en **162 filas**.
- Se recompila `01_ERS/ERS_SRS_2B_v2.0.pdf` desde la fuente actualizada y se verifica que el texto contiene al menos una ocurrencia de flujo principal, flujo alternativo, excepción, precondiciones y poscondiciones por cada uno de los 19 CU.
- Los manifiestos SHA-256 terminales permanecen pendientes y deberán regenerarse únicamente después de completar los demás puntos del examen suspenso.

## 2026-09-15 - Consolidación final PRE-CHECKSUMS (etiqueta terminal declarada `v2.0.3-final`)

- Se conserva `v2.0.2-final` sin mover ni sobrescribir como línea base histórica ya publicada.
- Se delimita el **equipo actual de cierre y examen final** a Mera, Mora y Ponce, conservando sin alterar la autoría histórica de Alvia y Vaca en los artefactos donde participaron.
- A2 documenta únicamente evidencia real del equipo actual de cierre: Mera 13, Mora 10 y Ponce 19; no se fabrican, reasignan ni retrofechan capturas.
- Se incorpora el inventario EXIF completo de 11 registros reales: 2 fotografías de equipo, 4 JPG de entorno y 5 fotografías de aplicación del cuestionario.
- Se reconcilia el conteo real de **16 consentimientos específicos de sesión** (10 ENTR + 3 WALK-TEC + 3 WALK-NTEC) frente a la mención de 17 en la guía; la diferencia se documenta como discrepancia de conteo, no como archivo faltante.
- Se añade un espejo byte-idéntico en `08_Etica/consentimientos/` para que funcione la ruta literal de verificación de la guía; la ubicación canónica continúa siendo `02_Evidencias/Consentimientos/` y los archivos no se cuentan dos veces.
- El manuscrito y la retrospectiva distinguen la autoría histórica del proyecto del equipo actual de cierre (Mera, Mora y Ponce), y declaran `v2.0.3-final` como la etiqueta terminal del cierre, creada únicamente después de verificar los manifiestos finales.
- Se conservan los resultados empíricos ya versionados y se corrigen únicamente los artefactos/documentación identificados por la auditoría de cierre; no se fuerza una regeneración masiva en este lote mínimo.
- Se deja documentado que el cierre de integridad se realizará con comandos manuales `sha256sum`, conforme a la guía de evaluación, sin modificar los scripts auxiliares existentes.
- **Los dos manifiestos terminales exigidos por §12 (`/checksums.sha256` y `07_Datos/checksums_datos.sha256`) no se regeneran en este lote de contenido.** Deben regenerarse una sola vez, al final absoluto, después de cualquier evidencia auténtica adicional y antes del siguiente tag.
- Se sincronizan las rutas de fotografías de equipo, se eliminan referencias a una verificación histórica inexistente, se estabiliza el corte documental de autoría y se cierra la redacción de Docker/Zenodo sin declarar tareas futuras no acreditadas.
- Se actualizan los manifiestos locales de defensa y del paquete académico `dataset_zenodo` para que describan exactamente los archivos actuales; estos no sustituyen a los dos manifiestos terminales exigidos por §12.

## 2026-09-14 — Corrección posterior a auditoría PRE-TAG (`v2.0.2-final`)

- Se completó `10_Autoria/exif_inventario.csv` con los 4 JPG de `02_Evidencias/Fotos_Entorno/`; el inventario queda en 11 registros reales (2 equipo + 4 entorno + 5 aplicación del cuestionario).
- Se sincronizaron `10_Autoria/README.md` y `10_Autoria/aporte_individual.md` con la URL canónica `gleiston-guerrero/FabroGym_ISR401`.
- Se corrigió la documentación A2 para reflejar las 13 capturas reales de `Emeraxs`, manteniendo 19 de `Mery` y 10 de `amorad35`.
- Se sincronizó `10_Autoria/EQUIPO_EXAMEN_FINAL.md` con la declaración detallada de composición vigente del equipo de examen.
- Se integró el paquete PRETAG consolidado sobre el snapshot `b6c9c99`, incluyendo la URL canónica `gleiston-guerrero/FabroGym_ISR401`, la retrospectiva del examen suspenso, el manuscrito con efecto por sesión (`n=3+3`) y el procedimiento reproducible de compilación.
- Se eliminó del mirror `01_ERS/modelado_final/04_Secuencia/` el conjunto obsoleto de 19 diagramas con identificadores internos antiguos (`RF-AUT-*`, `RF-CLI-*`, etc.); el mirror queda alineado con los 54 PNG canónicos de `03_Modelado/Diagramas_UML/`.
- Se corrigió el inventario A2 de Mera/Emeraxs de 12 a 13 capturas reales, sin fabricar evidencia ni modificar la atribución histórica de otros integrantes.
- Se aclaró que `v2.0.1-final` es una línea base histórica ya publicada y que la nueva etiqueta terminal debe ser `v2.0.2-final`, creada únicamente después de verificaciones y manifiestos finales.
- Los metadatos `ZENODO_METADATA_DRAFT.*` se conservaron únicamente como historial y se marcaron explícitamente como superados por el depósito Zenodo 2.0.0 ya publicado.
- Después de estas correcciones se deben ejecutar `run_all.py`, recompilar ERS/manuscrito, regenerar los manifiestos SHA-256 y verificar cero fallos antes de etiquetar.


## 2026-09-14 — Auditoría final de scripts y reproducibilidad

- Se actualizan `validar_entradas.py`, `analizar_walkthroughs.py` y `analizar_rnf.py` al esquema terminal real de `07_Datos`, manteniendo compatibilidad con la estructura histórica cuando corresponde.
- `run_all.py` valida de forma temprana las 76 filas de codificación, 4 candidatos RNF y 12 decisiones de member checking antes de regenerar resultados.
- Se comprueba que `run_all.py` reproduce F3-04 sin modificar ningún producto respecto del estado esperado: `n_unidades=6`, delta de Cliff `0.555556`, IC95% `[-0.333333, 1.000000]` e `interpretable=NO`.
- Se endurece `compilar_manuscrito.py` para generar `manuscrito_final.pdf` de forma byte-reproducible mediante fecha de construcción fija y supresión de metadatos variables.
- Se regenera la auditoría automática de privacidad sobre el árbol terminal y se confirma 0 hallazgos bloqueantes.
- Tras estas correcciones se regeneran nuevamente los manifiestos SHA-256 terminales.

## 2026-09-14 — Cierre §12: manifiestos SHA-256 terminales

- Se corrige `07_Datos/checksums_datos.sha256` para utilizar rutas relativas al propio paquete y permitir `sha256sum -c checksums_datos.sha256` desde `07_Datos/`.
- Se incorpora `07_Datos/scripts/regenerar_manifiestos_sha256.py` como procedimiento reproducible para regenerar primero el manifiesto de datos y después el manifiesto global.
- Se regenera `checksums.sha256` sobre el estado terminal previo al tag usando SHA-256 de los bytes físicamente presentes, de forma que `sha256sum -c checksums.sha256 --quiet` verifica también los punteros Git LFS incluidos en una exportación ZIP.
- Se documentan los comandos exactos de regeneración y verificación y se exige 0 fallos antes de crear el tag final.

## [2B-v2.0-correccion-url] - 2026-09-14

### Identificación del entregable y URL canónica (§1)

- Se actualizó la URL del repositorio en la carátula de la ERS/SRS a `https://github.com/gleiston-guerrero/FabroGym_ISR401`.
- Se actualizaron los campos `repository-code` y `url` de `CITATION.cff` para identificar el repositorio canónico vigente, manteniendo los DOI de Zenodo y OSF en sus campos específicos.
- El `README.md` raíz declara explícitamente el repositorio canónico y el comando para reapuntar/verificar el remoto local.
- Se sincronizaron las referencias activas al repositorio en `FAIR_CHECKLIST.md`, `10_Autoria/README.md` y `10_Autoria/aporte_individual.md`.
- Se normalizaron también las referencias locales al repositorio dentro de metadatos de publicación y del protocolo para evitar enlaces obsoletos tras la transferencia de propietario; el depósito Zenodo ya publicado no se modifica externamente.


Todos los cambios relevantes del proyecto FabroGym se documentan aquí siguiendo la estructura de Keep a Changelog.


## [2B-v2.0-cierre-informe] - 2026-09-14

### Informe y retrospectiva (§16)
- Se incorporó al `manuscrito_final.tex` la explicación explícita de la corrección de los consentimientos ENTR-02, ENTR-03, ENTR-04 y ENTR-06.
- Se consolidó la tabla de efecto por sesiones de §13 con `n_unidades=6` e `interpretable=NO` para inferencia poblacional.
- Se mantuvo explícita en amenazas a la validez la no aplicabilidad de la encuesta `n=70` al contraste técnico/no técnico de explicabilidad.
- Se añadió la sección `Retrospectiva del examen suspenso / Failed-exam correction retrospective` con hallazgo, corrección, evidencia y responsabilidad documentada.
- Se declaró en el informe el repositorio canónico `gleiston-guerrero/FabroGym_ISR401` y el identificador terminal de cierre `v2.0.2-final`.
- Se añadió `07_Publicacion/RETROSPECTIVA_EXAMEN_SUSPENSO.md` como apoyo auditable y se actualizó `07_Publicacion/README_Publicacion.md`.
- Se recompiló `07_Publicacion/manuscrito_final.pdf` desde la fuente canónica.

## [2B-v2.0-correccion-final] - 2026-09-14

### Corregido — B1 / integridad
- Se regeneró la cadena reproducible de `07_Datos/` y se verificaron sus checksums internos.
- Se normalizaron las referencias de archivos renombrados y se regeneró el manifiesto global de integridad sobre el estado final del repositorio.
- La comprobación automática de integridad queda preparada para terminar con cero fallos sobre el paquete entregado.

### Corregido — B2 / autoría
- Se sincronizaron los nombres reales de las fotografías del equipo en el inventario EXIF, README e informe de selección.
- La doble codificación A7 queda redactada como actividad ya revisada y confirmada por Mora y Ponce, conservando el subconjunto congelado de 16 fragmentos.

### Corregido — B5 / supervisión humana
- `RNF-17` explicita quién revisa la recomendación, las acciones aceptar/modificar/rechazar y el registro auditable de responsable, fecha y versión antes de asignar la rutina.
- Se sincronizó la especificación con el catálogo, el plan de verificación y la cobertura de los seis requisitos del componente inteligente.

### Corregido — B6 / consentimientos
- Los consentimientos censurados `ENTR-02`, `ENTR-03`, `ENTR-04` y `ENTR-06` se sustituyeron por copias rasterizadas de las mismas páginas, eliminando el origen Word y la capa de texto extraíble sin alterar el contenido visual.

### Corregido — §13 / tamaño del efecto y validez estadística
- Se corrigió la unidad independiente del contraste técnico/no técnico: las 18 categorías temáticas dejan de tratarse como observaciones independientes y el análisis utiliza las **6 sesiones WALK** (3 técnicas + 3 no técnicas).
- `tabla_efecto_perfiles.csv` incorpora explícitamente `n_unidades` e `interpretable`, con `n_unidades=6` e `interpretable=NO` para inferencia poblacional.
- La medida principal es delta de Cliff sobre la proporción de fragmentos pertinentes a explicabilidad por sesión: `delta=0.555556`, IC95% bootstrap exacto `[-0.333333, 1.000000]`.
- El contraste por conteo bruto (`delta=0.777778`) se conserva únicamente como análisis de sensibilidad descriptivo por la diferente cantidad de fragmentos codificados entre sesiones.
- Se documenta que el cuestionario de 70 respuestas no contiene perfil técnico/no técnico ni una escala de explicabilidad y, por tanto, no sustenta comparaciones inferenciales entre perfiles.
- Se sincronizaron el resumen reproducible, la ERS/SRS y el manuscrito fuente con el alcance descriptivo-exploratorio corregido.

## [2B-v2.0-cierre-canonico] - 2026-09-12

### Corregido — A5
- Se eliminaron del paquete local las copias divergentes `ERS_SRS_2B_v2.2.pdf` y `ERS_SRS_2B_v2.2.tex`.
- La única ERS/SRS académica vigente queda en `01_ERS/ERS_SRS_2B_v2.0.*`.
- `07_Publicacion/dataset_zenodo/srs/README.md` funciona únicamente como referencia documental hacia la ERS/SRS canónica.

### Consolidado — B1
- Se declara `07_Datos/` como **único paquete canónico, ejecutable y evaluable** de datos y análisis para la Entrega 4 (2B).
- El orquestador oficial es `07_Datos/scripts/run_all.py`.
- Las dependencias oficiales están en `07_Datos/scripts/requirements.txt`.
- Se actualiza `README.md` para eliminar la referencia de ejecución oficial a `06_Experimento/scripts_analisis/run_all.py`.
- `06_Experimento/` y `06_Experimento/scripts_analisis/` se conservan exclusivamente como procedencia/historial metodológico y no como segunda cadena canónica.
- `07_Publicacion/` queda identificado como paquete de publicación/replicación histórica y no sustituye a `07_Datos/`.

### Integridad
- No se modifican los datos crudos, CSV analíticos, tablas, figuras ni valores de resultados para esta normalización documental.
- No se elimina la evidencia histórica necesaria para trazabilidad.

## [2B-v2.0-cierre-fair-swh] - 2026-09-11

### Añadido
- Evaluación F-UJI real sobre el DOI Zenodo `10.5281/zenodo.22237884`.
- Evidencia `fair_assessment.pdf`.
- Snapshot verificable en Software Heritage: `swh:1:snp:be5a4db361a11e5287ed1f925ed1b387cf73588e`.
- Actualización de `README.md`, `FAIR_CHECKLIST.md` y `CITATION.cff` con identificadores y resultados reales.

### Verificado
- F-UJI 4.0.0 / métrica 0.8: **88 %**, FAIR **moderate**.
- Findable 7/7 (advanced), Accessible 6/7 (moderate), Interoperable 4/6 (moderate), Reusable 6/6 (moderate).

### Advertencia de preservación
- El SWHID existente conserva un estado anterior del repositorio.
- Se debe ejecutar **Save again** después del commit/tag final.

## [2B-v2.0-uml-secuencia-saneado] - 2026-09-05

### Cambiado
- Se sustituyeron los 19 diagramas de secuencia por exportaciones saneadas desde Visual Paradigm y se sincronizó la ERS/SRS v2.0.

## [2B-v2.0-normalizacion-ids] - 2026-09-04

### Cambiado
- Se consolidó `01_ERS/ERS_SRS_2B_v2.0.*` como única ERS/SRS vigente.
- Se normalizaron 25 RF, 23 RNF y 4 RD; se sincronizaron catálogo, matriz y modelado.
- Zenodo quedó publicado como versión 2.0.0 con DOI `10.5281/zenodo.22237884`.

## [2B-v2.0-predeposit] - 2026-09-01

### Añadido
- ERS/SRS 2B v2.0, análisis reproducible, resultados finales, RNF de explicabilidad, manuscrito y paquete de datos.

## [2B-preOSF-v1.4] - 2026-08-28

### Cambiado
- Prerregistro OSF v1.4 y aclaración de la cronología de walkthroughs.

## [2B-preOSF-v1.3] - 2026-08-28

### Añadido
- Instrumentos de explicabilidad y scripts reproducibles iniciales.

## [2A-v1.0] - 2026-07-29

### Añadido
- Estructura pública de ERS, evidencias, modelado, trazabilidad, MVP, experimento y publicación.

## [1B-v2.0] - 2026-06-27

### Añadido
- RF/RNF formalizados, mockups, UML, MoSCoW y trazabilidad parcial.

## [1A-v1.0] - 2026-05-31

### Añadido
- Planificación, stakeholders, elicitación inicial y primeras evidencias de campo.