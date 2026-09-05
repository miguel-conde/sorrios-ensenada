# Arquitectura objetivo ChatGPT + GitHub + Google Drive
## Guía de referencia para la evolución de Sorríos — Catastro de Ensenada

**Estado:** propuesta para revisión  
**Fecha:** 5 de septiembre de 2026  
**Versión actual comprobada:** 1.2.3  
**Versión objetivo:** posterior a 1.2.3; número por decidir al implementar  
**Repositorio:** `miguel-conde/sorrios-ensenada`

---

# 1. Objeto

Este documento define:

- la situación actual de la versión 1.2.3;
- la situación deseada;
- los requisitos de la arquitectura objetivo;
- qué componentes de 1.2.3 deben conservarse;
- qué componentes sobran;
- qué componentes deben modificarse;
- qué componentes faltan;
- el plan de migración;
- las instrucciones de instalación y uso desde cualquier ordenador;
- la relación entre Chat normal, la skill `editar-catastro-sorrios`, GitHub y Google Drive.

La finalidad es que el proyecto pueda utilizarse desde:

- ChatGPT Web;
- ChatGPT Desktop;

siempre mediante **Chat normal**, sin depender de Work ni de un entorno local instalado en el ordenador.

---

# 2. Decisión arquitectónica fundamental

La arquitectura objetivo se basa en dos únicas fuentes persistentes:

> **GitHub contiene todo el proyecto excepto el PDF original.**

> **Google Drive contiene únicamente el PDF autoritativo.**

ChatGPT actúa como cliente de ambas.

```text
                         USUARIO
                            │
                            ↓
                       ChatGPT
                    Chat normal
                  Web o Desktop
                            │
               ┌────────────┴────────────┐
               │                         │
               ↓                         ↓
            GitHub                  Google Drive
               │                         │
        TODO EL PROYECTO               PDF
          SALVO EL PDF             AUTORITATIVO
```

No habrá un workspace documental repartido entre GitHub y Drive.

No habrá sincronización GitHub ↔ Drive.

No habrá documentos vivos duplicados.

---

# 3. Papel de cada sistema

## 3.1. GitHub

GitHub será el **workspace canónico completo** del proyecto.

Contendrá:

- instrucciones;
- método;
- controles;
- estado;
- secuencia de unidades;
- Manual Editorial;
- edición crítica;
- diario editorial;
- glosario;
- índices;
- operaciones;
- historial complementario;
- resultados;
- archivos históricos que se decida conservar;
- plantillas;
- skill;
- plugin;
- código auxiliar;
- tests;
- documentación de desarrollo.

GitHub será de lectura y escritura.

---

## 3.2. Google Drive

Google Drive tendrá una única responsabilidad:

```text
Google Drive
└── sorrios_ensenada_orden_lectura_calidad_original.pdf
```

El PDF será de **solo lectura** para el trabajo normal.

Drive no almacenará:

- estado;
- controles;
- edición;
- diario;
- índices;
- glosario;
- resultados;
- operaciones;
- método;
- plantillas.

---

## 3.3. ChatGPT

ChatGPT será el ejecutor remoto.

Podrá trabajar mediante dos vías:

```text
                 NÚCLEO COMÚN
                      │
          ┌───────────┴───────────┐
          │                       │
     Chat normal               Skill
   Web / Desktop        editar-catastro-sorrios
```

Ambas deben terminar utilizando:

- el mismo método;
- el mismo proyecto vivo en GitHub;
- el mismo PDF en Drive.

---

# 4. Fuentes de autoridad

La arquitectura objetivo tendrá las siguientes autoridades:

| Ámbito | Fuente autoritativa |
|---|---|
| Imagen y materialidad | PDF original en Google Drive |
| Método editorial | `Manual_Editorial.md` en GitHub |
| Instrucciones generales | GitHub |
| Identidad/configuración | `proyecto.yaml` en GitHub |
| Estado | `estado.yaml` en GitHub |
| Secuencia de unidades | `unidades.yaml` en GitHub |
| Texto y aparato crítico | GitHub |
| Diario | GitHub |
| Glosario | GitHub |
| Índices | GitHub |
| Operaciones | GitHub |
| Historial técnico | Git |
| Historial semántico adicional | documentos que se decida conservar |
| Resultados | GitHub |
| Plantillas | GitHub |
| Skill | GitHub |
| Código auxiliar | GitHub |

ChatGPT nunca será fuente autoritativa de estado.

La memoria de una conversación tampoco.

---

# 5. Independencia del ordenador

El ordenador debe desaparecer de la arquitectura lógica.

Debe ser posible:

