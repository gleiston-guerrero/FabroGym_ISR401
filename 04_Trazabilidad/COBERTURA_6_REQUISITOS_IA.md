# Cobertura terminal de los seis requisitos del componente inteligente

Este documento no crea requisitos nuevos. Consolida cómo la especificación vigente cubre los **seis aspectos** exigidos para el componente inteligente propuesto, estableciendo una correspondencia principal uno-a-uno entre cada aspecto y un requisito auditable. RNF-16 se conserva como requisito complementario de explicación del objetivo/restricciones, pero el requisito principal de explicabilidad para B5 es RNF-19.

| Aspecto exigido | RNF terminal | Métrica / umbral | Verificación | Estado |
|---|---|---|---|---|
| 1. Recomendación de rutina | `RNF-20` | Pertinencia validada por entrenador >=80% | `PV-RNF-20` sobre casos sintéticos predefinidos | PROPUESTO / NO IMPLEMENTADO |
| 2. Explicabilidad | `RNF-19` | 100% de sugerencias automáticas con criterio principal visible | `PV-RNF-19` | PROPUESTO / NO IMPLEMENTADO |
| 3. Equidad | `RNF-21` | Diferencia máxima de recomendaciones no pertinentes <=10 pp entre grupos | `PV-RNF-21` con datos sintéticos balanceados | PROPUESTO / NO IMPLEMENTADO |
| 4. Supervisión humana | `RNF-17` | 100% de rutinas con estado de revisión y procedencia visible | `PV-RNF-17` | PROPUESTO / NO IMPLEMENTADO |
| 5. Monitoreo post-despliegue | `RNF-22` | 100% de recomendaciones y decisiones humanas registradas; resumen mensual | `PV-RNF-22` | PROPUESTO / NO IMPLEMENTADO |
| 6. Clasificación de riesgo | `RNF-23` | 100% de versiones con riesgo clasificado y justificado | `PV-RNF-23` | PROPUESTO / NO IMPLEMENTADO |

`RNF-18` se conserva como requisito complementario de **trazabilidad/historial de rutinas** y no se fuerza artificialmente a sustituir ninguno de los seis aspectos anteriores.

## Regla de integridad
Los umbrales normativos/de diseño no se presentan como resultados empíricos ya alcanzados. El motor recomendador permanece **propuesto**; por ello los planes de verificación están documentados pero no se declaran ejecutados cuando no existe implementación.
