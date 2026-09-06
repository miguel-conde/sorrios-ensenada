# Cambios

## 6 de septiembre de 2026 — Cutover GitHub workspace v2 (H4)

- H3 cerrado con todas las pruebas de aceptación previas al cutover en PASS, incluida invocación real del complemento/skill en ChatGPT Desktop.
- Verificado inmediatamente antes del cutover que `main` seguía en `cd683dd3a745c1f7bbabc154510885dbdad9dde8` y que `migration/github-workspace-v2` era un fast-forward puro hasta `eee9eddeaf7f1495c5cd48fb0bb12ff0ae0e009e`.
- Ejecutado fast-forward de `main` mediante `update_ref(..., force=false)`; GitHub pasa a ser el workspace canónico del proyecto vivo.
- Verificación post-cutover en `main`: schema 2; estado `portada` y `clean`; 35 unidades; Manual v1.5; Edición v3.4; Diario, Glosario, cinco índices e históricos preservados.
- Revalidado el PDF autoritativo de Drive: mismo file ID, nombre, tamaño, 18 páginas y SHA-256; acceso como archivo real y sin Base64.
- CI disparado sobre `main` tras el cutover: PASS.
- Se conserva `backup/pre-github-workspace-v2` para rollback durante la aceptación.
- H5 (ciclo editorial real y continuidad entre sesiones/ordenadores) y H6 (limpieza de Drive) siguen pendientes.

## 5 de septiembre de 2026 — GitHub workspace v2 (preparación 2.0.0)

- Construida la versión 2.0.0 en `migration/github-workspace-v2`.
- Migrados a `project/` los documentos vivos e históricos de texto; no se ha subido ningún PDF.
- `proyecto.yaml` pasa a schema 2 en la rama, con GitHub como workspace previsto tras el cutover; Drive queda reservado al PDF autoritativo en solo lectura.
- Añadido `PROJECT.md` para Chat normal y refactorizada la skill autocontenida.
- Retirada la materialización Base64/local; tools, tests y CI adaptados.
- Estado editorial preservado: portada; ninguna unidad validada o cerrada; D-001 abierta.
- `main` seguía sin cambios en ese momento; cutover y limpieza de Drive quedaban pendientes de H3/H4/H6.

## 1 de septiembre de 2026 — Migración de arquitectura

- Creada la copia completa `90_ARCHIVO/PREMIGRACION_2026-08-31`.
- Creada la estructura `00_CONTROL`, `10_FUENTE_PRIMARIA`, `20_TRABAJO_EDITORIAL`, `30_RESULTADOS` y `90_ARCHIVO`.
- Separados identidad (`proyecto.yaml`), estado (`estado.yaml`) y secuencia (`unidades.yaml`).
- Actualizado el Manual Editorial de v1.4 a v1.5 sin cambiar criterios paleográficos.
- Actualizada la Edición crítica de v3.3 a v3.4 sin cambiar transcripciones ni unidades.
- Reducidas las instrucciones del proyecto a su función de entrada.
- Conservado el Diario como registro de dudas, incidencias y decisiones.
- Estado conservado: portada; ninguna unidad validada o cerrada; D-001 abierta.

## Historial anterior

El historial anterior se conserva íntegro en el Diario Editorial y en la copia previa de `REGISTRO_FUENTES_Y_VERSIONES.md`.
