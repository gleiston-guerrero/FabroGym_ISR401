# F3-07 — Control de capa pública [P] y capa restringida [R]

## Regla obligatoria

FabroGym separa la evidencia en dos capas:

- **[P] Pública:** datos anonimizados o seudonimizados, transcripciones anonimizadas, matrices de análisis, scripts, resultados, instrumentos no identificables y copias censuradas/enmascaradas aptas para revisión pública.
- **[R] Restringida:** consentimientos originales firmados, firmas, cédulas, audios, videos identificables, transcripciones sin anonimizar, fotografías identificables sin autorización de publicación y demás datos personales directos.

La guía específica de FabroGym exige conservar una **capa restringida cifrada**. Por ello, la existencia de un contenedor cifrado y expresamente documentado no equivale a publicar su contenido en claro.

## Excepción documentada del proyecto

Se conserva como artefacto restringido versionado:

`02_Evidencias/00_Restringido/evidencias_restringidas.7z`

Condiciones obligatorias:

1. el contenedor debe permanecer cifrado/protegido;
2. la contraseña o clave **no puede** registrarse en GitHub, README, commits, scripts ni artefactos públicos;
3. los originales no deben extraerse dentro de rutas públicas del repositorio;
4. la capa pública/Zenodo debe contener únicamente derivados anonimizados, seudonimizados, censurados o agregados;
5. la existencia del contenedor se documenta, pero su contenido no se inspecciona ni se expone automáticamente.

El archivo:

`02_Evidencias/00_Restringido/fichas_tecnicas.csv`

se conserva como inventario técnico de evidencia. La guía específica validó este formato porque registra códigos de sesión, duración, códec, tamaño y SHA-256.

## Fotografías originales A11

El archivo:

`10_Autoria/fotos_equipo/02_Fotos_Aplicacion/A11 Fotos_Originales_Cuestionario.7z`

se mantiene como contenedor restringido con la credencial fuera del repositorio; las copias públicas se conservan autorizadas o suficientemente enmascaradas.

## Verificación automática

Ejecutar desde la raíz:

```bash
python 07_Datos/scripts/verificar_privacidad_publica.py
```

El verificador:

- no abre los `.7z`;
- no conoce contraseñas;
- no marca como error la sola presencia de los contenedores restringidos documentados;
- sí bloquea archivos restringidos adicionales no documentados, multimedia no clasificada o identificadores directos en datos públicos;
- genera `07_Datos/resultados/REVISION_PRIVACIDAD_PUBLICA.md`.

## Criterios humanos de aceptación del corte

El cierre ético aplica estos criterios: el contenedor restringido debe conservar protección criptográfica y su clave fuera del repositorio; los originales no se publican extraídos en rutas públicas; el contenedor A11 de originales conserva el mismo régimen de acceso restringido; las copias públicas de fotografías, consentimientos y actas se mantienen censuradas o enmascaradas; y Zenodo contiene únicamente derivados aptos para publicación.

En la exportación ZIP revisada, `evidencias_restringidas.7z` aparece como puntero Git LFS, de modo que el objeto binario restringido no está materializado localmente y el auditor no atribuye propiedades criptográficas al objeto ausente. La auditoría automática complementa esta política sin sustituir la verificación del objeto LFS en el entorno que lo materializa.
