# Estado de implementación — GitHub workspace v2

**Fecha:** 5 de septiembre de 2026  
**Rama:** `migration/github-workspace-v2`  
**Versión preparada:** 2.0.0  
**Estado:** H1 y H2 completados; H3 parcialmente validado

La arquitectura definida en `ARQUITECTURA_CHATGPT_GITHUB_DRIVE.md` está construida en la rama de migración. El plan detallado se mantiene en `PLAN_IMPLEMENTACION_GITHUB_WORKSPACE_V2.md` y los resultados de aceptación de H3 en `VALIDACION_H3_2026-09-05.md`.

## H3 validado

- CI en Windows y Ubuntu, Python 3.10 y 3.13: PASS.
- Bootstrap de Chat normal Web desde `PROJECT.md`: PASS.
- Reconstrucción de schema 2, estado y modos desde GitHub: PASS.
- PDF de Drive como archivo real sin Base64: PASS.
- Identidad, tamaño, SHA-256 y 18 páginas del PDF: PASS.
- Render y visión de unidades `complete`, `left` y `right`: PASS.
- Escritura Git reversible crear/leer/actualizar/borrar: PASS.
- Operación multiarchivo en un único commit atómico: PASS.
- Detección de concurrencia por `base_sha`: PASS.
- Plugin aislado autocontenido y skill estáticamente autocontenida: PASS mediante CI.

## H3 pendiente

- Repetir el bootstrap v2 en ChatGPT Desktop, en Chat normal y sin Work.
- Invocar realmente `editar-catastro-sorrios` en una superficie compatible con skills.

Hasta que esas dos pruebas sean PASS, H3 no se considera cerrado y no debe ejecutarse H4.

Aún no se ha hecho el cutover. `main` continúa en `cd683dd3a745c1f7bbabc154510885dbdad9dde8` y Google Drive no se ha limpiado.
