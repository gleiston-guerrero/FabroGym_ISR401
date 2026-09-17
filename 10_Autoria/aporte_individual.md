# Aporte individual — FabroGym

**Proyecto:** FabroGym — ISR-401  
**Entrega:** Entrega 4 (2B / Defensa Final)  
**Repositorio:** `https://github.com/gleiston-guerrero/FabroGym_ISR401`  
**Integrantes/autores del proyecto:** Alvia Villegas Erick Adalberto, Mera Arias Erick Jhair, Mora Duarte Alex José, Ponce Rivera Mery Helenmey y Vaca Romero David Octavio.  
**Criterio de corte:** se distingue el trabajo posterior a la guía de los aportes históricos previos, sin eliminar ni reasignar autoría.

## 1. Propósito

Este documento conserva la atribución real de las contribuciones del proyecto. Para el corte posterior a la guía diferencia la actividad efectivamente versionada en ese periodo de los aportes previos, sin convertir esa diferencia temporal en una exclusión de la autoría.

No se inventan evidencias recientes, no se redistribuye trabajo y las capturas añadidas para Alvia y Vaca se identifican expresamente como capturas actuales de commits históricos.

## 2. Criterio de inclusión

- Solo se registran contribuciones respaldadas por commits existentes en el repositorio oficial.
- No se atribuyen tareas a un integrante si el historial Git no permite verificar esa relación.
- Los commits de merge no se usan por sí solos como evidencia principal cuando existe un commit específico.
- Las actividades colaborativas en Discord se documentan en `10_Autoria/bitacora_sesiones.csv` y se contrastan con la actividad Git verificable.
- La evidencia firmada histórica se conserva en `10_Autoria/aporte_individual_FIRMA.pdf`. La interpretación vigente de autoría se documenta en `10_Autoria/EQUIPO_EXAMEN_FINAL.md` y `04_Trazabilidad/ACTA_RECONOCIMIENTO_AUTORIA_EQUIPO.md`; la solicitud del 15/09/2026 queda como antecedente.
- Los cambios locales todavía no versionados no se presentan como aportes cerrados ni se les asigna un SHA inexistente.
- El commit que contenga esta última sincronización documental constituirá el corte final de contenido previo al tag; su SHA no se inserta dentro de este mismo archivo para evitar una referencia circular.

---

## 3. Mera Arias Erick Jhair

**Usuario Git verificado:** `Emeraxs`

