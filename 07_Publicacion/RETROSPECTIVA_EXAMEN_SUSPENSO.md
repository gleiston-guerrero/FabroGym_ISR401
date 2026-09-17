# Retrospectiva del equipo - examen suspenso FabroGym

**Proyecto:** FabroGym - ISR-401  
**Fecha de corte de esta retrospectiva:** 17 de septiembre de 2026  
**Repositorio canónico:** `https://github.com/gleiston-guerrero/FabroGym_ISR401`  
**Línea base evaluada por el docente:** `v2.0.4-final` (`dc5a228`)  
**Corte documental:** pre-verificación posterior al informe del 17/09/2026  
**Identificador del cierre terminal:** `v2.0.5-final`; el tag se crea/publica únicamente después de una nueva verificación previa firmada y de regenerar/verificar ambos manifiestos SHA-256.

## 1. Propósito

Esta retrospectiva sustituye los cortes documentales anteriores y responde al informe docente del **17/09/2026, 03:02 (Ecuador)**. El informe declaró cumplido el manuscrito científico, pero observó que la retrospectiva estaba desactualizada, había eliminado la sección de **quién hizo qué**, contenía afirmaciones que ya no correspondían al estado del repositorio y no indicaba quién tomó las capturas atribuidas a Alvia y Vaca.

Esta actualización no modifica los resultados científicos aceptados. Su finalidad es registrar el estado real posterior al informe, los responsables verificables de cada corrección y la secuencia de cierre que aún falta ejecutar.

## 2. Estado de las observaciones del informe del 17/09/2026

| Bloque | Estado documental posterior al informe | Corrección realizada | Evidencia principal |
|---|---|---|---|
| §3 - Línea base | **Saneado documentalmente** | `v2.0.4-final` se conserva como línea base evaluada del 17/09; `v2.0.5-final` identifica el cierre terminal de las correcciones posteriores y se crea/publica solo al final de la secuencia de integridad. | `README.md`; `CHANGELOG.md`; `FAIR_CHECKLIST.md`; `07_Publicacion/README_Publicacion.md`. |
| §4 - Casos de uso | **Corregido** | Se eliminaron las siete contradicciones precondición/excepción observadas, se corrigieron los flujos alternativos cuestionados y los 19 FA indican apertura y retorno/terminación. La matriz mantiene 57 flujos sincronizados. | `01_ERS/ERS_SRS_2B_v2.0.tex`; `01_ERS/ERS_SRS_2B_v2.0.pdf`; `04_Trazabilidad/matriz_trazabilidad.csv`. |
| §12 - Reproducibilidad | **Contenido técnico corregido; manifiestos terminales pendientes** | Los dos `run_all.py` quedaron sincronizados, los scripts auxiliares fuerzan LF y los 38 resultados de `07_Datos/resultados/` y `06_Experimento/resultados/` permanecen byte-idénticos. | `.gitattributes`; `07_Datos/scripts/`; `06_Experimento/scripts_analisis/`; `04_Trazabilidad/VERIFICACION_SINCRONIA_RUN_ALL.md`. |
| §15 - Autoría A2 | **Corregido** | Alvia y Vaca realizaron y depositaron personalmente tres capturas de commits históricos propios cada uno. Las seis capturas observadas del 16/09 fueron retiradas. | `10_Autoria/capturas/`; `10_Autoria/capturas/inventario_capturas_alvia_vaca.csv`; `04_Trazabilidad/VERIFICACION_CAPTURAS_ALVIA_VACA_20260917.md`. |
| §15 - Notas / EXIF / acta | **Se conserva lo aceptado por el informe** | EXIF mantiene 25 fotografías trazadas; WALK-NTEC continúa como reconstrucción posterior y la cobertura de notas contemporáneas permanece en 13/16; el acta de autoría firmada por los cinco se conserva. | `10_Autoria/exif_inventario.csv`; `10_Autoria/bitacora_sesiones.csv`; `04_Trazabilidad/ACTA_RECONOCIMIENTO_AUTORIA_EQUIPO.pdf`. |
| Observación WALK-TEC-01 | **Aclarada** | El `creation_time` interno del MP4 no se usa como fecha de sesión. La sesión se consolida en 12/08/2026 mediante nota de campo, ficha técnica, hash, duración y trazabilidad previa. | `04_Trazabilidad/VERIFICACION_MULTIMEDIA_WALK.md`; `04_Trazabilidad/ACLARACION_FECHAS_WALK.md`. |
| Observación commit `fef33d8` | **Aclarada** | Se documenta que el mensaje anunciaba un script, pero el commit modificó únicamente `checksums.sha256`; el historial no se reescribe. | `04_Trazabilidad/ACLARACION_COMMIT_FEF33D8.md`. |
| §16 - Manuscrito | **Recompilado documentalmente** | Se mantiene intacto el análisis científico aceptado; solo se actualizan la retrospectiva y la línea base declarada para reflejar el informe del 17/09 y el cierre posterior. | `07_Publicacion/manuscrito_final.tex`; `07_Publicacion/manuscrito_final.pdf`. |
| §16 - Retrospectiva | **Actualizada** | Se restituye una sección explícita de quién hizo qué y se registra todo lo ocurrido después de `v2.0.4-final`. | `10_Autoria/retrospectiva_equipo.md`; `07_Publicacion/RETROSPECTIVA_EXAMEN_SUSPENSO.md`. |

