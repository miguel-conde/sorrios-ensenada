# Plan de implementación — GitHub workspace v2
## Migración de Sorríos — Catastro de Ensenada desde 1.2.3

**Estado:** propuesta para aprobación; no ejecutar todavía  
**Fecha:** 5 de septiembre de 2026  
**Versión de partida:** 1.2.3  
**Versión de destino recomendada:** 2.0.0

---

# 1. Resultado buscado

```text
GitHub       = proyecto vivo + método + skill + código + historial
Google Drive = únicamente PDF autoritativo
```

ChatGPT Web y Desktop deberán operar mediante Chat normal cargando `PROJECT.md`. La skill `editar-catastro-sorrios` seguirá funcionando en entornos compatibles mediante `SKILL.md`. Ambos consumirán las mismas referencias físicas.

---

# 2. Decisiones fijadas

1. Los documentos vivos residirán bajo `project/`.
2. El método común permanecerá físicamente en `plugins/sorrios-ensenada/skills/editar-catastro-sorrios/references/`.
3. Las plantillas comunes permanecerán en `assets/templates/` de la skill.
4. `PROJECT.md` y `SKILL.md` no dependerán entre sí; ambos apuntarán al mismo núcleo.
5. Las operaciones multiarchivo se publicarán mediante un único commit Git atómico.
6. Drive será de solo lectura y solo para el PDF.
7. La versión objetivo será 2.0.0 salvo decisión posterior explícita.

---

# 3. Estructura final

```text
/
├── PROJECT.md
├── project/
│   ├── 00_CONTROL/
│   │   ├── proyecto.yaml
│   │   ├── estado.yaml
│   │   ├── unidades.yaml
│   │   ├── Manual_Editorial.md
│   │   ├── CAMBIOS.md
│   │   └── OPERACIONES/
│   ├── 20_TRABAJO_EDITORIAL/
│   │   ├── Edicion_Critica.md
│   │   ├── Diario_Editorial.md
│   │   ├── Glosario.md
│   │   └── INDICES/
│   ├── 30_RESULTADOS/
│   └── 90_ARCHIVO/
├── plugins/sorrios-ensenada/
│   ├── .codex-plugin/plugin.json
│   ├── pyproject.toml
│   ├── skills/editar-catastro-sorrios/
│   │   ├── SKILL.md
│   │   ├── agents/openai.yaml
│   │   ├── references/
│   │   │   ├── task-modes.md
│   │   │   ├── workspace-contract.md
│   │   │   ├── editorial-procedure.md
│   │   │   ├── document-schemas.md
│   │   │   ├── github-operations.md
│   │   │   └── pdf-access.md
│   │   └── assets/templates/
│   └── tools/
├── docs/
│   ├── ARQUITECTURA_CHATGPT_GITHUB_DRIVE.md
│   └── PLAN_IMPLEMENTACION_GITHUB_WORKSPACE_V2.md
├── tests/
├── .github/workflows/
└── DEVELOPMENT.md
```

---

# 4. Inventario y estado de partida

Antes de ejecutar:

- confirmar `operation.status: clean`;
- confirmar `current_unit: portada`;
- registrar el SHA exacto de `main`;
- congelar temporalmente la edición editorial;
- inventariar Drive y GitHub;
- comprobar los históricos de `90_ARCHIVO`;
- confirmar que las carpetas heredadas vacías siguen vacías.

La migración anterior de 1 de septiembre sirve como precedente de rollback y verificación.

---

# 5. Migración de documentos de Drive

| Origen Drive | Destino GitHub | Tratamiento |
|---|---|---|
| `00_CONTROL/proyecto.yaml` | `project/00_CONTROL/proyecto.yaml` | importar exacto y luego convertir a schema 2 |
| `estado.yaml` | misma ruta bajo `project/` | copiar sin alterar estado editorial |
| `unidades.yaml` | misma ruta | copiar exactamente |
| `Manual_Editorial.md` | misma ruta | copiar exactamente |
| `CAMBIOS.md` | misma ruta | copiar y añadir después la nueva migración |
| `OPERACIONES/` | misma ruta | copiar íntegramente |
| `INSTRUCCIONES_PROYECTO.md` | `project/90_ARCHIVO/SISTEMA_1_2_3/` | archivar; sustituir funcionalmente por `PROJECT.md` |
| `Edicion_Critica.md` | misma ruta bajo `project/` | copiar exactamente |
| `Diario_Editorial.md` | misma ruta | copiar exactamente |
| `Glosario.md` | misma ruta | copiar exactamente |
| cinco índices | rutas equivalentes | copiar exactamente |
| `30_RESULTADOS/` | ruta equivalente | copiar exactamente |
| históricos textuales | `project/90_ARCHIVO/` | preservar |
| PDF | Drive | NO migrar |