```text
ordenador A
   ↓
ChatGPT Desktop
   ↓
trabajo y cierre

ordenador A apagado

ordenador B
   ↓
ChatGPT Web
   ↓
nuevo Chat
   ↓
GitHub + Drive
   ↓
continuación exacta
```

No debe transferirse ningún archivo entre A y B.

---

# 6. Requisitos de la situación deseada

La arquitectura deberá cumplir todos estos requisitos.

## Acceso

- cualquier ordenador;
- ChatGPT Web;
- ChatGPT Desktop;
- Chat normal;
- misma cuenta o cuenta con permisos equivalentes.

## Persistencia

- todo estado persistente en GitHub;
- PDF en Drive;
- nada indispensable en el ordenador;
- nada indispensable en el runtime temporal de ChatGPT.

## Uso

No requerir:

- Work;
- WSL;
- Python local;
- Git local;
- VS Code;
- Codex CLI;
- checkout;
- Google Drive Desktop;
- Poppler local;
- entorno virtual;
- instalación local del proyecto.

## Compatibilidad

La skill debe seguir existiendo para los entornos que la soporten.

Pero el proyecto también debe funcionar cuando la skill **no esté disponible**.

---

# 7. Situación actual comprobada: 1.2.3

La versión actual del plugin declarada en `main` es:

```text
1.2.3
```

La estructura actual relevante es:

```text
/
├── .agents/
├── .github/
├── DEVELOPMENT.md
├── pytest.ini
├── tests/
└── plugins/
    └── sorrios-ensenada/
        ├── .codex-plugin/
        │   └── plugin.json
        ├── pyproject.toml
        └── skills/
            └── editar-catastro-sorrios/
                ├── SKILL.md
                ├── agents/
                ├── assets/
                │   └── templates/
                ├── references/
                └── scripts/
```

La skill actual es una pieza real y debe conservarse.

---

# 8. Contenido actual de la skill

Actualmente:

```text
plugins/sorrios-ensenada/
└── skills/
    └── editar-catastro-sorrios/
        ├── SKILL.md
        ├── agents/
        ├── assets/
        │   └── templates/
        ├── references/
        │   ├── document-schemas.md
        │   ├── drive-materialization.md
        │   ├── editorial-procedure.md
        │   ├── local-execution.md
        │   ├── task-modes.md
        │   └── workspace-contract.md
        └── scripts/
            ├── materialize_drive_payload.py
            ├── materialize_drive_text.py
            ├── path_utils.py
            ├── render_unit.py
            ├── validate_operation.py
            └── validate_workspace.py
```

La 1.2.3 mezcla tres tipos de contenido:

```text
A. método común del proyecto
B. interfaz específica de skill/plugin
C. infraestructura de ejecución local
```

La migración debe separar claramente las tres cosas.

---

# 9. Situación actual de Google Drive

En la versión 1.2.3, Drive sigue siendo el workspace vivo.

Contiene:

```text
00_CONTROL/
10_FUENTE_PRIMARIA/
20_TRABAJO_EDITORIAL/
30_RESULTADOS/
90_ARCHIVO/
```

y otras carpetas heredadas.

En `00_CONTROL` existen actualmente, entre otros:

```text
proyecto.yaml
estado.yaml
unidades.yaml
Manual_Editorial.md
INSTRUCCIONES_PROYECTO.md
CAMBIOS.md
OPERACIONES/
```

En `20_TRABAJO_EDITORIAL`:

```text
Edicion_Critica.md
Diario_Editorial.md
Glosario.md
INDICES/
```

La situación actual no coincide todavía con la arquitectura objetivo.

---

# 10. Qué problema resolvía la 1.2.3

La arquitectura actual fue diseñada bajo esta hipótesis:

```text
Drive
  ↓
workspace completo
  ↓
materialización local
  ↓
Python / filesystem
  ↓
render / validación
```

Por ello incorpora:

- Base64;
- materialización;
- Python;
- TTY;
- WSL;
- Windows;
- Pillow;
- Poppler;
- validación del filesystem;
- render local.

Era una solución coherente con las restricciones conocidas entonces.

---

# 11. Qué ha cambiado

Las pruebas realizadas posteriormente demuestran que desde Chat normal se puede:

## GitHub

- leer el repositorio privado;
- leer archivos;
- obtener SHA;
- crear;
- modificar;
- borrar;
- verificar;
- detectar concurrencia;
- comparar commits;
- restaurar el estado.

## Drive

- localizar el PDF;
- descargarlo completo;
- solicitarlo sin Base64;
- obtener una referencia interna de archivo;
- utilizarla como PDF real.

## PDF

