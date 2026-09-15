# Selección A6 y control de metadatos fotográficos

## 1. Fotografías reales del equipo

El árbol actual contiene dos fotografías de equipo:

- `2026-07-27_equipo_fabrogym_01.jpg`
- `2026-07-27_equipo_fabrogym_02.jpg`

Ambas conservan fecha EXIF y están registradas con SHA-256 en `exif_inventario.csv`.

La guía del examen suspenso indicó tres fotografías de equipo, pero en el corte verificable sólo existen estas dos. No se crea ni duplica una tercera imagen para ajustar el conteo.

## 2. Fotografías de entorno

En `02_Evidencias/Fotos_Entorno/` existen **18 fotografías** y las 18 se incluyen ahora en `exif_inventario.csv`.

El inventario distingue entre:

- `OK`: fecha y dispositivo disponibles;
- `EXIF_PARCIAL`: existe fecha, pero falta Make/Model;
- `SIN_EXIF`: no hay fecha ni dispositivo recuperables.

De las 18 fotografías de entorno, 13 conservan fecha; cinco se declaran `SIN_EXIF`.

## 3. Fotografías de aplicación del cuestionario

Existen cinco fotografías reales de aplicación. Los originales con metadatos se conservan en el contenedor restringido:

`10_Autoria/fotos_equipo/02_Fotos_Aplicacion/A11 Fotos_Originales_Cuestionario.7z`

Las copias públicas enmascaradas están en:

`02_Evidencias/Cuestionario/Fotos_Aplicacion/`

El inventario mantiene la correspondencia entre original y copia pública sin exponer información personal.

## 4. Conteo verificable del corte

El conjunto fotográfico inventariado queda así:

- 2 fotografías de equipo;
- 18 fotografías de entorno;
- 5 fotografías de aplicación.

**Total: 25 fotografías reales y 25 filas de datos en `exif_inventario.csv`.**

La diferencia frente al conteo de 26 de la guía proviene exclusivamente de que la guía presupone tres fotografías de equipo y el árbol actual contiene dos.

## 5. Integridad

No se inventan metadatos, no se asignan fechas por inferencia y no se duplican fotografías. Los archivos sin metadatos se conservan y se declaran expresamente como `SIN_EXIF`.
