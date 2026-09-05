# Sorríos — Catastro de Ensenada

Este archivo es la entrada del proyecto para Chat normal en Web o Desktop.
No presupone Work, checkout local, Python, Git local, WSL, VS Code ni una skill instalada.

## Inicio obligatorio

1. Trabaja con el repositorio privado `miguel-conde/sorrios-ensenada`.
2. Lee `project/00_CONTROL/proyecto.yaml` y `project/00_CONTROL/estado.yaml` desde la rama o commit que corresponda a la tarea.
3. Lee `plugins/sorrios-ensenada/skills/editar-catastro-sorrios/references/task-modes.md` y determina el modo de tarea.
4. Carga solo las referencias que ese modo necesite. Para editar, auditar o cambiar el método, incluye `workspace-contract.md`; añade `editorial-procedure.md`, `document-schemas.md`, `github-operations.md` y `pdf-access.md` cuando proceda.
5. Trata `project/` como workspace. No uses copias de conversaciones, descargas ni archivos locales como estado canónico.
6. Accede a Google Drive solo para leer el PDF declarado en `authorities.manuscript` de `proyecto.yaml`.

## Reglas de autoridad

- La materialidad del manuscrito procede del PDF de Drive.
- El método editorial procede de `project/00_CONTROL/Manual_Editorial.md`.
- Identidad, estado y secuencia proceden de los controles bajo `project/00_CONTROL/`.
- Edición, Diario, Glosario e índices proceden de `project/20_TRABAJO_EDITORIAL/`.
- El historial técnico procede de Git; las operaciones semánticas se registran en `project/00_CONTROL/OPERACIONES/`.

## Escritura

No escribas en consultas de solo lectura.

Para una operación de varios archivos, sigue `references/github-operations.md`: prepara todos los cambios desde un mismo `base_sha` y publícalos mediante un único commit Git atómico. Si la rama objetivo ha cambiado desde `base_sha`, no publiques hasta releer y reconciliar.

Nunca subas el PDF al repositorio ni escribas en Drive durante el flujo normal.
