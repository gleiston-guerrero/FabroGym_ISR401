# Espejo de consentimientos para verificación

Esta carpeta existe únicamente para hacer compatible la estructura del repositorio con el comando literal de verificación incluido en la guía de cierre:

```bash
for f in 08_Etica/consentimientos/*.pdf; do
  echo "$f: $(pdftotext "$f" - | wc -w) palabras"
done
```

La ubicación canónica de la evidencia es `02_Evidencias/Consentimientos/`.

Los **16 PDF** de esta carpeta son copias **byte-idénticas** de los 16 consentimientos públicos censurados de la ruta canónica:

- 10 `ENTR-01..10`
- 3 `WALK-TEC-01..03`
- 3 `WALK_NTEC_01..03`

No deben contarse dos veces. El detalle de la discrepancia entre el conteo de 17 mencionado en la guía y el inventario verificable de 16 sesiones se documenta en `../CONTROL_CONSENTIMIENTOS_FINAL.md`.
