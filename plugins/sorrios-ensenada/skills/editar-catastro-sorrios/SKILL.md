---
name: editar-catastro-sorrios
description: Gestiona, consulta, audita y edita la edición crítica del Catastro de Ensenada de Sorribas y Santibáñez de Ordás de 1752. Úsala para cualquier tarea de este expediente; no la uses para otros catastros.
---

# Editar el Catastro de Sorríos

Esta skill es autocontenida. No requiere `PROJECT.md`, Work, checkout local, Git local, Python local, WSL ni VS Code.

El workspace canónico está en el repositorio privado `miguel-conde/sorrios-ensenada`, bajo `project/`. Google Drive conserva solo el PDF autoritativo y se usa en modo de solo lectura.

## Inicio

1. Determina la rama o commit de GitHub que corresponde a la tarea. En trabajo normal usa la rama canónica declarada en `project/00_CONTROL/proyecto.yaml`; durante una migración o prueba usa la rama indicada por el usuario.
2. Lee `project/00_CONTROL/proyecto.yaml` y `project/00_CONTROL/estado.yaml` desde ese mismo ref.
3. Comprueba que no exista una operación incompleta.
4. Lee [task-modes.md](references/task-modes.md) y fija el modo antes de abrir más archivos.
5. Carga solo las referencias y documentos que necesite ese modo.

Si falta un archivo declarado, el estado no concuerda con la edición, cambia el ref mientras preparas una escritura o existe una operación incompleta, detén la edición y audita.

## Modos

- **Consulta puntual:** lee solo controles y archivos necesarios. No escribas.
- **Edición de unidad:** lee controles, Manual, unidad del PDF y documentos afectados. Sigue el cierre completo.
- **Auditoría:** comprueba estructura, schema, versiones, estado, secuencia y operaciones. Corrige solo si el usuario lo pide.
- **Cambio metodológico:** prepara una propuesta. No cambies el Manual sin aprobación expresa.
- **Estudio histórico:** actúa solo si `historical_study_enabled` vale `true`.

## Reglas de autoridad

- El PDF de Drive manda sobre la lectura material del manuscrito.
- `project/00_CONTROL/Manual_Editorial.md` manda sobre el método.
- `project/00_CONTROL/proyecto.yaml`, `estado.yaml` y `unidades.yaml` mandan sobre identidad, estado y secuencia.
- `project/20_TRABAJO_EDITORIAL/` contiene la edición y sus derivados vivos.
- Git conserva el historial técnico; `project/00_CONTROL/OPERACIONES/` conserva las operaciones semánticas.
- `project/90_ARCHIVO/` es histórico y no se usa como fuente viva salvo auditoría o consulta histórica expresa.

## PDF

Accede a Drive solo para leer el archivo declarado en `authorities.manuscript` de `project/00_CONTROL/proyecto.yaml`. Comprueba `file_id`, nombre, tamaño y, cuando dispongas de los bytes, SHA-256. No escribas en Drive. No subas el PDF a GitHub. No uses Base64 ni materialización local como parte del flujo normal.

Lee [pdf-access.md](references/pdf-access.md) cuando una tarea requiera ver el manuscrito.

## Escritura en GitHub

No escribas en consultas de solo lectura.

Para una operación de varios archivos:

1. lee el SHA de la rama objetivo y guárdalo como `base_sha`;
2. prepara todos los cambios contra ese mismo estado;
3. valida el conjunto antes de publicar;
4. comprueba de nuevo que la rama sigue en `base_sha`;
5. publica todos los cambios en un único commit atómico;
6. verifica el commit y los archivos resultantes.

Si la rama cambió, no publiques: relee y reconcilia. Actualiza `estado.yaml` en último lugar dentro del conjunto preparado. No declares un cierre si falla una comprobación.

Lee [github-operations.md](references/github-operations.md) para el protocolo completo.

## Edición

- No uses una transcripción no validada como prueba histórica.
- No avances si la unidad anterior no está cerrada.
- No fuerces lecturas dudosas.
- Prepara primero las altas de Glosario e índices; incorpóralas solo tras validar la unidad.
- Verifica edición, derivados, Diario y estado antes de cerrar.

Lee [editorial-procedure.md](references/editorial-procedure.md) al editar o cerrar una unidad.

## Contrato y esquemas

Lee [workspace-contract.md](references/workspace-contract.md) para autoridades, estructura y conflictos. Lee [document-schemas.md](references/document-schemas.md) al crear, reparar o validar controles.

Las referencias de esta skill forman parte del plugin y explican el procedimiento. Los documentos vivos del proyecto están siempre bajo `project/` en GitHub.