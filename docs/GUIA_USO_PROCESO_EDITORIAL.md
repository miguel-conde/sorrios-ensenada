# Guía de uso del proceso editorial

## Catastro de Ensenada de Sorribas y Santibáñez de Ordás (1752)

**Finalidad:** guía práctica para el usuario del proyecto.  
**Carácter:** informativo y operativo; no normativo.  
**Rama normal de trabajo:** `main`.

> Esta guía explica cómo pedir a ChatGPT las distintas operaciones del proyecto. No define criterios paleográficos ni sustituye a `PROJECT.md`, al Manual Editorial, a `task-modes.md`, a `editorial-procedure.md` ni a las demás referencias operativas. En caso de discrepancia, prevalecen siempre las fuentes normativas y de control del proyecto.

---

# 1. Dos formas de entrar al proyecto

El proyecto está diseñado para funcionar por dos vías equivalentes.

## 1.1. Vía universal: ChatGPT Web o Desktop con `PROJECT.md`

Esta es la vía que debe funcionar siempre, incluso en un ordenador nuevo y sin ninguna instalación local del proyecto.

Basta con indicar:

```text
Trabaja con miguel-conde/sorrios-ensenada en main.
Carga PROJECT.md.
[petición]
```

`PROJECT.md` se encarga de reconstruir el estado canónico, determinar el modo de tarea, cargar las referencias necesarias y aplicar el protocolo correcto.

No hace falta repetir en cada prompt:

- las rutas de `proyecto.yaml`, `estado.yaml` o `unidades.yaml`;
- la ubicación del PDF;
- los pasos del procedimiento editorial;
- qué índices o documentos derivados pueden verse afectados;
- cómo realizar el commit atómico.

Todo eso pertenece al propio proyecto, no al prompt del usuario.

## 1.2. Vía abreviada: complemento/skill cuando esté disponible

En una superficie donde aparezca el complemento `Catastro de Sorríos`, puede invocarse directamente:

```text
@Catastro de Sorríos [petición]
```

La skill `editar-catastro-sorrios` es autocontenida y no necesita `PROJECT.md`.

Ejemplo:

```text
@Catastro de Sorríos Trabaja la unidad actual, pero preséntame la propuesta completa antes de escribir nada.
```

Actualmente esta vía puede estar disponible en algunas superficies —por ejemplo ChatGPT Desktop— y no en otras. La ausencia del complemento no impide trabajar: se usa entonces la vía universal con `PROJECT.md`.

**Regla práctica:**

- si ves `@Catastro de Sorríos`, úsalo para abreviar;
- si no lo ves, usa `PROJECT.md`;
- ambas vías deben reconstruir el mismo estado desde GitHub `main`.

---

# 2. Modelo mental del proyecto

El chat no es el estado del proyecto. Cada sesión debe reconstruirlo desde GitHub.

```text
Usuario
  |
  +-- Web/Desktop universal ------> PROJECT.md
  |
  `-- superficie con plugin ------> editar-catastro-sorrios
                                      |
                                      v
                                  GitHub main
                                      |
                         +------------+------------+
                         |                         |
                     project/                  Google Drive
                 workspace vivo           PDF autoritativo
                                            solo lectura
