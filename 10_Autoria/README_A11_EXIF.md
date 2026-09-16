# F4-A11 — Inventario EXIF y fotografías de evidencia

## Resultado técnico

El inventario se amplió para cubrir **todas las fotografías de evidencia físicamente identificadas en el corte actual**, no sólo las que conservan EXIF completo.

Distribución verificada:

- Fotografías reales del equipo: **2**.
- Fotografías de entorno: **18**.
- Fotografías de aplicación del cuestionario: **5**.
- Total de filas de datos en `exif_inventario.csv`: **25**.
- Filas con fecha de captura recuperable: **20**.
- Filas `SIN_EXIF`: **5**.
- Filas `EXIF_PARCIAL`: **2**.
- Fechas o dispositivos inventados: **0**.

La guía del examen suspenso contabilizó 26 fotografías asumiendo 3 fotos de equipo. El árbol verificable de FabroGym contiene **2 fotos de equipo + 18 de entorno + 5 de aplicación = 25 fotografías**. No se incorpora una tercera fotografía inexistente.

## Fotografías del equipo

Los dos archivos reales se encuentran en `10_Autoria/fotos_equipo/`:

- `2026-07-27_equipo_fabrogym_01.jpg`
- `2026-07-27_equipo_fabrogym_02.jpg`

Ambos conservan fecha EXIF del 27/07/2026. El inventario preserva sus SHA-256 y la información de dispositivo disponible.

## Fotografías de entorno

Se inventariaron las **18 fotografías físicamente presentes** en:

`02_Evidencias/Fotos_Entorno/`

No se excluyen los PNG por el mero hecho de ser PNG: se leen los metadatos que realmente conserve cada archivo.

Estado observado:

- **13/18** conservan fecha de captura recuperable en metadatos.
- **11/18** conservan además modelo o fabricante del dispositivo.
- **2/18** conservan fecha pero no Make/Model y se marcan `EXIF_PARCIAL`.
- **5/18** no exponen fecha ni dispositivo EXIF recuperables y se marcan `SIN_EXIF`.

Los cinco archivos `SIN_EXIF` son:

- `EV-FOT-ENT-06_vista_entrenamiento_garrosh.png`
- `EV-FOT-ENT-07_vista_general_garrosh.png`
- `EV-FOT-ENT-09_Maquinarias_2.png`
- `EV-FOT-ENT-10_Maquinarias_3.png`
- `EV-FOT-ENT-14_Pesas.png`

No se completa la fecha a partir del nombre, del orden del archivo ni de la fecha del sistema operativo.

## Fotografías de aplicación del cuestionario

Las cinco fotografías originales del cuestionario contienen personas identificables. Sus metadatos originales se conservan en el contenedor restringido:

`10_Autoria/fotos_equipo/02_Fotos_Aplicacion/A11 Fotos_Originales_Cuestionario.7z`

Las copias públicas enmascaradas permanecen en:

`02_Evidencias/Cuestionario/Fotos_Aplicacion/`

Las cinco filas del inventario conservan la correspondencia entre el original documentado y la copia pública asociada. El enmascaramiento puede cambiar el hash y los metadatos de la copia pública; por eso la fuente primaria de EXIF es el original preservado.

## Regla de integridad

Una fila del inventario significa **una fotografía real del expediente**, no una afirmación de que todo archivo tenga EXIF.

Cuando el metadato existe, se registra. Cuando falta, se declara `SIN_EXIF`; cuando sólo existe parte de la información, se declara `EXIF_PARCIAL`. No se inventan fechas, zonas horarias, fabricantes ni modelos.

## Correspondencia de originales del cuestionario

- `IMG_20260721_102618.jpg` → `Aplicacion_Cuestionario_01.jpg`
- `IMG_20260721_104307.jpg` → `Aplicacion_Cuestionario_02.jpg`
- `IMG_20260721_154701.jpg` → `Aplicacion_Cuestionario_03.jpg`
- `IMG_20260721_154901.jpg` → `Aplicacion_Cuestionario_04.jpg`
- `IMG_20260825_142844.jpg` → `Aplicacion_Cuestionario_05.jpg`


## Interpretación de hashes

`exif_inventario.csv` distingue dos valores cuando la fotografía de aplicación tiene un original restringido y una copia pública enmascarada:

- `SHA256`: hash del **original restringido con EXIF** para las cinco fotografías de aplicación; en el resto coincide con el archivo público.
- `SHA256_archivo_en_ruta`: hash de los bytes del archivo ubicado en `Ruta_final_o_prevista`.
- `Interpretacion_SHA256`: declara explícitamente cuál de los dos alcances aplica a cada fila.

Así se evita comparar el hash del original restringido con los bytes de una copia pública enmascarada, que necesariamente son diferentes.
