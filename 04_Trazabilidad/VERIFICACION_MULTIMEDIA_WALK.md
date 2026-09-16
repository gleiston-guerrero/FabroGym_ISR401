# Verificación técnica de multimedia WALK

**Fecha de verificación:** 16 de septiembre de 2026  
**Objetivo:** comprobar identidad, duración y metadatos técnicos de los cuatro MP4 observados durante la aclaración de fechas.

## Archivos verificados

| Archivo | SHA-256 verificado | Duración FFprobe | Coincide con ficha técnica |
|---|---|---:|---|
| `2026-08-12_Video_WALK-TEC-01_Ing.Soft.mp4` | `147eb88ebb07818179611e51e9381cff1f781f53408153f6623c03731326aa5a` | 1485.667 s (~24:46) | Sí |
| `2026-08-12_Video_WALK-TEC-02_Ing.Soft.mp4` | `7285c6d3ff83df7377ba5479cce8d66d9634b9a80a7bfb7fa2958842d3901d0e` | 1599.292 s (~26:39) | Sí |
| `2026-08-16_Video_WALK-NTEC-01_Instructor.mp4` | `893e21b1bf812da5dcad62cd2df801e0f27e7f17d6e57b649e9429ef8342d250` | 1072.917 s (~17:53) | Sí |
| `2026-08-16_Video_WALK-NTEC-02_Recepcionista.mp4` | `35426caae7e710c34a4d8609a9b5e04e98b89042cab6d69d1171f398ec994d98` | 1076.542 s (~17:57) | Sí |

## Metadatos de contenedor

Los cuatro archivos declaran `encoder = HandBrake 1.10.2 2025090600`. `WALK-NTEC-01` incorpora además el rótulo `clideo.com`.

Los valores `creation_time` recuperados del contenedor no son homogéneos respecto de las fechas de sesión:

- `WALK-TEC-01`: `2026-08-05T16:54:12Z`
- `WALK-TEC-02`: `2026-08-13T15:22:09Z`
- `WALK-NTEC-01`: `2026-08-30T21:27:02Z`
- `WALK-NTEC-02`: `2026-08-30T21:31:27Z`

Dado que los archivos son versiones procesadas/transcodificadas, esos valores no se consideran marcas de tiempo de captura y **no se utilizan para acreditar la fecha de realización de la sesión**.

## Resultado

La verificación demuestra que los cuatro MP4 revisados son byte-idénticos a los objetos catalogados por SHA-256 en `02_Evidencias/00_Restringido/fichas_tecnicas.csv`.

La fecha de sesión se sustenta documentalmente mediante la trazabilidad previa al commit `35c1893`, desarrollada en `04_Trazabilidad/ACLARACION_FECHAS_WALK.md`, y no mediante el `creation_time` del contenedor MP4.
