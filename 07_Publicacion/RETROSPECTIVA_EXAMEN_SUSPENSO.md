# Retrospectiva del examen suspenso — FabroGym

**Proyecto:** FabroGym — ISR-401  
**Artefacto principal asociado:** `07_Publicacion/manuscrito_final.tex` / `manuscrito_final.pdf`  
**Repositorio canónico de evaluación:** `https://github.com/gleiston-guerrero/FabroGym_ISR401`  
**Última etiqueta publicada:** `v2.0.2-final` (línea base histórica; no se mueve)  
**Siguiente etiqueta candidata:** `v2.0.3-final`, solo después de cerrar bloqueos y regenerar manifiestos al final

## 1. Propósito

Este documento resume las correcciones realizadas después de la revisión del examen suspenso y sirve como apoyo auditable del informe final. No sustituye al manuscrito: la retrospectiva también está incorporada dentro de `manuscrito_final.tex` y su PDF generado.

La corrección preserva la autoría histórica y evita confundir el trabajo correctivo reciente con la composición evaluable del equipo. La guía y los artefactos académicos mantienen a **Alvia, Mera, Mora, Ponce y Vaca** dentro del alcance evaluable mientras no exista una autorización docente posterior que lo modifique.

El trabajo de corrección reciente está documentado principalmente para Mera (`Emeraxs`), Mora (`amorad35`) y Ponce (`Mery-003`). El inventario A2 actual no localiza capturas suficientes para Alvia ni Vaca; por integridad académica no se fabrican, reasignan ni retrofechan evidencias. La declaración canónica está en `10_Autoria/EQUIPO_EXAMEN_FINAL.md`.

## 2. Correcciones ejecutadas

| Sección | Hallazgo de revisión | Corrección terminal | Evidencia principal | Responsable documentado |
|---|---|---|---|---|
| §15 Autoría | La corrección previa redujo sin autorización documentada el alcance del examen a tres integrantes y el inventario fotográfico requería normalización. | Se restituye el alcance evaluable de cinco integrantes según la guía; A2 declara 13 capturas de Mera, 10 de Mora, 19 de Ponce y 0 localizadas para Alvia/Vaca, sin fabricar evidencia. El EXIF se consolida con 11 registros reales. | `10_Autoria/EQUIPO_EXAMEN_FINAL.md`, `10_Autoria/capturas/README.md`, `10_Autoria/README_A11_EXIF.md`, `10_Autoria/exif_inventario.csv` | Revisión documental del cierre; la evidencia faltante de Alvia/Vaca permanece como pendiente real. |
| §7 Consentimientos | ENTR-02, ENTR-03, ENTR-04 y ENTR-06 estaban representados públicamente por PDFs de origen Word, lo que no acreditaba visualmente el escaneo firmado. | Se sustituyeron por copias escaneadas y censuradas de los formularios firmados. En el corte actual, `pdftotext` devuelve 0 palabras para los cuatro PDFs públicos. | `02_Evidencias/Consentimientos/`, `08_Etica/CONTROL_CONSENTIMIENTOS_FINAL.md`, `07_Datos/resultados/tablas/B6_control_metadatos_consentimientos.csv` | **Mera Arias / `Emeraxs`**, corrección registrada en `a68594a`. |
| §13 Resultados | Se usaban categorías temáticas como unidades independientes. | La unidad independiente pasó a ser la sesión WALK: 3 técnicas + 3 no técnicas (`n_unidades=6`). Se reporta Cliff's delta `0.555556`, IC95% `[-0.333333, 1.000000]` e `interpretable=NO` para inferencia poblacional. La encuesta `n=70` queda fuera del contraste de perfiles porque no contiene perfil técnico/no técnico ni ítems de explicabilidad. | `07_Datos/scripts/calcular_efecto_perfiles.py`, `07_Datos/resultados/tablas/tabla_efecto_perfiles.csv`, ERS/SRS y manuscrito final | **Mora Duarte / `amorad35`**, corrección base registrada en `01c87fb`; sincronización terminal revisada por el equipo de cierre. |
| §16 Informe | El informe no reunía en un único artefacto la tabla corregida, la limitación del cuestionario, la explicación ética, la línea base declarada y una retrospectiva con responsables. | El manuscrito integra esos elementos, distingue la línea base `v2.0.2-final` del siguiente cierre candidato y se recompila desde la fuente. | `07_Publicacion/manuscrito_final.tex`, `07_Publicacion/manuscrito_final.pdf`, `07_Publicacion/compilar_manuscrito.py` | Revisión cruzada del equipo de corrección; no altera la composición evaluable. |

## 3. Línea base declarada en el informe

El informe declara como repositorio canónico:

`https://github.com/gleiston-guerrero/FabroGym_ISR401`

La etiqueta de cierre declarada como vigente para la entrega terminal es:

`v2.0.2-final` permanece como línea base histórica publicada. El siguiente cierre candidato será `v2.0.3-final` únicamente después de resolver bloqueos y regenerar los manifiestos terminales.

El nombre de la etiqueta queda fijado en el informe para que el paso procedimental de cierre use exactamente ese identificador sobre el commit terminal, después de regenerar los manifiestos de integridad. El manuscrito no debe modificarse después de quedar congelado en este corte.

## 4. Regla de integridad

La retrospectiva no convierte limitaciones en evidencias inexistentes. En particular:

- no se crean capturas para integrantes históricos;
- no se inventa una sexta fotografía del cuestionario;
- no se reconstruyen firmas;
- no se transforma la encuesta de 70 respuestas en una escala de explicabilidad;
- no se tratan 18 categorías como 18 unidades independientes;
- no se afirma inferencia poblacional con tres sesiones por perfil.

El objetivo del cierre es que cada afirmación del informe pueda rastrearse a un artefacto real, un script reproducible o un registro verificable del repositorio.
