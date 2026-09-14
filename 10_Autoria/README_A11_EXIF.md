# F4-A11 — Inventario EXIF y fotografías de aplicación

## Resultado técnico

El inventario registra únicamente archivos que existen o cuyos originales están preservados en la capa restringida.

- Fotografías públicas del equipo en la organización: **2**.
- Fotografías originales de aplicación del cuestionario: **5**.
- Total de filas en `exif_inventario.csv`: **7**.
- Filas con fecha EXIF real: **7**.
- Fechas inventadas: **0**.
- Metadatos EXIF modificados en los originales: **0**.

## Fotografías del equipo

Las dos fotografías públicas están en `10_Autoria/fotos_equipo/01_fotos_equipo/` y conservan `DateTimeOriginal` del 27/07/2026. Los nombres se normalizaron para hacer visible la fecha, sin alterar el contenido ni los metadatos.

## Fotografías del cuestionario

Las cinco fotografías originales contienen personas identificables y se conservan en el contenedor restringido:

`10_Autoria/fotos_equipo/02_Fotos_Aplicacion/A11 Fotos_Originales_Cuestionario.7z`

Las copias públicas enmascaradas se encuentran en `02_Evidencias/Cuestionario/Fotos_Aplicacion/`. El inventario conserva la fecha, dispositivo y SHA-256 del original, por lo que el hash de la copia pública puede ser distinto.

Correspondencia:

- `IMG_20260721_102618.jpg` → `Aplicacion_Cuestionario_01.jpg`
- `IMG_20260721_104307.jpg` → `Aplicacion_Cuestionario_02.jpg`
- `IMG_20260721_154701.jpg` → `Aplicacion_Cuestionario_03.jpg`
- `IMG_20260721_154901.jpg` → `Aplicacion_Cuestionario_04.jpg`
- `IMG_20260825_142844.jpg` → `Aplicacion_Cuestionario_05.jpg`

## Regla de integridad

No se inventan fechas, dispositivos ni evidencias. El inventario evita declarar como públicas fotografías que no estén presentes en el repositorio.
