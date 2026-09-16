# 10_Autoria — Evidencia de autoría y trabajo propio

**Proyecto:** FabroGym — ISR-401  
**Entrega:** Entrega 4 (2B / Defensa Final)  
**Repositorio:** `https://github.com/gleiston-guerrero/FabroGym_ISR401`

## 1. Propósito

Esta carpeta reúne la evidencia verificable de autoría, contribución individual y trabajo propio del equipo FabroGym.

La rúbrica final exige que `10_Autoria/` exista con los elementos A1 a A12 como un conjunto completo. Esta carpeta complementa el historial Git y los artefactos técnicos; no los sustituye.

La retrospectiva requerida para el examen suspenso se conserva en `10_Autoria/retrospectiva_equipo.md`. Ese documento es transversal al conjunto A1-A12: registra las correcciones de §4, §12, §13 y §16, quién intervino en cada bloque y los aprendizajes del cierre, sin crear evidencia histórica inexistente.

## 2. Composición del examen suspenso y autoría histórica

Para la **evaluación del examen suspenso**, los integrantes evaluados son **Mera Arias Erick Jhair (`Emeraxs`)** y **Ponce Rivera Mery Helenmey (`Mery-003`)**.

**Mora Duarte Alex José (`amorad35`)** participa únicamente como **apoyo no evaluado**. Cualquier aporte suyo debe permanecer firmado con su propio usuario y no se reasigna ni se contabiliza como aporte de los dos evaluados.

**Alvia Villegas Erick Adalberto** y **Vaca Romero David Octavio** conservan la autoría histórica de los aportes realizados antes de dejar de participar en esta etapa. Sus contribuciones no se eliminan ni se redistribuyen.

La composición se formaliza en `../04_Trazabilidad/solicitud_cambio_composicion_equipo.pdf` y la interpretación canónica se mantiene en `EQUIPO_EXAMEN_FINAL.md`.

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
- **16 sesiones empíricas**: 10 de tipo `entrevista` y 6 de tipo `walkthrough`, incorporadas con su fecha canónica y su `ruta_nota_campo`.

El CSV incluye las columnas `tipo` y `ruta_nota_campo`. Toda fila de tipo `entrevista` o `walkthrough` apunta a una de las 16 notas reales depositadas en `10_Autoria/notas_campo/`. Las sesiones internas no requieren nota de campo.

Por tanto, el conteo correcto para A5 es **16/16 sesiones empíricas con nota**, no 28/28 filas de trabajo interno.

### A2 — `capturas/`

Las 42 capturas existentes se conservan con su autoría real. Para el **examen suspenso**, sólo se evalúan las capturas propias de:

- Mera (`Emeraxs`): 13;
- Ponce (`Mery`/`Mery-003`): 19.

Mora (`amorad35`) conserva 10 capturas propias como evidencia histórica/apoyo no evaluado. Alvia y Vaca no continúan en esta evaluación y no se les exige crear capturas nuevas. El detalle se encuentra en `capturas/README.md`.

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

En el corte actual hay **16 notas de campo asociables a las 16/16 sesiones empíricas**: 10/10 entrevistas, 3/3 walkthroughs técnicos y 3/3 walkthroughs no técnicos. Las notas `WALK-NTEC-01`, `WALK-NTEC-02` y `WALK-NTEC-03` ya están depositadas y sus rutas y SHA-256 se registran en el inventario. El detalle y las discrepancias históricas de fecha de dos notas técnicas se documentan en:

```text
10_Autoria/notas_campo/README.md
10_Autoria/notas_campo/inventario_notas_campo.csv
```

La cobertura A5 queda completa respecto del universo empírico versionado: **16/16 filas empíricas enlazadas a 16 notas reales**. Las otras 28 filas de A1 permanecen clasificadas como `trabajo_interno`.

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

`aporte_individual.md` distingue los **aportes evaluables de Mera y Ponce**, el **apoyo no evaluado de Mora** y los **aportes históricos de Alvia y Vaca**. Para cada aporte registrado se conservan actividad, ruta, rol y commit real o referencia al historial Git; ningún trabajo previo se borra, redistribuye ni atribuye a otro integrante.

La conformidad firmada disponible se conserva como:

```text
10_Autoria/aporte_individual_FIRMA.pdf
```

Ese PDF corresponde al **corte histórico del 11 de septiembre de 2026**, anterior a la formalización de la composición del examen suspenso del 15/09/2026. Por ello conserva la composición y URL vigentes en aquel corte y **no define la composición evaluada actual**. La fuente vigente para esta evaluación es `../04_Trazabilidad/solicitud_cambio_composicion_equipo.pdf`, complementada por `EQUIPO_EXAMEN_FINAL.md`. El PDF histórico no se reescribe ni se vuelve a firmar, para preservar su integridad documental.

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
