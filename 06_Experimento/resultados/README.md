# Resultados canónicos de FabroGym

La instancia **canónica, ejecutable y evaluable** de estas salidas es `07_Datos/resultados/`.

La carpeta `06_Experimento/resultados/` se mantiene únicamente como **espejo derivado byte-idéntico** para compatibilidad documental con artefactos históricos. No constituye una segunda cadena analítica y nunca se usa como entrada del pipeline.

La orden oficial es:

```bash
cd 07_Datos
python scripts/run_all.py
```

Semilla pseudoaleatoria explícita del pipeline: `401`.

Cuando se ejecuta dentro del repositorio completo, `run_all.py` sincroniza este directorio hacia `06_Experimento/resultados/` después de terminar el análisis. La identidad entre ambas carpetas debe comprobarse por rutas y SHA-256 antes del cierre.
