# Verificación técnica de multimedia WALK

**Proyecto:** FabroGym — ISR-401  
**Verificación inicial:** 16 de septiembre de 2026  
**Reverificación focal de `WALK-TEC-01`:** 17 de septiembre de 2026  
**Objetivo:** comprobar identidad, duración y metadatos técnicos de los MP4 observados y atender de forma explícita la observación docente sobre la diferencia entre `creation_time = 05/08/2026` y la fecha de sesión `12/08/2026` de `WALK-TEC-01`.

## 1. Archivos previamente verificados

| Archivo | SHA-256 verificado | Duración FFprobe | Coincide con ficha técnica |
|---|---|---:|---|
| `2026-08-12_Video_WALK-TEC-01_Ing.Soft.mp4` | `147eb88ebb07818179611e51e9381cff1f781f53408153f6623c03731326aa5a` | 1485.667 s (~24:46) | Sí |
| `2026-08-12_Video_WALK-TEC-02_Ing.Soft.mp4` | `7285c6d3ff83df7377ba5479cce8d66d9634b9a80a7bfb7fa2958842d3901d0e` | 1599.292 s (~26:39) | Sí |
| `2026-08-16_Video_WALK-NTEC-01_Instructor.mp4` | `893e21b1bf812da5dcad62cd2df801e0f27e7f17d6e57b649e9429ef8342d250` | 1072.917 s (~17:53) | Sí |
| `2026-08-16_Video_WALK-NTEC-02_Recepcionista.mp4` | `35426caae7e710c34a4d8609a9b5e04e98b89042cab6d69d1171f398ec994d98` | 1076.542 s (~17:57) | Sí |

## 2. Reverificación directa de `WALK-TEC-01` — 17/09/2026

Se volvió a analizar el archivo materializado correspondiente a `2026-08-12_Video_WALK-TEC-01_Ing.Soft.mp4`. La copia local recibida para la reverificación llevaba el sufijo `(1)` únicamente por descarga; su identidad se determinó por contenido.

### 2.1 Identidad del objeto audiovisual

- **SHA-256 calculado:** `147eb88ebb07818179611e51e9381cff1f781f53408153f6623c03731326aa5a`
- **SHA-256 registrado en `02_Evidencias/00_Restringido/fichas_tecnicas.csv`:** `147eb88ebb07818179611e51e9381cff1f781f53408153f6623c03731326aa5a`
- **Tamaño verificado:** `86 503 400` bytes, equivalente al tamaño reportado de aproximadamente `84 476 KiB`.
- **Duración de contenedor:** `1485.666667 s` (~24:45.667).
- **Video:** H.264, 1280×720, 24 fps.
- **Audio:** AAC, 48 kHz.

**Resultado:** el archivo reverificado es byte-idéntico al objeto catalogado por el proyecto para `WALK-TEC-01`.

### 2.2 Metadatos recuperados con FFprobe

El contenedor declara:

- `major_brand = mp42`
- `creation_time = 2026-08-05T16:54:12.000000Z`
- `date = 2026-08-05T16:54:12+0000`
- `encoder = HandBrake 1.10.2 2025090600`

Además, tanto el stream de video como el stream de audio contienen el mismo `creation_time = 2026-08-05T16:54:12.000000Z`.

Por tanto, **la existencia del valor 05/08/2026 queda confirmada y no se oculta ni se modifica**.

## 3. Interpretación del `creation_time` del 05/08/2026

El análisis técnico permite separar dos conceptos que no deben confundirse:

1. El archivo actual declara a **HandBrake 1.10.2** como codificador; por ello, el MP4 conservado es un archivo procesado/codificado.
2. El campo `creation_time = 2026-08-05T16:54:12Z` es un **metadato interno del contenedor MP4** y, por sí solo, no acredita la fecha en que se realizó la sesión.

Los artefactos conservados no permiten determinar de forma verificable por qué ese valor quedó escrito en el contenedor. Por ello, el proyecto no atribuye una causa que no pueda demostrar y tampoco modifica el archivo.