- renderizar página;
- seleccionar la región de una unidad;
- inspeccionar visualmente el manuscrito;
- efectuar lectura paleográfica.

Por tanto, gran parte de la infraestructura local de 1.2.3 deja de ser necesaria para el uso normal.

---

# 12. Compatibilidad comprobada

| Capacidad | Web | Desktop |
|---|---:|---:|
| GitHub privado | Sí | Sí |
| Escritura GitHub | Sí | Sí |
| SHA | Sí | Sí |
| Drive | Sí | Sí |
| PDF sin Base64 | Sí | Sí |
| PDF como archivo real | Sí | Sí |
| Render | Sí | Sí |
| Recorte | Sí | Sí |
| Visión paleográfica | Sí | Sí |
| Work necesario | No | No |

---

# 13. Situación de la skill en Chat normal

La skill:

```text
editar-catastro-sorrios
```

no ha resultado invocable desde el Chat normal probado.

No sabemos si:

- no está instalada;
- está instalada pero no accesible;
- pertenece a otra superficie.

Por tanto:

> La arquitectura no puede exigir la skill para funcionar desde Chat normal.

Esto **no significa eliminar la skill**.

Significa desacoplarla del núcleo del proyecto.

---

# 14. Arquitectura objetivo del repositorio

La estructura propuesta debe mostrar expresamente el proyecto vivo, el método común y la skill.

```text
/
├── PROJECT.md
│
├── project/
│   ├── 00_CONTROL/
│   │   ├── proyecto.yaml
│   │   ├── estado.yaml
│   │   ├── unidades.yaml
│   │   ├── Manual_Editorial.md
│   │   ├── CAMBIOS.md
│   │   └── OPERACIONES/
│   │
│   ├── 20_TRABAJO_EDITORIAL/
│   │   ├── Edicion_Critica.md
│   │   ├── Diario_Editorial.md
│   │   ├── Glosario.md
│   │   └── INDICES/
│   │
│   ├── 30_RESULTADOS/
│   │   ├── EDICION_PALEOGRAFICA/
│   │   └── ESTUDIO_HISTORICO/
│   │
│   └── 90_ARCHIVO/
│
├── method/
│   ├── task-modes.md
│   ├── workspace-contract.md
│   ├── editorial-procedure.md
│   ├── document-schemas.md
│   ├── github-operations.md
│   └── pdf-access.md
│
├── templates/
│   ├── ...
│   └── ...
│
├── plugins/
│   └── sorrios-ensenada/
│       ├── .codex-plugin/
│       │   └── plugin.json
│       ├── pyproject.toml
│       └── skills/
│           └── editar-catastro-sorrios/
│               ├── SKILL.md
│               ├── agents/
│               ├── references/
│               ├── assets/
│               └── scripts/
│
├── tests/
├── pytest.ini
└── DEVELOPMENT.md
```

Esta estructura es propuesta. La ubicación exacta debe aprobarse antes de modificar el repositorio.

---

# 15. Tres capas claramente separadas

La estructura objetivo debe tener tres capas.

## Capa 1 — Proyecto vivo

```text
project/
```

Contiene el estado real del trabajo.

No son plantillas.

No son ejemplos.

No son copias.

---

## Capa 2 — Método común

```text
PROJECT.md
method/
templates/
```

Describe cómo trabajar.

Es independiente del cliente.

---

## Capa 3 — Adaptadores

```text
plugins/sorrios-ensenada/
```

Contiene interfaces específicas para entornos que soportan plugins y skills.

La skill vive aquí.

---

# 16. Relación entre Chat normal y skill

La arquitectura correcta es:

```text
                    MÉTODO COMÚN
                 PROJECT.md + method/
                         │
             ┌───────────┴───────────┐
             │                       │
        Chat normal              SKILL.md
      Web / Desktop          editar-catastro-sorrios
             │                       │
             └───────────┬───────────┘
                         │
                         ↓
                      project/
                         │
                         +
                  PDF en Drive
```

No debe haber dos métodos distintos.

---

# 17. Punto de entrada para Chat normal

`PROJECT.md` será el bootstrap universal.

Un Chat normal hará:

```text
PROJECT.md
    ↓
método común
    ↓
project/
    ↓
Drive si necesita PDF
```

Debe ser pequeño y estable.

---

# 18. Punto de entrada para skill

La skill seguirá existiendo en:

```text
plugins/sorrios-ensenada/
└── skills/
    └── editar-catastro-sorrios/
        └── SKILL.md
```

Su flujo será:

```text
SKILL.md
   ↓
PROJECT.md
   ↓
method/
   ↓
project/
   ↓
Drive
```

---