| Actividad verificable | Artefacto / ruta | Commit | Tipo de aporte |
|---|---|---|---|
| Incorporar y ajustar el MVP académico | `05_MVP/` | `f24ae7f94055b501849067ec778676ba01625053` | Integración técnica |
| Congelar el paquete experimental destinado al prerregistro OSF | `06_Experimento/` | `9ef8ff6f4f3bd4d8671519a4798940b7b93e05eb` | Experimento / consolidación |
| Documentar reproducción, procedencia y uso del paquete canónico | `07_Datos/README_datos.md` | `7a99ec78711d708f603f8cf92f93220d174b4f53` | Reproducibilidad |
| Incorporar diccionario de datos | `07_Datos/diccionario_datos.csv` | `9e0a4a8e9dbec2a30b31f84d030d18622756866a` | Documentación de datos |
| Incorporar licencia del paquete anonimizado | `07_Datos/LICENSE-DATA.txt` | `f920fdec7beab161fa250891f86fd6ebeca5c683` | Publicación / licencia |
| Registrar el depósito Zenodo | `07_Datos/registro_deposito.md` | `94589ad7df7df603b2e0f9d22f941261b736eb12` | Ciencia abierta |
| Crear el índice y reglas de integridad de `10_Autoria` | `10_Autoria/README.md` | `cd7647fc96a01bccf9d722c0ef8828fa09f12e4b` | Autoría documental |
| Incorporar bitácora de sesiones | `10_Autoria/bitacora_sesiones.csv` | `88e78574353674875f0c3a4401d067535f2b41f6` | Trazabilidad de autoría |
| Normalizar evidencia fotográfica del equipo | `10_Autoria/fotos_equipo/` | `c1593702cb90ef9b234e1061210ac0bf82a6d21d` | Evidencia de autoría |
| Documentar compilación reproducible del ERS/SRS | `README.md` | `fa7873c35aa63575745378b94427b8b75ac0519b` | Reproducibilidad documental |
| Actualizar bitácora, aporte individual y materiales de defensa del cierre | `09_Defensa/`; `10_Autoria/` | `d4e34c1cf763728a6938b0fc99f9f76f20a0f095` | Cierre documental |
| Incorporar evaluación FAIR/F-UJI y metadatos de preservación/citación | `fair_assessment.pdf`; `FAIR_CHECKLIST.md`; `CITATION.cff`; `README.md`; `CHANGELOG.md` | `889475ed74a492466133730f1fee56ee0f64a5de` | FAIR / preservación / metadatos |
| Actualizar el reporte de revisión de privacidad pública con la lógica vigente | `07_Datos/resultados/REVISION_PRIVACIDAD_PUBLICA.md` | `bed95950312096597d5167f555f2de04e89fae60` | Privacidad / cierre B6 |
| Actualizar checklist final, README de autoría y checklist FAIR del cierre | `09_Defensa/checklist_defensa_final.md`; `10_Autoria/README.md`; `FAIR_CHECKLIST.md` | `d4a07e097906402db182de0de7c958a6095b90fd` | Cierre documental / verificación |
| Sincronizar aporte individual, bitácora e inventario EXIF con el estado de cierre | `10_Autoria/aporte_individual.md`; `10_Autoria/bitacora_sesiones.csv`; `10_Autoria/exif_inventario.csv` | `128c314849a1895cb7b0582609a85b546dfbb350` | Autoría / trazabilidad de cierre |
| Actualizar el reporte de privacidad y consolidar el estado A6 previo al cierre | `07_Datos/resultados/REVISION_PRIVACIDAD_PUBLICA.md`; `README.md` | `3a2914e986cad5897a7c357e869fb05bb2fb8a1d` | Privacidad / reproducibilidad documental |
| Corregir precondiciones, excepciones y flujos alternativos observados en §4 | `01_ERS/ERS_SRS_2B_v2.0.tex`; `01_ERS/ERS_SRS_2B_v2.0.pdf` | `1dd541b57101ee370ed6c1ad094fda6c8901f009` | Ingeniería de requisitos / casos de uso |
| Sincronizar los dos `run_all.py` y fijar política LF del pipeline | `.gitattributes`; `06_Experimento/scripts_analisis/run_all.py`; `07_Datos/scripts/run_all.py` | `53d17a01f22e282769536753c0ae0c8fe25dd4ab` | Reproducibilidad / §12 |
| Registrar la verificación de sincronía y reproducibilidad del pipeline | `04_Trazabilidad/VERIFICACION_SINCRONIA_RUN_ALL.md` | `318f4eb3cae0ee70f116038837f8694634c4bee4` | Verificación técnica / §12 |
| Verificar metadatos técnicos de WALK-TEC-01 | `04_Trazabilidad/VERIFICACION_MULTIMEDIA_WALK.md` | `d995cdb3afdf86cea84a103e0b1fa1cf1e116f68` | Trazabilidad multimedia |
| Retirar las seis capturas A2 observadas por el docente | `10_Autoria/capturas/`; documentación A2 | `0bf5014ab71fc1c634dc4d23023a577b4c816f52` | Autoría / saneamiento A2 |
| Documentar la verificación de las capturas propias de Alvia y Vaca | `04_Trazabilidad/VERIFICACION_CAPTURAS_ALVIA_VACA_20260917.md`; inventario A2 | `bf82034456649d25f9ad920ba3c11105d78fccec` | Autoría / verificación A2 |
| Eliminar las copias de Alvia depositadas accidentalmente en la raíz | raíz del repositorio; `10_Autoria/capturas/` | `ce89a2b42b8d1fdd1d86bfb7875c4ed393a6b205` | Limpieza documental A2 |
| Sincronizar línea base, FAIR y manuscrito con el cierre posterior a `v2.0.4-final` | `FAIR_CHECKLIST.md`; `07_Publicacion/README_Publicacion.md`; `07_Publicacion/manuscrito_final.*` | `3e16b35d9420cd56c3af909257ac54067ced9ca2` | Saneamiento documental §3 / §16 |

