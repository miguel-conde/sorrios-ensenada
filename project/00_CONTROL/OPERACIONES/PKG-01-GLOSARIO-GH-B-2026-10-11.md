# Operación: PKG-01 — Glosario canónico GH-B

- **Fecha:** 11 de octubre de 2026
- **Estado:** verified
- **Modo:** estudio histórico sobre derivado canónico
- **Paquete:** PKG-01
- **Rama:** `pkg-01/glosario-gh-b-v1`
- **Base SHA:** `da2c596b20abd5447c11c83955d18a99ad9af9a6`
- **Estado inicial:** `operation.status: clean`
- **Fase:** `estudio_historico`

## Objetivo

Aplicar el modelo GH-B selectivo al Glosario canónico mediante conocimiento ya
consolidado en el corpus interno, sin investigación externa nueva ni cambios en
la Edición Crítica, el Estudio Histórico o su Registro D/C/I/E/L.

## Archivos canónicos afectados

- `project/20_TRABAJO_EDITORIAL/Glosario.md`: siete mejoras G1 y seis altas.
- `project/00_CONTROL/CAMBIOS.md`: alta del cambio canónico.
- `project/00_CONTROL/OPERACIONES/PKG-01-GLOSARIO-GH-B-2026-10-11.md`: registro semántico de la operación.

`project/00_CONTROL/estado.yaml` permanece sin cambios y conserva
`operation.status: clean`, porque la operación no reabre unidades ni altera el
estado terminal de la edición paleográfica.

## Fuentes internas utilizadas

- `project/00_CONTROL/Manual_Editorial.md`, versión 1.6.
- `project/20_TRABAJO_EDITORIAL/Edicion_Critica.md`, versión 3.6.
- `project/20_TRABAJO_EDITORIAL/Glosario.md`.
- `project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md`, versión 1.2.
- `project/30_RESULTADOS/ESTUDIO_HISTORICO/Registro_Afirmaciones_Calculos_v1.md`, versión 1.2.
- `docs/AUDITORIA_GLOSARIO_ESTUDIO_HISTORICO_V1_0.md`, usada solo como diagnóstico y decisión editorial, no como evidencia histórica.

No se consultaron fuentes externas ni se abrieron los enlaces bibliográficos ya
registrados en el corpus.

## Decisión GH-B

Se conserva en cada entrada el sentido documentado en el expediente y se añade
contexto histórico breve solo cuando aporta una mejora real y está respaldado por
conocimiento canónico existente. Las cautelas D/C/I/E/L permanecen visibles. El
Glosario sigue siendo un instrumento breve de ayuda a la lectura y no sustituye
al Estudio Histórico.

## G1 modificadas

| Voz | Soporte canónico principal | Resultado y cautela |
|---|---|---|
| `Señorío` | R2, R22, R28–R29; `JUR-005`, `JUR-006`, `JUR-008` | Se distingue jurisdicción de propiedad y de derechos concretos; no se reconstruyen derechos no demostrados. |
| `medio vecino` | R21; `DEM-001`, `DEM-002`, `DEM-005`, `LIM-001` | Se explica como categoría fiscal o vecinal; no es fracción fija de persona, hogar o población. |
| `propios` | R23–R25; `FIS-005`–`FIS-007`, `FIS-016`, `INT-006` | Se sitúa en la hacienda local y se vincula al repartimiento; no se infiere pobreza ni propiedad común. |
| `arbitrio` | R24–R25; `FIS-005`–`FIS-007`, `FIS-016`, `INT-006` | Se coordina con propios y renta sin equipararlos ni generalizar un régimen fiscal. |
| `boto` | R15–R16; `FIS-001`–`FIS-004`, `FIS-013` | Se añade el contexto del Voto de Santiago conservando forma, receptor, cuantía y producto elidido. |
| `vecera` | R29; `TRA-005`, `TRA-006` | Se confirma el sentido rotatorio del servicio; no se extiende a otras actividades. |
| `hijo de familia` | R35; `TRA-001`, `INT-008`, `DEM-005` | Se aclara la posición doméstica documentada; no se infieren edad, estado civil o estatuto general. |

## Nuevas voces incorporadas