# 19. Nuevo papel de `SKILL.md`

Actualmente `SKILL.md` contiene una parte significativa de las reglas del proyecto.

Debe refactorizarse.

Su función futura será:

- identificar cuándo utilizar la skill;
- identificar Sorríos como proyecto;
- señalar el repositorio;
- cargar el bootstrap común;
- añadir únicamente las particularidades específicas del entorno de skill;
- remitir al núcleo común.

No debe contener una copia independiente del método completo.

---

# 20. Principio de una sola fuente del método

Debe evitarse:

```text
PROJECT.md
  └── método A

SKILL.md
  └── método B
```

porque terminarían divergiendo.

Debe existir:

```text
           method/
              │
       ┌──────┴──────┐
       │             │
 PROJECT.md       SKILL.md
```

---

# 21. Cinco modos de tarea

Se conservan íntegramente:

1. Consulta puntual.
2. Edición de unidad.
3. Auditoría.
4. Cambio metodológico.
5. Estudio histórico.

Los modos pertenecen al método común, no a la skill.

Por ello deben ubicarse fuera de ella:

```text
method/task-modes.md
```

La skill simplemente los utilizará.

---

# 22. Procedimiento editorial

También debe convertirse en parte del núcleo común.

La secuencia sigue siendo:

1. confirmar unidad;
2. leer la unidad completa;
3. transcribir línea a línea;
4. revisar contra el PDF;
5. aplicar el Manual;
6. completar observaciones, notas y referencias;
7. preparar glosario e índices;
8. registrar dudas;
9. control de calidad;
10. validar;
11. incorporar derivados;
12. actualizar Diario;
13. verificar;
14. actualizar `estado.yaml` al final;
15. cerrar la operación.

No es lógica específica de la skill.

---

# 23. Workspace canónico

El contrato debe cambiar de:

```text
Drive = workspace
```

a:

```text
GitHub = workspace
```

La estructura viva residirá en:

```text
project/
```

---

# 24. PDF

El PDF seguirá exclusivamente en Drive.

Flujo:

```text
unidades.yaml
      ↓
unit_id
      ↓
pdf_page + position
      ↓
Drive
      ↓
PDF
      ↓
runtime ChatGPT
      ↓
render
      ↓
unidad
      ↓
visión
```

No debe ser necesario descargarlo al ordenador del usuario.

---

# 25. Base64

El procedimiento Base64 actual se vuelve innecesario para el flujo normal.

Debe clasificarse:

**OBSOLETO PARA USO NORMAL.**

Solo podrá conservarse temporalmente como legado mientras se valida la nueva arquitectura.

---

# 26. `drive-materialization.md`

Debe dejar de existir como procedimiento operativo general.

Debe ser reemplazado por:

```text
method/pdf-access.md
```

que describa:

- identificación del PDF;
- acceso vía Drive;
- descarga sin Base64;
- uso de `file_uri` o equivalente;
- render;
- selección de unidad;
- tratamiento efímero del archivo.

---

# 27. `materialize_drive_payload.py`

Debe retirarse del flujo normal.

Su destino final será probablemente:

**ELIMINAR**, después de pruebas.

---

# 28. `materialize_drive_text.py`

Al migrar todos los textos vivos a GitHub pierde prácticamente toda su razón de existir.

Destino probable:

**ELIMINAR**, después de pruebas.

---

# 29. `render_unit.py`

Debe conservarse su función conceptual:

```text
unidad → página + posición → imagen
```

No es obligatorio conservar su ejecución local.

Puede quedar como:

- herramienta de desarrollo;
- implementación de referencia;
- validador independiente;
- prueba.

Su eliminación solo debe decidirse después de validar el render directo en ChatGPT para todos los tipos de unidad.

---

# 30. `validate_workspace.py`

Debe separarse:

```text
validación lógica
```

de:

```text
validación de filesystem local
```

La primera se conserva.

La segunda probablemente desaparece.

---

# 31. `validate_operation.py`

La función de comprobar operaciones sigue siendo necesaria.

Pero debe adaptarse al nuevo modelo basado en GitHub y SHA.

---

# 32. `path_utils.py`

Debe revisarse según los scripts finales.

No debe eliminarse ni conservarse por defecto.

---

# 33. `pyproject.toml`

Actualmente forma parte correctamente del plugin 1.2.3.

No debe eliminarse automáticamente.

La nueva arquitectura distingue:

```text
USO
```

de:

```text
DESARROLLO
```

Python puede dejar de ser requisito de uso y seguir siendo útil para:

- tests;
- scripts;
- desarrollo del plugin;
- validaciones independientes.

Al final de la migración se revisará qué dependencias siguen justificadas.