## 3. Qué ocurrió después del informe del 17/09/2026

### 3.1 Corrección de §4

- Mera corrigió en la ERS las precondiciones, excepciones y flujos alternativos observados por el docente (`1dd541b`).
- Ponce sincronizó las 19 trazas `FA-01` de la matriz con el ERS corregido, manteniendo los 57 identificadores de flujo (`0d42923`).

### 3.2 Corrección técnica de §12

- Mera sincronizó los dos `run_all.py`, fijó la política LF y documentó la verificación de sincronía/reproducibilidad (`53d17a0`, `318f4eb`).
- Ponce fijó LF en scripts auxiliares y aclaró documentalmente la cadena canónica `07_Datos` frente a `06_Experimento` (`6a68f3c`, `6244ea8`).
- Los manifiestos terminales no se regeneran todavía porque cualquier modificación documental posterior volvería a invalidarlos.

### 3.3 Cierre de la observación WALK-TEC-01

- Mera verificó el MP4 y documentó el significado limitado de su `creation_time` interno (`d995cdb`).
- Ponce consolidó la fecha de sesión del 12/08/2026 con las evidencias independientes existentes (`ab8d897`).

### 3.4 Sustitución de las capturas A2 observadas

- Vaca (`David-Bs1`) depositó personalmente tres capturas de commits históricos propios en `10_Autoria/capturas/` (`2ecbe55`).
- Alvia (`Erick-Alvia`) realizó un primer depósito (`e4881d1`) que dejó las imágenes accidentalmente en la raíz; posteriormente hizo el depósito correcto en `10_Autoria/capturas/` (`47cac43`). El depósito válido para A2 es el ubicado en la ruta canónica.
- Mera retiró las seis capturas del 16/09 que habían sido observadas por el docente (`0bf5014`), documentó la verificación de las nuevas capturas (`bf82034`) y eliminó las copias duplicadas de Alvia que quedaron accidentalmente en la raíz (`ce89a2b`).
- Ponce consolidó la documentación de autoría A2 y la retrospectiva (`fccdb9d`).

Los commits de Alvia y Vaca del 17/09 se clasifican como **depósito personal de evidencia histórica A2 solicitado por el docente**. No se presentan como nuevos aportes técnicos a §4, §12 o §16.

### 3.5 Micro-saneamiento final previo a la verificación

Después de los cuatro commits anteriores se ejecuta el último lote de coherencia documental antes de congelar el contenido. Este corte:

- sincroniza los PDF de `09_Defensa` con sus fuentes Markdown vigentes;
- regenera `09_Defensa/MANIFEST_DEFENSA.csv` sobre los bytes actuales de la carpeta;
- distingue en Defensa y Ética el trabajo técnico de Mera/Ponce de los depósitos históricos A2 de Alvia/Vaca;
- actualiza `aporte_individual.md` y ambas retrospectivas hasta los commits `e7668ef`, `d52ca17`, `08d4bf9` y `7eb007e`;
- amplía la aclaración histórica de checksums para incluir `c641540` y `dc5a228`;
- deja explícito que la causa del `creation_time` de WALK-TEC-01 no puede determinarse con la evidencia disponible.

El SHA del commit que integre este mismo lote no se inserta dentro de la retrospectiva para evitar una autorreferencia circular. El historial Git será la evidencia canónica de su integración. Después de este lote no se modifica contenido académico salvo que falle una comprobación de la verificación previa.

## 4. Quién hizo qué en el cierre posterior al informe

