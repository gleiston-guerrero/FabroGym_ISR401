# Notas de campo — alcance y correspondencia con las sesiones empíricas

## Criterio confirmado para el examen suspenso

El 15 de septiembre de 2026 se confirmó que la exigencia es **una nota de campo por sesión de elicitación/validación**, no una nota por cada fila de trabajo interno. `10_Autoria/bitacora_sesiones.csv` se sanea con la columna `tipo` y con 16 filas empíricas enlazadas mediante `ruta_nota_campo`.

Estado verificable: **16/16 sesiones empíricas con nota depositada** (10 entrevistas + 6 walkthroughs).


## 1. Qué documenta esta carpeta

`10_Autoria/notas_campo/` conserva notas producidas durante **sesiones empíricas de elicitación y validación** de FabroGym.

La bitácora A1 contiene ahora **44 filas**: 28 clasificadas como `trabajo_interno` y 16 clasificadas como sesiones empíricas (`entrevista` o `walkthrough`). Las notas de esta carpeta corresponden únicamente a esas 16 filas empíricas. Las 28 sesiones internas —revisión por Discord, edición de artefactos, modelado, documentación y commits— no representan entrevistas ni requieren nota de campo.

La fuente canónica para contar las sesiones empíricas es:

`07_Datos/datos_crudos/sesiones_multimedia_desde_ficha_v3_1.csv`

Ese archivo contiene **16 sesiones empíricas**:

- 10 entrevistas: `ENTR-01` a `ENTR-10`;
- 3 walkthroughs técnicos: `WALK-TEC-01` a `WALK-TEC-03`;
- 3 walkthroughs no técnicos: `WALK-NTEC-01` a `WALK-NTEC-03`.

Por tanto, la cobertura de notas de campo se contrasta con las **16 filas empíricas** de A1 y queda separada de las 28 filas de `trabajo_interno`.

## 2. Estado real de cobertura en este corte

El repositorio contiene **16 notas de campo asociables a las 16 sesiones empíricas**:

- 10/10 entrevistas;
- 3/3 walkthroughs técnicos;
- 3/3 walkthroughs no técnicos.

La cobertura A5 queda, por tanto, en **16/16 sesiones empíricas**. Las tres notas de walkthrough no técnico incorporadas son:

- `WALK-NTEC-01_notas_Campo.png` — código manuscrito `WALK-NTEC-01`, fecha 16/08/2026;
- `WALK-NTEC-02_notas_Campo.png` — código manuscrito `WALK-NTEC-02`, fecha 16/08/2026;
- `WALK-NTEC-03_notas_Campo.png` — código manuscrito `WALK-NTEC-03`, fecha 22/08/2026.

Las rutas y hashes SHA-256 de las 16 notas se registran en `inventario_notas_campo.csv`.

## 3. Discrepancias históricas de fecha en dos notas técnicas

La revisión visual de las notas técnicas detectó dos situaciones que se documentan sin alterar el contenido original:

1. `2026_07_12_WALK-TEC-01_notas_campo.png` contiene manuscrito el código **WALK-TEC-01** y la fecha **12/08/2026**, coherente con la fecha canónica de la sesión (`2026-08-12`). El prefijo histórico del archivo conserva `2026_07_12`; la discrepancia se limita al nombre del archivo.
2. `2026_07_12_WALK-TEC-02_notas_campo.png` identifica **WALK-TEC-02** y consigna manuscritamente **12/07/2026**, mientras el inventario multimedia canónico registra esa sesión el **2026-08-12**. La discrepancia se declara y no se corrige retrospectivamente.

Estas observaciones son de trazabilidad documental; no modifican los datos empíricos ni las grabaciones.

## 4. Relación con A1

La separación es intencional:

- **A1 — `bitacora_sesiones.csv`:** 44 filas en total, con columna `tipo`: 28 `trabajo_interno`, 10 `entrevista` y 6 `walkthrough`.
- **A5 — `notas_campo/`:** 16 notas producidas durante las 16 sesiones empíricas de elicitación/validación.

El denominador empírico verificable es 16 y la cobertura actual es **16/16**.

## 5. Regla de integridad

No se crean notas retrospectivas, no se duplican archivos para aparentar cobertura y no se modifica una nota manuscrita para hacerla coincidir con el inventario. Las 16 notas presentes se identifican por sesión, ruta y SHA-256 en el inventario.