---

# 34. `local-execution.md`

Deja de formar parte del flujo normal de usuario.

Si sigue siendo útil, deberá quedar explícitamente bajo la categoría:

```text
desarrollo
```

No deberá ser referenciado por `PROJECT.md` para el uso normal.

---

# 35. Plantillas

Las plantillas se conservan.

Pero se recomienda moverlas fuera de la skill si son comunes a todos los clientes.

Por ejemplo:

```text
templates/
├── estado.yaml
├── proyecto.yaml
├── unidades.yaml
├── Edicion_Critica.md
├── Diario_Editorial.md
├── Glosario.md
└── ...
```

La skill podrá usarlas, pero no será su propietaria exclusiva.

---

# 36. `agents/` de la skill

Debe mantenerse mientras forme parte de la interfaz del plugin.

Debe revisarse para comprobar que:

- no contiene método duplicado;
- no referencia la antigua arquitectura Drive;
- remite al núcleo común cuando corresponda.

---

# 37. `references/` de la skill

Debe reducirse.

Las referencias comunes deben migrar a:

```text
method/
```

En `references/` deben quedar únicamente documentos específicos de la skill, si realmente existen.

El resultado deseado podría llegar a ser:

```text
skills/editar-catastro-sorrios/
├── SKILL.md
├── agents/
├── references/
│   └── <solo contenido específico>
├── assets/
│   └── <solo contenido específico>
└── scripts/
    └── <solo contenido específico>
```

---

# 38. Qué se conserva de 1.2.3

Se conserva:

- repositorio GitHub;
- plugin;
- skill;
- `SKILL.md`;
- los cinco modos;
- método editorial;
- Manual;
- controles;
- estado;
- unidades;
- edición;
- diario;
- glosario;
- índices;
- resultados;
- operaciones;
- reglas de seguridad;
- verificación;
- actualización de estado en último lugar;
- plantillas;
- tests útiles;
- código que siga aportando valor.

---

# 39. Qué cambia de papel

| Componente | Nuevo papel |
|---|---|
| GitHub | workspace canónico completo |
| Drive | solo PDF |
| Skill | adaptador opcional |
| `SKILL.md` | bootstrap específico de skill |
| `PROJECT.md` | bootstrap universal |
| `method/` | núcleo común |
| `templates/` | plantillas compartidas |
| Python | solo si desarrollo/tests lo necesitan |
| scripts | utilidades, no infraestructura obligatoria |

---

# 40. Qué sobra como requisito de uso

Dejan de ser requisitos:

- Drive como workspace;
- Base64;
- materialización local;
- Python;
- venv;
- Poppler;
- Pillow;
- WSL;
- Git local;
- checkout;
- VS Code;
- Codex CLI;
- instalación del plugin;
- skill disponible en Chat normal;
- Work.

---

# 41. Qué falta

Debe añadirse:

## 41.1. Proyecto vivo en GitHub

Migración de los documentos canónicos.

## 41.2. `PROJECT.md`

Bootstrap universal.

## 41.3. `method/`

Extracción del método que ahora está dentro de la skill.

## 41.4. `github-operations.md`

Protocolo de lectura/escritura segura.

## 41.5. `pdf-access.md`

Protocolo de Drive exclusivo para el PDF.

## 41.6. Tests Web/Desktop

Formalización de las pruebas ya realizadas.

---

# 42. Escritura en GitHub

El flujo normal de modificación será:

```text
leer archivo
   ↓
obtener SHA
   ↓
preparar nueva versión
   ↓
escribir usando SHA anterior
   ↓
verificar
```

Si otro proceso ha cambiado el archivo:

```text
SHA esperado ≠ SHA actual
          ↓
         STOP
```

No se sobrescribe silenciosamente.

---

# 43. Operaciones de varios archivos

Una unidad puede requerir cambios en varios documentos.

Debe mantenerse un protocolo lógico:

```text
1. leer todos los archivos afectados y sus SHA
2. preparar todos los cambios
3. validar
4. registrar operación prepared
5. volver a comprobar precondiciones
6. escribir edición
7. escribir derivados
8. escribir Diario
9. verificar todo
10. escribir estado.yaml al final
11. cerrar operación verified
```

---

# 44. Concurrencia

Al quedar Drive en solo lectura, toda concurrencia editable se concentra en GitHub.

Esto simplifica el problema.

Ejemplo:

```text
Chat Web ──────┐
               ├── GitHub
Chat Desktop ──┘
```

Los SHA permiten detectar conflictos.

---

# 45. Estado

`estado.yaml` se conservará como fuente explícita del estado del proyecto.

