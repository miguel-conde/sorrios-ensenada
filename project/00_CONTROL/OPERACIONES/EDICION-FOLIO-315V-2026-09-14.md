# Operación EDICION-FOLIO-315V-2026-09-14

- **Tipo:** edición, validación y cierre documental de unidad
- **Estado:** verified
- **Fecha:** 14 de septiembre de 2026
- **Unidad editorial:** `folio_315v`
- **Rama canónica:** `main`
- **Base SHA:** `c3ac0835ba05016a33ae2e54605298b5a361debb`
- **Manual aplicado:** Manual Editorial v1.6
- **Edición vigente:** v3.5
- **PDF autoritativo:** `sorrios_ensenada_orden_lectura_calidad_original.pdf`, página 12 izquierda; Drive file ID `1GgBs68iTi53ue8-TbrYFABALxadhQe5u`; 18 páginas; tamaño 5038575 bytes; SHA-256 verificado `d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24`
- **Acceso al PDF:** lectura visual directa del PDF autoritativo; Drive no modificado; sin OCR

## Resultado editorial

- Leída visualmente la mitad izquierda de la página 12 del PDF autoritativo.
- Se continúa la respuesta 17.ª con la distribución de la propiedad de las ruedas de los molinos declarados en folio 315r.
- La primera casa de molino, de tres ruedas, queda distribuida entre `D[o]n Manuel Ant[oni]o cura De este Lugar`, `manuel, y Fran[cis]co F[ernande]z` y `Manuel G[onzale]z, y Fran[cis]co Diez`.
- Se documenta otro molino de dos ruedas, con participaciones de `Manuel G[arci]a, y c[onsor]tes` y de `Margarita G[arci]a, y Bartholome F[ernande]z`.
- Se documentan además un molino de dos ruedas propio de `Andres Suarez`, otro de una rueda propio de `Marcos Suarez` y un `molino venturero` que solo muele algunos meses en invierno con el agua disponible.
- Para determinadas ruedas se regula una utilidad de `quatro cargas De centeno`; la frase continúa materialmente en folio 316r.
- La inspección auxiliar del comienzo de folio 316r se usa únicamente para confirmar esa continuidad y no valida por anticipado la unidad siguiente.
- Se desarrollan `Ant[oni]o`, `Fran[cis]co`, `F[ernande]z`, `G[onzale]z`, `G[arci]a`, `c[onsor]tes`, `respectivam[en]te` y `d[ic]hos` conforme al criterio vigente de abreviaturas.
- Se conservan las grafías y formas documentales `manuel`, `Bartholome`, `Andres`, `Marcos`, `venturero`, `vna`, `acada`, `Dueños` y `quatro`, así como las divisiones `Bartho-` / `lome`, `pro-` / `pio`, `invier-` / `no`, `respec-` / `tivam[en]te`, `An-` / `dres`, `Manu-` / `el` y `re-` / `gulan`.
- No aparece ningún criterio metodológico nuevo y no quedan dudas abiertas.

## Control de Notas históricas A/B/C/D

- **A. Sin nota necesaria:** descripción material de las ruedas, uso de la fuerza del agua y atribución ordinaria de propiedad.
- **B. Glosario o índices:** `molino venturero`; las personas propietarias; `cura`; `carga` / `cargas`.
- **C. Nota histórica puntual:** no aparecen candidatos cuya interpretación requiera investigación externa en esta unidad.
- **D. Diario o futuro Estudio Histórico:** estructura de copropiedad de los molinos, estacionalidad del molino venturero y utilidad declarada por rueda.
- **Decisión:** la sección `Notas históricas` queda justificadamente sin notas puntuales. No se realiza investigación externa.

## Derivados

- Glosario: alta de `molino venturero`.
- Índice de personas: actualización de `Manuel Ant[oni]o De Bega` / `De Vega` y altas para las personas propietarias documentadas en la unidad, manteniendo como `Manuel` al propietario cuyo apellido no aparece explícitamente.
- Índice de oficios: actualización de `cura parrocho` / `Cura` con la nueva aparición.
- Índice de medidas: actualización de `carga` / `cargas` con la utilidad expresada en centeno.
- Índices de topónimos e instituciones: sin cambios justificados.
- Diario Editorial: registro de validación, cierre, continuidad, clasificación A/B/C/D y derivados.

## Archivos de la operación

Modificados:

- `project/00_CONTROL/estado.yaml`
- `project/20_TRABAJO_EDITORIAL/Diario_Editorial.md`
- `project/20_TRABAJO_EDITORIAL/Edicion_Critica.md`
- `project/20_TRABAJO_EDITORIAL/Glosario.md`
- `project/20_TRABAJO_EDITORIAL/INDICES/Indice_Personas.md`
- `project/20_TRABAJO_EDITORIAL/INDICES/Indice_Medidas.md`
- `project/20_TRABAJO_EDITORIAL/INDICES/Indice_Oficios.md`

Creado:

- `project/00_CONTROL/OPERACIONES/EDICION-FOLIO-315V-2026-09-14.md`

No se modifican el Manual Editorial, `proyecto.yaml`, `unidades.yaml`, `CAMBIOS.md`, los índices de topónimos e instituciones ni el PDF autoritativo.

## Estado resultante esperado

- `last_validated_unit: folio_315v`
- `last_closed_unit: folio_315v`
- `current_unit: folio_316r`
- `next_unit: folio_316v`
- `current_location.pdf_page: 12`
- `current_location.position: right`
- `open_issues: []`
- `operation.status: clean`

## Criterio de verificación

La operación solo se publica si `main` continúa exactamente en `c3ac0835ba05016a33ae2e54605298b5a361debb`. Tras publicar se verifican el padre del commit, la lista exacta de archivos afectados, el contenido de folio 315v, los derivados, la coherencia de `estado.yaml` con `unidades.yaml`, la ausencia del PDF en GitHub y el estado de CI.
