# Estado de implementación — GitHub workspace v2

**Fecha:** 6 de septiembre de 2026  
**Rama:** `migration/github-workspace-v2`  
**Versión preparada:** 2.0.0  
**Estado:** H1, H2 y H3 completados; preparado para H4

La arquitectura definida en `ARQUITECTURA_CHATGPT_GITHUB_DRIVE.md` está construida en la rama de migración. El plan detallado se mantiene en `PLAN_IMPLEMENTACION_GITHUB_WORKSPACE_V2.md` y los resultados de aceptación de H3 en `VALIDACION_H3_2026-09-05.md`.

## H3 validado

- CI en Windows y Ubuntu, Python 3.10 y 3.13: PASS.
- Bootstrap de Chat normal Web desde `PROJECT.md`: PASS.
- Bootstrap de ChatGPT Desktop, Chat normal y sin Work: PASS.
- Reconstrucción de schema 2, estado y modos desde GitHub: PASS.
- PDF de Drive como archivo real sin Base64: PASS.
- Identidad, tamaño, SHA-256 y 18 páginas del PDF: PASS.
- Render y visión de unidades `complete`, `left` y `right`: PASS.
- Escritura Git reversible crear/leer/actualizar/borrar: PASS.
- Operación multiarchivo en un único commit atómico: PASS.
- Detección de concurrencia por `base_sha`: PASS.
- Plugin aislado autocontenido y skill estáticamente autocontenida: PASS mediante CI.
- Instalación local Codex del plugin `sorrios-ensenada@personal` 2.0.0: PASS.
- Invocación real del complemento `Catastro de Sorríos` en ChatGPT Desktop: PASS.
- La skill real, sin `PROJECT.md` ni checkout local, leyó desde GitHub `project/00_CONTROL/proyecto.yaml` y `project/00_CONTROL/estado.yaml` sobre `migration/github-workspace-v2` y reconstruyó exactamente el estado canónico esperado: PASS.

## H4

H3 está cerrado. Antes del cutover deben comprobarse de nuevo:

1. que `main` siga exactamente en el SHA congelado `cd683dd3a745c1f7bbabc154510885dbdad9dde8`;
2. que la rama `migration/github-workspace-v2` esté en el commit final validado de H3;
3. que `main` sea ancestro de la rama de migración, sin divergencia;
4. que el CI del commit final de H3 sea completamente verde.

Solo entonces se podrá hacer fast-forward de `main` al HEAD validado mediante `update_ref(force=false)`, seguido de verificación de `main` y CI.

Aún no se ha hecho el cutover. En la última comprobación previa al cierre documental de H3, `main` continuaba en `cd683dd3a745c1f7bbabc154510885dbdad9dde8`. Google Drive no se ha limpiado.
