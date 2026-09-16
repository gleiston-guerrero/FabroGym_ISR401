# Notas de campo — alcance y correspondencia con las sesiones empíricas

## Estado corregido tras la revisión del 16/09/2026

La bitácora contiene **44 filas**: 28 de `trabajo_interno` y 16 sesiones empíricas (10 entrevistas + 6 walkthroughs). La cobertura de notas de campo se calcula únicamente sobre esas 16 sesiones empíricas.

Tras la observación del informe de evaluación del 16/09/2026, el estado verificable queda en:

- **10/10 entrevistas** con nota de campo;
- **3/3 walkthroughs técnicos** con nota de campo;
- **0/3 walkthroughs no técnicos** con nota de campo contemporánea acreditable.

Total: **13/16 sesiones empíricas con nota de campo contemporánea acreditable**.

## WALK-NTEC-01, WALK-NTEC-02 y WALK-NTEC-03

Las tres sesiones no técnicas quedan registradas como **sesiones sin nota de campo contemporánea**. Los PNG que antes estaban tratados como notas se conservan, sin alterar sus bytes, en:

`10_Autoria/reconstrucciones_posteriores/`

Su clasificación correcta es **reconstrucción posterior**. El hecho verificable es que fueron versionados por primera vez el 15/09/2026. En consecuencia, no computan en A5 y no se utilizan para probar qué se escribió durante la sesión.

En `10_Autoria/bitacora_sesiones.csv`, las tres filas WALK-NTEC mantienen `ruta_nota_campo` vacía.

## Inventario de notas

`inventario_notas_campo.csv` conserva una fila por cada sesión empírica. Para las tres WALK-NTEC:

- `estado_nota = SIN_NOTA_CONTEMPORANEA`;
- `nota_campo_ruta` queda vacía;
- `sha256_nota` queda vacío;
- la observación remite a la reconstrucción preservada y a su SHA-256.

Las reconstrucciones tienen su propio inventario en:

`10_Autoria/reconstrucciones_posteriores/inventario_reconstrucciones.csv`

## Fechas de las sesiones WALK

Este bloque **no vuelve a modificar las fechas de las transcripciones**. La aclaración definitiva se conserva en `04_Trazabilidad/ACLARACION_FECHAS_WALK.md`; los valores manuscritos discordantes se preservan sin edición y se explican allí como errores materiales de consignación del mes.

## Regla de integridad

No se crean notas retrospectivas para completar cobertura, no se modifica una reconstrucción para presentarla como contemporánea y no se usa la reconstrucción como evidencia de la fecha real de la sesión.