Una sesión nueva debe poder leer:

```text
fase
current_unit
operation.status
```

y cualquier otro campo necesario.

No debe necesitar conocer ninguna conversación previa.

---

# 46. `unidades.yaml`

Debe mantenerse como la correspondencia autoritativa entre:

```text
unit_id
pdf_page
position
previous
next
```

Las páginas nunca deben codificarse en prompts.

---

# 47. Manual Editorial

Debe migrarse a GitHub sin cambiar inicialmente su contenido.

Será versionado mediante Git.

Los cambios metodológicos podrán quedar reflejados tanto en:

- el propio Manual;
- los commits;
- el registro semántico que se decida mantener.

---

# 48. Documentos vivos que deben migrarse desde Drive

Al menos:

```text
proyecto.yaml
estado.yaml
unidades.yaml
Manual_Editorial.md
INSTRUCCIONES_PROYECTO.md
CAMBIOS.md
OPERACIONES/
Edicion_Critica.md
Diario_Editorial.md
Glosario.md
INDICES/
30_RESULTADOS/
```

También deben auditarse:

```text
90_ARCHIVO/
FUENTES ACTIVAS/
FUERA DEL CONTEXTO ACTIVO/
```

antes de decidir su destino.

---

# 49. Situación final de Drive

Al finalizar:

```text
Sorrios - Catastro Ensenada/
└── sorrios_ensenada_orden_lectura_calidad_original.pdf
```

Si se mantiene temporalmente un archivo histórico de la antigua estructura, debe quedar claramente identificado como:

```text
NO CANÓNICO
NO USAR EN TRABAJO NORMAL
```

---

# 50. Plan de migración

## Fase 1 — Inventario

Inventariar completamente GitHub y Drive.

Clasificar:

```text
MIGRAR
CONSERVAR
ADAPTAR
ARCHIVAR
ELIMINAR
```

---

## Fase 2 — Congelar estado

Antes de modificar:

- confirmar operación limpia;
- registrar estado;
- registrar SHA de `main`;
- suspender temporalmente edición editorial.

---

## Fase 3 — Diseñar estructura definitiva

Aprobar las rutas exactas de:

```text
project/
method/
templates/
plugins/
tests/
```

---

## Fase 4 — Crear núcleo común

Crear:

```text
PROJECT.md
method/
```

extrayendo, sin alterar su significado, el método actualmente residente en la skill.

---

## Fase 5 — Refactorizar skill

Mantener:

```text
plugins/sorrios-ensenada/
└── skills/
    └── editar-catastro-sorrios/
```

pero hacer que:

```text
SKILL.md
   ↓
PROJECT.md
   ↓
method/
```

---

## Fase 6 — Migrar proyecto vivo

Copiar los documentos canónicos desde Drive a `project/`.

Durante esta fase Drive sigue siendo autoridad.

---

## Fase 7 — Verificar migración

Comparar contenidos.

No cambiar todavía la autoridad hasta comprobar:

- existencia;
- contenido;
- estructura;
- codificación;
- referencias.

---

## Fase 8 — Cambiar autoridad

Actualizar instrucciones para establecer:

```text
GitHub = workspace
Drive = PDF
```

---

## Fase 9 — Sustituir materialización

Crear:

```text
method/pdf-access.md
```

y retirar del flujo:

```text
drive-materialization.md
materialize_drive_payload.py
materialize_drive_text.py
```

---

## Fase 10 — Adaptar validaciones

Rediseñar:

```text
validate_workspace.py
validate_operation.py
```

o sustituirlos por mecanismos nuevos.

---

## Fase 11 — Revisar scripts

Clasificar uno por uno:

```text
render_unit.py
path_utils.py
...
```

---

## Fase 12 — Adaptar tests

Los tests deberán reflejar la nueva arquitectura y conservar las garantías útiles.

---

## Fase 13 — Prueba Chat normal Web

Comprobar:

```text
PROJECT.md
→ estado
→ método
→ proyecto
→ PDF
→ visión
```

---

## Fase 14 — Prueba Chat normal Desktop

La misma prueba.

---

## Fase 15 — Prueba de la skill

Desde un entorno que soporte la skill:

```text
editar-catastro-sorrios
→ SKILL.md
→ PROJECT.md
→ método común
→ project/
→ PDF
```

Debe obtener el mismo comportamiento.

---

## Fase 16 — Escritura reversible GitHub

Repetir las garantías ya demostradas:

- SHA inicial;
- modificación;
- verificación;
- concurrencia;
- restauración cuando proceda.

---

## Fase 17 — Ciclo editorial completo

Ejecutar:

