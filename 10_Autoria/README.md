# 10_Autoria — Evidencia de autoría y trabajo propio

**Proyecto:** FabroGym — ISR-401  
**Entrega:** Entrega 4 (2B / Defensa Final)  
**Repositorio:** `https://github.com/gleiston-guerrero/FabroGym_ISR401`

## 1. Propósito

Esta carpeta reúne la evidencia verificable de autoría, contribución individual y trabajo propio del equipo FabroGym.

La rúbrica final exige que `10_Autoria/` exista con los elementos A1 a A12 como un conjunto completo. Esta carpeta complementa el historial Git y los artefactos técnicos; no los sustituye.

## 2. Equipo de cierre y autoría histórica

El **equipo actual de cierre y examen final** está conformado por Mera (`Emeraxs`), Mora (`amorad35`) y Ponce (`Mery-003`).

Alvia Villegas Erick Adalberto y Vaca Romero David Octavio conservan la autoría histórica de los aportes realizados durante etapas anteriores del proyecto. Esos aportes no se eliminan ni se reasignan, pero tampoco se presentan como pendientes A2 del cierre actual. El estado exacto se documenta en `10_Autoria/EQUIPO_EXAMEN_FINAL.md`.

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

Registro cronológico de sesiones reales de trabajo.

Cada fila debe documentar, según corresponda:

- identificador de sesión;
- fecha y horario;
- modalidad;
- participantes;
- usuarios Git;
- rutas trabajadas;
- decisiones tomadas;
- commits reales producidos;
- fuente de evidencia y observaciones.

La versión congelada no contiene marcadores provisionales de commit.

### A2 — `capturas/`

Capturas reales de trabajo individual o colaborativo sobre FabroGym. El inventario del equipo actual de cierre contiene 13 capturas de `Emeraxs`, 19 de `Mery` y 10 de `amorad35`, para un total de **42 capturas atribuibles**. El detalle de atribución está en `10_Autoria/capturas/README.md`.

Cada captura se relaciona con:

- herramienta utilizada;
- artefacto trabajado;
- usuario o integrante;
- fecha/hora cuando esté disponible.

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

Notas reales obtenidas durante actividades de elicitación, observación o validación.

No se reconstruyen notas posteriormente para aparentar evidencia de campo.

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

Las **dos fotografías reales del equipo disponibles en el repositorio** se encuentran directamente en `10_Autoria/fotos_equipo/`, renombradas con la fecha EXIF `2026-07-27`. La subcarpeta `01_fotos_equipo/` conserva únicamente documentación de referencia sobre esas fotografías. No se anuncian fotografías de equipo inexistentes. El inventario EXIF final refleja únicamente archivos físicamente presentes y trazables: **2 fotos de equipo, 4 JPG de entorno y 5 originales de aplicación del cuestionario**, para un total de **11 registros**.

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

`aporte_individual.md` documenta las contribuciones de cierre que pueden verificarse actualmente mediante commits y artefactos para **Mera, Mora y Ponce**, que conforman el equipo actual de cierre.

Para cada aporte registrado se conservan actividad, ruta, rol y commit real. Los aportes históricos de Alvia y Vaca permanecen en Git y en los artefactos correspondientes; no se borran ni se reasignan.

La conformidad firmada disponible se conserva como:

```text
10_Autoria/aporte_individual_FIRMA.pdf
```

Su alcance debe interpretarse según las personas que realmente la firmaron y no como sustituto de la evidencia individual exigida a cada integrante.

### A11 — `exif_inventario.csv`

Inventario técnico de fotografías utilizadas como evidencia.

El inventario final contiene **11 registros verificables**:

- 2 fotografías del equipo;
- 4 fotografías JPG de entorno de `02_Evidencias/Fotos_Entorno/`;
- 5 fotografías originales de aplicación del cuestionario.

Para cada registro se conserva, cuando está disponible en el archivo fuente:

- fecha EXIF;
- dispositivo;
- SHA-256;
- estado EXIF;
- ruta trazable dentro del repositorio.

Para las cinco fotografías del cuestionario se conserva además la relación entre el original restringido y la copia pública enmascarada. Las copias públicas pueden tener hash distinto del original por el enmascaramiento; el inventario primario se basa en los originales preservados.

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
6. dos fotografías reales de equipo con EXIF verificable y cinco fotografías de aplicación del cuestionario con trazabilidad EXIF/copia pública;
7. declaración de uso de IA consistente;
8. `aporte_individual.md` sincronizado con los commits finales;
9. privacidad automática sin bloqueos y revisión humana completada;
10. `git status` limpio antes de crear el tag.

La verificación terminal del repositorio se realiza sobre el estado final mediante los comandos de integridad y Git establecidos en la guía de cierre, inmediatamente antes de crear la etiqueta anotada terminal. No se mantiene un PDF adicional de “verificación previa” como requisito del cierre. La composición del equipo actual y el estado de evidencia individual vigente se documentan en `10_Autoria/EQUIPO_EXAMEN_FINAL.md`.

## 8. Estado de esta carpeta

`10_Autoria/` se mantiene como evidencia viva hasta el último commit previo al tag.

La versión de cierre mantiene sincronizados los documentos de autoría con el corte documental del examen y no conserva marcadores provisionales en la bitácora.

No se deben crear evidencias ficticias ni modificar evidencia histórica ya válida.
