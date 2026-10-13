# Decisiones editoriales 6A.2

**Fecha:** 9 de octubre de 2026<br>
**Fase:** 6A.2 — arquitectura y apertura de la candidata 1.0<br>
**Baseline documental:** `4c9bc14222b79aca151e5f0ff58c325e1aebe823`<br>
**Candidata técnica de referencia:** `49ab2e1b1a58ca9201efab54b42a3125de7326f8`<br>
**Estado:** decisiones humanas registradas; DEC-012 implementada mediante F3 global

## 1. Objeto y alcance

Este documento registra las decisiones adoptadas por el usuario a partir del
`Dossier 6A.2`. Cierra documentalmente la fase de decisiones editoriales sobre
apertura, preliminares, macroorden, relación facsímil/transcripción, cierres y
navegación HTML.

No modifica la candidata Quarto, no resuelve datos personales o legales que el
usuario todavía no ha proporcionado y no inicia las auditorías especializadas.
La implementación global de las decisiones permanece pendiente.

## 2. Registro DEC-001–DEC-015

| ID | Elección | Estado de la decisión | Decisión registrada | Pendiente / condición |
|---|---|---|---|---|
| DEC-001 | C / P3 | Cerrada editorialmente | Adoptar preliminares modulares multiformato. | Implementación pendiente. |
| DEC-002 | A | Cerrada editorialmente | Incluir un prólogo personal y firmado. | Redacción del usuario e implementación pendientes. |
| DEC-003 | A | Cerrada editorialmente | Reservar aproximadamente 900–1.500 palabras y situar el prólogo después de los créditos. | Texto pendiente. |
| DEC-004 | A | Cerrada editorialmente | Preparar una introducción con rutas de lectura y una pieza compacta separada de convenciones. | Redacción e implementación pendientes. |
| DEC-005 | A | Cerrada editorialmente | Conservar el capítulo 4 como explicación metodológica detallada; la introducción lo resumirá y enlazará. | Implementación pendiente; no se modifica ahora el capítulo 4. |
| DEC-006 | A | Cerrada editorialmente | Separar una landing HTML breve, una portada PDF propia y los preliminares. | Implementación pendiente. |
| DEC-007 | A / T1 | Cerrada editorialmente | Desarrollar el título **Sorribos y Santibáñez de Ordás en 1752** y el subtítulo **Estudio histórico y edición integral del Catastro de Ensenada**. | Es título de trabajo aprobado para desarrollar; la metadata actual no cambia todavía. |
| DEC-008 | A | Cerrada en principio; información pendiente | Usar créditos basados en roles esenciales y colaboradores identificables; reservar las herramientas para el colofón. | Nombres y asignaciones concretas pendientes del usuario. |
| DEC-009 | A | Cerrada en principio; información pendiente | Resolver copyright y licencia antes de construir la nueva candidata. | Titular y licencia concreta pendientes; no se inventan. |
| DEC-010 | A | Cerrada editorialmente | Cerrar el volumen con un colofón breve técnico-editorial. | Contenido definitivo e implementación pendientes. |
| DEC-011 | C | Cerrada editorialmente | Mantener el macroorden actual y ofrecer dos rutas explícitas: histórica y documental. | Implementación pendiente. |
| DEC-012 | C / F3 | **IMPLEMENTADA** | Adoptar facsímil completo, recorte al 74 % y lightbox con navegación bidireccional en HTML; en PDF, facsímil completo como reproducción principal y localizador al 28 % con página/posición textual y navegación bidireccional. | Prototipo, aprobación humana, despliegue global, validación e integración completados; candidata formal pendiente de regeneración posterior. |
| DEC-013 | B | Cerrada editorialmente | Dar a los capítulos 5–13 títulos conclusivos específicos con función común y sustituir `Síntesis` cuando exista un título informativo adecuado. | Revisión e implementación pendientes. |
| DEC-014 | A | Cerrada editorialmente | Mostrar la parte activa desplegada y las partes inactivas plegadas en HTML. | Implementación y validación pendientes. |
| DEC-015 | A | Cerrada editorialmente | No condicionar 1.0 a disponer de ISBN y no usar nunca un ISBN provisional o inventado. | Ninguno para cerrar 6A.2. |

## 3. Estado consolidado

### Cerradas editorialmente

`DEC-001`, `DEC-002`, `DEC-003`, `DEC-004`, `DEC-005`, `DEC-006`,
`DEC-007`, `DEC-010`, `DEC-011`, `DEC-013`, `DEC-014` y `DEC-015`.

### Cerradas en principio con información pendiente

- `DEC-008`: está aprobado el modelo de créditos; faltan nombres y roles
  concretos.