**Síntesis:** participación verificable en MVP, experimento, paquete `07_Datos`, reproducibilidad, publicación científica, autoría, defensa, privacidad y cierre FAIR/F-UJI.

---

## 4. Mora Duarte Alex José - aportes propios; sin actividad posterior a la guía

**Usuario Git verificado:** `amorad35`

| Actividad verificable | Artefacto / ruta | Commit | Tipo de aporte |
|---|---|---|---|
| Incorporar metadatos ORCID en la citación | `CITATION.cff` | `8431a3be8451df678a5c14d1d911f35265b4b012` | Metadatos |
| Incorporar evidencia del registro OSF | `06_Experimento/osf_registration.pdf` | `ee9901dd500751a7f1e912cdb784278719aa2f95` | Ciencia abierta |
| Actualizar README del experimento con OSF | `06_Experimento/README.md` | `00634f8ce4b225af6a27a60670398161a1264dff` | Documentación |
| Incorporar fuente editable UML | `03_Modelado/Diagramas_UML/` | `981f2b290e70e008c4ca3a1d7c5ac85a6254ba67` | Modelado |
| Incorporar modelos i* editables | `03_Modelado/Diagramas_UML/` | `ab266852820586621b6ed4ac1e3d8cf452b6df59`; `8c240a7337e28887f9e296ddd9c6878c24667504` | Modelado |
| Registrar codificación independiente | `10_Autoria/doble_codificacion/02_codificacion_mora.csv`; `.xlsx` | `e86e0488d1b70587b17566450ac4ed34ec10598f` | Doble codificación |
| Incorporar cálculo reproducible de acuerdo e IC95 % | `10_Autoria/doble_codificacion/` | `57edc42b7ff37a0a1b0a1c79e00abe1f737d4a9e` | Análisis reproducible |
| Actualizar checksums de `07_Datos` | `07_Datos/checksums_datos.sha256` | `5ea7e897ce23f3e6789d70067d4262c4eb1cd9c7` | Integridad |
| Incorporar fuentes editables de modelado en A3 | `10_Autoria/fuentes_editables/` | `37b04f8c3aff4352c844d1091c51371bba2ae322` | Autoría / modelado |
| Incorporar cinco fotografías originales del cuestionario | `02_Evidencias/Cuestionario/Fotos_Aplicacion/` | `5ad09c3ca5b0f55c4da4e18e7989ffba31fd587c` | Evidencia de campo |
| Corregir adaptación responsive del MVP sin alterar lógica | `05_MVP/` | `ce9dcfc7977ab6717d68ee2e71a680c8611fe03f` | Integración técnica / interfaz |
| Registrar checksums finales de integridad del MVP | `05_MVP/` | `20329ff70cbbc35f26611f2eba5ee52b8b5f2b52` | Integridad / reproducibilidad |
| Consolidar `07_Datos` como paquete canónico de análisis | `07_Datos/README_datos.md` | `2d57a9144aa5eefc18cc8a256805efaa65e1a223` | Reproducibilidad / B1 |
| Aclarar el rol de publicación frente a la cadena canónica | `07_Publicacion/README_Publicacion.md` | `361b46b8049d9083bb2d50ff414af0c9e90e1538` | Publicación / B1 |
| Consolidar el cierre canónico y estado final 2B | `README.md`; `CHANGELOG.md` | `df7550601b421c47e71c8e41865560c4dcbe4a5d` | Cierre canónico / documentación |

