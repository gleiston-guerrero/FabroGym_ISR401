# F3-04 — Tamaño del efecto técnico vs no técnico (CORREGIDO)

## Corrección de unidad de análisis

La unidad independiente es la **sesión de walkthrough**, no la categoría temática. El corpus contiene tres sesiones técnicas y tres no técnicas. Las 18 categorías siguen siendo categorías descriptivas del corpus, pero **no se usan como 18 observaciones independientes**.

## Fuente

`datos_crudos/codificacion_walkthroughs.csv`

El script agrega los fragmentos por `Codigo_Sesion` y calcula, para cada sesión, la proporción de fragmentos marcados `Aplicable_Explicabilidad = Si`.

## Datos por sesión

- Técnicas: WALK-TEC-01=2/15 (0.133), WALK-TEC-02=4/16 (0.250), WALK-TEC-03=1/18 (0.056)
- No técnicas: WALK-NTEC-01=1/8 (0.125), WALK-NTEC-02=0/8 (0.000), WALK-NTEC-03=1/11 (0.091)

## Medida principal

Se utiliza **delta de Cliff** para dos grupos independientes sobre la **proporción de fragmentos pertinentes a explicabilidad por sesión**.

- `n técnico = 3` sesiones.
- `n no técnico = 3` sesiones.
- `delta = 0.555556`.
- IC95% bootstrap exacto por remuestreo de sesiones: `[-0.333333, 1.000000]`.
- Media técnica = `0.146296`.
- Media no técnica = `0.071970`.

El intervalo es amplio porque solo existen tres sesiones por perfil; esta amplitud se reporta como limitación y no se maquilla.

## Análisis secundario de sensibilidad

Sobre el conteo bruto de fragmentos pertinentes por sesión:

- `delta = 0.777778`.
- IC95% bootstrap exacto: `[0.333333, 1.000000]`.

Este análisis secundario no sustituye a la medida principal porque el número total de fragmentos codificados difiere entre sesiones.

## Alcance metodológico

El resultado es **descriptivo-exploratorio**. No se genera p-valor ni se afirma una diferencia poblacional. El cuestionario de 70 respuestas **no se usa para esta comparación**, porque no registra perfil técnico/no técnico ni contiene una escala de explicabilidad.

## Reproducibilidad

Desde `07_Datos/`:

```bash
python scripts/calcular_efecto_perfiles.py
```

Desde `06_Experimento/` (espejo histórico):

```bash
python scripts_analisis/calcular_efecto_perfiles.py
```
