---
name: editar-catastro-sorrios
description: Gestiona, consulta, audita y edita la edición crítica del Catastro de Ensenada de Sorribas y Santibáñez de Ordás de 1752. Úsala para cualquier tarea de este expediente; no la uses para otros catastros.
---

# Editar el Catastro de Sorríos

La carpeta canónica es:

https://drive.google.com/drive/folders/1gS8ZUgCxdYuJmb3TCWAN-nYo_Rjds6tJ

## Inicio

1. Lee `00_CONTROL/proyecto.yaml` y `00_CONTROL/estado.yaml`.
2. Comprueba que no exista una operación incompleta.
3. Elige el modo antes de leer más archivos.
4. Localiza los archivos por sus identificadores de Drive.

Si falta un archivo declarado, cambia su identificador o hay una operación incompleta, detén la edición y audita.

## Modos

- **Consulta puntual:** lee solo los controles y los archivos necesarios. No escribas.
- **Edición de unidad:** lee los controles, el Manual, la unidad del PDF y los documentos afectados. Sigue el cierre completo.
- **Auditoría:** comprueba estructura, versiones, estado e identificadores. Corrige solo si el usuario lo pide.
- **Cambio metodológico:** prepara una propuesta. No cambies el Manual sin aprobación expresa.
- **Estudio histórico:** actúa solo si `historical_study_enabled` vale `true`.

Lee [task-modes.md](references/task-modes.md) para los límites de cada modo.

## Reglas

- El PDF manda sobre la lectura material.
- El Manual de Drive manda sobre el método.
- La skill guía el trabajo; no duplica el Manual.
- No uses una transcripción no validada como prueba histórica.
- No avances si la unidad anterior no está cerrada.
- No fuerces lecturas dudosas.
- Una consulta de solo lectura nunca cambia Drive.
- En una operación de varios archivos, prepara y valida todo antes de escribir.
- Actualiza `estado.yaml` en último lugar.
- Verifica cada archivo tras escribirlo.
- No declares un cierre si falla una comprobación.

Lee [workspace-contract.md](references/workspace-contract.md) para la autoridad y el protocolo de Drive. Lee [editorial-procedure.md](references/editorial-procedure.md) al editar o cerrar una unidad. Lee [document-schemas.md](references/document-schemas.md) al crear, reparar o validar archivos de control.

## Ayudas

- `scripts/validate_workspace.py`: valida una copia local de la carpeta.
- `scripts/render_unit.py`: extrae una unidad del PDF según `unidades.yaml`.
- `scripts/validate_operation.py`: compara estados anterior y posterior.

Las plantillas de `assets/templates/` sirven para crear o reparar archivos; nunca sustituyen a los documentos vivos de Drive.
