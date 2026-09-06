# Operación MIGRACION-GITHUB-WORKSPACE-V2-2026-09-05

- **Tipo:** migración técnica a GitHub workspace v2
- **Estado:** cutover_complete
- **Hito verificado:** H4
- **Fecha de inicio:** 5 de septiembre de 2026
- **Fecha de cutover:** 6 de septiembre de 2026
- **Rama canónica actual:** `main`
- **Base previa de `main`:** `cd683dd3a745c1f7bbabc154510885dbdad9dde8`
- **Commit de cutover:** `eee9eddeaf7f1495c5cd48fb0bb12ff0ae0e009e`
- **Versión de partida:** 1.2.3
- **Versión activa:** 2.0.0
- **Unidad editorial:** ninguna
- **Estado editorial preservado:** portada; ninguna unidad validada o cerrada; D-001 abierta; `operation.status: clean`
- **PDF autoritativo:** Drive file ID `1GgBs68iTi53ue8-TbrYFABALxadhQe5u`, 5.038.575 bytes, 18 páginas, SHA-256 `d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24`
- **PDF histórico duplicado:** hash idéntico al canónico; no migrado a GitHub.

## Commits principales de construcción

- A `d6bea94276de011dbee393cd60aa53fe576731d8` — importación exacta de documentos de Drive.
- B `26251001123881c3608573c74c0d52b7a568c37d` — `PROJECT.md`, schema 2 y referencias comunes.
- C `fc43a993ddba65cc8baaef020636fb307fe245ee` — skill y manifiestos.
- D `25bebffe5deebe9a195b1668953553ce5b5b851e` — retirada de materialización y reorganización de tools.
- E `55db324fc26817b60f996b8fceaf8d367d7e6710` — tests, CI, plantilla y desarrollo.
- H3 final `eee9eddeaf7f1495c5cd48fb0bb12ff0ae0e009e` — cierre de aceptación Web/Desktop/skill y CI.

## H3

- Chat normal Web: PASS.
- ChatGPT Desktop, Chat normal y sin Work: PASS.
- Skill real en Desktop: PASS; leyó controles desde GitHub bajo `project/00_CONTROL/` sin depender de `PROJECT.md` ni checkout local.
- PDF real desde Drive sin Base64, render/visión `complete`, `left`, `right`: PASS.
- Escritura reversible, atomicidad multiarchivo, control de concurrencia y plugin aislado: PASS.
- CI final sobre la rama de migración: PASS.

## H4

Antes del cutover:

- `main == cd683dd3a745c1f7bbabc154510885dbdad9dde8` — PASS.
- `backup/pre-github-workspace-v2` conservaba el mismo SHA — PASS.
- `migration/github-workspace-v2 == eee9eddeaf7f1495c5cd48fb0bb12ff0ae0e009e` — PASS.
- Comparación Git: fast-forward puro, `ahead_by: 14`, `behind_by: 0`, merge base = SHA inicial — PASS.

Cutover:

```text
update_ref(main, eee9eddeaf7f1495c5cd48fb0bb12ff0ae0e009e, force=false)
```

Resultado: éxito.

Después del cutover:

- `main` en el commit esperado — PASS.
- schema 2, estado `portada`/`clean`, 35 unidades — PASS.
- Manual v1.5, Edición v3.4, Diario, Glosario, cinco índices e históricos — PASS.
- PDF con identidad, tamaño, hash y páginas esperados; entrega sin Base64 — PASS.
- CI sobre `main` (run 46) — PASS.

## Pendiente

- H5: ciclo editorial real sobre `main` y continuidad desde otra sesión/ordenador.
- H6: limpieza de Drive y retirada final de legado después de superar la aceptación restante.

La rama `backup/pre-github-workspace-v2` debe conservarse durante esta fase. No usar `force=true` para rollback.