| Integrante | Trabajo verificable posterior al informe del 17/09 | Commits / evidencia |
|---|---|---|
| **Mera Arias Erick Jhair (`Emeraxs`)** | Corrección textual de §4; sincronización de `run_all.py`; política y normalización LF; verificación reproducible del pipeline; análisis técnico de WALK-TEC-01; retiro/verificación de capturas A2 observadas; limpieza de duplicados de Alvia; actualización del corte documental del ERS y recompilación de entregables. | `1dd541b`, `53d17a0`, `318f4eb`, `d995cdb`, `0bf5014`, `bf82034`, `ce89a2b`, `3e16b35`, `e7668ef`, `08d4bf9`. |
| **Ponce Rivera Mery Helenmey (`Mery-003`)** | Sincronización de trazabilidad de §4; LF en scripts auxiliares; documentación de cadena canónica; cierre documental de WALK-TEC-01; consolidación documental A2 y retrospectiva; corrección de SHA-256 de Vaca y consolidación de README/CHANGELOG/FAIR/publicación para pre-verificación. | `0d42923`, `6a68f3c`, `6244ea8`, `ab8d897`, `fccdb9d`, `37f02ac`, `d52ca17`, `7eb007e`. |
| **Alvia Villegas Erick Adalberto (`Erick-Alvia`)** | Depósito personal de tres capturas de aportes históricos, conforme a la instrucción del docente. El primer depósito quedó en ruta incorrecta y fue sustituido por el depósito canónico. | `e4881d1` (ruta incorrecta, superado); `47cac43` (depósito A2 vigente). |
| **Vaca Romero David Octavio (`David-Bs1`)** | Depósito personal de tres capturas de aportes históricos, conforme a la instrucción del docente. | `2ecbe55`. |
| **Mora Duarte Alex José (`amorad35`)** | No se le atribuye trabajo técnico nuevo posterior al informe del 17/09. Sus aportes históricos permanecen preservados. | Historial previo del repositorio. |

## 5. Notas de campo y evidencia histórica

El estado verificable se mantiene en:

- entrevistas: **10/10** notas contemporáneas;
- WALK técnicos: **3/3** notas contemporáneas;
- WALK no técnicos: **0/3** notas contemporáneas acreditables;
- total: **13/16**.

Los PNG de WALK-NTEC se conservan en `10_Autoria/reconstrucciones_posteriores/` como reconstrucciones posteriores y no se cuentan como notas tomadas durante las sesiones.

## 6. Fechas WALK

Las fechas consolidadas de sesión permanecen:

- `WALK-TEC-01`: **12/08/2026**;
- `WALK-TEC-02`: **12/08/2026**;
- `WALK-TEC-03`: **13/08/2026**;
- `WALK-NTEC-01`: **16/08/2026**;
- `WALK-NTEC-02`: **16/08/2026**;
- `WALK-NTEC-03`: **22/08/2026**.

La explicación completa se conserva en `04_Trazabilidad/ACLARACION_FECHAS_WALK.md` y `04_Trazabilidad/VERIFICACION_MULTIMEDIA_WALK.md`.

## 7. Integridad documental

La solicitud de cambio de composición del 15/09/2026 se conserva como antecedente histórico y no se reescribe. La autoría histórica de los cinco integrantes se mantiene según el historial Git. La actividad técnica posterior a la guía se atribuye únicamente a quien la realizó.

Asimismo, el commit `fef33d8` se conserva sin reescritura. Su mensaje no coincide con el cambio real versionado y esa diferencia queda explicitada en `04_Trazabilidad/ACLARACION_COMMIT_FEF33D8.md`.

La presente retrospectiva queda fechada y versionada como documento Markdown y sincronizada con el último lote de coherencia pre-verificación. La **verificación previa firmada** se emite en el siguiente paso, una vez congelado este contenido, para que certifique el corte real que antecederá a los manifiestos terminales.

## 8. Limitaciones que permanecen declaradas

- la comparación por perfil sigue basada en 3 sesiones técnicas y 3 no técnicas;
- el IC95% del delta de Cliff sigue siendo amplio e incluye cero;
- el cuestionario de 70 respuestas no contiene variable de perfil técnico/no técnico ni escala de explicabilidad;
- el indicador estricto de saturación de códigos permanece en `6.306%`, por encima del umbral de `5%`;
- las tres WALK-NTEC permanecen sin nota de campo contemporánea;
- los documentos históricos se preservan sin reescritura retrospectiva.

## 9. Secuencia de cierre pendiente

Después de este saneamiento documental, el orden restante es:

1. congelar el contenido;
2. emitir y firmar una **nueva `10_Autoria/verificacion_previa.pdf`** sobre ese corte;
3. regenerar `07_Datos/checksums_datos.sha256`;
4. regenerar `checksums.sha256`;
5. verificar ambos manifiestos sin fallos desde un clon limpio;
6. crear una **nueva etiqueta anotada `v2.0.5-final`** sobre el último commit de integridad;
7. no mover ni sobrescribir `v2.0.4-final`, que permanece como línea base evaluada en el informe del 17/09/2026.

El cierre se considera documentalmente coherente únicamente cuando ninguna modificación adicional ocurra después de la verificación previa y antes de regenerar los manifiestos.
