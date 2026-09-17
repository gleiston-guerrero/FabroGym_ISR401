# Aclaración documental de mensajes de commits históricos de cierre

**Fecha de aclaración:** 17 de septiembre de 2026  
**Repositorio:** `https://github.com/gleiston-guerrero/FabroGym_ISR401`

## Hecho verificado

El commit histórico `fef33d84301f73c230fa6f21d4488604029cc8bd` tiene como mensaje **“agregar script seguro para regenerar checksum raíz”**. Sin embargo, la revisión del historial Git confirma que ese commit modificó únicamente `checksums.sha256`; no incorporó ningún script al árbol del repositorio.

## Alcance de la aclaración

- No se reescribe, elimina ni altera el commit histórico.
- Se reconoce expresamente que su mensaje no describe con precisión el cambio realmente versionado.
- Para efectos de trazabilidad, el cambio efectivo de `fef33d8` se interpreta únicamente como una modificación histórica de `checksums.sha256`.
- No se utiliza ese mensaje como evidencia de la existencia de un script de regeneración.
- Los manifiestos terminales de la nueva línea de cierre se regenerarán y verificarán nuevamente después de congelar el contenido; por tanto, el manifiesto asociado a ese commit no se presenta como manifiesto vigente del cierre posterior al informe del 17/09/2026.

## Aclaración adicional: `c641540` y `dc5a228`

El informe docente del 17/09/2026 verificó el repositorio desde un clon limpio y determinó que el manifiesto raíz asociado al cierre `v2.0.4-final` no validaba: 157 de sus 993 entradas fallaban por diferencias CRLF/LF. Por ello, los mensajes históricos de `c641540` y `dc5a228`, que afirmaban "993 entradas verificadas sin fallos", **no se usan como evidencia vigente de integridad**.

Se conserva el historial Git sin modificar. La corrección consiste en documentar expresamente que esas afirmaciones correspondieron a una comprobación histórica que no reprodujo el resultado en el clon limpio evaluado. El cierre posterior al informe debe regenerar ambos manifiestos sobre el contenido congelado y demostrar cero fallos antes de crear `v2.0.5-final`.

## Estado

Quedan aclaradas, sin reescribir el historial Git, la discrepancia del mensaje de `fef33d8` y las afirmaciones históricas de verificación de `c641540` y `dc5a228`. Ninguno de esos mensajes se presenta como evidencia del estado terminal posterior al informe del 17/09/2026.