| Voz | Evidencia y función | Cautela |
|---|---|---|
| `avitadores` | R21; suma declarada de dieciocho vecinos y ocho medios vecinos. | No equivale a población individual ni absorbe a los residentes separados. |
| `utilidad` | R6, R17–R20, R29, R33 y R35; valoración o rendimiento regulado. | No equivale por sí sola a producción, beneficio o renta efectiva. |
| `repartimiento` | R25; pago vecinal de gastos del común al faltar recursos propios. | No constan cuotas, criterio distributivo ni presupuesto exhaustivo. |
| `quartal` | R9–R17 y R20; sembradura, rendimiento y prestaciones en especie. | No hay conversión moderna ni equivalencia con celemín o carga. |

## Candidatas condicionales

### `establecimiento del suelo` — INCORPORAR

- **A. Presencia significativa:** aparece en R22 como el concepto preciso al que se refiere la ausencia de pago señorial.
- **B. Utilidad:** impide convertir esa ausencia concreta en ausencia general de derechos del conde.
- **C. Autonomía:** la locución completa admite una entrada breve coordinada con `Señorío`.
- **D. Seguridad:** R22, R28–R29, `JUR-005`, `JUR-006` y `FIS-012` permiten formular su función y su límite sin reconstrucción jurídica.

### `arenta` — INCORPORAR

- **A. Presencia significativa:** R20 aplica la forma a bueyes y vacas y declara prestaciones diferenciadas en centeno.
- **B. Utilidad:** la forma documental es opaca para el lector y describe un régimen ganadero económicamente relevante.
- **C. Autonomía:** la entrada explica el uso local sin duplicar otra voz del Glosario.
- **D. Seguridad:** `GAN-001` y `GAN-008` permiten una interpretación cauta en relación con renta o aparcería; no se normaliza la forma ni se completan condiciones contractuales.

## Exclusiones preservadas

- G3 no investigadas ni ampliadas: `añino`, `alcavalas`, `servicio ordinario y extraordinario`, `pobre de solemnidad`.
- G4 no ampliadas: `entreparedes`, `fejes`, `pies de abejas`.
- Las demás voces G0 permanecen sin cambios.
- No se modifica el orden canónico para satisfacer el orden alfabético de la salida publicada.

## Límites

- No hay investigación externa nueva.
- No se alteran transcripciones, notas de la Edición Crítica ni el Manual.
- No se modifica el Estudio Histórico ni el Registro D/C/I/E/L.
- No se modifica ningún índice.
- No se inicia PKG-05 ni se genera la publicación.

## Validaciones y cierre

- Validador local 2.0.2 `plugins/sorrios-ensenada/tools/validate_project.py`: PASS (`VALID: GitHub workspace v2 coherent`).
- Pruebas focalizadas de contrato, manifiestos, estado, operaciones, rutas, empaquetado, skill y ausencia de PDF: PASS (32 pruebas).
- Las siete voces G1 están presentes y mejoradas con separación entre sentido documental y contexto: PASS.
- Las cuatro altas obligatorias y las dos candidatas incorporadas tienen evidencia, referencias y cautelas: PASS.
- Las cuatro G3 y las tres G4 conservan byte a byte su contenido previo; no se investigaron ni ampliaron: PASS.
- Las restantes voces G0 conservan su contenido previo: PASS.
- Recuento de entradas: 28, sin encabezados duplicados: PASS.
- `git diff --check`: PASS.
- Alcance limitado a Glosario, `CAMBIOS.md` y este registro: PASS.
- `project/00_CONTROL/estado.yaml` conserva `operation.status: clean`: PASS.
- Edición Crítica, Estudio Histórico, Registro D/C/I/E/L, Manual, índices, `proyecto.yaml`, `estado.yaml`, `unidades.yaml`, PDF autoritativo, `publication/`, `docs/`, plugin, tests y `.github/`: sin cambios.
- Estado operativo final: `verified`; no queda operación abierta o incompleta.

## Commit final

Mensaje previsto: `feat(project): enrich canonical glossary for 1.0`.

El SHA no puede incorporarse al propio registro sin crear una autorreferencia que
cambiaría ese mismo SHA. El commit final será el commit atómico que contenga este
registro, con padre directo en la base declarada; su SHA se verificará y comunicará
en el informe de entrega.
