# Retrospectiva del equipo - examen suspenso FabroGym

**Proyecto:** FabroGym - ISR-401  
**Fecha de corte de esta retrospectiva:** 17 de septiembre de 2026  
**Repositorio canónico:** `https://github.com/gleiston-guerrero/FabroGym_ISR401`  
**Línea base evaluada:** `v2.0.4-final` (`dc5a228`)  
**Siguiente etiqueta terminal prevista:** `v2.0.5-final`, únicamente después de la verificación previa final y de regenerar/verificar los manifiestos SHA-256.

## 1. Propósito

Esta retrospectiva sustituye el corte del 15/09/2026 y documenta las correcciones realizadas después de la revisión del examen suspenso del 16/09/2026.

El informe del docente indicó que el **manuscrito estaba en orden** y que el pendiente de §16 era la retrospectiva: debía recoger todo lo ocurrido hasta el último corte y corregir la afirmación relativa a las notas de campo.

Por ello, esta actualización no reabre los resultados numéricos ni modifica el análisis científico ya aceptado. Su finalidad es dejar trazable el cierre documental posterior: autoría, notas WALK-NTEC, aclaración de fechas WALK, acta de los cinco integrantes y alineación de la portada ERS.

## 2. Estado de las correcciones

| Bloque | Estado documentado | Corrección / cierre realizado | Evidencia principal |
|---|---|---|---|
| §4 - Casos de uso | Cerrado previamente | Los 19 CU Must mantienen actor, disparador, precondiciones, flujo principal, alternativa, excepción y poscondiciones, con 57 trazas de flujo añadidas. | `01_ERS/ERS_SRS_2B_v2.0.tex`; `04_Trazabilidad/matriz_trazabilidad.csv`. |
| §12 - Reproducibilidad | Cerrado previamente | `07_Datos/resultados/` permanece como fuente canónica; `06_Experimento/resultados/` es espejo derivado. `SEED = 401` permanece declarado. | `07_Datos/scripts/run_all.py`; README de datos/resultados. |
| §15 - Autoría A2 | **Cerrado documentalmente** | Por instrucción del docente, Alvia y Vaca realizan y depositan personalmente 3 capturas históricas propias cada uno. Las 6 capturas observadas se retiran. A2 mantiene **48 capturas**. | `10_Autoria/capturas/README.md`; `04_Trazabilidad/VERIFICACION_CAPTURAS_ALVIA_VACA_20260917.md`. |
| §15 - Alcance de A2 / autoría | Actualizado | La solicitud del 15/09 se conserva sin modificar. Los commits del 17/09 de Alvia y Vaca se documentan solo como depósito de evidencia histórica A2 solicitado por el docente, no como nuevo trabajo técnico. | `04_Trazabilidad/ACLARACION_ALCANCE_CAPTURAS_ALVIA_VACA_20260917.md`; `10_Autoria/EQUIPO_EXAMEN_FINAL.md`. |
| §15 - Notas de campo | Rectificado | La cobertura verificable pasa de `16/16` a **13/16 notas contemporáneas**. `WALK-NTEC-01`, `02` y `03` figuran como sesiones sin nota contemporánea. Sus PNG se conservan como reconstrucciones posteriores, sin utilizarlos como prueba de lo escrito durante la sesión. | `10_Autoria/bitacora_sesiones.csv`; `10_Autoria/notas_campo/inventario_notas_campo.csv`; `10_Autoria/reconstrucciones_posteriores/`. |
| Observación de fechas WALK | Explicada por escrito | Se documentó por qué las fechas antiguas `18/08` y `24/08` correspondían a elaboración/ratificación de actas y se consolidaron las fechas de sesión utilizadas por la trazabilidad multimedia. No se reescribió el contenido conversacional de las transcripciones. | `04_Trazabilidad/ACLARACION_FECHAS_WALK.md`; `04_Trazabilidad/VERIFICACION_MULTIMEDIA_WALK.md`. |
| §16 - Manuscrito | Sin cambios sustantivos | Se conserva el manuscrito evaluado porque el informe lo declaró en orden: usa sesión WALK como unidad independiente, 3+3 sesiones, y no trata las 18 categorías como unidades independientes. | `07_Publicacion/manuscrito_final.tex`; `07_Publicacion/manuscrito_final.pdf`. |
| §16 - Retrospectiva | **Actualizada en este parche** | Se reemplaza el corte desactualizado del 15/09, se incorpora todo lo ocurrido después y se elimina la afirmación incompatible con la reclasificación de las notas NTEC. | `10_Autoria/retrospectiva_equipo.md`; `07_Publicacion/RETROSPECTIVA_EXAMEN_SUSPENSO.md`. |