Para fechar `WALK-TEC-01` se utilizan las evidencias documentales de la sesión descritas en la sección siguiente, que ya estaban registradas antes de la corrección de las transcripciones. En consecuencia, **el `creation_time` del 05/08/2026 se conserva como metadato del archivo, pero no se utiliza como fecha de realización de la sesión**.

## 4. Sustento documental de la fecha de sesión `12/08/2026`

La fecha consolidada de `WALK-TEC-01` se apoya en evidencias independientes del `creation_time` del MP4:

| Evidencia | Fecha / dato | Valor probatorio para la cronología |
|---|---|---|
| Nota de campo `10_Autoria/notas_campo/2026-08-12_WALK-TEC-01_notas_campo.png` | manuscrito `12/08/2026`; duración `24'46 aprox.` | Evidencia de campo enlazada a la sesión; el informe docente del 17/09 acepta las notas WALK técnicas como contemporáneas. |
| `02_Evidencias/00_Restringido/fichas_tecnicas.csv` | `fecha_sesion = 2026-08-12`; duración `00:24:46`; mismo SHA-256 del MP4 | Registro técnico versionado desde el 01/09/2026, anterior al cambio de fecha de las transcripciones. |
| Commit `387d825` | 01/09/2026 | Incorporó/modificó la ficha técnica que ya vinculaba el objeto audiovisual con `WALK-TEC-01`. |
| `07_Datos/desviaciones.md` | cronología WALK desde 12/08/2026 | La cronología estaba documentada antes del commit `35c1893` que corrigió los encabezados de las transcripciones. |
| Acta `WALK-TEC-01_Acta.pdf` | fecha de **elaboración y ratificación** `18/08/2026`; duración `24:45 aprox.` | Corrobora la identidad/duración de la sesión; su fecha no se usa como fecha de ejecución porque el propio campo se define como elaboración/ratificación. |
| Consentimiento censurado | plantilla `Versión 1.0 - 12 de agosto de 2026`; fecha manuscrita con mes `07/2026` | Presenta una inconsistencia material interna y, por ello, no se utiliza de manera aislada para fijar la fecha de sesión. |

La duración de la nota (`24'46 aprox.`), la ficha (`00:24:46`), el acta (`24:45 aprox.`) y el MP4 reverificado (`24:45.667`) son coherentes entre sí y refuerzan la correspondencia entre esos artefactos y la misma sesión.

## 5. Cierre de la observación docente

Para `WALK-TEC-01` quedan diferenciados y documentados los siguientes hitos:

- **fecha de sesión:** `12/08/2026`;
- **`creation_time` del MP4 procesado:** `05/08/2026 16:54:12Z`;
- **fecha de elaboración/ratificación del acta:** `18/08/2026`;
- **fecha de procesamiento/catalogación de la ficha:** `01/09/2026`.

Estas fechas corresponden a campos y momentos documentales distintos y no se sustituyen entre sí.

**Conclusión técnica y documental:** el `creation_time = 05/08/2026` se mantiene íntegro como metadato interno del MP4, pero **no se emplea para fechar la sesión**. La fecha de realización de `WALK-TEC-01` se establece en **12/08/2026** porque está respaldada por la nota de campo contemporánea, la ficha técnica versionada con el mismo SHA-256 y duración, y la cronología del repositorio anterior a la corrección de las transcripciones.

**Estado de la observación del informe del 17/09/2026: ATENDIDA.**

## 6. Comandos de comprobación

Con el objeto LFS materializado, la verificación puede reproducirse mediante:

```bash
sha256sum "2026-08-12_Video_WALK-TEC-01_Ing.Soft.mp4"
ffprobe -v error -show_format -show_streams -of json \
  "2026-08-12_Video_WALK-TEC-01_Ing.Soft.mp4"
```

Los valores esperados para la identidad son:

```text
SHA-256: 147eb88ebb07818179611e51e9381cff1f781f53408153f6623c03731326aa5a
Duración: 1485.666667 s
creation_time: 2026-08-05T16:54:12.000000Z
encoder: HandBrake 1.10.2 2025090600
```
