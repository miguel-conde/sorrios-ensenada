# Operación EDICION-FOLIO-307V-2026-09-06

- **Tipo:** edición, validación y cierre documental de unidad
- **Estado:** verified
- **Fecha:** 6 de septiembre de 2026
- **Unidad editorial:** `folio_307v`
- **Rama canónica:** `main`
- **Base SHA:** `1451ca63cd1862ea72ebd2a014c3c354fc31de4d`
- **Manual aplicado:** Manual Editorial v1.6
- **Edición vigente:** v3.5
- **PDF autoritativo:** Drive file ID `1GgBs68iTi53ue8-TbrYFABALxadhQe5u`, página 4 izquierda, 5.038.575 bytes, 18 páginas, SHA-256 declarado `d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24`
- **Acceso al PDF:** lectura directa del archivo autoritativo obtenido de Google Drive como PDF real; Drive no modificado; sin Base64 y sin OCR

## Resultado editorial

- Leída visualmente la mitad izquierda de la página 4 del PDF autoritativo.
- La unidad continúa y concluye la tercera respuesta: completa el lindero meridional con `Otro Lugar De Rioseco`, fija `Villapodambre` como lindero del Norte y remite a la figura situada en el margen mediante `su figura la de el marg[e]n`.
- La remisión a la figura se relaciona con el croquis ya transcrito en folio 307r y queda plenamente cubierta por Manual Editorial v1.6, § 11.1; no aparece ningún criterio metodológico nuevo.
- Comienza la cuarta respuesta y se transcriben las cinco primeras especies de tierras: `Ferrañales centenales De secano`, `Tierras linares De regadio`, `Tierras linares De secano`, `Tierras centenales De secano` y `Prados cercados De regadio`.
- Se conservan las grafías históricas `vn`, `Zevada`, `intermision`, así como las divisiones visibles `pro-` / `ducen`.
- Los puntos y trazos de relleno que prolongan varios renglones tras `forraje`, `Zevada`, `Centeno`, `otro` y `otoño` se omiten como relleno gráfico sin valor verbal conforme al criterio ya vigente para signos no verbales.
- La inspección auxiliar del comienzo de folio 308r confirma que la cuarta respuesta continúa con la sexta especie; esta comprobación se usa solo para delimitar la unidad y no valida por anticipado folio 308r.
- No quedan dudas abiertas.

## Derivados

- Glosario: altas de `Ferrañales` y `pelo`, con definiciones estrictamente contextuales.
- Índice de topónimos: actualización de `Rioseco` y alta de `Villapodambre`.
- Índices de personas, instituciones, medidas y oficios: sin cambios justificados por esta unidad.
- Diario Editorial: registro de la validación, cierre, continuidad y aplicación de criterios vigentes.

## Archivos de la operación

Modificados:

- `project/00_CONTROL/estado.yaml`
- `project/20_TRABAJO_EDITORIAL/Edicion_Critica.md`
- `project/20_TRABAJO_EDITORIAL/Diario_Editorial.md`
- `project/20_TRABAJO_EDITORIAL/Glosario.md`
- `project/20_TRABAJO_EDITORIAL/INDICES/Indice_Toponimos.md`

Creado:

- `project/00_CONTROL/OPERACIONES/EDICION-FOLIO-307V-2026-09-06.md`

No se modifican el Manual Editorial, `proyecto.yaml`, `unidades.yaml`, los otros cuatro índices ni el PDF autoritativo.

## Estado resultante esperado

- `last_validated_unit: folio_307v`
- `last_closed_unit: folio_307v`
- `current_unit: folio_308r`
- `next_unit: folio_308v`
- `current_location.pdf_page: 4`
- `current_location.position: right`
- `open_issues: []`
- `operation.status: clean`

## Criterio de verificación

La operación solo se publica si `main` continúa exactamente en el Base SHA indicado. Tras publicar se verifican el padre del commit, la lista exacta de archivos afectados, el contenido de folio 307v y de los derivados, la coherencia de `estado.yaml` con `unidades.yaml`, la ausencia de PDF en GitHub y el CI completo.