```

En trabajo normal:

- GitHub `main` contiene el workspace vivo;
- `project/` contiene controles, edición y derivados;
- Google Drive se usa únicamente para leer el PDF autoritativo;
- no se depende de conversaciones anteriores;
- no se necesita Work, checkout local, Git local, Python local, WSL ni VS Code.

---

# 3. Los cinco modos de trabajo

| Modo | Para qué sirve | ¿Escribe? |
|---|---|---|
| Consulta puntual | Preguntar por estado, contenido o un dato concreto | No |
| Edición de unidad | Transcribir, validar y cerrar la unidad actual | Sí, si procede |
| Auditoría | Comprobar coherencia, estructura, versiones y estado | No, salvo petición posterior |
| Cambio metodológico | Proponer o aprobar un criterio editorial nuevo | Solo tras aprobación expresa |
| Estudio histórico | Elaborar el estudio cuando esté habilitado | Solo cuando `historical_study_enabled: true` |

El usuario normalmente solo necesita expresar el objetivo. El bootstrap o la skill deben determinar el modo cuando sea evidente.

---

# 4. Edición normal de una unidad

Una unidad editorial se trata como una operación completa. Internamente el sistema debe:

1. reconstruir estado y secuencia desde GitHub;
2. comprobar que la operación esté `clean` y que la unidad anterior esté cerrada;
3. localizar y leer visualmente la unidad en el PDF autoritativo;
4. transcribir línea por línea;
5. revisar la lectura contra la imagen;
6. aplicar el Manual;
7. completar aparato editorial;
8. preparar las altas de Glosario e índices;
9. registrar dudas sin forzar lecturas;
10. superar control de calidad y validar;
11. incorporar derivados justificados;
12. actualizar Diario, registro de operación y estado;
13. validar el conjunto;
14. publicar en un único commit Git atómico;
15. verificar el resultado.

El usuario no necesita enumerar estos pasos en el prompt.

## Con complemento

```text
@Catastro de Sorríos Edita y cierra la unidad actual. Si aparece un problema que requiera un criterio nuevo, detente y consúltamelo antes de publicar.
```

## Sin complemento

```text
Trabaja con miguel-conde/sorrios-ensenada en main.
Carga PROJECT.md.
Edita y cierra la unidad actual. Si aparece un problema que requiera un criterio nuevo, detente y consúltamelo antes de publicar.
```

---

# 5. Edición con revisión humana antes de publicar

Esta modalidad es recomendable para unidades difíciles.

## Con complemento

```text
@Catastro de Sorríos Trabaja la unidad actual, pero preséntame la propuesta completa antes de escribir nada.
```

## Sin complemento

```text
Trabaja con miguel-conde/sorrios-ensenada en main.
Carga PROJECT.md.
Trabaja la unidad actual, pero preséntame la propuesta completa antes de escribir nada.
```

La propuesta debe incluir transcripción, aparato editorial, dudas y cambios derivados. Después de revisarla basta con responder:

```text
Aprobado. Publica la operación propuesta y verifica el resultado.
```

Antes de publicar, el sistema debe volver a comprobar que `main` no ha cambiado respecto del `base_sha` usado para preparar la operación.

---

# 6. Consulta puntual y solo lectura

Ejemplos:

- cuál es la unidad actual;
- qué dudas siguen abiertas;
- cómo quedó transcrita una unidad;
- si aparece una persona, topónimo, institución, medida u oficio;
- qué dice un archivo concreto.

## Con complemento

```text
@Catastro de Sorríos ¿Cuál es el estado actual del proyecto y qué unidad toca ahora?
```

## Sin complemento

```text
Trabaja con miguel-conde/sorrios-ensenada en main.
Carga PROJECT.md.
Consulta puntual y solo lectura: ¿cuál es el estado actual del proyecto y qué unidad toca ahora?
```

No hace falta abrir el Manual ni Drive salvo que la respuesta dependa de un criterio editorial o de la imagen del manuscrito.

Si hay que mirar el manuscrito, puede añadirse simplemente:

```text
Compruébalo visualmente en el PDF autoritativo. No modifiques nada.
```

---

# 7. Lecturas dudosas

Las dudas paleográficas forman parte del flujo normal. No constituyen por sí mismas un cambio metodológico.

El sistema debe intentar resolverlas mediante las comparaciones permitidas por el Manual y, si persisten, conservarlas con la notación adecuada. Nunca debe inventar ni forzar una lectura.

Petición suficiente:

```text
Presta especial atención a las lecturas dudosas. Intenta resolverlas según el Manual, pero no fuerces ninguna.
```

---

# 8. Auditoría

La auditoría comprueba el proyecto sin editar la unidad actual.

## Con complemento

```text
@Catastro de Sorríos Audita el estado del proyecto. No corrijas nada todavía.
```

## Sin complemento

```text
Trabaja con miguel-conde/sorrios-ensenada en main.
Carga PROJECT.md.
Audita el estado del proyecto. No corrijas nada todavía.
```

Si el diagnóstico confirma problemas objetivos:

```text
Corrige los problemas objetivos encontrados, sin cambiar criterios editoriales, y verifica el resultado.
```

---

# 9. Cambio metodológico

Se usa cuando aparece un caso que el Manual no resuelve o cuando se desea cambiar conscientemente un criterio vigente.

Nunca debe introducirse un criterio nuevo de forma implícita durante una edición ordinaria.

## Con complemento

```text
@Catastro de Sorríos Tenemos este caso no previsto: [DESCRIPCIÓN]. Comprueba si el Manual ya lo resuelve; si no, propón un criterio nuevo y espera mi aprobación.
```

## Sin complemento

```text
Trabaja con miguel-conde/sorrios-ensenada en main.
Carga PROJECT.md.
Cambio metodológico: tenemos este caso no previsto: [DESCRIPCIÓN]. Comprueba si el Manual ya lo resuelve; si no, propón un criterio nuevo y espera mi aprobación.
```

Tras aprobar:

```text
Apruebo el criterio. Incorpóralo con la trazabilidad necesaria, aplica solo los efectos aprobados y verifica el resultado.
```

---

# 10. Revisión de una unidad ya validada

Una unidad validada no debe reabrirse como si fuera la unidad corriente. Primero se audita en solo lectura.

Petición:

```text
Revisa la unidad [UNIDAD] ya validada porque sospecho este problema: [PROBLEMA]. Compara la edición con el PDF y el Manual. No modifiques nada.
```

Solo si se confirma una causa suficiente —imagen mejor, lectura demostrablemente superior o error objetivo— se autoriza la corrección:

```text
Corrige la unidad validada conforme a la auditoría. No cambies la secuencia editorial. Registra la corrección y actualiza los derivados afectados.
```

---

# 11. Investigación histórica durante la edición

Pueden consultarse fuentes externas para identificaciones, equivalencias o contexto auxiliar cuando el Manual lo permita.

Debe distinguirse siempre entre:

- lo que afirma el manuscrito;
- lo que procede de fuentes externas;
- lo que sea inferencia o hipótesis.

Petición útil:

```text
Investiga externamente solo lo necesario para identificar o contextualizar esta unidad. Distingue manuscrito, fuente externa e inferencia, y cita las fuentes.
```

---

# 12. Estudio histórico

Solo puede escribirse cuando `historical_study_enabled` sea `true`.

Mientras esté desactivado puede prepararse un plan o comprobar si procede activarlo:

```text
Estudia si procede activar el Estudio Histórico. Revisa estado y Manual, pero no actives nada todavía.
```

Cuando se habilite, la base documental sobre el expediente será la edición paleográfica validada, salvo cambio metodológico expreso.

---

# 13. Cómo continuar en un chat nuevo

No hace falta recordar manualmente la última unidad.

## Con complemento

```text
@Catastro de Sorríos Continúa con la unidad actual.
```

## Sin complemento

```text
Trabaja con miguel-conde/sorrios-ensenada en main.
Carga PROJECT.md.
Continúa con la unidad actual.
```

GitHub, no la conversación anterior, determina dónde continúa el trabajo.

---

# 14. Cuándo indicar una unidad concreta

En edición normal conviene pedir simplemente «la unidad actual».

Indica una unidad concreta cuando quieras:

- consultarla;
- auditarla;
- revisar una lectura ya validada;
- compararla con otra;
- investigar una duda localizada.

---

# 15. Una unidad cada vez

No se recomienda pedir varias unidades como una única operación editorial. Cada unidad debe completar su ciclo de lectura, validación, derivados, cierre y verificación antes de empezar la siguiente.

Después de cerrar una unidad, puede bastar:

```text
Adelante con la siguiente unidad.
```

El sistema debe releer el estado canónico antes de empezar.

---

# 16. Referencia rápida

| Situación | Petición mínima |
|---|---|
| Saber algo | `Consulta puntual y solo lectura: [pregunta]` |
| Continuar la edición | `Edita y cierra la unidad actual` |
| Revisar antes de escribir | `Trabaja la unidad actual, pero preséntame la propuesta antes de escribir` |
| Auditar | `Audita el estado del proyecto. No corrijas todavía` |
| Cambiar una regla | `Comprueba si el Manual cubre este caso; si no, propón un criterio y espera aprobación` |
| Revisar una unidad cerrada | `Audita primero la unidad [X]; no modifiques nada` |
| Investigar una identificación | `Distingue manuscrito, fuente externa e inferencia` |
| Continuar en otro chat | `Continúa con la unidad actual` |

Si se usa ChatGPT Web o Desktop sin complemento, antepón:

```text
Trabaja con miguel-conde/sorrios-ensenada en main.
Carga PROJECT.md.
```

Si el complemento está disponible, puede sustituirse todo ese arranque por:

```text
@Catastro de Sorríos
```

---

# 17. Regla práctica final

La complejidad debe estar en el proyecto, no en los prompts.

El usuario solo necesita expresar:

1. **cómo entra:** `@Catastro de Sorríos` si está disponible, o `PROJECT.md` si no;
2. **qué quiere hacer:** consultar, editar, auditar, cambiar método o estudiar historia;
3. **si autoriza publicar** o quiere revisar antes.

Todo lo demás —archivos necesarios, unidad actual, página del PDF, procedimiento, derivados afectados, control de concurrencia, estado resultante y protocolo Git— debe reconstruirse desde las fuentes canónicas del proyecto.