**Síntesis:** participación verificable en OSF, metadatos, modelado editable, doble codificación, integridad de datos, evidencia de campo, paquete canónico y cierre técnico del MVP.

---

## 5. Ponce Rivera Mery Helenmey

**Usuario Git verificado:** `Mery-003`

| Actividad verificable | Artefacto / ruta | Commit | Tipo de aporte |
|---|---|---|---|
| Actualizar mockups del rol Instructor | `03_Modelado/Mockups/04_Instructor/` | `6be79a82c1c169ffae9865e30ee1569057f93a1d` | Modelado |
| Actualizar mockups del rol Cliente | `03_Modelado/Mockups/05_Cliente/` | `f7c9524023ef3156026b4dd1fe82f0b85cd62b22` | Modelado |
| Reorganizar consentimientos censurados | `02_Evidencias/Consentimientos/` | `1c601523dba2aab510b2f1392bc21c32ab7513a0` | Ética / evidencia |
| Registrar codificación independiente | `10_Autoria/doble_codificacion/03_codificacion_ponce.csv`; `.xlsx` | `ae278a145989ecef7de869ec35031fe1bdc1bdaa` | Doble codificación |
| Corregir CSV de codificación independiente | `10_Autoria/doble_codificacion/03_codificacion_ponce.csv` | `1b30176d5db7f072a0c5aea2e40147bbd661acb9` | Calidad de datos |
| Documentar y verificar el uso de IA | `10_Autoria/declaracion_uso_ia.md` | `c6c206a5c129dfb00a76eb1228dbe4f500634b72` | Transparencia / IA |
| Incorporar correspondencia verificable con la organización | `10_Autoria/correspondencia/` | `87d667969192f9f86c19ae70848acec06008ea30` | Coordinación |
| Incorporar el video real de defensa | `09_Defensa/video_defensa.mp4` | `631579ced1e93029829166dde5db03cae6299806` | Evidencia audiovisual / defensa |
| Sincronizar documentación y manifiesto de cierre de defensa | `09_Defensa/` | `2b8b50cd440702e791e784abf33654167749a635` | Defensa / integridad |
| Incorporar el aporte individual firmado disponible | `10_Autoria/aporte_individual_FIRMA.pdf` | `ab26e952f59a862486921d4c86bb13ecc98eaec5` | Autoría / conformidad |
| Actualizar verificación de privacidad pública y evidencia A6 | `07_Datos/resultados/REVISION_PRIVACIDAD_PUBLICA.md`; `10_Autoria/exif_inventario.csv` | `ade8366361cf0c32d302d4b879a5446ee39884ca` | Privacidad / evidencia de campo |
| Cerrar evidencia A6 y trazabilidad de fotografías | `02_Evidencias/Cuestionario/Fotos_Aplicacion/`; `10_Autoria/exif_inventario.csv`; documentación A6 | `5542e050ca8a492ffd528f01cbde497b958ad922` | Evidencia A6 / trazabilidad |
| Actualizar checksums SHA-256 generales con las rutas vigentes del repositorio | `checksums.sha256` | `5961a4a6d231bf1419ab6bc0bde4a3fd0587c70d` | Integridad / cierre |
| Estabilizar la reproducibilidad y los checksums de `07_Datos` | `.gitattributes`; `07_Datos/checksums_datos.sha256`; `07_Datos/scripts/calcular_efecto_perfiles.py` | `ed4fbf40fa6c5a4222adada63589c94afee36f36` | Reproducibilidad / integridad |
| Sincronizar los 19 flujos alternativos corregidos con la matriz | `04_Trazabilidad/matriz_trazabilidad.csv` | `0d42923be7070ed67030ae3095495f9c09b11266` | Trazabilidad / §4 |
| Fijar LF en scripts auxiliares del pipeline | `06_Experimento/scripts_analisis/`; `07_Datos/scripts/` | `6a68f3cbb86d294930651feb74c7c286422fbd69` | Reproducibilidad / §12 |
| Aclarar la cadena canónica y el procedimiento reproducible | `06_Experimento/README.md`; `07_Datos/README_datos.md` | `6244ea87e1f96638f5d09a882f9dfa8447835171` | Documentación B1 / §12 |
| Cerrar documentalmente la fecha de sesión de WALK-TEC-01 | `04_Trazabilidad/ACLARACION_FECHAS_WALK.md` | `ab8d8978204e90c849bd10cb4b042f747148dcc3` | Trazabilidad multimedia |
| Consolidar el cierre documental de autoría A2 | `10_Autoria/`; retrospectivas | `fccdb9d9c619871d3cd307b148b1c7c3486876ee` | Autoría / §15 |
| Consolidar retrospectiva y saneamiento documental posterior al informe | `CHANGELOG.md`; retrospectivas; `04_Trazabilidad/ACLARACION_COMMIT_FEF33D8.md` | `37f02ac47189bf37fadd010445cb4a8679e6d50e` | Saneamiento documental §3 / §16 |

