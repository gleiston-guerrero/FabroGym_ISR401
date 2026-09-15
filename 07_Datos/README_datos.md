# Paquete canónico de datos de FabroGym

`07_Datos/` es el **único paquete canónico, ejecutable y evaluable de datos y análisis para la Entrega 4 (2B)**.

Reúne los insumos públicos anonimizados, la cadena consolidada de análisis y sus productos reproducibles. La existencia de datos o scripts históricos en `06_Experimento/` documenta procedencia y evolución metodológica, pero **no constituye una segunda cadena canónica**.

## Regla de unicidad B1

Para la evaluación final:

```text
Paquete canónico:        07_Datos/
Orquestador oficial:     07_Datos/scripts/run_all.py
Dependencias oficiales:  07_Datos/scripts/requirements.txt
Datos crudos oficiales:  07_Datos/datos_crudos/
Salidas oficiales:       07_Datos/datos_procesados/ y 07_Datos/resultados/
```

`06_Experimento/` se conserva como fuente metodológica/histórica. `07_Publicacion/` conserva artefactos de publicación y depósitos históricos. Ninguna de esas carpetas sustituye a `07_Datos/` para B1.

## Estructura

```text
07_Datos/
├── datos_crudos/
├── datos_procesados/
├── scripts/
├── resultados/
├── diccionario_datos.csv
├── README_datos.md
├── LICENSE-DATA.txt
├── checksums_datos.sha256
├── desviaciones.md
└── registro_deposito.md
```

## Procedencia

Los insumos de `datos_crudos/` proceden de evidencia y matrices previamente versionadas, incluida la documentación metodológica de `06_Experimento/`. Los scripts consolidados derivan de la cadena desarrollada durante el proyecto.

`datos_crudos/PROVENIENCIA_FUENTES.md` documenta la fuente inmediata de cada familia de insumos.

Esta procedencia **no convierte `06_Experimento/` en un segundo paquete activo**.

## Corte analítico del cuestionario

La muestra analítica oficial del cuestionario está formada por **70 respuestas**. El archivo canónico es:

```text
datos_crudos/encuesta_clientes_anonimizada.csv
```

El corte utilizado por el proyecto quedó congelado hasta **31/08/2026 23:58:25**. Las respuestas posteriores no se incorporan retroactivamente.

## Separación entre entrada y productos

- `datos_crudos/`: insumos fuente congelados;
- `datos_procesados/`: salidas generadas por `scripts/run_all.py`;
- `resultados/`: tablas, figuras y resúmenes reproducibles.

## Requisitos

Se requiere Python 3. La reproducción fue verificada con Python 3.12.13 y las dependencias declaradas en:

```text
scripts/requirements.txt
```

Instalación:

```bash
python -m pip install -r scripts/requirements.txt
```

## Ejecución reproducible — única orden oficial

Desde la raíz de `07_Datos/`:

```bash
python scripts/run_all.py
```

No se requieren pasos manuales intermedios.

### Validación estructural previa

El orquestador ejecuta validaciones tempranas sobre las matrices de codificación,
candidatos RNF y member checking. También pueden verificarse de forma aislada:

```bash
python scripts/validar_entradas.py \
  --codificacion datos_crudos/codificacion_walkthroughs.csv \
  --rnf datos_crudos/candidatos_RNF_explicabilidad_member_checked.csv \
  --member-checking datos_crudos/member_checking_estructurado.csv
```

Para el corte terminal esperado, la validación debe informar **76 filas de
codificación, 4 candidatos RNF y 12 decisiones de member checking**, sin errores
de esquema.

El pipeline regenera:

- `datos_procesados/`;
- tablas de resultados;
- figuras;
- resúmenes analíticos;
- artefactos de desviaciones definidos por la cadena.

## Comparación técnico vs. no técnico — criterio terminal F3-04

La comparación de perfiles usa como unidad independiente la **sesión de walkthrough** y no las categorías temáticas derivadas. El conjunto contiene **6 unidades independientes**: 3 sesiones técnicas y 3 no técnicas.

La salida canónica es:

```text
resultados/tablas/tabla_efecto_perfiles.csv
```

La medida principal es delta de Cliff sobre la proporción de fragmentos pertinentes a explicabilidad por sesión, con IC95% obtenido mediante bootstrap exacto de las seis sesiones. La tabla expone explícitamente `n_unidades` e `interpretable`. En este proyecto, `interpretable = NO` significa **no interpretable como inferencia poblacional** debido al tamaño extremadamente pequeño de unidades independientes; la estimación se conserva como descripción exploratoria del caso.

El cuestionario de 70 respuestas no se utiliza para este contraste porque no contiene variable técnico/no técnico ni una escala de explicabilidad.

## Integridad SHA-256

El manifiesto `checksums_datos.sha256` usa **rutas relativas a la raíz de `07_Datos/`**. Esta decisión es intencional: evita prefijos duplicados y permite ejecutar literalmente el comando de verificación desde el directorio canónico.

Verificación terminal del paquete:

```bash
cd 07_Datos
python scripts/run_all.py
sha256sum -c checksums_datos.sha256
```

El resultado esperado es que **todas las entradas terminen en `OK` y existan 0 fallos**. El propio manifiesto se excluye de su contenido para evitar una referencia hash circular.

La regeneración de los dos manifiestos terminales se realiza **solo después de cerrar el contenido del repositorio**, desde la raíz:

```bash
python 07_Datos/scripts/regenerar_manifiestos_sha256.py
```

Ese script regenera primero `07_Datos/checksums_datos.sha256` y luego `checksums.sha256`. El manifiesto raíz cubre también el manifiesto de `07_Datos` y calcula los hashes sobre los bytes físicamente presentes en la entrega. Por ello `sha256sum -c checksums.sha256 --quiet` funciona también cuando la exportación contiene un puntero Git LFS: se verifica el puntero entregado, mientras su `oid sha256` se conserva únicamente como referencia al objeto LFS remoto.

## Privacidad

Este paquete incluye únicamente datos públicos anonimizados o seudonimizados aptos para el análisis reproducible. La evidencia identificable/restringida se gobierna mediante la política de `08_Etica/` y no forma parte de los datos crudos públicos de B1.

## Relación con Zenodo

El depósito Zenodo 2.0.0 (DOI `10.5281/zenodo.22237884`) es un registro histórico publicado. `07_Datos/` es el paquete canónico de la **entrega académica vigente** y no se afirma que sea idéntico byte a byte a ese depósito histórico.

## Limitaciones

- El cuestionario no contiene perfil técnico/no técnico ni una escala Likert de explicabilidad.
- La saturación estricta de códigos no alcanza el umbral del 5 %.
- Los SHA-256 de multimedia restringida documentan evidencia que no forma parte de la capa pública de datos.
- El member checking dispone de evidencia documental pública, pero no de grabación audiovisual.

## Estado B1

**CANÓNICO / EJECUTABLE / EVALUABLE: `07_Datos/`**

No existe otra carpeta que deba utilizarse como cadena oficial para reproducir los resultados de la Entrega Final.
