# Guía de uso del proceso editorial

## Catastro de Ensenada de Sorribas y Santibáñez de Ordás (1752)

**Finalidad:** guía práctica para el usuario del proyecto.  
**Carácter:** informativo y operativo; no normativo.  
**Rama normal de trabajo:** `main`.

> Esta guía explica cómo solicitar a ChatGPT las distintas operaciones del proyecto. No define criterios paleográficos ni sustituye a `PROJECT.md`, al Manual Editorial, a `task-modes.md`, a `editorial-procedure.md` ni a las demás referencias operativas. En caso de discrepancia, prevalecen siempre las fuentes normativas y de control del proyecto.

---

# 1. Modelo mental del proyecto

El usuario no debe mantener manualmente el estado de la edición en el chat. El estado canónico se reconstruye en cada sesión desde GitHub.

```text
Usuario
  |
  | petición
  v
ChatGPT
  |
  +-- PROJECT.md                         entrada para Chat normal
  +-- proyecto.yaml                      identidad y autoridades
  +-- estado.yaml                        estado operativo actual
  +-- unidades.yaml                      secuencia editorial
  +-- Manual_Editorial.md                método editorial
  |
  +-- GitHub main                        workspace vivo completo
  |
  `-- Google Drive
       `-- PDF autoritativo              manuscrito, solo lectura
```

En trabajo normal:

- GitHub `main` contiene el workspace vivo;
- `project/` es la raíz documental del proyecto;
- Google Drive se usa únicamente para leer el PDF autoritativo;
- el chat anterior no es una fuente de estado;
- no es necesario disponer de checkout local, Git local, Python local, WSL, VS Code ni Work.

En Chat normal Web/Desktop se usa `PROJECT.md` como entrada. En un entorno con la skill instalada puede invocarse `editar-catastro-sorrios`; ambas vías deben reconstruir el mismo estado canónico.

---

# 2. Los cinco modos de trabajo

El proyecto distingue cinco modos oficiales.

| Modo | Para qué sirve | ¿Escribe? |
|---|---|---|
| Consulta puntual | Preguntar por estado, contenido o un dato concreto | No |
| Edición de unidad | Transcribir, validar y cerrar la unidad actual | Sí, si procede |
| Auditoría | Comprobar coherencia, estructura, versiones y estado | No, salvo petición posterior |
| Cambio metodológico | Proponer o aprobar un criterio editorial nuevo | Solo tras aprobación expresa |
| Estudio histórico | Elaborar el estudio cuando esté habilitado | Solo cuando `historical_study_enabled: true` |

La primera decisión al comenzar una tarea debe ser identificar cuál de estos modos corresponde.

---

# 3. Edición normal de una unidad

Una unidad editorial debe tratarse como una operación completa. No se debe comenzar la siguiente hasta cerrar documentalmente la actual.

El ciclo normal es:

1. leer `proyecto.yaml`, `estado.yaml` y `unidades.yaml` desde el mismo estado de GitHub;
2. comprobar que `operation.status` sea `clean`, que la unidad actual sea coherente y que la anterior esté cerrada;
3. obtener el PDF autoritativo de Drive y localizar exactamente página y posición;
4. leer visualmente la unidad completa;
5. transcribir línea por línea;
6. revisar la transcripción contra la imagen;
7. aplicar el Manual vigente;
8. completar Imagen, Transcripción paleográfica, Observaciones editoriales, Notas paleográficas, Notas históricas y Referencias cruzadas;
9. preparar las posibles altas o cambios del Glosario y los índices;
10. registrar las dudas que sigan abiertas sin forzar lecturas;
11. superar el control de calidad y validar la unidad;
12. incorporar únicamente los derivados justificados de la unidad validada;
13. actualizar Diario, registro de operación y `estado.yaml`;
14. validar el conjunto completo;
15. comprobar que la rama objetivo no ha cambiado desde el `base_sha`;
16. publicar todos los cambios mediante un único commit Git atómico;
17. verificar el commit, los archivos afectados, el estado resultante y, cuando corresponda, el CI.

La unidad es, por tanto, la transacción editorial básica del proyecto.

---

# 4. Prompt estándar de producción

Para continuar normalmente la edición en un chat nuevo:

```text
Trabaja con el proyecto Sorríos del repositorio privado
miguel-conde/sorrios-ensenada.

Usa la rama main.
Carga PROJECT.md y sigue sus instrucciones.

Modo: edición de unidad.

Reconstruye primero el estado canónico y confirma:
- operation.status;
- last_validated_unit;
- last_closed_unit;
- current_unit;
- next_unit;
- current_location.

Después trabaja únicamente la unidad actual indicada por estado.yaml.

Realiza el ciclo editorial completo conforme al Manual vigente:
1. lee visualmente la unidad completa en el PDF autoritativo;
2. transcribe línea por línea;
3. revisa la lectura contra la imagen;
4. completa todo el aparato editorial;
5. identifica y trata correctamente todas las dudas;
6. prepara y aplica, tras la validación, únicamente los cambios justificados
   en Glosario e índices;
7. actualiza Diario, registro de operación y estado;
8. valida el conjunto;
9. publica mediante un único commit Git atómico;
10. verifica el commit, el estado resultante y el CI.

No fuerces ninguna lectura.
No avances a la siguiente unidad.
Si aparece una situación que exija un criterio metodológico nuevo,
detente antes de publicar y preséntamela para decisión.
```

Este es el prompt recomendado para la mayoría de las unidades.

---

# 5. Edición con revisión humana antes de publicar

En una unidad difícil puede convenir separar análisis y escritura.

Primera petición:

```text
Trabaja con el proyecto Sorríos del repositorio
miguel-conde/sorrios-ensenada.

Usa main, carga PROJECT.md y sigue sus instrucciones.

Modo: edición de unidad.

Trabaja únicamente la unidad actual.
Realiza todo el análisis editorial y prepara la operación completa,
pero NO modifiques todavía ningún archivo de GitHub.

Preséntame para revisión:
- lectura de la unidad;
- transcripción paleográfica;
- observaciones editoriales;
- notas paleográficas;
- notas históricas;
- referencias cruzadas;
- dudas;
- cambios propuestos en Glosario e índices;
- cambios propuestos en Diario y estado.

Espera mi aprobación antes de publicar.
```

Tras aprobar la propuesta:

```text
Aprobado.

Publica exactamente la operación propuesta siguiendo el protocolo Git
atómico del proyecto. Antes de escribir, relee el HEAD de main y comprueba
que no ha cambiado; si ha cambiado, detente y reconcilia.

Después verifica el commit, el estado resultante y el CI.
```

Este modo de trabajo es recomendable cuando existen lecturas difíciles, varias dudas o decisiones editoriales delicadas.

---

# 6. Lecturas dudosas

Las dudas paleográficas forman parte del flujo normal y no constituyen por sí mismas un cambio metodológico.

El Manual exige, cuando sea útil:

1. comparar con otras apariciones;
2. comparar con firmas;
3. comparar con documentos paralelos;
4. si persiste la duda, conservar una lectura responsable marcada con `[?]`;
5. si no existe una lectura responsable, utilizar `[...]`.

Nunca se debe inventar ni forzar una lectura.

Petición útil:

```text
Trabaja la unidad actual en modo edición.

Presta especial atención a las lecturas dudosas.
Intenta resolverlas paleográficamente utilizando las comparaciones permitidas
por el Manual, pero no fuerces ninguna.

Si persiste alguna duda, márcala correctamente y consérvala como duda abierta
en los documentos de control que correspondan.
```

---

# 7. Consulta puntual y solo lectura

Se usa para preguntas concretas sobre el proyecto, por ejemplo:

- cuál es la unidad actual;
- qué dudas están abiertas;
- cómo quedó transcrita una unidad;
- si aparece una persona, topónimo, institución, medida u oficio;
- qué dice un archivo determinado.

Plantilla:

```text
Trabaja con el proyecto Sorríos del repositorio
miguel-conde/sorrios-ensenada.

Usa main y carga PROJECT.md.

Modo: consulta puntual y solo lectura.

[MI PREGUNTA]

No modifiques ningún archivo.
```

En este modo deben leerse solo los controles y la fuente concreta necesaria. No hace falta abrir el Manual ni Drive salvo que la pregunta dependa de un criterio editorial o de la imagen del manuscrito.

Si la consulta exige comprobar el manuscrito:

```text
Para responder necesitas comprobar directamente el PDF autoritativo.
Léelo visualmente, pero mantén la operación en solo lectura.
```

---

# 8. Auditoría

La auditoría sirve para comprobar el proyecto sin editar una unidad.

Plantilla:

```text
Trabaja con el proyecto Sorríos del repositorio
miguel-conde/sorrios-ensenada.

Usa main y carga PROJECT.md.

Modo: auditoría.

Audita el workspace canónico completo según las reglas del proyecto:
estructura, controles, versiones, secuencia, estado, 35 unidades,
secciones obligatorias, operaciones, derivados, autoridades y ausencia
del PDF en GitHub.

Informa de todos los problemas encontrados.
No corrijas nada todavía.
```

Si la auditoría detecta problemas objetivos, la corrección debe solicitarse después de conocer el diagnóstico:

```text
Corrige todos los problemas objetivos encontrados en la auditoría.
No cambies ningún criterio editorial.
Usa operaciones Git atómicas y verifica el resultado.
```

---

# 9. Cambio metodológico

Un cambio metodológico es necesario cuando aparece una situación que el Manual vigente no resuelve o cuando se desea alterar conscientemente un criterio existente.

Nunca debe introducirse un criterio nuevo de forma implícita durante la edición de una unidad.

Plantilla:

```text
Trabaja con el proyecto Sorríos usando main.
Carga PROJECT.md.

Modo: cambio metodológico.

Ha aparecido este problema:

[DESCRIPCIÓN]

Comprueba primero si el Manual vigente ya contiene un criterio aplicable.

Si lo contiene, indícame cuál y no modifiques el Manual.

Si no lo contiene, prepara una propuesta de criterio nuevo:
- problema;
- alternativas;
- criterio recomendado;
- justificación;
- cambios exactos necesarios en el Manual;
- efectos sobre unidades ya validadas, si los hubiera.

No publiques ningún cambio hasta que yo lo apruebe.
```

Tras la aprobación:

```text
Apruebo el nuevo criterio.

Incorpóralo al Manual, actualiza los documentos de trazabilidad necesarios
y aplica únicamente los efectos derivados que hayamos aprobado.

Publica la operación de forma atómica y verifica el resultado.
```

---

# 10. Revisión de una unidad ya validada

Una unidad validada no debe reabrirse como si fuera la unidad corriente. El Manual solo justifica modificarla cuando aparezca una imagen mejor, una lectura demostrablemente superior o un error objetivo.

Primero debe auditarse la unidad en solo lectura:

```text
Modo: auditoría y solo lectura.

Revisa la unidad [UNIDAD] ya validada porque sospecho este problema:

[PROBLEMA]

Compara la edición con el PDF autoritativo y con el Manual.
Determina si existe realmente:
- un error objetivo;
- una lectura demostrablemente superior;
- o ninguna razón suficiente para modificar la unidad.

No modifiques nada.
```

Si la corrección está justificada:

```text
Corrige la unidad validada [UNIDAD] conforme al resultado de la auditoría.

No cambies la secuencia editorial ni current_unit.
Registra expresamente la corrección en Diario Editorial y CAMBIOS.md,
actualiza cualquier derivado afectado y publica todo mediante una única
operación Git atómica.

Verifica después el resultado.
```

---

# 11. Consultas e investigación histórica durante la edición

Durante la edición pueden utilizarse fuentes externas para comprobar identificaciones, equivalencias o contexto auxiliar cuando el Manual lo permita.

Debe distinguirse siempre:

- lo que afirma el manuscrito;
- lo que procede de fuentes externas;
- cualquier inferencia o hipótesis.

Las fuentes externas no convierten sus contenidos en hechos del expediente ni constituyen por sí mismas base documental autónoma del Estudio Histórico.

Petición útil:

```text
Durante la edición de esta unidad, investiga externamente únicamente las
identificaciones históricas necesarias para notas, Glosario o índices.

Distingue claramente:
- lo que afirma el manuscrito;
- lo que procede de fuentes externas;
- y cualquier inferencia.

Cita las fuentes externas utilizadas.
```

---

# 12. Estudio histórico

El modo Estudio histórico solo puede escribir cuando `historical_study_enabled` sea `true` en el control canónico del proyecto.

