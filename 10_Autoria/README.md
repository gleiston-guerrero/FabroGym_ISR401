# 10_Autoria — Evidencia de autoría y trabajo propio

**Proyecto:** FabroGym — ISR-401  
**Entrega:** Entrega 4 (2B / Defensa Final)  
**Repositorio:** `https://github.com/gleiston-guerrero/FabroGym_ISR401`

## 1. Propósito

Esta carpeta reúne la evidencia verificable de autoría, contribución individual y trabajo propio del equipo FabroGym.

La rúbrica final exige que `10_Autoria/` exista con los elementos A1 a A12 como un conjunto completo. Esta carpeta complementa el historial Git y los artefactos técnicos; no los sustituye.

La retrospectiva requerida para el examen suspenso se conserva en `10_Autoria/retrospectiva_equipo.md`. Ese documento es transversal al conjunto A1-A12: registra las correcciones de §4, §12, §13 y §16, quién intervino en cada bloque y los aprendizajes del cierre, sin crear evidencia histórica inexistente.

## 2. Equipo, autoría y corte de actividad

FabroGym conserva la autoría verificable de los cinco integrantes: **Alvia Villegas Erick Adalberto (`Erick-Alvia`)**, **Mera Arias Erick Jhair (`Emeraxs`)**, **Mora Duarte Alex José (`amorad35`)**, **Ponce Rivera Mery Helenmey (`Mery-003`)** y **Vaca Romero David Octavio (`David-Bs1`)**.

Para el corte posterior a la guía se distingue el trabajo realmente versionado durante ese periodo de los aportes históricos previos. Esa distinción no elimina integrantes ni autoría.

La interpretación canónica se mantiene en `EQUIPO_EXAMEN_FINAL.md` y `../04_Trazabilidad/ACTA_RECONOCIMIENTO_AUTORIA_EQUIPO.md`. La solicitud del 15/09/2026 se conserva únicamente como antecedente documental.

## 3. Principios de integridad

Toda evidencia incorporada en `10_Autoria/` debe:

- corresponder a una actividad real;
- conservar fecha y procedencia reales;
- no ser retrofechada;
- no ser reconstruida artificialmente para aparentar trabajo previo;
- no contener placeholders ni archivos vacíos que anuncien evidencia inexistente;
- utilizar hashes de commit reales cuando se cite trabajo versionado;
- mantener coherencia entre artefacto, persona responsable e historial Git;
- respetar las reglas de privacidad y la separación entre capa pública y restringida.

## 4. Estructura A1–A12

### A1 — `bitacora_sesiones.csv`

La bitácora distingue ahora dos universos que antes estaban mezclados conceptualmente:

- **28 sesiones de `trabajo_interno`**: coordinación, edición, modelado, documentación y commits del equipo.
- **16 sesiones empíricas**: 10 de tipo `entrevista` y 6 de tipo `walkthrough`. La cobertura de nota de campo se registra separadamente.

El CSV incluye las columnas `tipo` y `ruta_nota_campo`. En el corte corregido, **13 sesiones empíricas** enlazan una nota de campo contemporánea. `WALK-NTEC-01`, `WALK-NTEC-02` y `WALK-NTEC-03` mantienen `ruta_nota_campo` vacía y se declaran como sesiones **sin nota de campo contemporánea acreditable**. Los tres PNG correspondientes se preservan aparte como reconstrucciones posteriores.

Por tanto, el estado A5 verificable es **13/16 sesiones empíricas con nota contemporánea y 3/16 ausencias declaradas**, no 28/28 filas de trabajo interno.

### A2 — `capturas/`

La carpeta conserva **48 capturas auténticas**:

- Mera (`Emeraxs`): 13;
- Ponce (`Mery` / `Mery-003`): 19;
- Mora (`amorad35`): 10;
- Alvia (`Erick-Alvia`): 3 capturas tomadas el 16/09/2026 de commits históricos reales;
- Vaca (`David-Bs1`): 3 capturas tomadas el 16/09/2026 de commits históricos reales.

Las seis capturas nuevas no se retrofechan y no se interpretan como trabajo nuevo del examen suspenso. Solo hacen visible actividad histórica ya existente en Git.

El detalle se encuentra en `capturas/README.md` e `capturas/inventario_capturas_alvia_vaca.csv`.

### A3 — `fuentes_editables/`

Fuentes editables de diagramas y modelos utilizados en el proyecto.

Incluye, cuando corresponda:

```text
*.vpp
*.drawio
*.puml
```

Las exportaciones PNG/PDF/SVG no sustituyen la fuente editable cuando esta existe.

### A4 — `grabaciones/`

Grabaciones reales de sesiones de trabajo del equipo.

Deben corresponder a actividades efectivas de revisión, edición, discusión o toma de decisiones sobre FabroGym.

### A5 — `notas_campo/`

