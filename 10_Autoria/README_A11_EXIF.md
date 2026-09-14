# F4-A11 — Inventario EXIF y fotografías de aplicación

## Resultado técnico

El inventario conserva únicamente evidencia que existe y puede trazarse.

- Fotografías reales del equipo: **2**.
- Fotografías originales de aplicación del cuestionario documentadas: **5**.
- Total de filas en `exif_inventario.csv`: **7**.
- Filas con fecha EXIF real documentada: **7**.
- Fechas inventadas: **0**.
- Filas de fotografías de equipo inexistentes: **0**.

## Fotografías del equipo

Los dos archivos reales se encuentran en `10_Autoria/fotos_equipo/01_fotos_equipo/` con nombres normalizados por fecha:

- `2026-07-27_Equipo_FabroGym_01.jpg` — `DateTimeOriginal: 2026:07:27 17:52:21`.
- `2026-07-27_Equipo_FabroGym_02.jpg` — `DateTimeOriginal: 2026:07:27 17:50:39`.

El renombrado hace legible la fecha sin modificar los bytes de imagen ni los metadatos EXIF.

## Fotografías del cuestionario

Las cinco fotografías originales del cuestionario contienen personas identificables. Para preservar la evidencia original y sus metadatos EXIF se conservan dentro del contenedor restringido:

`10_Autoria/fotos_equipo/02_Fotos_Aplicacion/A11 Fotos_Originales_Cuestionario.7z`

Las copias públicas enmascaradas se conservan en:

`02_Evidencias/Cuestionario/Fotos_Aplicacion/`

El estado de las cinco filas `F3-01_APLICACION_CUESTIONARIO` es `PUBLICA_ENMASCARADA_ORIGINAL_RESTRINGIDO`.

## Regla de integridad

No se inventan fechas, modelos de dispositivo ni archivos. Los originales del cuestionario no se sustituyen por las versiones enmascaradas. La columna `Nombre` conserva el nombre del original del que procede el EXIF y la columna `Ruta_final_o_prevista` identifica la copia pública asociada.

## Correspondencia con las copias públicas actuales

- `IMG_20260721_102618.jpg` → `Aplicacion_Cuestionario_01.jpg`
- `IMG_20260721_104307.jpg` → `Aplicacion_Cuestionario_02.jpg`
- `IMG_20260721_154701.jpg` → `Aplicacion_Cuestionario_03.jpg`
- `IMG_20260721_154901.jpg` → `Aplicacion_Cuestionario_04.jpg`
- `IMG_20260825_142844.jpg` → `Aplicacion_Cuestionario_05.jpg`
