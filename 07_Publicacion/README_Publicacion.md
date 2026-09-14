# 07_Publicacion — FabroGym

## Propósito

Esta carpeta conserva el manuscrito y artefactos de publicación/replicación asociados al proyecto FabroGym. El registro Zenodo publicado se mantiene como evidencia histórica externa.

> **Importante para B1:** `07_Publicacion/` **no es el paquete canónico de datos y análisis de la Entrega Final**. La única cadena canónica y evaluable es `07_Datos/`.

## Contenido

- `manuscrito_final.tex` — fuente canónica del informe/manuscrito;
- `manuscrito_final.pdf` — PDF regenerado desde la fuente;
- `compilar_manuscrito.py` — compilación reproducible de la entrega académica;
- `RETROSPECTIVA_EXAMEN_SUSPENSO.md` — apoyo auditable de la retrospectiva incorporada también en el informe;
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

Etiqueta de cierre declarada en el informe para la entrega terminal:

`v2.0.2-final`

El manuscrito no debe editarse después de este cierre documental; el tag anterior `v2.0.1-final` se conserva como línea base histórica previa, no como identificador terminal de esta nueva corrección.

## Autoría histórica y equipo del examen

Los autores consignados en artefactos históricos de publicación y en el depósito Zenodo corresponden a la participación acumulada durante el desarrollo del proyecto y se conservan por integridad académica.

El equipo que realiza el cierre, defensa y examen final de este corte está conformado por:

- **Mera Arias Erick Jhair** — `Emeraxs`;
- **Mora Duarte Alex José** — `amorad35`;
- **Ponce Rivera Mery Helenmey** — `Mery-003`.

Alvia Villegas Erick Adalberto y Vaca Romero David Octavio mantienen únicamente las contribuciones y autoría históricas que realmente les corresponden. No se les atribuyen evidencias del corte actual. La delimitación canónica se encuentra en `../10_Autoria/EQUIPO_EXAMEN_FINAL.md`.

## Estado de la corrección §16

El informe final incorpora de forma explícita:

1. la tabla de efectos corregida de §13, con `n_unidades=6` e `interpretable=NO` para inferencia poblacional;
2. la limitación de la encuesta `n=70` dentro de amenazas a la validez;
3. la explicación del cierre ético de ENTR-02, ENTR-03, ENTR-04 y ENTR-06;
4. el repositorio canónico y la etiqueta de cierre `v2.0.2-final` declarada como vigente para la entrega terminal;
5. la sección **“Retrospectiva del examen suspenso / Failed-exam correction retrospective”**, con corrección, evidencia y responsable documentado;
6. la delimitación entre autoría histórica y equipo actual de examen.

El informe conserva estos elementos en estado terminal y no contiene marcadores de trabajo abierto para el cierre §16.

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
