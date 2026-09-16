# 07_Publicacion — FabroGym

## Propósito

Esta carpeta conserva el manuscrito y artefactos de publicación/replicación asociados al proyecto FabroGym. El registro Zenodo publicado se mantiene como evidencia histórica externa.

> **Importante para B1:** `07_Publicacion/` **no es el paquete canónico de datos y análisis de la Entrega Final**. La única cadena canónica y evaluable es `07_Datos/`.

## Contenido

- `manuscrito_final.tex` — fuente canónica del informe/manuscrito;
- `manuscrito_final.pdf` — PDF regenerado desde la fuente;
- `compilar_manuscrito.py` — compilación reproducible de la entrega académica;
- `RETROSPECTIVA_EXAMEN_SUSPENSO.md` — espejo documental de la retrospectiva canónica `../10_Autoria/retrospectiva_equipo.md`;
- tablas y figuras sincronizadas con `07_Datos/`;
- artefactos de metadatos y publicación;
- copia local normalizada del paquete asociado al depósito Zenodo.

## Ejecución canónica del análisis

Desde la raíz del repositorio:

```bash
cd 07_Datos
python -m pip install -r scripts/requirements.txt
python scripts/run_all.py
```

`07_Publicacion/` no constituye una segunda cadena analítica. Sus tablas y figuras son productos de publicación sincronizados con la cadena canónica de `07_Datos/`.

## ERS/SRS

La única ERS/SRS académica vigente está en:

```text
01_ERS/ERS_SRS_2B_v2.0.pdf
01_ERS/ERS_SRS_2B_v2.0.tex
```

## Repositorio y línea base declarada

Repositorio canónico de evaluación:

`https://github.com/gleiston-guerrero/FabroGym_ISR401`

Línea base histórica publicada previa al cierre:

`v2.0.2-final`

Esa etiqueta se conserva intacta como línea base histórica. Las correcciones posteriores corresponden al corte PRE-CHECKSUM que antecede a la etiqueta terminal `v2.0.3-final`, creada únicamente después de cerrar todo el contenido y verificar los manifiestos SHA-256 finales.

## Autoría histórica y equipo del examen

Los autores consignados en artefactos históricos de publicación y en el depósito Zenodo corresponden a la participación acumulada durante el desarrollo del proyecto y se conservan por integridad académica.

Para la **evaluación del examen suspenso**, los integrantes evaluados son **Mera Arias Erick Jhair** y **Ponce Rivera Mery Helenmey**. **Mora Duarte Alex José** participa únicamente como apoyo no evaluado y todo aporte suyo conserva su propia autoría. **Alvia Villegas Erick Adalberto** y **Vaca Romero David Octavio** permanecen como autores/participantes históricos en los artefactos donde realmente intervinieron; su autoría no se elimina ni se reasigna.

El estado de composición y evidencia individual evaluable se documenta en `../10_Autoria/EQUIPO_EXAMEN_FINAL.md` y se formaliza en `../04_Trazabilidad/solicitud_cambio_composicion_equipo.pdf`.

## Estado de la corrección §16

El informe final queda recompilado **después de la regeneración reproducible de §12** y mantiene correspondencia con las salidas canónicas de `07_Datos/resultados/`.

El informe incorpora de forma explícita:

1. la tabla de efectos corregida de §13, con `n_unidades=6` e `interpretable=NO` para inferencia poblacional;
2. la limitación de la encuesta `n=70` dentro de amenazas a la validez;
3. el resultado de saturación de códigos `6.306 %` y la estabilización axial `1.852 %`, sin convertir el incumplimiento del umbral estricto en un resultado positivo;
4. la explicación del cierre ético de ENTR-02, ENTR-03, ENTR-04 y ENTR-06;
5. el repositorio canónico, `v2.0.2-final` como línea base histórica publicada y `v2.0.3-final` como etiqueta terminal declarada, creada únicamente después de verificar los manifiestos SHA-256 finales;
6. la sección **“Retrospectiva del examen suspenso / Failed-exam correction retrospective”**, actualizada con §4, §12, §13 y §16;
7. la retrospectiva canónica `../10_Autoria/retrospectiva_equipo.md`, con qué se corrigió, responsables documentados y aprendizajes del equipo;
8. la distinción entre autoría histórica del proyecto, apoyo no evaluado de Mora y composición evaluada del examen suspenso conformada por Mera y Ponce.

El manuscrito se congela en este corte de §16; cualquier corrección posterior que altere resultados obligaría a recompilarlo antes del cierre terminal.

## Compilación reproducible del manuscrito final

Desde `07_Publicacion/`:

```bash
python compilar_manuscrito.py
```

El script genera `manuscrito_final.pdf` desde el contenido canónico de `manuscrito_final.tex`, ejecuta LaTeX y bibliografía, comprueba que no queden citas o referencias indefinidas y elimina los temporales de compilación. La cabecera Springer Nature permanece en la fuente editorial; la vista académica transitoria permite recompilar el PDF sin depender de que `sn-jnl.cls` esté instalado externamente en el entorno de evaluación.

La compilación fija la fecha de construcción y elimina metadatos variables de pdfTeX, de modo que **dos ejecuciones equivalentes producen el mismo SHA-256 del PDF**.

## Estado de Zenodo

El depósito publicado es la versión 2.0.0 con DOI específico:

`10.5281/zenodo.22237884`

El depósito publicado se conserva como evidencia histórica externa. Las correcciones posteriores del repositorio no se presentan como byte-idénticas a ese snapshot.

## Licencia

Los datos y documentación pública anonimizada se documentan bajo CC BY 4.0. La evidencia restringida se rige por las reglas de custodia/cifrado del expediente ético.