- `DEC-009`: está aprobada la obligación de resolver copyright y licencia antes
  de la nueva candidata; faltan titular y licencia concreta.

Estos pendientes no reabren globalmente 6A.2.

### Decisión implementada tras prototipo

`DEC-012` siguió la secuencia completa: hipótesis F3, prototipo del commit
`7c6d6870214cac19b799d57b392bb1b9d347edd1`, aprobación humana
`F3-APROBAR`, despliegue global, validación e integración. H1–H5 y P1–P8
obtuvieron **Sí**. El commit global
`61a50987a4ce3d05721834043d4e1c5c6c611a39` aplica a 18/18 páginas y
35/35 unidades los parámetros aprobados —74 % en HTML y 28 % en PDF— con
facsímil completo y navegación bidireccional. **DEC-012 queda implementada.**

## 4. Relación con REV-*

| REV | DEC relacionadas | Resultado 6A.2 | Estado de implementación |
|---|---|---|---|
| REV-001 | DEC-007, DEC-008, DEC-009, DEC-015 | Identidad de trabajo, modelo de créditos, puerta legal y política de ISBN acordados; quedan datos humanos y legales. | No iniciada. |
| REV-005 | DEC-001, DEC-003, DEC-004 | Arquitectura P3 y piezas principales aprobadas. | No iniciada. |
| REV-007 | DEC-010 | Colofón breve aprobado. | No iniciada; depende parcialmente de la Auditoría C y de datos finales. |
| REV-013 | DEC-002, DEC-003 | Prólogo personal, firmado y situado después de créditos. | No iniciada; texto pendiente del usuario. |
| REV-014 | DEC-004, DEC-005, DEC-011 | Introducción con rutas, convenciones separadas y frontera con el capítulo 4 acordadas. | No iniciada. |
| REV-015 | DEC-006, DEC-007 | Landing HTML, portada PDF y preliminares separados, con T1 como identidad de trabajo. | No iniciada. |
| REV-016 | DEC-012 | F3 aprobada tras prototipo y revisión humana. | **Resuelta e implementada** en la rama de publicación mediante el despliegue global integrado. |
| REV-017 | DEC-011 | Macroorden actual conservado con rutas histórica y documental. | No iniciada. |
| REV-018 | DEC-014 | Parte activa desplegada y partes inactivas plegadas. | No iniciada. |
| REV-019 | DEC-013 | Cierres específicos con función común. | No iniciada. |
| REV-022 | DEC-006, DEC-007 | La identidad final no usará «Edición en desarrollo»; T1 es la fórmula de trabajo aprobada. | No iniciada; metadata intacta hasta la implementación. |

Las restantes `REV-*` conservan su estado anterior y serán tratadas por las
auditorías especializadas o por operaciones posteriores.

## 5. Datos editoriales pendientes del usuario

Sin inventar valores, siguen pendientes:

- nombre que debe figurar como autor;
- roles editoriales concretos;
- responsables de transcripción y modernización, si deben acreditarse de forma
  diferenciada;
- colaboradores;
- titular del copyright;
- licencia concreta;
- fecha editorial final;
- URL canónica cuando exista;
- identidad de proyecto que deba mostrarse.

Estos datos deben resolverse antes de la nueva candidata cuando afecten a sus
metadatos o créditos, pero no bloquean el cierre documental de 6A.2.

## 6. Dependencias y trabajo posterior

1. La Auditoría A determinará si el glosario y el Estudio Histórico cubren el
   contexto necesario o si existe una necesidad real de investigación nueva.
2. La Auditoría B revisará gráficos, cartografía y recuadros.
3. La Auditoría C revisará fuentes, bibliografía y aparatos narrativos; sus
   resultados condicionarán parte del colofón y de los metadatos finales.
4. Solo después se fijará el alcance definitivo de 1.0 y se preparará una
   implementación atómica.
5. F3 completó el prototipo, la aprobación humana, el despliegue sobre las 35
   unidades, la validación y la integración en la rama de publicación.

## 7. Versión, etiqueta e integridad

- No se crea ninguna etiqueta en 6A.2.
- La candidata técnica `49ab2e1b1a58ca9201efab54b42a3125de7326f8`
  no es la edición 1.0.
- La consolidación documental y este cierre tampoco son la edición 1.0.
- No se crea una etiqueta intermedia.
- La etiqueta final solo podrá plantearse después de auditorías, implementación,
  nueva candidata, preview, aceptación humana y Fase 6B.

La candidata formal y sus metadatos permanecen intactos. F3 está desplegada e
integrada en la rama de publicación; la candidata consolidada se regenerará en
un paquete posterior.

## 8. Siguiente paso

`PKG-05 — correcciones técnicas y rendimiento.`
