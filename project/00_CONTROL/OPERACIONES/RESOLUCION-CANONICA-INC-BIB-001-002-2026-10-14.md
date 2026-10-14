# Operación: resolución canónica de INC-BIB-001 e INC-BIB-002

- **Fecha:** 14 de octubre de 2026
- **Estado:** verified
- **Modo:** estudio histórico sobre fuentes canónicas
- **Rama:** `canonical/inc-bib-001-002-v1`
- **Base SHA:** `d4153c60489f4df24cdadf75d7740ec85b9406dd`
- **Estado inicial:** `operation.status: clean`
- **Fase:** `estudio_historico`

## Objeto

Resolver en la capa canónica las incompatibilidades de correspondencia entre
fuente y uso registradas como `INC-BIB-001` e `INC-BIB-002`, sin investigación
externa nueva, sin alterar la Edición Crítica y sin propagar todavía los cambios
a la publicación Quarto.

## Autoridad y decisión

- R29 y `TRA-005` conservan autoridad suficiente para el hecho local de la
  taberna por vecera. Se retira del Registro vigente la fila `TRA-006` porque el
  Registro no dispone de un estado establecido de retirada y no se inventa una
  categoría nueva. Los demás identificadores no se renumeran.
- R21 y `DEM-001` conservan autoridad suficiente para el dato local de los
  vecinos, medios vecinos, dos viudas y residentes. `DEM-005` queda restringido
  al contexto general efectivamente acreditado por BIB-015.
- La edición institucional de BIB-015 ya verificada en PKG-02 sustituye en
  `DEM-005` al enlace de plataforma; no se realizó ninguna consulta externa.

## Archivos canónicos afectados

- `project/30_RESULTADOS/ESTUDIO_HISTORICO/Registro_Afirmaciones_Calculos_v1.md`:
  v1.2 → v1.3; retirada de `TRA-006` y restricción de `DEM-005`.
- `project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md`: v1.2 → v1.3;
  separación D/E/I/L en población y retirada del paralelo externo de vecera.
- `project/20_TRABAJO_EDITORIAL/Glosario.md`: corrección de los contextos de
  `medio vecino` y `vecera`; el uso de `DEM-005` en `hijo de familia` se conserva
  porque la formulación reducida sigue sustentando el contexto doméstico.
- `project/00_CONTROL/CAMBIOS.md`: alta de la operación.
- `docs/RESOLUCION_CANONICA_INC_BIB_001_002.md`: dossier de resolución y
  propagaciones pendientes.
- Este registro semántico de operación.

`project/00_CONTROL/estado.yaml` permanece sin cambios y conserva
`operation.status: clean`, pues no se reabre ni avanza ninguna unidad y la
operación queda completamente registrada en un único commit atómico.

## Preservación

- Edición Crítica y manuscrito: sin cambios.
- R21, R29, `DEM-001` y `TRA-005`: sin cambios sustantivos.
- `DEM-002`, `CAL-001`–`CAL-020`, tablas cuantitativas, cantidades y lineación:
  sin cambios.
- `proyecto.yaml`, `estado.yaml` y `unidades.yaml`: sin cambios.
- `publication/`: sin cambios; su estado anterior queda inventariado en el
  dossier para PKG-08.

## Residuos clasificados

Las menciones anteriores que sobreviven en registros de operaciones,
diagnósticos, verificaciones o planes versionados describen el estado histórico
que dio origen a las incidencias; no autorizan afirmaciones en el Registro v1.3.
Las propagaciones activas bajo `publication/` permanecen deliberadamente sin
corregir y están enumeradas en el dossier para PKG-08.

## Validación

- Validador canónico 2.0.2: PASS.
- Pruebas focalizadas de contrato, esquema, manifiestos, operaciones, rutas,
  empaquetado, invariantes editoriales, bootstrap, ausencia de workspace Drive,
  skill y ausencia de PDF: PASS (32 pruebas).
- Integridad de IDs y resolución de referencias del Estudio v1.3: PASS.
- Tablas Markdown del Registro y sintaxis de los tres documentos: PASS.
- Auditoría semántica posterior de `TRA-006`, `DEM-005`, vecera y medio vecino:
  PASS; los únicos residuos no vigentes quedan clasificados como históricos o
  como propagación editorial pendiente.
- Preservación de R21/R29, `DEM-001`/`TRA-005`, cálculos y controles: PASS.
- `git diff --check`: PASS.
- Alcance del diff: PASS; ningún archivo de `publication/` modificado.
- Estado operativo final: `verified`; `operation.status` conserva `clean`.

La suite general obtiene 586 pruebas superadas, ocho fallos y 36 errores. Todos
los resultados no superados pertenecen exclusivamente a la sincronización de
`publication/` deliberadamente pospuesta: el parser de aparatos exige todavía
el Registro 1.2, `publication.yml` declara el blob anterior del Glosario y los
capítulos 11 y 13 conservan `TRA-006`. No se modifican esos contratos, derivados
o capítulos en esta operación; su corrección corresponde a PKG-08.

## Exclusiones

- No se investigan ni sustituyen fuentes.
- No se modifica la Edición Crítica ni se reinterpreta la fuente primaria.
- No se ejecuta PKG-08, no se sincroniza procedencia y no se evalúa GATE-01.
- No se integra, publica, etiqueta ni crea una release.

## Commit final

Mensaje previsto: `fix(project): resolve canonical bibliography incidents`.

El SHA se verificará y comunicará en el informe final; no se incorpora aquí para
evitar una autorreferencia que alteraría el propio commit.
