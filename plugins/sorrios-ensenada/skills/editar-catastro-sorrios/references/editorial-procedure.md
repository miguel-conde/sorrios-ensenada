# Procedimiento editorial

1. Lee `proyecto.yaml`, `estado.yaml` y `unidades.yaml` desde el mismo `base_sha`.
2. Confirma la unidad actual, su ubicación y que la anterior esté cerrada.
3. Obtén el PDF de Drive según `pdf-access.md` y lee visualmente la unidad completa.
4. Transcribe línea por línea.
5. Revisa la transcripción contra el PDF.
6. Aplica el Manual vigente.
7. Antes de decidir las Notas históricas, inventaría los posibles datos históricos de la unidad y clasifica expresamente cada uno como: **A. Sin nota necesaria**; **B. Glosario o índice**; **C. Nota histórica puntual**; o **D. Diario o futuro Estudio Histórico**.
8. Investiga externamente solo los candidatos C cuya clasificación o contenido no pueda resolverse con las fuentes internas. Distingue siempre lo que afirma el manuscrito, lo que aporta la fuente externa y cualquier inferencia editorial.
9. Decide de forma positiva si `Notas históricas` debe contener una o más notas o puede quedar justificadamente vacía. Comprueba además que los elementos B se dirigen al Glosario o índice correcto y que los D no se convierten prematuramente en afirmaciones históricas consolidadas.
10. Completa observaciones, notas y referencias.
11. Prepara, sin publicar, las altas del Glosario y los índices.
12. Registra las dudas que sigan abiertas.
13. Supera el control de calidad y valida la unidad. El control debe responder expresamente: «¿Se ha evaluado, y no por defecto, si esta unidad necesita una Nota histórica puntual?», con apoyo en la clasificación A/B/C/D.
14. Prepara los cambios de edición, derivados, Diario, registro de operación y `estado.yaml`; calcula el nuevo estado al final de la preparación.
15. Valida el conjunto completo sin publicar estados parciales.
16. Comprueba que la rama objetivo sigue en `base_sha`.
17. Publica todos los archivos mediante un único commit Git atómico según `github-operations.md`.
18. Verifica el nuevo commit, los archivos afectados y el estado resultante.

No comiences la unidad siguiente hasta completar los dieciocho pasos.