Notas reales obtenidas durante **sesiones empíricas de elicitación y validación**.

La cobertura A5 se calcula únicamente sobre las filas de `bitacora_sesiones.csv` cuyo `tipo` es `entrevista` o `walkthrough`. La bitácora contiene además **28 filas de `trabajo_interno`** para coordinación, edición, modelado, documentación y commits; esas filas no requieren nota de campo.

La fuente canónica para el universo empírico es `07_Datos/datos_crudos/sesiones_multimedia_desde_ficha_v3_1.csv`, que contiene **16 sesiones**: 10 entrevistas, 3 walkthroughs técnicos y 3 walkthroughs no técnicos.

En el corte corregido hay **13 notas de campo contemporáneas acreditables para 16 sesiones empíricas**: 10/10 entrevistas y 3/3 walkthroughs técnicos. `WALK-NTEC-01`, `WALK-NTEC-02` y `WALK-NTEC-03` se registran como sesiones sin nota contemporánea. Los tres PNG previamente tratados como notas se preservan, sin edición, como **reconstrucciones posteriores que no computan en A5**.

El detalle se documenta en:

```text
10_Autoria/notas_campo/README.md
10_Autoria/notas_campo/inventario_notas_campo.csv
10_Autoria/reconstrucciones_posteriores/README.md
10_Autoria/reconstrucciones_posteriores/inventario_reconstrucciones.csv
```

La cobertura A5 queda en **13/16 con nota contemporánea + 3/16 ausencias declaradas**. Las otras 28 filas de A1 permanecen clasificadas como `trabajo_interno`. Este parche no vuelve a modificar las transcripciones WALK. La explicación definitiva de los cambios de fecha y su verificación multimedia se conserva en `04_Trazabilidad/ACLARACION_FECHAS_WALK.md` y `04_Trazabilidad/VERIFICACION_MULTIMEDIA_WALK.md`.

### A6 — `fotos_equipo/`

La evidencia fotográfica de autoría se organiza en:

```text
10_Autoria/
└── fotos_equipo/
    ├── 2026-07-27_equipo_fabrogym_01.jpg
    ├── 2026-07-27_equipo_fabrogym_02.jpg
    ├── 01_fotos_equipo/
    │   └── README.md
    └── 02_Fotos_Aplicacion/
        └── A11 Fotos_Originales_Cuestionario.7z
```

Las **dos fotografías reales del equipo disponibles en el repositorio** se encuentran directamente en `10_Autoria/fotos_equipo/`, renombradas con la fecha EXIF `2026-07-27`. La subcarpeta `01_fotos_equipo/` conserva únicamente documentación de referencia sobre esas fotografías. No se anuncian fotografías de equipo inexistentes. El inventario EXIF final registra **todas las fotografías de evidencia físicamente identificadas en el corte**: 2 fotos de equipo, 18 fotografías de entorno y 5 fotografías de aplicación del cuestionario, para un total de **25 registros**. Cuando un archivo no conserva fecha o dispositivo EXIF, se declara `SIN_EXIF` o `EXIF_PARCIAL`; no se inventan metadatos.

Además, las **cinco copias públicas enmascaradas de aplicación del cuestionario** se encuentran en:

```text
02_Evidencias/Cuestionario/Fotos_Aplicacion/
```

Los originales utilizados para preservar EXIF se conservan dentro del contenedor restringido:

```text
10_Autoria/fotos_equipo/02_Fotos_Aplicacion/
A11 Fotos_Originales_Cuestionario.7z
```

Ese contenedor debe permanecer cifrado/protegido y su contraseña o clave no debe almacenarse en el repositorio.

### A7 — `doble_codificacion/`

Evidencia de doble codificación independiente de un subconjunto común del corpus de walkthroughs.

Debe conservar:

- las dos hojas independientes;
- el subconjunto codificado;
- el script de cálculo;
- kappa/acuerdo e intervalo de confianza.

### A8 — `correspondencia/`

Comunicaciones reales y fechadas con la organización relacionadas con el proyecto.

Antes de publicar cualquier pieza se revisa que no exponga datos personales no autorizados.

### A9 — `declaracion_uso_ia.md`

Declaración del uso de herramientas de IA por sección o artefacto relevante.

Debe indicar:

- herramienta;
- propósito;
- responsable de revisión;
- método de verificación;
- secciones donde no se utilizó IA, cuando corresponda.

### A10 — `aporte_individual.md` y evidencia firmada

`aporte_individual.md` conserva los aportes verificables de **los cinco integrantes** y distingue el trabajo posterior a la guía de la autoría histórica previa. Para cada aporte registrado se conservan actividad, ruta, rol y commit real o referencia al historial Git; ningún trabajo se borra, redistribuye ni atribuye a otro integrante.

La conformidad firmada disponible se conserva como:

```text
10_Autoria/aporte_individual_FIRMA.pdf
```

