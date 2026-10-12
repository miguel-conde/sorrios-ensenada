# CR-V1-001 — Cierre

## 1. Estado

`CERRADA E INTEGRADA`

Veredicto de revisión: `CR-V1-001: APTO PARA INTEGRACIÓN`.

## 2. Problema original

El analizador del Glosario exigía exactamente cinco campos y era incompatible
con el contrato GH-B aprobado, que permite `Contexto histórico` de forma
selectiva. El fallo era anterior a PKG-03 y no fue causado por la cartografía.

## 3. Propagación técnica detectada

La revisión identificó los consumidores que debían sincronizarse:

- parser y modelo de datos del Glosario;
- snapshot del blob canónico;
- procedencia vigente de `project/`;
- conteo de 22 a 28 entradas;
- tests de Fase 6A, separando estado vigente y registro histórico;
- derivado local generado, que había quedado obsoleto.

## 4. Solución final

Se restauró el flujo previsto por la arquitectura:

`fuentes versionadas → prepare.py → generated/ ignorado → validate_publication.py`

No se aceptan derivados antiguos como excepción ni se versionan resultados de
generación.

## 5. Parser GH-B

El parser mantiene cinco campos base obligatorios y admite `Contexto histórico`
como `str | None`, solo inmediatamente antes de `Notas`. Acepta entradas de
cinco o seis campos y su mezcla. Sigue rechazando campos desconocidos,
duplicados, obligatorios ausentes y encabezados inválidos.

## 6. Provenance y snapshot

- `base.git_commit` vigente:
  `9ae4d1fd46d9f2d7bca685de861bff2a554a7a39`.
- Blob vigente del Glosario:
  `5f1e78adee096f5d5752d6fe1af866ca5e5c8b17`.
- El tree `project/` de ese commit coincide con el de la base de CR-V1-001.
- El SHA `e81dc9239ac8dbabfe77168a50ef98c4d3b79170` se conserva exclusivamente
  como procedencia histórica legítima de la candidata anterior.

## 7. Conteo 28

El Glosario derivado contiene 28 entradas e incluye las seis altas de PKG-01:
`avitadores`, `utilidad`, `repartimiento`, `quartal`, `establecimiento del
suelo` y `arenta`. Las siete entradas G1 actualizadas permanecen fieles a la
fuente. El modelo conserva 13 valores de `Contexto histórico`.

## 8. Phase 6A histórico/vigente

Las comprobaciones distinguen el estado canónico vigente de los informes
históricos. Fase 6 continúa abierta, Fase 6B sigue prohibida antes del preview y
la aceptación humana, y PKG-04 solo queda desbloqueado: no se ha iniciado.

## 9. Política generated/

- Se detectó `GEN-C`: derivados locales obsoletos frente a la fuente actual.
- El intento intermedio `a10823c...` fue descartado y no integrado.
- Se restauró la política normal de regeneración mediante `prepare.py`.
- Hay cero archivos de `publication/generated/` versionados.
- No se modificaron `.gitignore` ni `publication/README.md`.

Resultado: `GEN-C RESUELTA`.

## 10. Reproducibilidad

Dos reconstrucciones consecutivas produjeron hashes SHA-256 idénticos:

| Aparato | SHA-256 |
|---|---|
| `glosario.qmd` | `53f68d645492b61566450410a999a3bd538c1780662f64db0ed9201b407820ec` |
| `cuadros-cuantitativos.qmd` | `fafd07ff9628e39bc1ab45cb3bccff81bc740d683a6c5355a5ad3bae4c38b351` |
| `concordancia.qmd` | `9d88215df603bbfaf001116726e115dbfa0f68e80563b8ba9b9a3bb00e5f59a2` |
| `matriz-evidencia.qmd` | `28ff369c1d494b8df0820bf7d7383fe59bfbec79a219b465a1662778869b6795` |

## 11. Suite completa

Antes y después de la integración, Phase 4D dio `51 passed`, Phase 6A dio
`10 passed`, `check_sources.py` y `validate_publication.py` dieron PASS, y la
suite completa dio `585 passed`, sin fallos, errores, skips ni xfails. También
pasaron `validate_project.py`, cartografía `--check`, compilación Python y
`git diff --check`.

## 12. Integración Git

- Base: `0d31d64023603e7713b5def51ab0275ed727de2f`.
- Commit revisado: `c07bc011a42952f64622e3f78e8d759ad361cf29`.
- Ajuste autorizado del test del roadmap: el commit
  `14c8781aff3742d35de8263333021c3a5b1b65be` sustituye las aserciones del
  estado previo al cierre por CR cerrada y PKG-04 listo, sin relajar Fase 6B ni
  la aceptación humana.
- Rama de origen: `cr-v1-001/glossary-parser-gh-b`.
- Rama de destino: `feature/quarto-book`.
- Método: fast-forward estricto, sin merge commit.
- No se hizo push, tag ni release.

## 13. Integridad canónica

CR-V1-001 no modificó `project/`. El Glosario canónico, los mapas, los
capítulos y la bibliografía permanecen intactos.

## 14. Pendientes deliberadamente NO resueltos

- REV-024 — alfabetización del Glosario derivado;
- presentación editorial de `Contexto histórico`;
- `INC-BIB-001`;
- `INC-BIB-002`;
- regeneración de la candidata HTML/PDF.

## 15. Siguiente paso

`PKG-04 — prototipo F3`
