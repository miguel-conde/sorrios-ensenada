# CR-V1-001 — Compatibilidad del analizador del Glosario GH-B

## Identificación

- **ID:** `CR-V1-001`.
- **Fecha:** 11 de octubre de 2026.
- **Origen:** validación completa durante la revisión e integración de PKG-03.
- **Estado:** `APROBADA COMO CORRECCIÓN NECESARIA — EJECUCIÓN PENDIENTE`.
- **Tipo:** `CORRECCIÓN TÉCNICA / NO AMPLIACIÓN DE ALCANCE`.

## Evidencia

### Test y error

- Test:
  `tests/test_publication_phase4d.py::test_glossary_has_no_invented_version_and_all_unique_entries`.
- Fixture: `glossary`, en `tests/test_publication_phase4d.py:30–32`.
- Consumidor: `load_glossary()` → `parse_glossary()` en
  `publication/scripts/apparatus_sources.py`.
- Excepción: `apparatus_sources.ApparatusSourceError`.
- Condición exacta: la entrada `Señorío` contiene los campos
  `Término documentado`, `Definición`, `Primera unidad`, `Referencias`,
  `Contexto histórico` y `Notas`, mientras `GLOSSARY_FIELDS` exige exactamente
  los cinco anteriores salvo `Contexto histórico`.

### Comparación base / PKG-03

Se ejecutó exactamente el mismo test en dos worktrees/estados aislados:

| Estado | Commit | Resultado | Condición |
|---|---|---|---|
| A — base previa a PKG-03 | `ddfa2adb9f06f7b50585dbc80f156e62c968f570` | ERROR | mismo `ApparatusSourceError`, primera entrada `Señorío`, seis campos recibidos frente a cinco exigidos |
| B — PKG-03 | `4d0210f5f127933ac7a059bb029cde04ecd6d28b` | ERROR | misma excepción, parser y condición semántica |

Los blobs de `apparatus_sources.py`, `test_publication_phase4d.py` y
`Glosario.md` son idénticos entre A y B. El diff de PKG-03 añade únicamente el
dossier, los assets/datos cartográficos, el generador y sus tests; no modifica
el Glosario, el parser ni las pruebas de Fase 4D.

Resultado: `FALLO PREEXISTENTE A PKG-03`.

### Relación con PKG-01

- Antes de PKG-01, en `da2c596b20abd5447c11c83955d18a99ad9af9a6`,
  el mismo test pasa (`1 passed`).
- PKG-01, commit `9ae4d1fd46d9f2d7bca685de861bff2a554a7a39`,
  modificó el Glosario canónico e incorporó selectivamente el campo
  `Contexto histórico` conforme a `DEC-016`–`DEC-019`.
- PKG-01 no modificó `apparatus_sources.py` ni
  `test_publication_phase4d.py`; ambos conservan los mismos blobs anteriores.
- El parser exige igualdad exacta con una tupla fija de cinco campos y por ello
  no reconoce el sexto campo canónico en las entradas GH-B enriquecidas.

## Autoridad

El Glosario canónico GH-B, aprobado por decisión humana e integrado mediante
PKG-01, es la autoridad. `apparatus_sources.py` es un consumidor técnico
derivado. La fuente canónica no debe revertirse ni empobrecerse para satisfacer
un parser que conserva el contrato anterior.

## Clasificación

`TECH-A — Parser/test obsoleto respecto al contrato canónico GH-B ya aprobado.`

La incidencia es un **DEFECTO TÉCNICO**. No constituye una nueva función ni un
cambio de alcance.

## Solución prevista

Adaptar el parser, el modelo de datos derivado y las pruebas al contrato GH-B
vigente, donde `Contexto histórico` es un campo selectivo: debe conservarse
cuando existe sin obligarlo a todas las entradas. La ejecución deberá comprobar
también que los generadores consumidores propagan el campo sin mezclarlo con la
definición documental.

Esta solución se ejecutará en una operación técnica posterior; este registro no
modifica código ni tests.

## Límites

La futura corrección no podrá:

- cambiar contenido del Glosario;
- eliminar o degradar `Contexto histórico`;
- modificar las decisiones GH-B;
- introducir entradas nuevas;
- modificar `project/`;
- reabrir PKG-01;
- iniciar PKG-04 antes de recuperar una suite general verde.

## Criterio de cierre

- Parser compatible con la estructura GH-B real y selectiva.
- Campo `Contexto histórico` preservado en los derivados cuando exista.
- Tests específicos del parser y Fase 4D en PASS.
- Suite completa en PASS.
- Ninguna regresión de las entradas legítimas de cinco campos ni de otros
  formatos anteriores todavía vigentes.
- `project/` byte a byte intacto durante la corrección técnica.

## Estado

`APROBADA COMO CORRECCIÓN NECESARIA — EJECUCIÓN PENDIENTE`
