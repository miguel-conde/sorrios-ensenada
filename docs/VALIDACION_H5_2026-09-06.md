# Validación H5 — ciclo editorial real y continuidad entre ordenadores

**Fecha:** 6 de septiembre de 2026  
**Resultado:** PASS  
**Rama canónica:** `main`

## Alcance

H5 exige dos comprobaciones sobre la arquitectura ya cortada a GitHub:

1. ejecutar un ciclo editorial real sobre `main`;
2. reconstruir el estado resultante desde otro ordenador/sesión sin depender de checkout local ni herramientas locales.

## 1. Ciclo editorial real

Antes del ciclo se detectó que `tests/test_editorial_invariants.py` fijaba de forma permanente `current_unit: portada`, lo que habría impedido cualquier avance editorial legítimo. Se sustituyó por invariantes dinámicos de coherencia entre `estado.yaml` y `unidades.yaml`.

- Commit de preparación: `53b7d17940e8d5a84728624237fdf8a2f2b030c6` (`test: make editorial state invariant progress-aware`).
- CI run 49: PASS en Windows y Ubuntu, Python 3.10 y 3.13.

Con ese commit como `base_sha` se trabajó exclusivamente la unidad `portada`.

- PDF autoritativo leído desde Google Drive como archivo real, sin Base64 y sin OCR.
- Página trabajada: 1, posición `complete`.
- Manual aplicado: v1.5.
- D-001 resuelta como cruz invocativa reconocible, representada mediante `†`.
- Se completaron las seis secciones editoriales de la Portada.
- Se añadieron únicamente `Sorribas` y `Santibañez De Ordas` al Índice de topónimos.
- Sin altas justificadas en Glosario ni en índices de personas, instituciones, medidas u oficios.
- Publicación Git multiarchivo atómica con comprobación previa de `base_sha` y `update_ref(..., force=false)`.

Commit editorial:

`6bf596546ce3141d1cd2d13f236b5ec7af76383f` — `editorial: validate and close portada`

El commit afectó exactamente a:

- `project/00_CONTROL/OPERACIONES/EDICION-PORTADA-2026-09-06.md`
- `project/00_CONTROL/estado.yaml`
- `project/20_TRABAJO_EDITORIAL/Diario_Editorial.md`
- `project/20_TRABAJO_EDITORIAL/Edicion_Critica.md`
- `project/20_TRABAJO_EDITORIAL/INDICES/Indice_Toponimos.md`

CI run 50 sobre el commit editorial: PASS en Windows y Ubuntu, Python 3.10 y 3.13.

Estado resultante:

- `last_validated_unit: portada`
- `last_closed_unit: portada`
- `current_unit: reverso_portada`
- `next_unit: folio_306r`
- `current_location.pdf_page: 2`
- `current_location.position: left`
- `open_issues: []`
- `operation.status: clean`

Transcripción validada de la Portada:

```text
†
Copia De las resp[ues]tas. G[enera]les. De
el Lugar De Sorribas,
y Santibañez De Ordas..
```

## 2. Continuidad desde otro ordenador

La prueba se ejecutó desde otro ordenador en ChatGPT, mediante Chat normal y `PROJECT.md`, sin plugin del proyecto y sin usar checkout local, Git local, Python local, WSL, VS Code ni Google Drive.

La consulta fue puntual y de solo lectura contra GitHub `main`.

El segundo ordenador reconstruyó exactamente:

- `project_id: sorrios-ensenada-1752`
- `fase: edicion_paleografica`
- `last_validated_unit: portada`
- `last_closed_unit: portada`
- `current_unit: reverso_portada`
- `next_unit: folio_306r`
- `current_location.pdf_page: 2`
- `current_location.position: left`
- `open_issues: []`
- `operation.status: clean`

También recuperó exactamente las cuatro líneas de la transcripción validada de la Portada.

Archivos leídos por esa prueba, todos desde GitHub `main`:

- `PROJECT.md`
- `project/00_CONTROL/proyecto.yaml`
- `project/00_CONTROL/estado.yaml`
- `plugins/sorrios-ensenada/skills/editar-catastro-sorrios/references/task-modes.md`
- `project/20_TRABAJO_EDITORIAL/Edicion_Critica.md`

No se modificó ningún archivo.

## Veredicto

**H5 = PASS.**

Queda demostrado que el proyecto puede:

- avanzar editorialmente sobre el workspace canónico de GitHub;
- publicar operaciones multiarchivo de forma atómica;
- conservar un estado coherente y validado por CI;
- reconstruirse correctamente desde otro ordenador usando solo ChatGPT + GitHub y `PROJECT.md`, sin depender del entorno local del ordenador original.

El siguiente hito es H6: limpieza de Google Drive y retirada del legado, conservando únicamente el PDF autoritativo según el plan de migración.