## 3. Cronología del cierre posterior al corte anterior

### 15 de septiembre de 2026

- se completó y recompiló el manuscrito final después del cierre de los resultados;
- se reorganizaron notas y metadatos de sesión;
- se modificaron los encabezados de fecha de las seis transcripciones WALK para sincronizarlos con la cronología ya registrada por el proyecto.

### 16 de septiembre de 2026 - madrugada

- se emitió `10_Autoria/verificacion_previa.pdf` sobre el corte existente en ese momento.

### 16 de septiembre de 2026 - revisión del docente

El informe de evaluación señaló dos problemas posteriores al corte de la retrospectiva anterior:

1. tres imágenes WALK-NTEC no podían acreditarse como notas contemporáneas;
2. el cambio de fechas de las transcripciones WALK requería explicación escrita.

También indicó que el manuscrito estaba en orden y que la retrospectiva debía actualizarse.

### 16 de septiembre de 2026 - correcciones posteriores al informe

- `WALK-NTEC-01`, `02` y `03` se reclasificaron como **reconstrucciones posteriores**;
- esas tres sesiones quedaron sin `ruta_nota_campo` y la cobertura real quedó en **13/16**;
- se creó `04_Trazabilidad/ACLARACION_FECHAS_WALK.md`;
- se verificaron los archivos multimedia observados por SHA-256 y se documentó por qué sus `creation_time` no se utilizan como fecha de captura;
- se incorporó inicialmente un conjunto de seis capturas A2 que el informe del 17/09 observó por haber sido tomadas desde una sesión ajena;
- la evidencia A2 quedó en **48 capturas**;
- se sustituyó la interpretación unilateral de composición por reconocimiento de autoría verificable de los cinco integrantes;
- se incorporó el acta firmada por los cinco integrantes en `04_Trazabilidad/ACTA_RECONOCIMIENTO_AUTORIA_EQUIPO.pdf`;
- la portada de la ERS se alineó con esa interpretación, sin modificar los casos de uso ni el contenido técnico ya aceptado;
- el último estado previo a esta retrospectiva quedó en `main` commit `fc0344dec7ecc39d4d8a121a59607345cb227982`.

## 4. Autoría y participación

El historial Git conserva la autoría histórica verificable de los cinco integrantes. Para el corte técnico posterior a la guía, el informe del 17/09/2026 constató trabajo sobre los ítems evaluados para **Mera Arias Erick Jhair** y **Ponce Rivera Mery Helenmey**.

Después del informe, el docente indicó que Alvia y Vaca debían realizar e incorporar personalmente sus capturas. Por ello:

- **Alvia (`Erick-Alvia`)** realiza y deposita tres capturas de sus commits históricos `98fe055`, `af63622` y `e73613e`;
- **Vaca (`David-Bs1`)** realiza y deposita tres capturas de sus commits históricos `8e66445`, `10a010f` y `9cd5b20`;
- **Mera/Ponce** consolidan inventario, verificación y documentación de cierre sin atribuirse la toma de esas capturas.

Los commits de Alvia y Vaca del 17/09 se clasifican como **depósito de evidencia histórica A2**. No se presentan como nuevos aportes técnicos de la fase de corrección y no cambian la fecha ni la autoría de los commits históricos mostrados.

La solicitud del 15/09/2026 se conserva sin modificar como antecedente y el depósito personal de A2 no se documenta como modificación de aquella solicitud.

## 5. Rectificación específica sobre las notas de campo

La retrospectiva anterior afirmaba que las 16 sesiones empíricas tenían `16/16` notas de campo y utilizaba una formulación general que ya no era compatible con lo observado por el docente.

El cierre corregido es:

- entrevistas: **10/10** notas contemporáneas;
- WALK técnicos: **3/3** notas contemporáneas;
- WALK no técnicos: **0/3** notas contemporáneas acreditables;
- total: **13/16**.

Los tres PNG de WALK-NTEC se preservan por trazabilidad en `10_Autoria/reconstrucciones_posteriores/`, pero se declaran explícitamente como **reconstrucciones posteriores** y no computan como notas de campo tomadas durante las sesiones.

La corrección no consiste en ocultar o eliminar esos archivos, sino en **clasificarlos de acuerdo con lo que realmente pueden acreditar**.

## 6. Aclaración de las fechas WALK

Las fechas consolidadas de sesión son:

- `WALK-TEC-01`: **12/08/2026**
- `WALK-TEC-02`: **12/08/2026**
- `WALK-TEC-03`: **13/08/2026**
- `WALK-NTEC-01`: **16/08/2026**
- `WALK-NTEC-02`: **16/08/2026**
- `WALK-NTEC-03`: **22/08/2026**

La explicación completa y la evidencia utilizada se mantienen en `04_Trazabilidad/ACLARACION_FECHAS_WALK.md`.

Las fechas `18/08/2026` y `24/08/2026` que figuraban anteriormente en los encabezados correspondían a elaboración/ratificación de actas. Los documentos manuscritos con anotaciones discordantes se preservan sin edición y la discrepancia se explica, no se oculta.

## 7. Qué aprendimos

1. **Una evidencia debe declararse por lo que realmente puede demostrar.** Conservar un archivo no obliga a clasificarlo como evidencia contemporánea si fue construido posteriormente.

2. **Una corrección documental debe conservar la historia del cambio.** La solicitud de composición del 15/09 se mantiene como antecedente, pero ya no se usa como fuente canónica después del acta suscrita por los cinco.

3. **Las fechas de sesión y las fechas de elaboración documental no son equivalentes.** La trazabilidad debe distinguir ejecución, elaboración de acta, procesamiento multimedia y versionado Git.

4. **La autoría no se corrige reasignando trabajo.** Las capturas nuevas de Alvia y Vaca documentan commits existentes; no crean contribuciones nuevas.

5. **La unidad de análisis debe corresponder al diseño.** Para el efecto por perfiles se conservan seis sesiones independientes, tres técnicas y tres no técnicas; las 18 categorías temáticas no se tratan como observaciones independientes.

6. **El cierre debe ser secuencial.** Primero se congela el contenido, después se realiza la verificación previa final, luego se regeneran los manifiestos y solo al final se crea una nueva etiqueta.

## 8. Limitaciones que permanecen declaradas

- la comparación por perfil sigue basada en 3 sesiones técnicas y 3 no técnicas;
- el IC95% del delta de Cliff sigue siendo amplio e incluye cero;
- el cuestionario de 70 respuestas no contiene variable de perfil técnico/no técnico ni escala de explicabilidad;
- el indicador estricto de saturación de códigos permanece en `6.306%`, por encima del umbral de `5%`;
- las tres WALK-NTEC permanecen sin nota de campo contemporánea;
- los documentos históricos y sus discrepancias se conservan, no se reescriben retrospectivamente.

## 9. Regla de cierre terminal

Con esta actualización queda atendido el pendiente documental señalado para la retrospectiva de §16.

Todavía **no** se declaran terminales los manifiestos ni la nueva etiqueta. El orden restante es:

1. ejecutar una **nueva verificación previa** sobre el estado posterior a esta retrospectiva;
2. congelar cualquier último cambio documental;
3. regenerar `07_Datos/checksums_datos.sha256`;
4. regenerar `checksums.sha256`;
5. verificar ambos manifiestos sin fallos;
6. crear una **nueva etiqueta anotada** sobre el último commit; por secuencia del repositorio, la etiqueta prevista es `v2.0.5-final`;
7. no mover ni sobrescribir `v2.0.4-final`, que se conserva como referencia de la línea base evaluada el 17/09/2026.

El objetivo de este cierre es que cada afirmación del repositorio sea consistente con la evidencia que realmente existe y con las observaciones expresas del informe de evaluación.