**Síntesis:** participación verificable en mockups, ética, doble codificación, uso de IA, coordinación, defensa final, evidencia firmada de autoría, integridad y reproducibilidad pre-tag.

---

## 6. Alvia Villegas Erick Adalberto — autoría histórica verificable; depósito A2 propio del 17/09/2026
**Usuario Git verificado:** `Erick-Alvia`

Sus aportes históricos se conservan según Git. Para atender §15, y por instrucción directa del docente, Alvia realiza y deposita personalmente tres capturas desde su sesión autenticada.

| Actividad histórica verificable | Artefacto / ruta | Commit histórico | Captura A2 vigente |
|---|---|---|---|
| Actualización de diagramas de casos de uso | `03_Modelado/Diagramas_UML/02_Casos_de_Uso/` | `98fe055ea547306f272e7c651937ad4c8fcbae98` | `2026-09-17_Erick-Alvia_commit_98fe055_diagramas_casos_uso.png` |
| Incorporación de transcripciones anonimizadas de walkthrough | `02_Evidencias/Transcripciones/` | `af636224d7437106ba746a0ed73de924fbad2c55` | `2026-09-17_Erick-Alvia_commit_af63622_transcripciones_walkthrough.png` |
| Actualización de evidencia restringida | `02_Evidencias/00_Restringido/` | `e73613ef9d1908abcde7560fbf725deeffaae4e7` | `2026-09-17_Erick-Alvia_commit_e73613e_evidencia_restringida.png` |

El depósito canónico de estas imágenes fue realizado por `Erick-Alvia` en `47cac4329ebb25bf0bae36f75698ebf24b81eeb0`. El depósito previo `e4881d11624007c0850bec64d613909bd45c40e6` quedó superado por haber ubicado las imágenes accidentalmente en la raíz. Ambos se interpretan únicamente como **depósito de evidencia histórica A2**, no como nuevo aporte técnico al contenido mostrado.

## 7. Vaca Romero David Octavio — autoría histórica verificable; depósito A2 propio del 17/09/2026
**Usuario Git verificado:** `David-Bs1`

Sus aportes históricos se conservan según Git. Para atender §15, y por instrucción directa del docente, Vaca realiza y deposita personalmente tres capturas desde su sesión autenticada.