Ese PDF corresponde al **corte histórico del 11 de septiembre de 2026** y se conserva sin reescritura. La interpretación vigente de autoría se documenta en `EQUIPO_EXAMEN_FINAL.md` y `../04_Trazabilidad/ACTA_RECONOCIMIENTO_AUTORIA_EQUIPO.md`. La solicitud del 15/09/2026 se conserva solo como antecedente y no se utiliza como cambio unilateral de composición.

Su alcance debe interpretarse según las personas que realmente la firmaron y no como sustituto de la evidencia individual exigida a cada integrante.

### A11 — `exif_inventario.csv`

Inventario técnico de fotografías utilizadas como evidencia.

El inventario actual contiene **25 registros**:

- 2 fotografías del equipo;
- 18 fotografías del entorno de `02_Evidencias/Fotos_Entorno/`;
- 5 fotografías de aplicación del cuestionario.

De esos 25 registros, **20 conservan una fecha de captura en metadatos** y **5 se declaran `SIN_EXIF`** porque no exponen fecha ni dispositivo recuperables. Dos archivos adicionales conservan fecha pero no Make/Model y se marcan `EXIF_PARCIAL`.

Para cada registro se conserva, cuando está disponible:

- fecha EXIF;
- dispositivo;
- SHA-256;
- estado EXIF;
- ruta trazable dentro del repositorio.

La guía del examen contabilizó 26 fotografías suponiendo 3 fotos de equipo. El árbol verificable actual contiene **2 fotos de equipo + 18 de entorno + 5 de aplicación = 25 fotografías**. No se crea una tercera foto de equipo inexistente para forzar el conteo.

Para las cinco fotografías del cuestionario se conserva además la relación entre el original restringido y la copia pública enmascarada.

### A12 — `/.mailmap`

La evidencia A12 se mantiene en la raíz:

```text
/.mailmap
```

Su función es normalizar identidades históricas de Git hacia nombres y correos institucionales sin reescribir el historial.

No se crea una segunda `.mailmap` dentro de `10_Autoria/`.

## 5. Relación con el historial Git

El historial Git es evidencia central de autoría.

Reglas:

- cada contribución citada debe apuntar a commits reales;
- los integrantes activos deben usar identidad real y correo institucional;
- no se atribuyen a una persona commits producidos por otra;
- no se reescribe el historial para fabricar distribución de trabajo;
- los mensajes de commit deben describir el cambio realizado.

Para la revisión final se recomienda comprobar:

```bash
git shortlog -sne --all --use-mailmap
```

## 6. Privacidad

`10_Autoria/` contiene evidencia del trabajo del equipo y debe respetar la política definida en `08_Etica/`.

Antes del tag final se debe confirmar:

- que los contenedores restringidos estén cifrados/protegidos;
- que sus contraseñas no estén almacenadas en Git;
- que las copias públicas enmascaradas no revelen identificadores no autorizados;
- que los consentimientos, actas y correspondencia pública estén adecuadamente censurados.

El reporte automático vigente se conserva en:

```text
07_Datos/resultados/REVISION_PRIVACIDAD_PUBLICA.md
```

y actualmente documenta **0 hallazgos automáticos bloqueantes**.

## 7. Verificación de cierre

Antes de congelar la entrega se debe comprobar:

1. A1–A12 presentes y coherentes;
2. ausencia de archivos vacíos/placeholder;
3. hashes de commit citados existentes;
4. autores normalizados mediante `.mailmap`;
5. doble codificación reproducible;
6. inventario EXIF con 25 fotografías reales del corte (2 equipo + 18 entorno + 5 aplicación), declarando de forma explícita los archivos `SIN_EXIF` o `EXIF_PARCIAL`;
7. declaración de uso de IA consistente;
8. `aporte_individual.md` sincronizado con los commits finales;
9. privacidad automática sin bloqueos y revisión humana completada;
10. `git status` limpio antes de crear el tag.

La guía vigente del examen suspenso exige una **verificación previa firmada**. Por ello, `10_Autoria/verificacion_previa.pdf` debe generarse únicamente cuando el contenido del repositorio esté congelado, después de cerrar la evidencia A5/A11 y antes de los manifiestos terminales y de la etiqueta anotada. El documento debe reflejar el estado real de ese corte y ser firmado por los **dos integrantes evaluados del examen suspenso, Mera y Ponce**; no se reutiliza una verificación de una versión anterior. Mora puede apoyar la revisión, pero no firma como integrante evaluado.

## 8. Estado de esta carpeta

`10_Autoria/` se mantiene como evidencia viva hasta el último commit previo al tag.

La versión de cierre mantiene sincronizados los documentos de autoría con el corte documental del examen y no conserva marcadores provisionales en la bitácora.

No se deben crear evidencias ficticias ni modificar evidencia histórica ya válida.