```text
estado
→ unidad
→ PDF
→ lectura
→ propuesta
→ aprobación
→ edición
→ derivados
→ diario
→ estado
→ verified
```

---

## Fase 18 — Cambio de ordenador

Probar:

```text
Desktop A
→ cierre
→ Web B
→ nuevo Chat
→ continuación
```

y el camino inverso.

---

## Fase 19 — Limpiar Drive

Solo después de superar las pruebas:

- mantener PDF;
- archivar o retirar el resto.

---

## Fase 20 — Retirar legado

Solo entonces decidir definitivamente:

- Base64;
- scripts de materialización;
- `local-execution.md`;
- dependencias;
- utilidades sobrantes.

---

# 51. Uso desde ChatGPT Web

## Configuración inicial

La cuenta debe disponer de:

- acceso a GitHub;
- acceso al repositorio privado;
- acceso a Google Drive;
- acceso al PDF.

## Uso diario

Abrir un Chat normal.

No usar Work.

Prompt objetivo:

```text
Trabaja con el proyecto Sorríos del repositorio
miguel-conde/sorrios-ensenada.

Carga PROJECT.md y sigue sus instrucciones.

Modo: <modo>.
Tarea: <tarea>.
```

---

# 52. Uso desde ChatGPT Desktop

La operativa debe ser idéntica.

Instalar únicamente ChatGPT Desktop si se desea utilizar ese cliente.

Después:

```text
Chat normal
→ GitHub
→ PROJECT.md
→ proyecto
→ Drive si se necesita PDF
```

No debe haber instrucciones distintas para Desktop.

---

# 53. Uso mediante skill

En entornos compatibles podrá utilizarse:

```text
$editar-catastro-sorrios
```

o el identificador equivalente que corresponda.

La skill deberá cargar el mismo método común.

Ejemplo conceptual:

```text
Usa $editar-catastro-sorrios en modo edición de unidad.
Trabaja únicamente la unidad actual.
Presenta la propuesta para revisión antes de escribir.
```

La disponibilidad de esta vía es adicional.

No sustituye al acceso mediante Chat normal.

---

# 54. Qué no instalar para uso normal

No se requerirá:

```text
Git
GitHub CLI
Python
PyYAML
Pillow
Poppler
WSL
VS Code
Codex CLI
plugin
skill local
Google Drive Desktop
```

Para Desktop solo será necesaria la propia aplicación ChatGPT Desktop.

---

# 55. Desarrollo del proyecto

El desarrollo de la arquitectura es otra actividad.

Puede seguir utilizando:

- Git;
- Python;
- pytest;
- VS Code;
- WSL;
- Poppler;
- Codex;
- plugin local.

Estas herramientas pertenecen a:

```text
DEVELOPMENT.md
```

No a las instrucciones de uso editorial.

---

# 56. Clasificación de componentes 1.2.3

| Componente | Destino |
|---|---|
| GitHub privado | CONSERVAR / workspace canónico |
| Drive | CONSERVAR solo para PDF |
| PDF | CONSERVAR |
| documentos vivos de Drive | MIGRAR |
| plugin `sorrios-ensenada` | CONSERVAR |
| skill `editar-catastro-sorrios` | CONSERVAR Y REFACTORIZAR |
| `SKILL.md` | CONSERVAR / convertir en adaptador |
| `agents/` | CONSERVAR Y REVISAR |
| `references/` de skill | REDUCIR |
| `assets/` de skill | REVISAR |
| `scripts/` de skill | REVISAR |
| `PROJECT.md` | CREAR |
| `method/` | CREAR |
| `project/` | CREAR |
| `templates/` comunes | EXTRAER/CREAR |
| cinco modos | CONSERVAR |
| procedimiento editorial | CONSERVAR |
| Manual | MIGRAR |
| estado | MIGRAR |
| unidades | MIGRAR |
| edición | MIGRAR |
| diario | MIGRAR |
| glosario | MIGRAR |
| índices | MIGRAR |
| resultados | MIGRAR |
| operaciones | MIGRAR |
| Base64 | RETIRAR |
| materializadores | RETIRAR |
| `drive-materialization.md` | SUSTITUIR |
| `local-execution.md` | SOLO DESARROLLO O RETIRAR |
| `render_unit.py` | REVISAR |
| `validate_workspace.py` | REDISEÑAR |
| `validate_operation.py` | REDISEÑAR |
| `path_utils.py` | REVISAR |
| `pyproject.toml` | CONSERVAR mientras sea necesario |
| tests | ADAPTAR |
| Work | NO REQUERIDO |

---

# 57. Pruebas de aceptación