Mientras permanezca desactivado pueden hacerse consultas o preparar un plan, pero no debe escribirse el Estudio Histórico como resultado vivo del proyecto.

Para estudiar su futura activación:

```text
Modo: cambio metodológico.

Quiero estudiar si procede activar la fase de Estudio Histórico.

Revisa el estado de la edición y las condiciones del Manual.
No actives nada todavía.

Explícame qué condiciones se cumplen, cuáles faltan y qué cambios de control
serían necesarios para establecer historical_study_enabled: true.
```

Cuando se habilite, la base documental sobre el expediente será exclusivamente la edición paleográfica validada, salvo que el Manual se modifique expresamente.

---

# 13. Cómo continuar en un chat nuevo

No debe dependerse de frases como «continúa donde lo dejamos» si el chat no contiene el contexto suficiente.

La forma robusta es:

```text
Trabaja con el proyecto Sorríos del repositorio
miguel-conde/sorrios-ensenada.

Usa main.
Carga PROJECT.md y reconstruye el estado canónico.

Modo: edición de unidad.
Continúa el trabajo con la unidad actual indicada por estado.yaml.
```

El repositorio, no la conversación anterior, determina dónde continúa el trabajo.

---

# 14. Cuándo indicar una unidad concreta

En edición normal es preferible decir:

```text
trabaja la unidad actual indicada por estado.yaml
```

No es necesario recordar manualmente qué folio sigue.

Conviene indicar una unidad concreta cuando se quiera:

- hacer una consulta específica;
- auditarla;
- revisar una lectura ya validada;
- comparar dos unidades;
- investigar una duda localizada.

---

# 15. Una unidad cada vez

No se recomienda pedir varias unidades como una sola operación editorial. Cada unidad debe completar su propio ciclo de lectura, transcripción, control de calidad, validación, derivados, cierre y verificación antes de comenzar la siguiente.

Una vez cerrada una unidad, dentro del mismo chat puede bastar:

```text
Adelante con la siguiente unidad.
Relee antes el estado canónico y sigue el procedimiento completo.
```

El sistema deberá volver a consultar el estado antes de comenzar la nueva unidad.

---

# 16. Uso desde un entorno con skill

Si el entorno permite invocar la skill instalada, puede sustituirse el arranque mediante `PROJECT.md` por una invocación explícita de `editar-catastro-sorrios`.

Ejemplo conceptual:

```text
Usa explícitamente la skill editar-catastro-sorrios.
Modo: edición de unidad.
Trabaja sobre la rama canónica y la unidad actual.
[resto de la petición]
```

La skill es autocontenida; no debe depender de `PROJECT.md`. El resultado operativo debe ser equivalente porque ambas vías usan las mismas autoridades canónicas bajo `project/`.

---

# 17. Referencia rápida

| Situación | Petición recomendada |
|---|---|
| Quiero saber algo | `Modo: consulta puntual y solo lectura` |
| Quiero continuar la edición | `Modo: edición de unidad. Trabaja la unidad actual y cierra el ciclo completo` |
| Quiero revisar antes de escribir | `Modo: edición de unidad. Prepara todo pero no publiques hasta mi aprobación` |
| Sospecho un problema general | `Modo: auditoría. Informa; no corrijas todavía` |
| Falta una regla editorial | `Modo: cambio metodológico. Prepara propuesta y espera mi aprobación` |
| Sospecho un error en una unidad validada | `Audita primero esa unidad; corrígela solo tras confirmar que existe causa suficiente` |
| Quiero investigar una identificación | `Consulta o edición, distinguiendo manuscrito, fuente externa e inferencia` |
| Quiero iniciar el Estudio Histórico | `Cambio metodológico para comprobar si procede activarlo` |

---

# 18. Regla práctica final

En caso de duda sobre cómo formular una petición, basta con indicar:

1. el repositorio `miguel-conde/sorrios-ensenada`;
2. la rama `main`;
3. que se cargue `PROJECT.md` en Chat normal;
4. el modo de tarea;
5. el objetivo concreto;
6. si se autoriza publicar o se desea revisión previa.

Todo lo demás —archivos necesarios, unidad actual, página del PDF, derivados afectados, estado resultante y protocolo Git— debe reconstruirse desde las fuentes canónicas del propio proyecto.
