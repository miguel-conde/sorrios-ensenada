# Estado de implementación — GitHub workspace v2

**Fecha:** 6 de septiembre de 2026  
**Rama canónica:** `main`  
**Versión activa:** 2.0.0  
**Estado:** H1, H2, H3 y H4 completados; H5 es el siguiente hito

La arquitectura definida en `ARQUITECTURA_CHATGPT_GITHUB_DRIVE.md` está activa en `main`. GitHub es ya el workspace canónico del proyecto vivo y Google Drive queda reservado al PDF autoritativo en solo lectura. El plan detallado se mantiene en `PLAN_IMPLEMENTACION_GITHUB_WORKSPACE_V2.md`; la validación de H3 está en `VALIDACION_H3_2026-09-05.md` y la de H4 en `VALIDACION_H4_2026-09-06.md`.

## H3 validado

- CI en Windows y Ubuntu, Python 3.10 y 3.13: PASS.
- Bootstrap de Chat normal Web desde `PROJECT.md`: PASS.
- Bootstrap de ChatGPT Desktop, Chat normal y sin Work: PASS.
- Reconstrucción de schema 2, estado y modos desde GitHub: PASS.
- PDF de Drive como archivo real sin Base64: PASS.
- Identidad, tamaño, SHA-256 y 18 páginas del PDF: PASS.
- Render y visión de unidades `complete`, `left` y `right`: PASS.
- Escritura Git reversible, atomicidad multiarchivo y concurrencia por `base_sha`: PASS.
- Plugin aislado autocontenido y skill estáticamente autocontenida: PASS.
- Instalación Codex del plugin `sorrios-ensenada@personal` 2.0.0: PASS.
- Invocación real del complemento `Catastro de Sorríos` en ChatGPT Desktop: PASS; sin `PROJECT.md` ni checkout local leyó desde GitHub los controles de `project/00_CONTROL/` y reconstruyó exactamente el estado esperado.

## H4 completado

- `main` se revalidó en el SHA congelado `cd683dd3a745c1f7bbabc154510885dbdad9dde8` inmediatamente antes del cutover.
- `backup/pre-github-workspace-v2` conserva ese mismo SHA.
- La rama `migration/github-workspace-v2` estaba en el commit final validado `eee9eddeaf7f1495c5cd48fb0bb12ff0ae0e009e`.
- La comparación confirmó fast-forward puro: `ahead_by: 14`, `behind_by: 0`, merge base igual al SHA inicial.
- Se ejecutó `update_ref(main, eee9edde…, force=false)` con éxito.
- `main` quedó exactamente en `eee9eddeaf7f1495c5cd48fb0bb12ff0ae0e009e`.
- El CI disparado sobre `main` (run 46) terminó `success`.
- Verificación post-cutover desde `main`: schema 2; plugin/skill 2.0.0; estado `portada`, página 1 `complete`, `operation.status: clean`; 35 unidades; Manual v1.5; Edición v3.4; Diario, Glosario, cinco índices e históricos presentes.
- El PDF canónico fue revalidado desde Drive: mismo file ID, nombre, MIME, 5.038.575 bytes, 18 páginas y SHA-256 `d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24`; entrega sin Base64.

## Siguiente

- **H5:** ejecutar un ciclo editorial real sobre `main` y comprobar continuidad desde otro ordenador/sesión.
- **H6:** limpiar Drive y retirar legado únicamente después de superar H5 y la aceptación restante.

Google Drive todavía no se ha limpiado. La rama `backup/pre-github-workspace-v2` debe conservarse durante la fase de aceptación y rollback.
