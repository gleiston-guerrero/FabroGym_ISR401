# Selección A6 y control de privacidad

## Fotografías reales del equipo incorporadas

- `2026-07-27_equipo_fabrogym_01.jpg`
- `2026-07-27_equipo_fabrogym_02.jpg`

Estas son las dos fotografías de equipo que existen físicamente en `10_Autoria/fotos_equipo/`. Ambas conservan `DateTimeOriginal` de 2026-07-27 y su SHA-256 se registra en `exif_inventario.csv`. No se anuncian fotografías adicionales de equipo que no estén presentes en el repositorio.

## Fotografías de entorno incorporadas al inventario

El inventario EXIF incluye también los cuatro archivos JPG físicamente presentes en `02_Evidencias/Fotos_Entorno/`:

- `EV-FOT-ENT-01_levantamiento_informacion_area_funcional.jpg`
- `EV-FOT-ENT-02_vista_general_area_entrenamiento.jpg`
- `EV-FOT-ENT-03_estanteria_implementos_entrenamiento.jpg`
- `EV-FOT-ENT-05_registro_observacion_junto_maquinaria.jpg`

Los cuatro conservan fecha EXIF del 27/07/2026, dispositivo y SHA-256 real.

## Fotografías de aplicación del cuestionario

La evidencia del cuestionario cuenta con **cinco fotografías originales** con fecha EXIF, dispositivo y SHA-256 documentados en `exif_inventario.csv`.

Para preservar los metadatos originales, los archivos identificables se conservan en el contenedor restringido:

`10_Autoria/fotos_equipo/02_Fotos_Aplicacion/A11 Fotos_Originales_Cuestionario.7z`

Las copias destinadas a revisión pública se encuentran en:

`02_Evidencias/Cuestionario/Fotos_Aplicacion/`

y se clasifican como copias públicas enmascaradas.

En `exif_inventario.csv`, las cinco filas `F3-01_APLICACION_CUESTIONARIO` tienen el estado `PUBLICA_ENMASCARADA_ORIGINAL_RESTRINGIDO`.

## Integridad

El inventario final contiene **11 filas reales**: 2 fotografías de equipo, 4 fotografías JPG de entorno y 5 fotografías originales de aplicación del cuestionario. No se mantienen filas correspondientes a archivos inexistentes. Las copias públicas del cuestionario pueden diferir en hash o metadatos como consecuencia del enmascaramiento y no sustituyen a los originales como fuente primaria del inventario.
