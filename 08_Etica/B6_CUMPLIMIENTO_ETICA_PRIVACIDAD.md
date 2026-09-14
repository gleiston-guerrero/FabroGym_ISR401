# B6 — Cumplimiento de ética y protección de datos

**Proyecto:** FabroGym — ISR-401  
**Entrega:** Entrega 4 (2B / Defensa Final)

## 1. Matriz de cumplimiento

| Requisito | Evidencia / decisión |
|---|---|
| **Base de licitud / fundamento de participación** | Participación voluntaria y consentimiento informado para la evidencia primaria de campo. |
| **Finalidad** | Uso académico para levantamiento, análisis, especificación y validación de requisitos, trazabilidad, reproducibilidad y publicación anonimizada. |
| **Plazo de conservación** | Las copias restringidas o reidentificables se mantienen únicamente durante el periodo autorizado para el proyecto/evaluación y, cuando corresponda, bajo custodia institucional. |
| **Responsable de custodia académica** | Equipo actual de cierre: Mera Arias Erick Jhair, Mora Duarte Alex José y Ponce Rivera Mery Helenmey, bajo supervisión académica del docente responsable. |

## 2. Separación pública / restringida

**[P] Pública:** transcripciones anonimizadas, matrices, resultados, requisitos, modelado, scripts, datos derivados y copias censuradas/enmascaradas aptas para publicación.

**[R] Restringida:** originales identificables, consentimientos firmados, grabaciones, fotografías originales no aptas para publicación y demás material con datos personales directos.

La guía específica de FabroGym exige mantener una **capa restringida cifrada** y una capa pública derivada sin datos personales.

## 3. Contenedor restringido documentado

Se conserva deliberadamente:

`02_Evidencias/00_Restringido/evidencias_restringidas.7z`

Su presencia no significa que los datos contenidos se publiquen en claro. En el cierre se clasifica como capa restringida: la credencial de acceso se mantiene fuera del repositorio, los originales no se extraen a rutas públicas y Zenodo/`07_Datos` contienen únicamente derivados aptos para publicación.

También se conserva `02_Evidencias/00_Restringido/fichas_tecnicas.csv` como inventario técnico de evidencia, sin sustituir ni exponer los archivos originales.

## 4. Fotografías A11

`10_Autoria/fotos_equipo/02_Fotos_Aplicacion/A11 Fotos_Originales_Cuestionario.7z` se trata como contenedor restringido. Permanece clasificado como contenedor restringido; la credencial de acceso no se versiona y las copias públicas se conservan enmascaradas/autorizadas.

## 5. Regla de minimización

FabroGym no publica en la capa [P]:

- cédulas;
- firmas originales;
- teléfonos o correos privados;
- datos reales de salud;
- biometría;
- medidas corporales identificables;
- pagos reales asociados a personas;
- historiales clínicos;
- originales identificables no autorizados.

## 6. Verificación de cierre

Ejecutar:

```bash
python 07_Datos/scripts/verificar_privacidad_publica.py
```

El verificador automático se ejecuta sobre la capa pública y su salida forma parte del cierre reproducible. La revisión visual confirma que las copias públicas censuran identificadores directos. Las cuatro copias anteriormente observadas (`ENTR-02`, `ENTR-03`, `ENTR-04` y `ENTR-06`) fueron sustituidas el 14 de septiembre de 2026 por versiones escaneadas y censuradas de los formularios firmados. En el corte actual, las cuatro tienen tres páginas y no declaran Microsoft Word en los campos Creator/Producer. El control técnico actualizado se conserva en `07_Datos/resultados/tablas/B6_control_metadatos_consentimientos.csv`.

**Estado documental:** INTEGRADO Y VERSIONADO EN EL REPOSITORIO.  
**Estado de cierre ético:** CONSOLIDADO; la observación documental sobre las cuatro copias públicas queda cerrada en el corte actual y los originales identificables permanecen en la capa restringida.

## 7. Verificación técnica de contenedores

La evidencia técnica del contenedor A11 y la referencia Git LFS de la capa restringida se documentan en `08_Etica/VERIFICACION_CIFRADO_CONTENEDORES.md`. El contenedor A11 presenta método AES en su estructura 7z y las credenciales permanecen fuera de la capa pública.
