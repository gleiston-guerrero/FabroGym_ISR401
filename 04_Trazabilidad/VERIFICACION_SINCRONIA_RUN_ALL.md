# Verificación de sincronía y reproducibilidad de `run_all.py`

**Proyecto:** FabroGym — ISR-401  
**Fecha de verificación:** 2026-09-17  
**Alcance:** cierre de las observaciones técnicas sobre divergencia entre orquestadores y finales de línea de las salidas generadas.

## 1. Fuente canónica

La cadena oficial y evaluable permanece en:

`07_Datos/scripts/run_all.py`

La ruta `06_Experimento/scripts_analisis/run_all.py` se conserva únicamente como copia de compatibilidad y trazabilidad. Ambos archivos se mantienen **byte-idénticos** para evitar una segunda versión divergente del orquestador.

SHA-256 verificado en ambos archivos:

`8b5a3092bf9589970e15f2d686219fbdf0d95f2e93ce1552c3938fde2275782b`

Comprobación:

`cmp -s 06_Experimento/scripts_analisis/run_all.py 07_Datos/scripts/run_all.py`

Resultado: **sin diferencias**.

## 2. Guarda de ejecución

El orquestador detecta el directorio raíz mediante `ROOT` e identifica como canónica únicamente la ejecución desde `07_Datos`. La sincronización hacia `06_Experimento/resultados/` se realiza solo en ese caso. Si la copia de compatibilidad se ejecuta desde `06_Experimento`, no intenta borrar ni copiar su propio directorio de resultados.

## 3. Finales de línea deterministas

Las escrituras de texto del pipeline se fijaron explícitamente a **LF (`\n`)**:

- CSV generados con `lineterminator="\n"`;
- archivos Markdown/JSON generados con `newline="\n"`;
- escritores auxiliares de member checking y tamaño del efecto con LF explícito;
- reporte de privacidad con LF explícito;
- fuentes Python protegidas con `*.py text eol=lf` en `.gitattributes`.

Esto evita que una ejecución en Windows produzca CRLF por defecto en las salidas textuales del pipeline.

## 4. Pruebas ejecutadas sobre el snapshot de cierre

Se ejecutó:

`cd 07_Datos && python scripts/run_all.py`

Resultados verificados:

- ejecución completa sin errores;
- 16 sesiones procesadas;
- 70 respuestas de encuesta;
- 76 fragmentos de walkthrough;
- 4 RNF terminales;
- semilla reproducible `SEED = 401`;
- 38 archivos en `07_Datos/resultados/` y 38 en `06_Experimento/resultados/`;
- **0 diferencias byte a byte** entre ambos directorios de resultados;
- dos ejecuciones consecutivas del pipeline produjeron los mismos hashes en los 38 resultados;
- **0 archivos textuales generados con CRLF** en la comprobación realizada;
- las 38 salidas regeneradas conservaron los mismos bytes que las salidas presentes en el snapshot recibido.

También se ejecutó la copia de compatibilidad desde `06_Experimento`; terminó sin errores y reportó correctamente que la sincronización cruzada no aplica en una ejecución no canónica.

## 5. Estado

**Observación de divergencia entre `run_all.py`: atendida.**  
**Determinismo LF de las escrituras del pipeline: atendido para esta cadena analítica.**

El manifiesto SHA-256 raíz no se regenera en esta fase; debe generarse únicamente después de cerrar todas las correcciones pendientes del repositorio.