| Requisito | Web Chat | Desktop Chat | Skill |
|---|---:|---:|---:|
| Cargar núcleo común | Sí | Sí | Sí |
| Leer estado GitHub | Sí | Sí | Sí |
| Leer Manual | Sí | Sí | Sí |
| Determinar unidad | Sí | Sí | Sí |
| Obtener PDF | Sí | Sí | Sí |
| Sin Base64 | Sí | Sí | Sí |
| Render | Sí | Sí | Sí |
| Visión paleográfica | Sí | Sí | Sí |
| Escritura GitHub | Sí | Sí | Sí |
| Control SHA | Sí | Sí | Sí |
| Verificación | Sí | Sí | Sí |
| Detección de conflicto | Sí | Sí | Sí |
| Ciclo editorial completo | Sí | Sí | Sí |
| Método idéntico | Sí | Sí | Sí |
| Work | No | No | No necesario |
| Entorno local | No | No | solo si el entorno de skill lo exige |

La columna Skill deberá probarse en una superficie que realmente soporte su invocación.

---

# 58. Principio de no duplicación

La arquitectura deberá cumplir:

> Un concepto debe tener una única fuente de verdad.

Ejemplos:

```text
estado → project/00_CONTROL/estado.yaml
unidades → project/00_CONTROL/unidades.yaml
método → method/
Manual → project/00_CONTROL/Manual_Editorial.md
skill → adaptador
PDF → Drive
```

La skill no tendrá copias divergentes del método.

---

# 59. Principio de migración segura

Ninguna garantía debe desaparecer sin reemplazo.

```text
garantía
   ↓
mecanismo 1.2.3
   ↓
nuevo mecanismo
   ↓
prueba
   ↓
retirada del antiguo
```

Por ejemplo:

```text
concurrencia
→ validación anterior
→ SHA GitHub
→ prueba
→ retirada
```

---

# 60. Criterio de finalización

La migración estará terminada cuando:

> El repositorio GitHub contenga el proyecto vivo, el método común, el plugin, la skill, las plantillas, los resultados y las herramientas. Google Drive contenga únicamente el PDF autoritativo. ChatGPT Web y Desktop puedan operar mediante Chat normal cargando `PROJECT.md`. Los entornos compatibles con skills puedan utilizar `editar-catastro-sorrios`, que actuará como adaptador sobre ese mismo núcleo común. Ninguna de estas vías dependerá de una copia local del proyecto.

---

# 61. Arquitectura final resumida

```text
                         USUARIO
                            │
          ┌─────────────────┼─────────────────┐
          │                                   │
          ↓                                   ↓
   Chat normal                           Entorno skill
 Web / Desktop                                 │
          │                                    ↓
          ↓                         editar-catastro-sorrios
      PROJECT.md                               │
          │                                    │
          └───────────────┬────────────────────┘
                          ↓
                       method/
                          │
                          ↓
                       project/
                          │
                   GitHub canónico
                          │
                          ├──────────────┐
                          │              │
                          ↓              ↓
                  documentos vivos   historial Git
                          │
                          │
                          └───────┐
                                  │
                                  ↓
                         Google Drive
                                  │
                                  ↓
                           PDF autoritativo
```

---

# 62. Regla final de arquitectura

La arquitectura objetivo puede resumirse así:

> **GitHub es el workspace canónico.**

> **Google Drive conserva únicamente el PDF autoritativo.**

> **`PROJECT.md` es la entrada universal para Chat normal.**

> **`editar-catastro-sorrios` se conserva como skill y se convierte en un adaptador opcional del mismo núcleo común.**

> **`method/` contiene el método compartido por Chat normal y la skill.**

> **El ordenador no contiene estado ni dependencias obligatorias del proyecto.**

> **Web y Desktop deben comportarse igual.**

> **Work no forma parte de la arquitectura requerida.**

---

# 63. Siguiente paso

Una vez aprobado este documento, el siguiente entregable debe ser un **plan de implementación archivo por archivo sobre la versión 1.2.3**.

Ese plan deberá especificar, sin realizar todavía cambios:

- estructura final exacta;
- origen y destino de cada archivo;
- qué contenido se extrae de `SKILL.md`;
- qué referencias pasan de la skill a `method/`;
- cómo queda el nuevo `SKILL.md`;
- contenido de `PROJECT.md`;
- documentos que migran de Drive;
- código que se conserva;
- código que se elimina;
- tests que cambian;
- nuevos tests;
- secuencia de commits;
- momento de cambio de autoridad de Drive a GitHub;
- limpieza final de Drive;
- pruebas Web;
- pruebas Desktop;
- prueba específica de la skill;
- criterios de aceptación y rollback.
