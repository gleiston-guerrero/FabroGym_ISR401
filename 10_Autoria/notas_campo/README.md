# Notas de campo — alcance y correspondencia con las sesiones empíricas

## 1. Qué documenta esta carpeta

`10_Autoria/notas_campo/` conserva notas contemporáneas producidas durante **sesiones empíricas de elicitación y validación** de FabroGym.

Estas notas **no corresponden a cada fila de `10_Autoria/bitacora_sesiones.csv`**. La bitácora A1 registra 28 sesiones internas de trabajo del equipo —revisión por Discord, edición de artefactos, modelado, documentación y commits— y cumple una finalidad de autoría. No representa 28 entrevistas ni 28 sesiones de elicitación.

La fuente canónica para contar las sesiones empíricas es:

`07_Datos/datos_crudos/sesiones_multimedia_desde_ficha_v3_1.csv`

Ese archivo contiene **16 sesiones empíricas**:

- 10 entrevistas: `ENTR-01` a `ENTR-10`;
- 3 walkthroughs técnicos: `WALK-TEC-01` a `WALK-TEC-03`;
- 3 walkthroughs no técnicos: `WALK-NTEC-01` a `WALK-NTEC-03`.

Por tanto, la cobertura de notas de campo debe contrastarse con esas **16 sesiones empíricas**, no con las 28 sesiones internas de trabajo A1.

## 2. Estado real de cobertura en este corte

El repositorio contiene **13 notas de campo contemporáneas** que pueden asociarse a 13 de las 16 sesiones empíricas:

- 10/10 entrevistas;
- 3/3 walkthroughs técnicos;
- 0/3 walkthroughs no técnicos.

Las tres sesiones sin nota depositada son:

- `WALK-NTEC-01`;
- `WALK-NTEC-02`;
- `WALK-NTEC-03`.

El detalle máquina-legible está en `inventario_notas_campo.csv`.

Si existe una nota física contemporánea de alguna de estas tres sesiones, debe digitalizarse y depositarse conservando su fecha y contenido real. Si no existe, la ausencia debe permanecer declarada. **No se redactan notas nuevas con fecha retrospectiva para completar un conteo.**

## 3. Dos discrepancias históricas de nombre/fecha

La revisión visual de las notas técnicas detectó dos situaciones que se documentan sin alterar el contenido original:

1. `2026_07_12_WALK-TEC-03_notas_campo.png` contiene manuscrito el código **WALK-TEC-01** y la fecha **12/08/2026**. El inventario lo vincula con `WALK-TEC-01` y conserva la ruta histórica para no modificar la evidencia.
2. `2026_07_12_WALK-TEC-02_notas_campo.png` identifica **WALK-TEC-02** y consigna manuscritamente **12/07/2026**, mientras el inventario multimedia canónico registra esa sesión el **2026-08-12**. La discrepancia se declara y no se corrige retrospectivamente.

Estas observaciones son de trazabilidad documental; no modifican los datos empíricos ni las grabaciones.

## 4. Relación con A1

La separación es intencional:

- **A1 — `bitacora_sesiones.csv`:** sesiones de trabajo y coordinación del equipo con rutas, decisiones y commits.
- **A5 — `notas_campo/`:** notas producidas durante sesiones empíricas de elicitación/validación con participantes.

Por ello, no es correcto exigir una nota de campo por cada una de las 28 filas de A1. El denominador empírico verificable es 16.

## 5. Regla de integridad

No se crean notas retrospectivas, no se duplican archivos para aparentar cobertura y no se modifica una nota manuscrita para hacerla coincidir con el inventario. La cobertura se informa tal como existe en el repositorio.
