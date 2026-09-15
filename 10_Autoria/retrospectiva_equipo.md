# Retrospectiva del equipo - examen suspenso FabroGym

**Proyecto:** FabroGym - ISR-401  
**Fecha de corte de esta retrospectiva:** 15 de septiembre de 2026  
**Repositorio canónico:** `https://github.com/gleiston-guerrero/FabroGym_ISR401`  
**Línea base histórica publicada:** `v2.0.2-final`  
**Etiqueta terminal prevista:** `v2.0.3-final`, únicamente después del cierre documental, la verificación de integridad y los manifiestos SHA-256 terminales.

## 1. Propósito

Esta retrospectiva documenta qué se corrigió durante el examen suspenso, quién realizó o verificó cada bloque y qué aprendió el equipo del proceso. Se redacta después de las correcciones de especificación de casos de uso (§4) y de reproducibilidad/carpeta canónica de resultados (§12), y se vincula con el manuscrito final recompilado en `07_Publicacion/`.

No sustituye el historial Git ni reasigna autoría histórica. La autoría acumulada del proyecto se conserva en los artefactos originales. Para el cierre reciente, la documentación distingue a Mera (`Emeraxs`), Mora (`amorad35`) y Ponce (`Mery-003`) como equipo de corrección, sin atribuir a Alvia o Vaca actividades recientes que no estén respaldadas por evidencia verificable.

## 2. Qué corregimos

| Bloque | Hallazgo del examen | Corrección realizada | Evidencia verificable |
|---|---|---|---|
| §4 - ERS/SRS | Los 19 casos de uso Must estaban modelados y trazados, pero no especificados textualmente con el nivel de comportamiento exigido. | Se incorporó para cada CU actor, disparador, precondiciones, flujo principal numerado, flujo alternativo con condición, excepción con condición y poscondiciones. Se añadieron `ID_Flujo` y `Descripcion_Flujo` en la matriz y 57 trazas explícitas de flujo. | `01_ERS/ERS_SRS_2B_v2.0.tex`, `01_ERS/ERS_SRS_2B_v2.0.pdf`, `04_Trazabilidad/matriz_trazabilidad.csv`; commits `eaec001`, `da6e327`, `b494bf4`, `3a9697f`. |
| §12 - reproducibilidad | El corte evaluado tenía diferencias entre `06_Experimento/resultados/` y `07_Datos/resultados/`, y la semilla del proceso no estaba declarada como una constante única del cierre. | Se dejó `07_Datos/resultados/` como única salida canónica; `06_Experimento/resultados/` se mantiene solo como espejo derivado byte-idéntico. `run_all.py` declara `SEED = 401`. Dos ejecuciones consecutivas sobre los mismos datos fueron verificadas con hashes idénticos en las salidas generadas. | `07_Datos/scripts/run_all.py`, `07_Datos/README_datos.md`, `07_Datos/resultados/README.md`, `06_Experimento/README.md`, `06_Experimento/resultados/`; commits `330bdc9`, `33988cb` y sincronizaciones posteriores. |
| §13 - tamaño del efecto | Un análisis anterior había tratado categorías temáticas como si fueran unidades independientes. | La unidad independiente se corrigió a sesión WALK: 3 técnicas y 3 no técnicas (`n_unidades=6`). El análisis principal reporta Cliff's delta `0.555556`, IC95% `[-0.333333, 1.000000]` e `interpretable=NO` para inferencia poblacional. | `07_Datos/resultados/tablas/tabla_efecto_perfiles.csv`, `07_Datos/resultados/F3-04_TAMANIO_EFECTO.md`, `07_Datos/scripts/calcular_efecto_perfiles.py`. |
| §16 - manuscrito | El manuscrito evaluado era anterior al análisis corregido y no existía la retrospectiva canónica en `10_Autoria/`. | Se sincronizó la narración de resultados y discusión con las tablas canónicas, se mantuvieron explícitas las limitaciones reales, se recompiló el PDF después del cierre de resultados de §12 y se creó esta retrospectiva. | `07_Publicacion/manuscrito_final.tex`, `07_Publicacion/manuscrito_final.pdf`, `10_Autoria/retrospectiva_equipo.md`. |

