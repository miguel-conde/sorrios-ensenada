# Arquitectura objetivo ChatGPT + GitHub + Google Drive
## Guía de referencia — Sorríos, Catastro de Ensenada

**Estado:** propuesta aprobable para migración  
**Fecha:** 5 de septiembre de 2026  
**Versión actual comprobada:** 1.2.3  
**Versión objetivo recomendada:** 2.0.0  
**Repositorio:** `miguel-conde/sorrios-ensenada`

---

# 1. Objeto

Esta guía define la arquitectura objetivo del proyecto y sustituye las versiones anteriores de este documento. Describe la situación 1.2.3, los requisitos de la solución deseada, qué se conserva, qué se retira o modifica, la estructura futura, el modelo de operación y los criterios para utilizar el proyecto desde cualquier ordenador mediante ChatGPT Web o Desktop, siempre en Chat normal y sin Work.

La decisión central es:

> **GitHub será el workspace canónico completo. Google Drive conservará únicamente el PDF autoritativo.**

---

# 2. Arquitectura objetivo

```text
                         USUARIO
                            │
          ┌─────────────────┴─────────────────┐
          │                                   │
          ↓                                   ↓
   Chat normal                           Entorno skill
 Web / Desktop                                 │
          │                                    ↓
          ↓                                 SKILL.md
      PROJECT.md                               │
          │                                    │
          └───────────────┬────────────────────┘
                          ↓
 plugins/sorrios-ensenada/skills/editar-catastro-sorrios/
             references/ + assets/templates/
                     NÚCLEO COMÚN
                          │
                          ↓
                       project/
                          │
                   GitHub canónico
                          │
                          └───────────┐
                                      ↓
                                Google Drive
                                      │
                                      ↓
                               PDF autoritativo
```

El ordenador no contiene estado del proyecto. ChatGPT tampoco es fuente de estado. El estado persistente procede de GitHub y la materialidad documental del PDF de Drive.

---

# 3. Papel de cada sistema

## GitHub

Contendrá todo salvo el PDF:

- instrucciones y bootstraps;
- método común;
- controles y estado;
- Manual Editorial;
- secuencia de unidades;
- edición crítica;
- diario;
- glosario e índices;
- operaciones e historial;
- resultados;
- archivo histórico textual;
- plantillas;
- plugin y skill;
- tools, tests y documentación de desarrollo.

GitHub será de lectura y escritura.

## Google Drive

Conservará únicamente:

```text
sorrios_ensenada_orden_lectura_calidad_original.pdf
```

El PDF será de solo lectura en el flujo normal.

## ChatGPT

Habrá dos entradas al mismo núcleo:

- `PROJECT.md` para Chat normal Web/Desktop;
- `SKILL.md` para entornos que soporten `editar-catastro-sorrios`.

Ninguna de las dos contendrá una copia independiente del método.

---

# 4. Fuentes de autoridad

| Ámbito | Autoridad |
|---|---|
| Imagen/materialidad | PDF original en Drive |
| Método editorial | `project/00_CONTROL/Manual_Editorial.md` |
| Identidad/configuración | `project/00_CONTROL/proyecto.yaml` |
| Estado | `project/00_CONTROL/estado.yaml` |
| Secuencia | `project/00_CONTROL/unidades.yaml` |
| Edición | `project/20_TRABAJO_EDITORIAL/Edicion_Critica.md` |
| Diario | `project/20_TRABAJO_EDITORIAL/Diario_Editorial.md` |
| Glosario/índices | `project/20_TRABAJO_EDITORIAL/` |
| Operaciones | `project/00_CONTROL/OPERACIONES/` |
| Historial técnico | Git |
| Resultados | `project/30_RESULTADOS/` |
| Método común | `plugins/.../editar-catastro-sorrios/references/` |
| Plantillas | `plugins/.../editar-catastro-sorrios/assets/templates/` |

La memoria de una conversación nunca sustituye estos controles.

---

# 5. Requisitos

La solución debe:

- funcionar desde cualquier ordenador;
- funcionar en ChatGPT Web y ChatGPT Desktop;
- utilizar siempre Chat normal;
- no requerir Work;
- no requerir checkout local;
- no requerir WSL, Python local, Poppler, Git local, VS Code o Codex CLI para el uso normal;
- no depender de una skill instalada para funcionar en Chat normal;
- conservar la skill para entornos compatibles;
- reconstruir el estado desde GitHub en una conversación nueva;
- obtener el PDF directamente de Drive sin Base64;
- trabajar visualmente sobre páginas/unidades del manuscrito;
- detectar concurrencia antes de publicar cambios;
- publicar operaciones multiarchivo de forma atómica.

---

# 6. Situación actual: 1.2.3

La versión actual declarada del plugin es 1.2.3. La skill vive en:

```text
plugins/sorrios-ensenada/skills/editar-catastro-sorrios/
```

con `SKILL.md`, `agents/`, `references/`, `assets/templates/` y `scripts/`.

La 1.2.3 mezcla:

1. método editorial común;
2. interfaz específica de skill/plugin;
3. infraestructura local para materializar, validar y renderizar un workspace de Drive.

Drive sigue conteniendo actualmente controles, Manual, edición, diario, glosario, índices, resultados y archivos históricos. Esa es la situación de partida, no la deseada.

---

# 7. Capacidades ya comprobadas

En Chat normal se ha demostrado:

| Capacidad | Web | Desktop |
|---|---:|---:|
| GitHub privado | Sí | Sí |
| lectura/escritura GitHub | Sí | Sí |
| control por SHA | Sí | Sí |
| Drive | Sí | Sí |
| PDF sin Base64 | Sí | Sí |
| PDF como archivo real | Sí | Sí |
| render/recorte | Sí | Sí |
| visión paleográfica | Sí | Sí |
| Work necesario | No | No |

La skill personal no resultó invocable en el Chat normal probado. Por tanto, la arquitectura no puede depender de ella.

---

# 8. Estructura objetivo del repositorio

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
├── plugins/
│   └── sorrios-ensenada/
│       ├── .codex-plugin/plugin.json
│       ├── pyproject.toml
│       ├── skills/
│       │   └── editar-catastro-sorrios/
│       │       ├── SKILL.md
│       │       ├── agents/
│       │       ├── references/
│       │       │   ├── task-modes.md
│       │       │   ├── workspace-contract.md
│       │       │   ├── editorial-procedure.md
│       │       │   ├── document-schemas.md
│       │       │   ├── github-operations.md
│       │       │   └── pdf-access.md
│       │       └── assets/templates/
│       └── tools/
├── docs/
│   ├── ARQUITECTURA_CHATGPT_GITHUB_DRIVE.md
│   └── PLAN_IMPLEMENTACION_GITHUB_WORKSPACE_V2.md
├── tests/
├── .github/workflows/
└── DEVELOPMENT.md
```

No se crea un `method/` ni un `templates/` independiente en la raíz. Mantener el núcleo físicamente dentro del plugin conserva su capacidad de funcionar de manera autocontenida cuando se empaqueta o prueba aisladamente.

---

# 9. Método común y skill

El método común único vive en:

```text
plugins/sorrios-ensenada/skills/editar-catastro-sorrios/references/
```

Las plantillas comunes únicas viven en:

```text
plugins/sorrios-ensenada/skills/editar-catastro-sorrios/assets/templates/
```

Los dos bootstraps consumen directamente ese mismo núcleo:

```text
PROJECT.md ──┐
             ├── references/ + templates/
SKILL.md ────┘
```

`SKILL.md` **no dependerá de `PROJECT.md`**. De ese modo una distribución aislada del plugin conserva todo lo necesario para la skill.

Los cinco modos siguen siendo:

1. consulta puntual;
2. edición de unidad;
3. auditoría;
4. cambio metodológico;
5. estudio histórico.

---

# 10. `PROJECT.md`

Será el bootstrap universal para Chat normal. Debe ser pequeño y estable.

Su función será:

1. identificar el proyecto/repo;
2. leer `proyecto.yaml` y `estado.yaml`;
3. remitir a `references/task-modes.md`;
4. cargar solo las referencias necesarias para el modo;
5. utilizar `project/` como workspace;
6. acceder a Drive únicamente cuando se requiera el PDF.

No debe duplicar el Manual ni el procedimiento editorial.

---

# 11. PDF

`unidades.yaml` seguirá definiendo:

```text
unit_id → pdf_page + position
```

Flujo objetivo:

```text
unidades.yaml
      ↓
Drive → PDF completo sin Base64
      ↓
runtime efímero de ChatGPT
      ↓
render de página
      ↓
left / right / complete
      ↓
visión paleográfica
```

OCR nunca sustituye a la lectura visual del original.

---

# 12. Escritura y concurrencia en GitHub

Un cambio aislado de un solo archivo puede usar la API de contenidos con SHA previo.

Una operación editorial que afecte a varios archivos deberá publicarse mediante **un único commit Git atómico**:

```text
leer main = base_sha
      ↓
leer archivos desde base_sha
      ↓
preparar todos los cambios
      ↓
crear blobs + tree
      ↓
crear un commit con padre base_sha
      ↓
comprobar main == base_sha
      ↓
update_ref(main, commit, force=false)
      ↓
