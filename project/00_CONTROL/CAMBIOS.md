# Cambios

## 6 de septiembre de 2026 — Guía de uso del proceso editorial

- Añadida `docs/GUIA_USO_PROCESO_EDITORIAL.md` como guía práctica para el usuario del proyecto.
- La guía explica cómo solicitar los cinco modos de tarea, el ciclo normal de edición de una unidad, revisión previa a publicación, tratamiento de dudas, auditorías, cambios metodológicos, revisión de unidades validadas y futura activación del Estudio Histórico.
- Añadidas plantillas reutilizables de prompts para Chat normal y una referencia al uso equivalente desde entornos con la skill instalada.
- `PROJECT.md` enlaza la guía como ayuda informativa para el operador y aclara que no es necesario cargarla en cada tarea.
- La guía no es normativa y no modifica el Manual Editorial, la skill, los controles, el estado editorial ni el PDF autoritativo.

## 6 de septiembre de 2026 — H6 completado

- Inventariada la carpeta canónica de Google Drive y contrastado su contenido con GitHub.
- Confirmado que los textos vivos e históricos necesarios están preservados en GitHub `main`.
- Confirmado que el PDF histórico duplicado dentro de `90_ARCHIVO/PREMIGRACION_2026-08-31` era binariamente idéntico al PDF canónico.
- Movido el PDF canónico a la raíz de la carpeta `Sorrios - Catastro Ensenada`, conservando file ID `1GgBs68iTi53ue8-TbrYFABALxadhQe5u`, nombre, 5.038.575 bytes y SHA-256 `d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24`.
- El intento de borrado permanente del legado fue bloqueado por los controles de seguridad de la plataforma; no se produjo borrado parcial.
- Las siete carpetas antiguas fueron retiradas de la carpeta canónica y archivadas de forma reversible en la carpeta hermana `Sorrios - legado Drive retirado 2026-09-06` (ID `1cdycMdPbmP_-AXJgn2UnxiCrc_TZeUSh`).
- La carpeta canónica de Drive contiene ahora exactamente un elemento: el PDF autoritativo.
- Revalidado el PDF después del movimiento: archivo real, sin Base64, mismo tamaño y hash.
- H6 queda cerrado en PASS; H1-H6 están completados.

## 6 de septiembre de 2026 — H5 completado

- Corregido `tests/test_editorial_invariants.py` para que compruebe coherencia dinámica del progreso editorial en lugar de fijar permanentemente la Portada como unidad actual.
- Commit de preparación `53b7d17940e8d5a84728624237fdf8a2f2b030c6`; CI run 49: PASS en Windows/Ubuntu y Python 3.10/3.13.
- Ejecutado el primer ciclo editorial real sobre `main` con la unidad Portada.
- Leída visualmente la página 1 del PDF autoritativo desde Google Drive como archivo real, sin OCR y sin Base64.
- Validada y cerrada la Portada; resuelta D-001 como cruz invocativa reconocible (`†`).
- Actualizados únicamente la Edición crítica, Diario Editorial, Índice de topónimos, `estado.yaml` y el registro de operación correspondiente.
- Publicación Git multiarchivo atómica sobre `base_sha` mediante `update_ref(..., force=false)` en `6bf596546ce3141d1cd2d13f236b5ec7af76383f` (`editorial: validate and close portada`).
- CI run 50 sobre la operación editorial: PASS en Windows/Ubuntu y Python 3.10/3.13.
- Estado editorial resultante: Portada validada y cerrada; `reverso_portada` como unidad actual, página 2 izquierda; sin dudas abiertas; operación `clean`.
- Probada la continuidad desde otro ordenador mediante Chat normal y `PROJECT.md`, usando solo GitHub `main`: PASS.
- El segundo ordenador reconstruyó exactamente el estado y la transcripción validada de la Portada sin checkout local, Git local, Python local, WSL, VS Code, Drive ni plugin del proyecto.
- H5 queda cerrado en PASS.

## 6 de septiembre de 2026 — Cutover GitHub workspace v2 (H4)

- H3 cerrado con todas las pruebas de aceptación previas al cutover en PASS, incluida invocación real del complemento/skill en ChatGPT Desktop.
- Verificado inmediatamente antes del cutover que `main` seguía en `cd683dd3a745c1f7bbabc154510885dbdad9dde8` y que `migration/github-workspace-v2` era un fast-forward puro hasta `eee9eddeaf7f1495c5cd48fb0bb12ff0ae0e009e`.
- Ejecutado fast-forward de `main` mediante `update_ref(..., force=false)`; GitHub pasa a ser el workspace canónico del proyecto vivo.
- Verificación post-cutover en `main`: schema 2; estado `portada` y `clean`; 35 unidades; Manual v1.5; Edición v3.4; Diario, Glosario, cinco índices e históricos preservados.
- Revalidado el PDF autoritativo de Drive: mismo file ID, nombre, tamaño, 18 páginas y SHA-256; acceso como archivo real y sin Base64.
- CI disparado sobre `main` tras el cutover: PASS.
- Se conserva `backup/pre-github-workspace-v2` para rollback durante la aceptación.

## 5 de septiembre de 2026 — GitHub workspace v2 (preparación 2.0.0)

- Construida la versión 2.0.0 en `migration/github-workspace-v2`.
- Migrados a `project/` los documentos vivos e históricos de texto; no se ha subido ningún PDF.
- `proyecto.yaml` pasa a schema 2 en la rama, con GitHub como workspace previsto tras el cutover; Drive queda reservado al PDF autoritativo en solo lectura.
- Añadido `PROJECT.md` para Chat normal y refactorizada la skill autocontenida.
- Retirada la materialización Base64/local; tools, tests y CI adaptados.
- Estado editorial preservado: portada; ninguna unidad validada o cerrada; D-001 abierta.

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