## 3. Quién hizo qué

### Mera Arias Erick Jhair - `Emeraxs`

- completó la especificación textual de los 19 casos de uso en la ERS y recompiló el documento;
- documentó el cierre §4 en README/CHANGELOG;
- ajustó la ejecución reproducible de `run_all.py` para declarar `SEED = 401` y sincronizar el espejo de resultados;
- participó en la revisión del manuscrito final y en la comprobación de consistencia entre resultados y texto.

### Ponce Rivera Mery Helenmey - `Mery-003`

- reemitió la matriz de trazabilidad para incorporar los 57 flujos `FP/FA/EX` sin alterar los requisitos terminales;
- actualizó el checklist de defensa para reflejar el nuevo estado de los casos de uso y la trazabilidad;
- participó en la revisión documental de las salidas de resultados y del cierre de publicación.

### Mora Duarte Alex Jose - `amorad35`

- realizó la corrección estadística base que sustituyó la categoría temática por la sesión WALK como unidad independiente;
- verificó la interpretación del tamaño del efecto y la limitación del cuestionario `n=70` para la comparación técnico/no técnico;
- participó en la revisión cruzada de la coherencia entre tablas canónicas, discusión y amenazas a la validez.

## 4. Qué aprendimos

1. **Trazabilidad no equivale a especificación.** Tener `CU/HU/CA` vinculados a un requisito no sustituye describir el comportamiento completo del caso de uso. Para un cierre verificable, el flujo principal, las alternativas y las excepciones deben existir y poder rastrearse.

2. **La unidad de análisis debe corresponder al diseño real.** Las categorías temáticas ayudan a interpretar el corpus, pero no son observaciones independientes. La sesión WALK es la unidad defendible para la comparación exploratoria realizada.

3. **Reproducibilidad significa una sola fuente canónica.** Conservar resultados duplicados sin una regla explícita crea ambigüedad. El cierre deja `07_Datos/resultados/` como única fuente evaluable y cualquier copia adicional como espejo derivado.

4. **Un resultado negativo también es un resultado válido.** El indicador estricto de saturación de códigos es `6.306%`, superior al umbral de `5%`; no se reclasifica como cumplimiento. Del mismo modo, el IC95% del delta de Cliff es amplio e incluye cero, por lo que no se formula una inferencia poblacional.

5. **No se corrige una carencia fabricando evidencia.** El equipo conserva las discrepancias que no pueden resolverse retroactivamente con evidencia real. No se inventan consentimientos, capturas, fotografías, notas de campo ni observaciones estadísticas.

6. **El manuscrito debe congelarse después de los resultados que reporta.** Por eso el PDF final de §16 se recompila después de la regeneración reproducible de §12 y antes de los manifiestos terminales.

## 5. Limitaciones y asuntos que no deben maquillarse

- La comparación por perfil se basa en tres sesiones técnicas y tres no técnicas; se mantiene como descriptiva/exploratoria.
- El cuestionario de 70 respuestas no contiene una variable de perfil técnico/no técnico ni una escala de explicabilidad y no se usa para esa comparación.
- El indicador estricto de saturación de códigos no alcanza el umbral del 5%.
- La evidencia histórica de autoría se conserva tal como existe; cualquier elemento adicional de §15 sólo puede incorporarse si es real y verificable.

## 6. Regla de cierre

Esta retrospectiva no declara cerrados los manifiestos SHA-256 ni la etiqueta terminal. Esos pasos se ejecutan únicamente cuando ya no se modificará ningún contenido evaluable. El orden terminal es:

1. cerrar los artefactos documentales y de autoría que correspondan;
2. regenerar `07_Datos/checksums_datos.sha256`;
3. regenerar `checksums.sha256`;
4. verificar ambos sin fallos;
5. crear la etiqueta anotada `v2.0.3-final` sobre el commit final.

La meta del cierre no es aumentar artificialmente el expediente, sino lograr que cada afirmación pueda rastrearse a evidencia real, un requisito versionado, un resultado reproducible o un commit verificable.
