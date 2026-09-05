# Procedimiento editorial

1. Lee `proyecto.yaml`, `estado.yaml` y `unidades.yaml` desde el mismo `base_sha`.
2. Confirma la unidad actual, su ubicación y que la anterior esté cerrada.
3. Obtén el PDF de Drive según `pdf-access.md` y lee visualmente la unidad completa.
4. Transcribe línea por línea.
5. Revisa la transcripción contra el PDF.
6. Aplica el Manual vigente.
7. Completa observaciones, notas y referencias.
8. Prepara, sin publicar, las altas del Glosario y los índices.
9. Registra las dudas que sigan abiertas.
10. Supera el control de calidad y valida la unidad.
11. Prepara los cambios de edición, derivados, Diario, registro de operación y `estado.yaml`; calcula el nuevo estado al final de la preparación.
12. Valida el conjunto completo sin publicar estados parciales.
13. Comprueba que la rama objetivo sigue en `base_sha`.
14. Publica todos los archivos mediante un único commit Git atómico según `github-operations.md`.
15. Verifica el nuevo commit, los archivos afectados y el estado resultante.

No comiences la unidad siguiente hasta completar los quince pasos.
