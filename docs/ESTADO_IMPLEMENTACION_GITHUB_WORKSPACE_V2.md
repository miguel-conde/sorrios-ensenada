# Estado de implementación — GitHub workspace v2

**Fecha:** 6 de septiembre de 2026  
**Rama canónica:** `main`  
**Versión activa:** 2.0.0  
**Estado:** H1, H2, H3, H4 y H5 completados; H6 es el siguiente hito

La arquitectura definida en `ARQUITECTURA_CHATGPT_GITHUB_DRIVE.md` está activa en `main`. GitHub es ya el workspace canónico del proyecto vivo y Google Drive queda reservado al PDF autoritativo en solo lectura. El plan detallado se mantiene en `PLAN_IMPLEMENTACION_GITHUB_WORKSPACE_V2.md`; las validaciones de H3, H4 y H5 están en `VALIDACION_H3_2026-09-05.md`, `VALIDACION_H4_2026-09-06.md` y `VALIDACION_H5_2026-09-06.md`.

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

## H5 completado

- Adaptado el test de estado editorial para validar progreso coherente en lugar de fijar permanentemente `current_unit: portada`.
- Commit de preparación `53b7d17940e8d5a84728624237fdf8a2f2b030c6`; CI run 49: PASS.
- Ejecutado el primer ciclo editorial real sobre `main`, unidad `portada`, leyendo visualmente el PDF autoritativo desde Drive sin OCR ni Base64.
- Resuelta D-001 como cruz invocativa reconocible (`†`).
- Completada y validada la Portada; actualizados Diario e Índice de topónimos únicamente con derivados justificados.
- Publicación atómica con `base_sha` y `update_ref(..., force=false)` en el commit `6bf596546ce3141d1cd2d13f236b5ec7af76383f` (`editorial: validate and close portada`).
- CI run 50 sobre el commit editorial: PASS en Windows y Ubuntu, Python 3.10 y 3.13.
- Estado resultante: `last_validated_unit: portada`, `last_closed_unit: portada`, `current_unit: reverso_portada`, página 2 `left`, sin dudas abiertas y `operation.status: clean`.
- Prueba de continuidad desde otro ordenador, en Chat normal y solo lectura, usando `PROJECT.md` y GitHub `main`: PASS.
- El segundo ordenador reconstruyó exactamente el estado resultante y la transcripción validada de la Portada sin checkout local, Git local, Python local, WSL, VS Code, Drive ni plugin del proyecto.

## Siguiente

- **H6:** limpiar Google Drive y retirar el legado únicamente después de una última comprobación del inventario y de que todo texto/histórico necesario está preservado en GitHub.

Google Drive todavía no se ha limpiado. La rama `backup/pre-github-workspace-v2` debe conservarse durante la fase final de aceptación y rollback hasta completar H6.