Para cualquier PDF histórico duplicado, comparar hash con el canónico. Si coincide, conservar solo metadatos en GitHub; si no coincide, detener su eliminación hasta decisión específica.

---

# 6. Nuevo `proyecto.yaml`

Evolucionará a `schema_version: 2` y declarará:

- repositorio `miguel-conde/sorrios-ensenada`;
- rama canónica `main`;
- `project_root: project`;
- plugin/skill 2.0.0;
- GitHub como proveedor de Manual, controles y documentos;
- Drive exclusivamente para `authorities.manuscript`;
- file ID, nombre, SHA-256, tamaño y páginas del PDF.

Se eliminan los IDs de Drive de controles, Manual, edición, diario, índices y resultados.

---

# 7. `PROJECT.md`

Crear un bootstrap breve para Chat normal que:

1. lea `proyecto.yaml` y `estado.yaml`;
2. cargue `references/task-modes.md`;
3. determine el modo;
4. cargue las referencias necesarias;
5. opere sobre `project/`;
6. acceda a Drive únicamente para el PDF;
7. no presuponga Work ni entorno local.

No duplicará el método.

---

# 8. Refactorización de la skill

`SKILL.md` se conserva, pero se simplifica para cargar directamente las referencias de su propio directorio y operar contra el repo canónico.

`SKILL.md` no dependerá de `/PROJECT.md`.

`agents/openai.yaml` conservará la interfaz y se actualizará el prompt por defecto para dejar de tratar Drive como workspace.

`plugin.json` conservará nombre y skill path, actualizará versión/descripciones y mantendrá capacidad de escritura.

---

# 9. Método común

Conservar/adaptar:

- `task-modes.md`;
- `workspace-contract.md`;
- `editorial-procedure.md`;
- `document-schemas.md`.

Crear:

- `github-operations.md`;
- `pdf-access.md`.

Retirar del método normal:

- `drive-materialization.md`;
- `local-execution.md`.

El contenido de desarrollo que siga siendo útil se moverá a `DEVELOPMENT.md`.

---

# 10. Operaciones Git atómicas

Para una operación multiarchivo:

```text
1. leer main = base_sha
2. leer todos los archivos desde base_sha
3. preparar todos los contenidos
4. crear blobs
5. crear tree basado en base_sha
6. crear un único commit con padre base_sha
7. comprobar main == base_sha
8. si cambió: abortar
9. si no cambió: update_ref(main, commit, force=false)
10. verificar main y todos los archivos
```

Edición, derivados, Diario, estado y registro de operación se publican juntos.

No se utilizará `force=true` en operaciones normales.

---

# 11. Concurrencia

Control optimista mediante `base_sha`:

```text
A lee X → crea Y padre X
B lee X → crea Z padre X
A publica Y
B ve main=Y ≠ X → no publica Z
```

B debe releer y reconciliar.

Drive no necesita lock porque será solo lectura.

---

# 12. Scripts/tools

| Actual | Destino |
|---|---|
| `materialize_drive_payload.py` | eliminar |
| `materialize_drive_text.py` | eliminar |
| `render_unit.py` | conservar inicialmente como tool de desarrollo/referencia |
| `path_utils.py` | conservar/simplificar rutas lógicas |
| `validate_workspace.py` | sustituir por `validate_project.py` |
| `validate_operation.py` | retirar; sustituir por protocolo Git + tests |

`validate_project.py` verificará estructura, schema, 35 unidades, orden/IDs, coherencia de estado, secciones editoriales, rutas y metadatos del PDF, sin exigir un PDF físico local.

---

# 13. Tests

Eliminar:

- tests de materializadores.

Adaptar:

- `test_manifests.py`;
- `test_packaging.py`;
- `test_paths.py`;
- `test_render_unit.py` si se conserva el tool.

Sustituir:

- `test_validate_workspace.py`;
- `test_validate_operation.py`.

Añadir:

- `test_project_contract.py`;
- `test_bootstrap_contract.py`;
- `test_no_drive_workspace.py`;
- `test_project_schema.py`;
- `test_editorial_invariants.py`;
- `test_operation_records.py`;
- `test_no_committed_pdf.py`;
- `test_skill_self_contained.py`.

