# Aclaración definitiva de fechas — sesiones WALK

**Proyecto:** FabroGym — ISR-401  
**Fecha de aclaración inicial:** 16 de septiembre de 2026  
**Actualización focal por observación docente:** 17 de septiembre de 2026  
**Alcance:** `WALK-NTEC-01..03` y `WALK-TEC-01..03`  
**Motivo:** observaciones escritas de evaluación y, en particular, la solicitud del informe del 17/09/2026 de explicar la diferencia entre `creation_time = 05/08/2026` y la fecha de sesión `12/08/2026` de `WALK-TEC-01`.

## 1. Objeto de la aclaración

El commit `35c1893` modificó únicamente la línea `Fecha de sesión` de las seis transcripciones WALK. No modificó intervenciones, respuestas ni contenido empírico.

Los encabezados anteriores eran:

- `24/08/2026` para `WALK-NTEC-01`, `WALK-NTEC-02` y `WALK-NTEC-03`;
- `18/08/2026` para `WALK-TEC-01`, `WALK-TEC-02` y `WALK-TEC-03`.

Esos valores coinciden con el campo **“Fecha de elaboración y ratificación del acta”** de las actas públicas de walkthrough. Por tanto, correspondían a una fecha posterior de documentación/ratificación y no a la fecha de ejecución de la sesión.

La corrección del encabezado se realizó para sustituir esa fecha de acta por la fecha de sesión ya utilizada en la trazabilidad multimedia del proyecto.

## 2. Fechas consolidadas para las seis sesiones

| Sesión | Fecha anterior de la transcripción | Fecha de sesión consolidada | Estado |
|---|---:|---:|---|
| `WALK-NTEC-01` | 24/08/2026 | **16/08/2026** | **CONSOLIDADA** |
| `WALK-NTEC-02` | 24/08/2026 | **16/08/2026** | **CONSOLIDADA** |
| `WALK-NTEC-03` | 24/08/2026 | **22/08/2026** | **CONSOLIDADA** |
| `WALK-TEC-01` | 18/08/2026 | **12/08/2026** | **CONSOLIDADA** |
| `WALK-TEC-02` | 18/08/2026 | **12/08/2026** | **CONSOLIDADA** |
| `WALK-TEC-03` | 18/08/2026 | **13/08/2026** | **CONSOLIDADA** |

No se vuelve a modificar el contenido de las transcripciones con esta aclaración.

## 3. Evidencia anterior al cambio de las transcripciones

Las fechas consolidadas no fueron creadas por el commit `35c1893`.

### 3.1 Ficha técnica versionada el 01/09/2026

El commit `387d825` incorporó, antes del cambio de las transcripciones, la ficha técnica de las evidencias WALK con los siguientes nombres, fechas y SHA-256 de video:

- `2026-08-16_Video_WALK-NTEC-01_Instructor.mp4`  
  SHA-256: `893e21b1bf812da5dcad62cd2df801e0f27e7f17d6e57b649e9429ef8342d250`
- `2026-08-16_Video_WALK-NTEC-02_Recepcionista.mp4`  
  SHA-256: `35426caae7e710c34a4d8609a9b5e04e98b89042cab6d69d1171f398ec994d98`
- `2026-08-12_Video_WALK-TEC-01_Ing.Soft.mp4`  
  SHA-256: `147eb88ebb07818179611e51e9381cff1f781f53408153f6623c03731326aa5a`
- `2026-08-12_Video_WALK-TEC-02_Ing.Soft.mp4`  
  SHA-256: `7285c6d3ff83df7377ba5479cce8d66d9634b9a80a7bfb7fa2958842d3901d0e`

La misma ficha registra `WALK-NTEC-03` en `22/08/2026` y `WALK-TEC-03` en `13/08/2026`.

### 3.2 Registro de desviaciones versionado el 04/09/2026

Antes del commit `35c1893`, el archivo `07_Datos/desviaciones.md` ya documentaba la cronología exacta:

- `WALK-TEC-01`: 12/08/2026
- `WALK-TEC-02`: 12/08/2026
- `WALK-TEC-03`: 13/08/2026
- `WALK-NTEC-01`: 16/08/2026
- `WALK-NTEC-02`: 16/08/2026
- `WALK-NTEC-03`: 22/08/2026

Por ello, el cambio posterior en las transcripciones no introdujo una cronología nueva; sincronizó sus encabezados con una cronología que ya estaba documentada en el repositorio.

## 4. Tratamiento de las fechas manuscritas `07/2026`

Se revisaron los consentimientos censurados y las notas manuscritas disponibles.

En los consentimientos de `WALK-TEC-01`, `WALK-TEC-02`, `WALK-NTEC-01` y `WALK-NTEC-02` aparece manuscrito el mes `07/2026`. Esos cuatro formularios pertenecen a una plantilla cuya primera página identifica **“Versión 1.0 - 12 de agosto de 2026”**. En consecuencia, la consignación manuscrita de julio resulta incompatible con la propia versión documental del formulario y con la trazabilidad multimedia ya registrada antes del cambio de las transcripciones.

Además:

- la nota manuscrita de `WALK-TEC-01` indica `12/08/2026`;
- la nota manuscrita de `WALK-TEC-02` indica `12/07/2026`;
- la nota manuscrita de `WALK-TEC-03` indica `13/08/2026`;
- los consentimientos de `WALK-TEC-03` y `WALK-NTEC-03` indican, respectivamente, `13/08/2026` y `22/08/2026`.

Para el cierre documental, los valores `07/2026` se tratan como **errores materiales de consignación del mes** en esos documentos manuscritos. Los archivos firmados y las imágenes manuscritas **no se editan, sustituyen ni retocan**; la diferencia se conserva visible y se explica en este documento.

Esta interpretación se adopta porque la cronología de agosto ya estaba asentada en el registro técnico del 01/09 y en el registro metodológico del 04/09, ambos anteriores al cambio cuestionado de las transcripciones.

## 5. Verificación multimedia y tratamiento específico de `WALK-TEC-01`

Se verificaron los objetos multimedia observados y el 17/09/2026 se realizó una **reverificación focal directa** del archivo materializado de `WALK-TEC-01`.

El SHA-256 calculado del MP4 reverificado es:

`147eb88ebb07818179611e51e9381cff1f781f53408153f6623c03731326aa5a`

Ese valor coincide exactamente con la ficha técnica ya versionada. FFprobe confirma una duración de `1485.666667 s` (~24:45.667), H.264/AAC y los siguientes metadatos de contenedor:

- `creation_time = 2026-08-05T16:54:12.000000Z`;
- `date = 2026-08-05T16:54:12+0000`;
- `encoder = HandBrake 1.10.2 2025090600`.

El archivo conservado declara a HandBrake como codificador. El valor `creation_time = 05/08/2026` se conserva íntegro, pero se interpreta únicamente como **metadato interno del contenedor MP4 procesado**. Los artefactos disponibles no permiten determinar de forma verificable por qué ese valor quedó escrito en el archivo; por ello no se atribuye una causa no demostrable.

La fecha de sesión `12/08/2026` no se obtiene del `creation_time`. Se sustenta por evidencia documental independiente: la nota de campo manuscrita de `WALK-TEC-01` registra `12/08/2026` y `24'46 aprox.`; la ficha técnica versionada desde el 01/09 registra `fecha_sesion = 2026-08-12`, duración `00:24:46` y el mismo SHA-256 del MP4; y la cronología de `07_Datos/desviaciones.md` ya consignaba agosto antes de la corrección posterior de las transcripciones. El acta, elaborada/ratificada el 18/08, reporta además `24:45 aprox.`, duración coherente con el archivo.

Por tanto, para trazabilidad quedan separados cuatro datos: **05/08** (`creation_time` interno del MP4 procesado), **12/08** (fecha de sesión), **18/08** (elaboración/ratificación del acta) y **01/09** (procesamiento/catalogación de la ficha técnica). Ninguno sustituye a otro, y el `creation_time` no se utiliza como evidencia de la fecha de realización de la sesión.

La verificación técnica reproducible, los comandos utilizados y los límites de interpretación se conservan en:

`04_Trazabilidad/VERIFICACION_MULTIMEDIA_WALK.md`

## 6. Relación con las notas WALK-NTEC

Las imágenes asociadas a `WALK-NTEC-01`, `WALK-NTEC-02` y `WALK-NTEC-03`, versionadas por primera vez el 15/09/2026, se conservan en:

`10_Autoria/reconstrucciones_posteriores/`

Se clasifican como **reconstrucciones posteriores**, no como notas de campo contemporáneas.

Por tanto:

- no se utilizan para acreditar la fecha histórica de la sesión;
- no cuentan como notas de campo tomadas durante la sesión;
- las tres sesiones WALK-NTEC figuran en la bitácora **sin nota de campo contemporánea**;
- la cobertura de notas contemporáneas queda en **13/16**.

## 7. Conclusión documental

Para el cierre se consolidan como fechas de sesión:

- `WALK-TEC-01`: **12/08/2026**
- `WALK-TEC-02`: **12/08/2026**
- `WALK-TEC-03`: **13/08/2026**
- `WALK-NTEC-01`: **16/08/2026**
- `WALK-NTEC-02`: **16/08/2026**
- `WALK-NTEC-03`: **22/08/2026**

Las fechas anteriores `18/08/2026` y `24/08/2026` eran fechas de elaboración/ratificación de las actas y fueron usadas incorrectamente como fechas de sesión en los encabezados históricos de las transcripciones.

Las anotaciones manuscritas `07/2026` se conservan sin modificación y se documentan como errores materiales de consignación del mes, sin ocultarlas ni sustituir la evidencia primaria.

Para `WALK-TEC-01`, el `creation_time = 05/08/2026` se conserva sin modificación como metadato interno del MP4 procesado y **no se utiliza para fechar la sesión**. La fecha `12/08/2026` queda establecida mediante evidencia documental independiente y anterior al cambio de las transcripciones, además de la correspondencia de identidad y duración del MP4 verificado.

Con esta separación explícita entre metadato del contenedor, fecha de sesión, fecha del acta y fecha de catalogación, **queda atendida la observación del informe docente del 17/09/2026 sobre `WALK-TEC-01`**. No se alteran transcripciones ni evidencia primaria y no se utilizan las reconstrucciones NTEC como prueba contemporánea.
