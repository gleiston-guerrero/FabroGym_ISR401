# Control final de consentimientos - B6

La evaluación final reconoció la existencia de los consentimientos firmados y observó la forma documental de cuatro copias públicas censuradas que anteriormente declaraban Microsoft Word como creador/productor.

## Cierre de la observación documental

El 14 de septiembre de 2026 se sustituyeron las cuatro copias observadas por sus versiones escaneadas y censuradas de los formularios firmados:

- `ENTR-02_Consentimiento_Censurado.pdf` — código asignado P02 — fecha 27/07/2026.
- `ENTR-03_Consentimiento_Censurado.pdf` — código asignado P03 — fecha 27/07/2026.
- `ENTR-04_Consentimiento_Censurado.pdf` — código asignado P04 — fecha 27/07/2026.
- `ENTR-06_Consentimiento_Censurado.pdf` — código asignado P06 — fecha 29/07/2026.

La verificación técnica del corte actual confirma que las cuatro copias públicas tienen tres páginas, están compuestas por páginas escaneadas y no declaran Microsoft Word en los campos Creator/Producer. La revisión visual confirma que conservan la estructura del consentimiento, las autorizaciones específicas y la sección de declaración y firmas, manteniendo censurados los identificadores directos y las firmas en la copia pública.

No se realizó una reconstrucción artificial del contenido para aparentar un escaneo; se versionaron las copias escaneadas y censuradas suministradas para el cierre.

La matriz actualizada de metadatos se conserva en `07_Datos/resultados/tablas/B6_control_metadatos_consentimientos.csv`.

La separación pública/restringida, la finalidad académica, la minimización y la custodia se documentan en `08_Etica/B6_CUMPLIMIENTO_ETICA_PRIVACIDAD.md` y `07_Datos/PRIVACIDAD_CAPAS.md`.

**Estado de la observación documental B6:** CERRADA en el corte actual.


## Reconciliación del conteo de consentimientos

El inventario verificable de sesiones contiene **16 consentimientos individuales**: 10 asociados a `ENTR-01..10`, 3 a `WALK-TEC-01..03` y 3 a `WALK_NTEC_01..03`. Esta cantidad coincide con las **16 sesiones** documentadas del trabajo de campo. La tabla `07_Datos/resultados/tablas/B6_control_metadatos_consentimientos.csv` registra esas mismas 16 copias públicas.

La guía de cierre menciona textualmente **17 consentimientos**, pero en el expediente reproducible disponible no existe un decimoséptimo formulario individual de sesión que pueda identificarse sin duplicar o reclasificar artificialmente otro documento. Por integridad académica, la diferencia se registra como **discrepancia de conteo de la guía frente al inventario verificable**, no como un archivo faltante del repositorio.

El expediente ético contiene además `13_A13_Participantes_Externos_FabroGym_Firmado.pdf` y `Adenda_Segunda_Ronda_FabroGym_Firmado.pdf` como documentos complementarios. No se contabilizan como un consentimiento individual adicional.

### Rutas de verificación

- Ruta canónica: `02_Evidencias/Consentimientos/`
- Ruta espejo para el comando literal de la guía: `08_Etica/consentimientos/`

Los 16 PDFs del espejo son **byte-idénticos** a sus equivalentes de la ruta canónica y no constituyen evidencia adicional. Así, el comando de la guía sobre `08_Etica/consentimientos/*.pdf` puede ejecutarse sin mover ni duplicar conceptualmente los consentimientos.
