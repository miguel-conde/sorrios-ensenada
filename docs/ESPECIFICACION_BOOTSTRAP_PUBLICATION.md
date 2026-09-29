# Especificación de bootstrap de `publication/`

**Estado:** lista para ejecutar  
**Fase:** 2A  
**Dependencia:** fases 0, 1 y 1B completadas  
**Alcance:** infraestructura mínima; sin migración de contenido histórico

`publication/` no existe todavía. Este documento sustituye provisionalmente a su futuro `README.md` y define su creación en la siguiente tarea. Cuando el bootstrap se complete, `publication/README.md` será la guía operativa diaria y este documento quedará como especificación histórica de aceptación.

## 1. Resultado buscado

Crear un Quarto Book mínimo, independiente dentro del repositorio, que:

- lea instrucciones y metadatos sin modificar `project/`;
- renderice HTML;
- intente renderizar PDF y deje diagnóstico exacto del entorno;
- demuestre la separación `content/`/`generated/`;
- congele el snapshot de fuentes auditado;
- no copie todavía contenido histórico ni el manuscrito.

Rama de trabajo recomendada: `feature/quarto-book`.

## 2. Rutas autorizadas en la tarea

- crear archivos bajo `publication/**`;
- actualizar `.gitignore` solo para salidas y derivados de `publication/`.

No modificar `project/`, `plugins/`, `tests/`, `docs/`, `PROJECT.md` ni las instrucciones de Copilot durante este bootstrap, salvo una corrección imprescindible y previamente explicada.

## 3. Archivos mínimos

```text
publication/
├── _quarto.yml
├── index.qmd
├── README.md
├── references.bib
├── content/
│   └── 00-preliminares/
│       └── 00-prueba-tecnica.qmd
├── meta/
│   ├── publication.yml
│   ├── chapters.yml
│   ├── indexes.yml
│   └── assets.yml
├── scripts/
│   └── prepare.py
└── styles/
    └── book.scss
```

`prepare.py` creará `generated/` si no existe. `_book/` y el contenido de `generated/` se ignorarán en Git. Los demás directorios de la arquitectura se crearán cuando contengan su primer recurso real; no hace falta llenar Git con marcadores vacíos.

## 4. Configuración mínima

`_quarto.yml` debe declarar:

- `project.type: book`;
- `project.output-dir: _book`;
- `project.pre-render: scripts/prepare.py`;
- `index.qmd` y el capítulo técnico en orden explícito;
- título provisional aprobado;
- búsqueda HTML;
- descarga PDF desde HTML, sin enlazar un PDF inexistente tras un render fallido;
- formatos HTML y PDF;
- HTML con `styles/book.scss`;
- PDF con `lualatex`, sujeto a `quarto check`.

No añadir todavía filtros, JavaScript propio, despliegue, analítica ni personalización LaTeX avanzada.

## 5. Manifiesto de publicación

`meta/publication.yml` debe registrar, sin duplicar otros datos innecesarios:

```yaml
publication:
  version: "0.1.0-dev"
  status: development

base:
  git_commit: "6b49be848c92c4772b37c46495135352821d50f8"

sources:
  critical_edition:
    path: project/20_TRABAJO_EDITORIAL/Edicion_Critica.md
    version: "3.6"
  historical_study:
    path: project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md
    version: "1.2"
  evidence_register:
    path: project/30_RESULTADOS/ESTUDIO_HISTORICO/Registro_Afirmaciones_Calculos_v1.md
    version: "1.2"
  modernized_edition:
    path: project/30_RESULTADOS/EDICION_DIVULGATIVA/Catastro_Sorrios_1752_Version_Modernizada.md
    version: "1.3"

manuscript:
  metadata_source: project/00_CONTROL/proyecto.yaml
  file_id: "1GgBs68iTi53ue8-TbrYFABALxadhQe5u"
  sha256: "d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24"
  pages: 18
```

El commit fija el snapshot documental, no el futuro HEAD de la rama de infraestructura. `prepare.py` debe comparar rutas y versiones con las fuentes, no asumir que todo `main` seguirá apuntando al mismo SHA.

`chapters.yml` declara solo la portada y el capítulo de prueba. `indexes.yml` y `assets.yml` deben contener schema/propósito y listas vacías válidas, no entradas ficticias.

## 6. Contenido de prueba

`index.qmd` y `00-prueba-tecnica.qmd` contienen únicamente texto técnico inequívoco: estado de desarrollo, objetivo de la prueba y enlaces entre páginas. No copian pasajes del Estudio, la Edición Crítica, la modernizada ni el PDF 0.6.

El capítulo de prueba debe demostrar:

- jerarquía de encabezados;
- una referencia cruzada o enlace interno;
- una nota breve;
- una tabla pequeña no histórica;
- equivalencia básica entre HTML y PDF.

No usar datos de ejemplo que puedan confundirse con afirmaciones históricas reales.

## 7. `prepare.py`

En esta fase hace solo lo imprescindible:

1. resuelve la raíz del repositorio de forma portable;
2. comprueba que existe `project/00_CONTROL/proyecto.yaml`;
3. comprueba las cuatro rutas declaradas en `publication.yml`;
4. crea `publication/generated/` si falta;
5. termina con código distinto de cero y mensaje accionable si una precondición falla.

No descarga Drive, no analiza el manuscrito, no genera capítulos reales, no instala dependencias y no escribe fuera de `publication/generated/`.

## 8. README operativo futuro

`publication/README.md` debe explicar:

- función de `publication/` y sus límites de autoridad;
- qué se edita y qué se genera;
- requisitos: Quarto, Python compatible y una distribución LaTeX para PDF;
- comandos desde la raíz:

```text
quarto check
quarto preview publication
quarto render publication --to html
quarto render publication --to pdf
```

- salida en `publication/_book/`;
- solución de problemas de Quarto/LaTeX sin tocar fuentes canónicas;
- enlace al plan maestro y al roadmap;
- prohibición de confirmar `generated/`, `_book/` y cualquier PDF fuente.

## 9. Validación de la tarea

Antes de cerrar:

1. guardar el SHA base de la rama y verificar que no cambió antes de publicar;
2. revisar la lista exacta de archivos;
3. ejecutar los tests existentes del repositorio;
4. ejecutar `quarto check`;
5. ejecutar el render HTML y abrir la salida;
6. ejecutar el render PDF si LaTeX está disponible; si no, registrar componente ausente y salida exacta;
7. comprobar que `git diff -- project plugins tests docs PROJECT.md` está vacío;
8. comprobar que ningún PDF o `_book/` queda versionado;
9. comprobar que una segunda ejecución de `prepare.py` produce el mismo estado;
10. publicar todos los cambios como un único commit atómico.

## 10. Criterios de aceptación

- árbol mínimo creado y documentado;
- separación `content/`/`generated/` evidente;
- manifiesto con las versiones verificadas;
- `prepare.py` portable, idempotente y sin escrituras canónicas;
- HTML en PASS;
- estado del PDF conocido y documentado tras una prueba real;
- `project/` intacto;
- sin contenido histórico migrado;
- sin PDF fuente, PDF 0.6 ni derivados facsimilares;
- diff pequeño y un único commit.

Solo entonces `docs/ESTADO_PUBLICACION_QUARTO.md` podrá marcar la Fase 2A como completada y señalar la Fase 2B.

