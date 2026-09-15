# Verificación técnica de contenedores restringidos

La capa restringida se mantiene separada de la capa pública. La comprobación técnica disponible en este corte arroja:

- `10_Autoria/fotos_equipo/02_Fotos_Aplicacion/A11 Fotos_Originales_Cuestionario.7z`: **cifrado AES detectado en la cabecera 7z** (método 7z AES `06 F1 07 01`).
- `02_Evidencias/00_Restringido/evidencias_restringidas.7z`: en la exportación ZIP se conserva como **puntero Git LFS** con `oid sha256:a1b9b56a4fddf469a39bab3a51bcc891c85c0d0ce70432bf8602513f84c24070` y tamaño declarado `1521924213` bytes. El `oid sha256` identifica al objeto LFS remoto; el manifiesto global de esta exportación verifica, con `sha256sum` estándar, los bytes del puntero que está físicamente presente en el ZIP.
- Las credenciales de acceso no se almacenan en la capa pública del repositorio.

Comando reproducible:

```bash
python 07_Datos/scripts/verificar_cifrado_7z.py
```

Esta verificación complementa `CONTROL_CAPAS_PUBLICA_RESTRINGIDA.md` y `B6_CUMPLIMIENTO_ETICA_PRIVACIDAD.md`.
