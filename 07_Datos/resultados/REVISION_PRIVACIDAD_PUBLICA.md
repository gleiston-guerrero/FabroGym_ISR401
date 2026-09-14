# Revisión automática de privacidad — F3-07 / B6

**Estado automático:** **SIN HALLAZGOS AUTOMÁTICOS BLOQUEANTES**.

## Criterio aplicado

- `07_Datos/` y los artefactos de publicación deben permanecer sin datos personales directos.
- La capa restringida cifrada se trata de forma separada.
- La presencia de un contenedor restringido expresamente documentado no constituye por sí sola un hallazgo bloqueante.
- El auditor no abre contenedores cifrados ni conoce contraseñas; por ello registra ese límite técnico sin inferir un estado que no pueda observar.

## Alcance de la auditoría

- Archivos inspeccionados por nombre/extensión: **965**.
- CSV inspeccionados en `07_Datos/datos_crudos` y `datos_procesados`: **20**.
- CSV no legibles: **0**.
- Hallazgos automáticos bloqueantes: **0**.
- Advertencias automáticas: **0**.

## Capa restringida documentada

- `02_Evidencias/00_Restringido/evidencias_restringidas.7z` — **DOCUMENTADO** — Contenedor de evidencia restringida previsto por el proyecto y versionado mediante Git LFS. Debe permanecer cifrado/protegido y la clave no debe almacenarse en el repositorio.
- `02_Evidencias/00_Restringido/fichas_tecnicas.csv` — **DOCUMENTADO** — Inventario técnico de evidencia (códigos, duración, códec, tamaño y SHA-256). La guía específica de FabroGym indica conservar este formato.
- `10_Autoria/fotos_equipo/02_Fotos_Aplicacion/A11 Fotos_Originales_Cuestionario.7z` — **DOCUMENTADO** — Contenedor de originales A11 para preservar EXIF. Solo es admisible si está cifrado/protegido y la clave permanece fuera del repositorio.

## Resultado automático

No se detectaron hallazgos automáticos bloqueantes con las reglas aplicadas.

## Verificaciones informativas

- **A6_EXIF_OK** — `10_Autoria/exif_inventario.csv` — 5 registros F3-01 documentan fecha EXIF, dispositivo y SHA-256 válidos
- **CONTROL_CUSTODIA_RESTRINGIDA** — `02_Evidencias/00_Restringido/evidencias_restringidas.7z` — contenedor clasificado en capa restringida; la clave/credencial no se almacena en rutas públicas del repositorio y el auditor no extrae su contenido
- **CONTROL_CUSTODIA_RESTRINGIDA** — `10_Autoria/fotos_equipo/02_Fotos_Aplicacion/A11 Fotos_Originales_Cuestionario.7z` — contenedor clasificado en capa restringida; la clave/credencial no se almacena en rutas públicas del repositorio y el auditor no extrae su contenido
- **LFS_RESTRINGIDO_ESPERADO** — `02_Evidencias/00_Restringido/evidencias_restringidas.7z` — puntero Git LFS documentado (size=1521924213 bytes; sha256:a1b9b56a4fddf469a39bab3a51bcc891c85c0d0ce70432bf8602513f84c24070)
- **RESTRINGIDO_DOCUMENTADO** — `02_Evidencias/00_Restringido/evidencias_restringidas.7z` — Contenedor de evidencia restringida previsto por el proyecto y versionado mediante Git LFS. Debe permanecer cifrado/protegido y la clave no debe almacenarse en el repositorio.
- **RESTRINGIDO_DOCUMENTADO** — `02_Evidencias/00_Restringido/fichas_tecnicas.csv` — Inventario técnico de evidencia (códigos, duración, códec, tamaño y SHA-256). La guía específica de FabroGym indica conservar este formato.
- **RESTRINGIDO_DOCUMENTADO** — `10_Autoria/fotos_equipo/02_Fotos_Aplicacion/A11 Fotos_Originales_Cuestionario.7z` — Contenedor de originales A11 para preservar EXIF. Solo es admisible si está cifrado/protegido y la clave permanece fuera del repositorio.

## Verificación técnica A6 — fotografías y EXIF

- Registros F3-01 en `10_Autoria/exif_inventario.csv`: **5**.
- Registros EXIF técnicamente válidos: **5**.
- Copias fotográficas en `02_Evidencias/Cuestionario/Fotos_Aplicacion/`: **5**.
- Resultado técnico A6: **CUMPLE**.

## Alcance visual/manual documentado

- Consentimientos censurados: **16**.
- Actas WALK: **6**.
- Fotografías públicas del cuestionario: **5**.
- Fotografías del equipo/autoria: **2**.
- Total de piezas visuales a revisar: **29**.

### Estado registrable desde este corte

- `02_Evidencias/00_Restringido/evidencias_restringidas.7z` está representado en este ZIP por un puntero Git LFS; el objeto binario restringido no está contenido en la exportación y su cifrado no se infiere desde el puntero.
- La búsqueda automática no detectó contraseñas o claves expuestas en las rutas públicas inspeccionadas.
- `A11 Fotos_Originales_Cuestionario.7z` permanece como contenedor de originales A11; el auditor no atribuye propiedades criptográficas que no pueda verificar con las herramientas disponibles.
- Las cinco fotografías públicas del cuestionario están registradas como copias públicas enmascaradas y enlazadas con sus originales en `10_Autoria/exif_inventario.csv`.
- Los consentimientos y actas públicas forman parte de la revisión visual declarada; el control automático no detectó identificadores directos en los CSV ni nombres de archivo públicos evaluados.

## Interpretación del código de salida

- `0`: no existen hallazgos automáticos bloqueantes; los límites de observación manual quedan documentados sin convertirlos en marcadores de trabajo inconcluso.
- `2`: existe al menos un hallazgo automático que debe corregirse antes del release/tag final.