| Actividad histórica verificable | Artefacto / ruta | Commit histórico | Captura A2 vigente |
|---|---|---|---|
| Checksums SHA-256 de la Entrega 4 | `checksums.sha256` | `8e664455294b272b007c8f8a600781a1d5a809f7` | `2026-09-17_David-Bs1_commit_8e66445_checksums_entrega4.png` |
| Consentimientos censurados de walkthrough | `02_Evidencias/` | `10a010ff3bff283f7bf33b7eb56097e867f9c967` | `2026-09-17_David-Bs1_commit_10a010f_consentimientos_walkthrough.png` |
| Evidencias de validación walkthrough | `02_Evidencias/` | `9cd5b20742afcd80cd79adbac41b15896888e082` | `2026-09-17_David-Bs1_commit_9cd5b20_evidencias_walkthrough.png` |

El depósito canónico de estas imágenes fue realizado por `David-Bs1` en `2ecbe55e722ea3bee3725dc011681956ac3eb499`. Se interpreta únicamente como **depósito de evidencia histórica A2**, no como nuevo aporte técnico al contenido mostrado.

## 8. Sesión histórica de cierre verificada - 11 de septiembre de 2026

Esta sesión ocurrió antes del corte de correcciones del 15/09/2026. Se conserva para acreditar el trabajo realmente realizado en ese momento y no se utiliza para reasignar autoría.

Entre las **22:07 y 22:52 (UTC-05:00)**, Mera, Mora y Ponce permanecieron reunidos de forma **Remota — Discord** durante el bloque de cierre. La modalidad y participación están documentadas en la bitácora; las actividades concretas se contrastan con el historial Git.

| Integrante | Actividad versionada durante el bloque | Commit(s) |
|---|---|---|
| Mera Arias Erick Jhair | FAIR/F-UJI, metadatos, citación y preservación | `889475ed74a492466133730f1fee56ee0f64a5de` |
| Ponce Rivera Mery Helenmey | Video final, cierre documental de defensa y aporte firmado | `631579ced1e93029829166dde5db03cae6299806`; `2b8b50cd440702e791e784abf33654167749a635`; `ab26e952f59a862486921d4c86bb13ecc98eaec5` |
| Mora Duarte Alex José | Corrección responsive del MVP y checksums de integridad | `ce9dcfc7977ab6717d68ee2e71a680c8611fe03f`; `20329ff70cbbc35f26611f2eba5ee52b8b5f2b52` |

El merge `d0a32b007deba27353d57d877b84e1d28047b55f` es un commit técnico de integración y no se utiliza como evidencia principal de contribución individual.

## 9. Relación con otras evidencias

Esta relación se contrasta con:

- `10_Autoria/bitacora_sesiones.csv`;
- `10_Autoria/aporte_individual_FIRMA.pdf`;
- `10_Autoria/capturas/`;
- `.mailmap`;
- historial Git del repositorio;
- artefactos existentes en las rutas citadas.

## 10. Declaración de integridad

Las contribuciones incluidas se basan en evidencia versionada verificable. No se fabrican commits, no se atribuyen cambios locales no versionados y no se reasignan aportes históricos.

La autoría del proyecto corresponde a los cinco integrantes según sus contribuciones verificables. El trabajo posterior a la guía se interpreta según el historial del periodo evaluado. Ningún aporte se elimina, reasigna ni presenta con una autoría distinta de la real.

## 11. Corte documental de cierre

Este documento resume los aportes verificables versionados hasta el corte PRE-CHECKSUM vigente. El historial Git del repositorio constituye la fuente canónica para identificar los commits posteriores de cierre.

No se fija aquí el SHA del commit que contiene este propio documento, con el fin de evitar una referencia circular u obsoleta.

El identificador del cierre terminal de este ciclo de correcciones es `v2.0.5-final`. El procedimiento exige congelar primero el contenido, incorporar la verificación previa firmada y regenerar/verificar ambos manifiestos SHA-256 antes de crear y publicar esa etiqueta sobre el último commit de integridad. `v2.0.4-final` permanece como referencia histórica del corte evaluado el 17/09/2026 y no se mueve ni se sobrescribe.

La creación y publicación de dicha etiqueta y las operaciones posteriores de preservación no requieren modificar nuevamente este documento.
