# CR-V1-001 — Compatibilidad del analizador del Glosario GH-B

## Identificación

- **ID:** `CR-V1-001`.
- **Fecha de apertura:** 11 de octubre de 2026.
- **Fecha de cierre:** 12 de octubre de 2026.
- **Origen:** validación completa durante la revisión e integración de PKG-03.
- **Estado:** `CERRADA E INTEGRADA`.
- **Tipo:** `TECH-A — CORRECCIÓN TÉCNICA / NO AMPLIACIÓN DE ALCANCE`.
- **Commit final integrado:** `c07bc011a42952f64622e3f78e8d759ad361cf29`.

## Problema y autoridad

PKG-01 amplió el Glosario canónico GH-B de 22 a 28 entradas y añadió
selectivamente `Contexto histórico` conforme a `DEC-016`–`DEC-019`. El consumidor
`publication/scripts/apparatus_sources.py` conservaba un contrato exacto de
cinco campos y rechazaba las entradas enriquecidas con el sexto campo.

El Glosario canónico integrado en
`9ae4d1fd46d9f2d7bca685de861bff2a554a7a39` era la autoridad; por tanto, la
corrección debía adaptar el consumidor técnico sin revertir, empobrecer ni
modificar `project/`.

## Solución integrada

El parser acepta ahora:

- cinco campos base obligatorios;
- `Contexto histórico` como `str | None`;
- el campo opcional únicamente entre `Referencias` y `Notas`;
- entradas de cinco campos, de seis campos y mezclas de ambas.

Mantiene controles estrictos: rechaza campos desconocidos, duplicados,
obligatorios ausentes y encabezados inválidos. No se introdujo tolerancia
genérica basada en el mero número de campos.

El snapshot técnico quedó sincronizado con:

- `base.git_commit`:
  `9ae4d1fd46d9f2d7bca685de861bff2a554a7a39`;
- blob del Glosario:
  `5f1e78adee096f5d5752d6fe1af866ca5e5c8b17`;
- conteo vigente: 28 entradas.

Fase 6A distingue la procedencia canónica vigente del registro histórico de
la candidata: el SHA `e81dc9239ac8dbabfe77168a50ef98c4d3b79170` se conserva
solo donde documenta legítimamente aquel estado histórico.

## Derivados y diagnóstico GEN-C

La primera validación también detectó aparatos locales obsoletos. La solución
final no los versiona ni crea una excepción a la arquitectura existente:

`fuentes versionadas → prepare.py → generated/ ignorado → validate_publication.py`

Los cuatro aparatos se reconstruyen desde sus fuentes, permanecen bajo
`publication/generated/` y no aparecen en el índice de Git. `.gitignore` y
`publication/README.md` permanecen intactos. El intento intermedio
`a10823c...` se descartó y no se integró.

Clasificación final: `GEN-C RESUELTA` mediante restauración del flujo
reproducible normal.

## Verificación y cierre

- Phase 4D: `51 passed`.
- Phase 6A: `10 passed` tras la integración y el cierre documental.
- `check_sources.py`: PASS con 28 entradas y procedencia correcta.
- `validate_publication.py`: PASS integral tras `prepare.py`.
- Suite completa preintegración: `585 passed`.
- Suite completa posintegración y tras el cierre documental: `585 passed`.
- `validate_project.py`, cartografía `--check`, compilación Python y
  `git diff --check`: PASS.
- `publication/generated/`: cero archivos versionados.
- `project/`: árbol idéntico al de la base de la operación.

La rama `feature/quarto-book` incorporó el commit final mediante fast-forward
estricto. El cierre detallado queda en
[CIERRE_CR_V1_001_GLOSARIO_GH_B.md](./CIERRE_CR_V1_001_GLOSARIO_GH_B.md).

## Límites conservados

Este cierre no:

- inicia PKG-04;
- resuelve REV-024 ni presenta editorialmente `Contexto histórico`;
- resuelve `INC-BIB-001` o `INC-BIB-002`;
- regenera la candidata HTML/PDF;
- modifica el Glosario canónico, la cartografía, los capítulos o la
  bibliografía;
- autoriza push, tag o release.

## Estado final

`CERRADA E INTEGRADA`
