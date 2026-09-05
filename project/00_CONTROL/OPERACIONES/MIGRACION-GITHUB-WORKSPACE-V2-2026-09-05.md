# Operación MIGRACION-GITHUB-WORKSPACE-V2-2026-09-05

- **Tipo:** migración técnica a GitHub workspace v2
- **Estado:** prepared
- **Hito verificado:** H2
- **Fecha:** 5 de septiembre de 2026
- **Rama:** `migration/github-workspace-v2`
- **Base de `main`:** `cd683dd3a745c1f7bbabc154510885dbdad9dde8`
- **Versión de partida:** 1.2.3
- **Versión preparada:** 2.0.0
- **Unidad editorial:** ninguna
- **Estado editorial:** portada; ninguna unidad validada o cerrada; D-001 abierta; `operation.status: clean`
- **PDF autoritativo:** Drive file ID `1GgBs68iTi53ue8-TbrYFABALxadhQe5u`, 5.038.575 bytes, 18 páginas, SHA-256 `d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24`
- **PDF histórico duplicado:** hash idéntico al canónico; no migrado a GitHub.
- **Criterio de H2:** proyecto, bootstrap, núcleo común, skill, tools, tests, CI y documentación adaptados sin tocar `main`.

## Commits de construcción

- A `d6bea94276de011dbee393cd60aa53fe576731d8` — importación exacta de documentos de Drive.
- B `26251001123881c3608573c74c0d52b7a568c37d` — `PROJECT.md`, schema 2 y referencias comunes.
- C `fc43a993ddba65cc8baaef020636fb307fe245ee` — skill y manifiestos.
- D `25bebffe5deebe9a195b1668953553ce5b5b851e` — retirada de materialización y reorganización de tools.
- E `55db324fc26817b60f996b8fceaf8d367d7e6710` — tests, CI, plantilla y desarrollo.
- F — documentación y registro de cierre de H2 (este commit).

## Verificación de H2

- `project/` contiene los textos vivos e históricos y no contiene ningún PDF.
- `proyecto.yaml` usa schema 2, GitHub para el workspace y Drive solo para el manuscrito.
- Se conservan 35 unidades en el mismo orden.
- Se conservan Manual v1.5 y Edición v3.4.
- Se conservan Diario, Glosario, cinco índices, resultados e históricos textuales.
- `PROJECT.md` y `SKILL.md` son entradas independientes al mismo núcleo.
- Se retiraron los materializadores locales y se reorganizaron las tools.
- Tests y CI se adaptaron al contrato v2; Poppler ya no es requisito general de CI.
- `main` permanece en el SHA base.

## Pendiente antes del cutover

- H3: CI y validación en Chat normal Web/Desktop y en una superficie compatible con la skill.
- H3: acceso al PDF sin Base64, render/visión `complete`, `left` y `right`, escritura reversible en GitHub y plugin aislado.
- H4: fast-forward de `main` solo si sigue en el SHA base.
- H6: limpieza de Drive después de superar la aceptación.
