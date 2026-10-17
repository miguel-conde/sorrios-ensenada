# PUB-REPO-01 — Preparación controlada para apertura pública

## Estado

- Operación: `R3 — PUB-REPO-01`.
- Base: `73ed35830ca2cc3c36b531da4d8bde47efa73686`.
- Rama: `pub-repo-01/prepare-public-v1`.
- Resultado: `R3: APTO PARA REVISIÓN E INTEGRACIÓN`.
- La visibilidad del repositorio no cambia en esta operación.

## Decisiones humanas aplicadas

R2A autoriza conservar las menciones familiares del prólogo y el correo
histórico del autor en la metadata Git. No se reescribe el historial y no se
usa `git filter-repo`. Sigue siendo condición previa a R5:

`REVISIÓN FAMILIAR DEL PRÓLOGO PENDIENTE`

Las personas nombradas deberán haber podido leer el prólogo; cualquier objeción
se resolverá antes del cambio de visibilidad. Las conformidades no se
versionarán.

R2B fija la siguiente estructura:

| Componente | Régimen |
|---|---|
| Código, scripts, tests, tooling, estilos y configuración ejecutables | MIT (`LICENSE`) |
| Contenido y documentación originales, aportaciones editoriales y gráficos originales | CC BY 4.0 (`LICENSE-CONTENT.md`) |
| Manuscrito, reproducciones, cartografía de origen, citas, enlaces y demás terceros | Régimen propio y exclusiones de `NOTICE` |

No se afirman derechos exclusivos sobre el texto histórico, los hechos o los
metadatos no protegibles.

## Materiales de terceros

`NOTICE` conserva las atribuciones de BDLJE, NGBE e IGR_HIDROGRAFIA v1 2023 y
explica que los mapas son obras derivadas. Los SVG y
`publication/assets/cartography/cartography.json` permanecen sin cambios.

El PDF manuscrito autoritativo no se incorpora. Sus páginas rasterizadas,
facsímiles y recortes continúan como derivados locales no versionados y fuera
de las licencias del repositorio. Citas, bibliografía, obras enlazadas,
materiales externos y dependencias conservan sus respectivos regímenes.

## Entrada pública y comunicación

Se crea un `README.md` raíz orientado a nuevos visitantes. Explica el proyecto,
el libro, la relación Sorríos/Sorribos, el contenido del repositorio, sus
exclusiones, los límites de reproducibilidad, las licencias y el estado
editorial. No usa la jerga interna de paquetes o gates ni declara publicada la
edición 1.0.

Se añaden dos plantillas accesibles bajo `.github/ISSUE_TEMPLATE/`:

- corrección de transcripción o errata;
- problema técnico del repositorio, scripts, generación o navegación.

El correo público continúa como
`EMAIL DE CONTACTO — PLACEHOLDER PENDIENTE`; no se inventa una dirección.

## Packaging y GitHub Actions

El manifiesto del plugin y `plugins/sorrios-ensenada/pyproject.toml` declaran
MIT sin cambiar versión ni dependencias.

El workflow portable conserva sus triggers, matriz y cobertura. Se añaden
`permissions: contents: read` y una concurrencia que cancela ejecuciones
redundantes de la misma referencia. `actions/checkout@v4` y
`actions/setup-python@v5` se conservan: fijarlos a SHA queda como hardening no
bloqueante para R4/R5 porque R3 no acredita esos SHA y no los infiere.

## Referencias y rutas

Las menciones normativas a un repositorio necesariamente privado se reformulan
de modo neutral en `PROJECT.md`, la skill, el Plan Maestro y la arquitectura de
uso. Los dossiers de cierre, migración y validación que describen situaciones
históricas conservan su redacción.

Cuatro enlaces absolutos al workspace en
`docs/Inventario y cuestionario cierre v1_0.md` se convierten en enlaces
relativos. Se conservan como evidencia, sin presentarlas como navegación
pública, la ruta local histórica del manuscrito en el estado editorial, la
preview localhost del dossier de candidata y las cadenas de ejemplo usadas por
tests y validadores.

## Ramas

No se elimina ni publica ninguna rama. Clasificación para la auditoría R4:

| Categoría | Ramas o patrones | Tratamiento antes de R5 |
|---|---|---|
| Conservar | `main`, `feature/quarto-book`; la rama R3 hasta su revisión e integración | Mantener |
| Históricas útiles | `origin/backup/pre-github-workspace-v2`, `origin/migration/github-workspace-v2` | Valorar conservación por trazabilidad |
| Candidatas a borrar | remotas `origin/tmp*`, `origin/codex/*` y ramas auxiliares ya integradas `origin/pkg-*`, `origin/cr-*`, `origin/fix/*` | Revisar y, si se aprueba, limpiar en operación separada antes de R5 |
| Locales/checkpoint | ramas locales `pkg-*`, `canonical/*`, `workflow/*`, `rev-lector-*` y otras ramas de trabajo | No se transfieren a GitHub por el cambio de visibilidad; limpieza local opcional |

## Pendientes antes del cambio de visibilidad

1. Ejecutar R4 sobre HEAD e historial y obtener resultado `APTO`.
2. Completar la revisión familiar del prólogo y resolver objeciones.
3. Decidir en operación separada la limpieza de ramas remotas candidatas.
4. Valorar el pinning acreditado por SHA de las actions.
5. Completar el correo público antes de la publicación definitiva.

R3 no inicia E4, no ejecuta R5 y no hace push, tag, release ni reescritura de
historial.

## Validaciones focales

Resultados:

- parse de TOML, JSON y YAML: PASS;
- construcción focal del wheel del plugin: PASS;
- tests de manifiestos, packaging, skill y preparación pública: `14 passed`;
- tests focales de rutas: `9 passed`;
- enlaces relativos de la entrada pública y enlaces corregidos: PASS;
- escaneo focal de secretos en HEAD y cambios R3: PASS;
- rutas absolutas usadas como enlaces Markdown: 0;
- afirmaciones de repositorio privado en documentación normativa vigente: 0;
- `git diff --check`: PASS;
- árbol `project/`: intacto.

No se ejecutan renders, `prepare.py` ni la suite completa.