El test de plugin aislado debe verificar que `plugins/sorrios-ensenada` contiene todo lo necesario para la skill, incluidas referencias y plantillas.

---

# 14. CI y desarrollo

Mantener matriz Windows/Ubuntu y Python soportado para tests.

Eliminar Poppler como requisito general de CI; si `render_unit.py` sobrevive, su integración real podrá probarse opcionalmente.

`DEVELOPMENT.md` debe indicar expresamente que Python, Git, VS Code, WSL, Poppler y demás herramientas son solo de desarrollo, no requisitos de uso.

---

# 15. Estrategia Git de migración

Desde el SHA inicial crear:

```text
migration/github-workspace-v2
backup/pre-github-workspace-v2
```

`main` no cambia durante construcción y validación.

Secuencia recomendada de commits en la rama:

| Commit | Contenido |
|---|---|
| A | importar documentos activos e históricos de Drive sin transformarlos |
| B | crear `PROJECT.md`, schema 2 y adaptar referencias comunes |
| C | refactorizar skill/manifiestos |
| D | retirar materialización y reorganizar tools |
| E | adaptar tests, CI y `DEVELOPMENT.md` |
| F | actualizar documentación, `CAMBIOS.md`, operación y versión 2.0.0 |

---

# 16. Pruebas previas al cutover

Sobre la rama deben pasar:

- Chat normal Web;
- Chat normal Desktop;
- skill en entorno compatible;
- CI;
- lectura de controles;
- acceso al PDF sin Base64;
- render/visión de unidades `complete`, `left` y `right`;
- prueba reversible de escritura GitHub;
- validación de plugin aislado.

---

# 17. Cutover

Antes de publicar comprobar:

```text
main == SHA inicial
```

Si no coincide: STOP y reconciliar.

Si coincide:

```text
update_ref(main, migration_head, force=false)
```

El cambio debe ser fast-forward.

En ese instante GitHub pasa a ser la autoridad del proyecto vivo.

---

# 18. Verificación posterior

Comprobar inmediatamente:

- `main` en commit esperado;
- schema 2 válido;
- `estado.yaml` sigue `portada` y `clean`;
- 35 unidades;
- Manual v1.5;
- Edición v3.4 preservada;
- Diario, glosario e índices preservados;
- históricos preservados;
- `PROJECT.md` operativo en Web/Desktop;
- skill operativa donde proceda;
- PDF con file ID/tamaño/hash esperados;
- paleografía funcional.

---

# 19. Rollback

## Antes del cutover

No hay que revertir `main`; se corrige o descarta la rama.

## Después del cutover y antes de limpiar Drive

Conservar `backup/pre-github-workspace-v2`. Si es preciso volver atrás y no hay cambios legítimos posteriores, crear un nuevo commit de rollback cuyo árbol reproduzca el estado anterior; evitar retroceder `main` con `force=true`.

Si existen cambios posteriores, detener el rollback automático y reconciliar.

---

# 20. Limpieza de Drive

Solo después de superar toda la aceptación:

- comprobar que todo texto e histórico necesario está en GitHub;
- comprobar cualquier PDF histórico duplicado;
- retirar documentos no PDF;
- conservar el PDF canónico con su identidad actual.

Resultado deseado:

```text
Google Drive
└── sorrios_ensenada_orden_lectura_calidad_original.pdf
```

---

# 21. Criterios de aceptación final

Deben ser PASS:

- Web Chat normal;
- Desktop Chat normal;
- skill en entorno compatible;
- mismo núcleo común;
- plugin aislado autocontenido;
- GitHub lectura/escritura;
- commit multiarchivo atómico;
- concurrencia por SHA base;
- Drive solo lectura;
- PDF sin Base64;
- render `left/right/complete`;
- visión paleográfica;
- estado editorial preservado;
- 35 unidades;
- Manual, edición, diario, derivados e históricos preservados;
- continuidad entre ordenadores.

Deben ser NO REQUERIDOS para uso:

- Work;
- Python local;
- WSL;
- Git local;
- VS Code;
- checkout del proyecto;
- Poppler local.

---

# 22. Hitos

| Hito | Resultado |
|---|---|
| H1 | inventario, congelación, backup y rama |
| H2 | proyecto GitHub + bootstrap + núcleo/skill adaptados |
| H3 | tests/CI y validación Web/Desktop/skill |
| H4 | cutover fast-forward de `main` |
| H5 | ciclo editorial real y cambio de ordenador |
| H6 | limpieza de Drive y retirada de legado |

No avanzar mientras el hito anterior tenga un fallo abierto.