verificar
```

Si `main` ha cambiado, no se publica y la sesión relee/reconcilia.

Edición, derivados, Diario, `estado.yaml` y registro de operación pueden así aparecer juntos en `main`, evitando estados parciales.

---

# 13. Qué se conserva

Se conservan:

- GitHub privado;
- plugin y skill;
- `SKILL.md` y `agents/`;
- cinco modos;
- procedimiento editorial;
- Manual;
- controles y estado explícito;
- `unidades.yaml`;
- edición, diario, glosario e índices;
- resultados;
- operaciones e historial semántico útil;
- plantillas;
- tests y tools que sigan aportando garantías;
- regla de no forzar lecturas;
- verificación posterior a cada operación.

---

# 14. Qué se retira del flujo normal

Dejan de ser requisitos de uso:

- Drive como workspace;
- Base64;
- materialización local;
- Python/venv locales;
- Poppler/Pillow locales;
- WSL;
- Git/checkouts locales;
- VS Code;
- Codex CLI;
- plugin instalado localmente;
- Work.

`materialize_drive_payload.py` y `materialize_drive_text.py` quedan destinados a eliminación tras superar la migración.

`drive-materialization.md` será sustituido por `pdf-access.md` y `github-operations.md`.

---

# 15. Qué se rediseña

- `proyecto.yaml`: schema 2, GitHub como workspace, Drive solo para el PDF.
- `workspace-contract.md`: nuevo contrato de autoridades.
- `editorial-procedure.md`: cierre mediante commit atómico.
- `document-schemas.md`: nuevo schema.
- `validate_workspace.py`: sustituido por validación lógica del proyecto GitHub, sin PDF local.
- `validate_operation.py`: sustituido por protocolo Git atómico y tests.
- `render_unit.py`: opcional como tool de desarrollo/referencia.
- `path_utils.py`: conservar solo lo útil, especialmente rutas lógicas.
- `local-execution.md`: retirar del método normal e integrar lo útil en `DEVELOPMENT.md`.
- CI: Poppler deja de ser requisito general.

---

# 16. Documentos que migran desde Drive

Migrarán a `project/`:

- `proyecto.yaml`;
- `estado.yaml`;
- `unidades.yaml`;
- `Manual_Editorial.md`;
- `CAMBIOS.md`;
- `OPERACIONES/`;
- `Edicion_Critica.md`;
- `Diario_Editorial.md`;
- `Glosario.md`;
- cinco índices;
- `30_RESULTADOS/`;
- históricos textuales de `90_ARCHIVO/`.

`INSTRUCCIONES_PROYECTO.md` se conservará como histórico de 1.2.3 y será sustituido funcionalmente por `PROJECT.md`.

No se subirá ningún PDF a GitHub.

Las carpetas heredadas vacías no necesitan migrarse.

---

# 17. Versión objetivo

Se recomienda **2.0.0**, no 1.3.0, porque el cambio rompe el contrato operativo de 1.2.3:

```text
1.2.3 → Drive es workspace
2.0.0 → GitHub es workspace
```

Además `proyecto.yaml` cambia de schema 1 a schema 2.

---

# 18. Uso desde cualquier ordenador

## Web

1. iniciar sesión en ChatGPT;
2. disponer de conexión GitHub al repo privado;
3. disponer de conexión Drive al PDF;
4. abrir Chat normal;
5. pedir cargar `PROJECT.md`;
6. indicar modo/tarea.

## Desktop

Exactamente el mismo procedimiento, instalando únicamente la aplicación ChatGPT Desktop si se desea utilizar ese cliente.

Prompt objetivo:

```text
Trabaja con el proyecto Sorríos del repositorio
miguel-conde/sorrios-ensenada.
Carga PROJECT.md y sigue sus instrucciones.

Modo: <modo>.
Tarea: <tarea>.
```

## Skill

En un entorno compatible:

```text
$editar-catastro-sorrios
→ SKILL.md
→ mismas references
→ project/
→ Drive solo para PDF
```

---

# 19. Pruebas de aceptación

La nueva arquitectura solo se considera terminada si pasan:

- Chat normal Web;
- Chat normal Desktop;
- skill en superficie compatible;
- mismo núcleo común en ambas vías;
- plugin aislado autocontenido;
- lectura/escritura GitHub;
- commit multiarchivo atómico;
- detección de conflicto por SHA base;
- Drive solo lectura;
- PDF sin Base64;
- render `left`, `right` y `complete`;
- visión paleográfica;
- conservación del estado editorial;
- 35 unidades;
- Manual, edición, diario, derivados e históricos preservados;
- continuidad entre ordenadores;
- ausencia de Python, WSL y Work como requisitos de uso.

---

# 20. Plan y regla de migración

El plan detallado autoritativo está en:

```text
docs/PLAN_IMPLEMENTACION_GITHUB_WORKSPACE_V2.md
```

La regla general será:

> **No eliminar una garantía hasta que su mecanismo sustituto esté implementado y probado.**

La migración se construirá en una rama, se validará antes de modificar `main`, y el cutover se hará mediante fast-forward sin `force` si `main` conserva el SHA base esperado. Drive no se limpiará hasta completar todas las pruebas.

---

# 21. Regla final

> **GitHub es el workspace canónico.**

> **Drive conserva únicamente el PDF autoritativo.**

> **`PROJECT.md` y `SKILL.md` son dos entradas independientes al mismo núcleo físico en `references/` y `assets/templates/`.**

> **La skill se conserva y el plugin sigue siendo autocontenido.**

> **Las operaciones multiarchivo se publican como un único commit Git atómico condicionado al SHA base de `main`.**

> **Web y Desktop funcionan mediante Chat normal, sin Work ni entorno local del proyecto.**
