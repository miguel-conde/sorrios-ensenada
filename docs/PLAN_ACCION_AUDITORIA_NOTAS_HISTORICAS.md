# Plan de acción tras la auditoría retrospectiva de Notas históricas

## Proyecto

**Catastro de Ensenada de Sorribos y Santibáñez de Ordás (1752)**

## Objeto del plan

Este documento convierte en acciones concretas los resultados de la auditoría retrospectiva realizada sobre las **Notas históricas de todas las unidades ya validadas y cerradas**, desde la Portada hasta `last_closed_unit`, según el estado canónico del proyecto en el momento de ejecutar cada acción.

El plan tiene cuatro objetivos:

1. corregir las omisiones puntuales detectadas en las Notas históricas;
2. mejorar determinados derivados —Glosario e índices— cuando la auditoría ha encontrado información suficientemente fundamentable;
3. reforzar el procedimiento operativo para evitar que las Notas históricas queden vacías por inercia;
4. preservar estrictamente la separación entre Notas históricas de unidad, Glosario, índices, Diario Editorial y futuro Estudio Histórico.

Este documento **no autoriza por sí mismo ninguna modificación**. Cada bloque deberá ejecutarse únicamente tras la aprobación correspondiente.

> **Rectificación de 18 de septiembre de 2026:** la lectura paleográfica `Sorribas` usada en la versión inicial de este plan queda sustituida por `Sorribos` tras la relectura visual completa del manuscrito y el contraste histórico externo. La sección 4.1 se actualiza en consecuencia.

---

# 1. Principios de ejecución

## 1.1. Estado de referencia

Todas las actuaciones deberán reconstruir el estado desde las fuentes canónicas del proyecto en el momento de ejecutarse.

El límite retrospectivo será siempre:

```text
last_closed_unit
```

No deberá codificarse en el procedimiento un folio concreto como último folio procesado.

Antes de cualquier intervención deberá verificarse:

- rama canónica;
- `last_validated_unit`;
- `last_closed_unit`;
- `current_unit`;
- `operation.status`;
- Manual Editorial vigente;
- versión vigente de la Edición Crítica;
- ausencia de operaciones incompletas.

## 1.2. Preservación de la edición paleográfica

Las correcciones previstas por este plan afectan principalmente a:

- Notas históricas;
- Glosario;
- índices;
- procedimiento de la skill;
- documentación operativa asociada.

No se modificarán transcripciones paleográficas ya validadas salvo que, durante la ejecución del plan, aparezca de forma independiente un error objetivo de lectura, supuesto que deberá tratarse mediante el procedimiento ordinario previsto por el Manual.

## 1.3. Separación documental

Se mantendrá estrictamente la siguiente distribución:

- **Notas históricas:** identificación, equivalencia o contexto local puntual, comprobable y directamente ligado a una unidad.
- **Glosario:** términos históricos documentados y su definición contextual o fundamentada.
- **Índices:** personas, topónimos, instituciones, medidas y oficios con sus identificaciones y equivalencias estructuradas.
- **Diario Editorial:** dudas, hipótesis, incidencias y relaciones provisionales.
- **Estudio Histórico:** interpretación consolidada de conjunto basada en la edición validada.

El hecho de que `historical_study_enabled` sea `false` no impedirá incorporar Notas históricas puntuales cuando el Manual lo permita o exija.

## 1.4. Investigación externa

Solo se realizará investigación externa cuando pueda cambiar una decisión editorial concreta.

Para cada dato externo deberán distinguirse:

1. lo que afirma el manuscrito;
2. lo que afirma la fuente externa;
3. cualquier inferencia editorial propia.

Las fuentes externas utilizadas para identificaciones o equivalencias no pasarán a constituir base documental autónoma del Estudio Histórico.

---

# 2. Fase 0 — Congelar temporalmente el avance editorial

Antes de continuar la edición más allá de `last_closed_unit`, conviene resolver la incidencia retrospectiva detectada.

El objetivo de esta pausa es evitar que el mismo sesgo operativo se reproduzca en nuevas unidades mientras se corrige el procedimiento.

Durante esta fase:

- no se editarán nuevas unidades;
- no se modificará el Estudio Histórico;
- no se alterará el Manual salvo que una revisión posterior demostrase que el criterio normativo es realmente insuficiente;
- se mantendrá el estado canónico coherente con `last_closed_unit`.

---

# 3. Fase 1 — Reforzar el procedimiento para las unidades futuras

## 3.1. Mantener, en principio, el Manual Editorial vigente

La auditoría concluye que el Manual ya contiene la norma sustantiva necesaria:

- define la función de las Notas históricas;
- separa Notas históricas, Diario y Estudio Histórico;
- permite fuentes externas para identificaciones y equivalencias fundamentadas;
- ordena añadir Notas históricas puntuales cuando proceda;
- exige en control de calidad que las notas pertinentes estén incorporadas en el documento correcto.

Por tanto, **no se propone inicialmente una nueva versión del Manual Editorial**.

## 3.2. Reforzar `editorial-procedure.md`

Se propone introducir un checkpoint explícito antes de validar cada unidad.

El procedimiento deberá obligar a:

1. inventariar los posibles datos históricos presentes en la unidad;
2. clasificarlos expresamente como:
   - **A. Sin nota necesaria**;
   - **B. Glosario o índice**;
   - **C. Nota histórica puntual**;
   - **D. Diario o futuro Estudio Histórico**;
3. investigar externamente únicamente los candidatos C cuya clasificación no pueda resolverse con las fuentes internas;
4. decidir de manera positiva si la sección `Notas históricas`:
   - debe contener una o más notas; o
   - puede quedar justificadamente vacía;
5. verificar que los elementos B se hayan dirigido al Glosario o índice correcto;
6. verificar que los elementos D no se hayan convertido prematuramente en afirmaciones históricas consolidadas.

## 3.3. Reforzar el control de calidad operativo

Se propone incorporar al QC una pregunta explícita:

> ¿Se ha evaluado expresamente, y no por defecto, si esta unidad necesita una Nota histórica puntual?

La respuesta deberá basarse en la clasificación A/B/C/D.

## 3.4. Revisar la propia `SKILL.md` solo si es necesario

Una vez preparado el cambio exacto de `editorial-procedure.md`, deberá comprobarse si la `SKILL.md` necesita también una referencia explícita a este checkpoint.

No debe duplicarse innecesariamente el procedimiento si basta con reforzar la referencia al documento operativo.

## Puerta de aprobación 1

Antes de modificar ningún archivo metodológico se presentará:

- texto exacto propuesto para `editorial-procedure.md`;
- eventual cambio mínimo de `SKILL.md`;
- justificación;
- efecto sobre unidades futuras.

Solo tras aprobación expresa se publicará el cambio.

---

# 4. Fase 2 — Reparación retrospectiva de Notas históricas

La auditoría ha identificado cuatro posibles Notas históricas de grupo C distribuidas en tres unidades ya cerradas.

Estas notas deberán revisarse y aprobarse individualmente antes de su incorporación.

## 4.1. Portada — rectificación paleográfica de `Sorribos`

### Problema detectado

La relectura visual de todas las apariciones del topónimo en el manuscrito corrige la lectura anterior `Sorribas`. La Portada contiene `Sorribos`; el folio 306r lo presenta dos veces, una de ellas con la división de línea `Sorri-` / `bos`; y el folio 306v vuelve a registrar `Sorribos`.

La lectura `Sorribas`, adoptada en una fase anterior del proyecto, debe considerarse un error paleográfico y no una variante del manuscrito.

La documentación externa refuerza esta lectura: PARES documenta `Santibáñez de Sorribos` en 1715; el estudio histórico-etimológico de Fernando Álvarez-Balbuena recoge para el actual Sorrios formas medievales como `Sorribios` y `Sorribos` y la pervivencia de `Sorribos` en el siglo XIX; una escritura de 1831 publicada en la Gaceta de Madrid menciona el `Barrio de Sorribos`; y el Ayuntamiento de Santa María de Ordás identifica hoy Sorrios como barrio de Santibáñez de Ordás.

### Acción propuesta

- fijar `Sorribos` como forma manuscrita de 1752;
- corregir la transcripción paleográfica en Portada, folio 306r y folio 306v, incluida la división `Sorri-` / `bos`;
- corregir el Índice de topónimos y todos los documentos vivos derivados;
- registrar expresamente que `Sorribas` fue un error paleográfico del proyecto y no una variante histórica de este núcleo de Ordás;
- conservar los documentos archivados como testimonio de estados anteriores, cubiertos por una errata expresa;
- incorporar al Estudio Histórico una nota sobre la continuidad documental `Sorribos` → `Sorrios`, sin fijar una secuencia fonética completa más allá de lo que permiten las fuentes.

### Derivado relacionado

Revisar la entrada `Sorribos` del Índice de topónimos y el registro de afirmaciones del Estudio Histórico.

---

## 4.2. Folio 306r — `Concejo de Ordas`

### Problema detectado

El manuscrito sitúa Sorribos y Santibáñez en el `Concejo de Ordas`.

Una equivalencia directa con el municipio contemporáneo podría inducir a error.

### Acción propuesta

Preparar una Nota histórica puntual que:

- identifique `Concejo de Ordas` como circunscripción histórica;
- distinga esta realidad del municipio contemporáneo;
- explique de manera breve y fundamentada la relación entre `Ordás` y la denominación moderna `Santa María de Ordás`;
- evite reconstruir en la nota la historia administrativa completa del territorio.

### Derivados relacionados

Revisar, cuando proceda:

- Índice de topónimos;
- Índice de instituciones.

---

## 4.3. Folio 306r — `abogado De los R[eale]s Consejos`

### Problema detectado

La expresión puede interpretarse erróneamente como si Joachin Aguado fuese empleado de un órgano concreto denominado `Reales Consejos`.

### Acción propuesta

Preparar una Nota histórica puntual que:

- explique el carácter de título o habilitación profesional de `abogado de los Reales Consejos`;
- indique el contexto institucional del Consejo de Castilla cuando la fuente lo permita;
- deje claro que el manuscrito no demuestra por sí mismo que Joachin Aguado estuviera al servicio permanente de un consejo concreto.

### Derivados relacionados

Revisar:

- entrada `R[eale]s Consejos` del Índice de instituciones;
- entrada `abogado` del Índice de oficios, únicamente si el contexto actual resulta insuficiente.

### Exclusión expresa

No identificar biográficamente a Joachin Aguado salvo que aparezca evidencia externa suficientemente concluyente.

---

## 4.4. Folio 307r — `Conde De Luna`

### Problema detectado

La unidad menciona al `Conde De Luna`, pero el Índice de personas no establece actualmente una identificación nominal.

La auditoría encontró evidencia externa suficiente para proponer la identificación del titular del condado en 1752 con **Francisco Alfonso Pimentel, XV conde de Luna**.

### Acción propuesta

Preparar una Nota histórica que distinga con precisión:

- **manuscrito:** el concejo es de señorío y pertenece al Conde de Luna;
- **fuente externa:** identificación nominal del titular del título en 1752;
- **inferencia editorial:** correspondencia entre el título citado y el titular documentado para ese año.

### Derivado relacionado

Actualizar, si se aprueba la identificación, la entrada `Conde De Luna` del Índice de personas.

---

## Puerta de aprobación 2

Antes de modificar la Edición Crítica deberán presentarse juntas:

- las cuatro Notas históricas en su redacción exacta;
- fuentes utilizadas;
- grado de seguridad;
- modificaciones exactas asociadas en los índices.

Cada nota deberá poder aprobarse, modificarse o rechazarse independientemente.

---

# 5. Fase 3 — Reparación de derivados de grupo B

Estas mejoras no justifican necesariamente Notas históricas, porque su lugar natural es Glosario o índices.

## 5.1. Índice de topónimos

Revisar sistemáticamente las identificaciones modernas de:

- `Sorribos`;
- `Ordas`;
- `Tapia`;
- `Rioseco`;
- `Santa Maria`;
- `Villapodambre`.

### Criterio

Para cada topónimo deberá registrarse:

- forma original;
- forma moderna;
- localización;
- unidades donde aparece;
- fuente de identificación;
- grado de seguridad cuando la equivalencia no sea completamente inequívoca.

### Precaución

Las identificaciones de linderos deben comprobarse con especial rigor, porque una equivalencia moderna incorrecta condicionaría posteriormente la reconstrucción territorial del Estudio Histórico.

---

## 5.2. Glosario

### `Ferrañales`

Revisar si puede enriquecerse la definición con la equivalencia regional documentada de terreno destinado a cereal segado o aprovechado en verde para forraje.

La definición deberá seguir ligada al tenor documental y evitar una explicación agronómica de conjunto.

### `pelo`

Revisar el significado histórico de `pelo`, especialmente dentro de la expresión regional `pelo y otoño`.

El objetivo es mejorar la definición del Glosario, no construir todavía una interpretación completa del sistema de aprovechamiento de los prados.

### `negrillos`

Revisar la actual cautela que evita su identificación botánica.

Si la fuente lexicográfica se confirma suficiente, incorporar:

```text
negrillos = olmos
```

con la correspondiente cita o referencia.

### `pan`

Evaluar la creación de una nueva entrada para el sentido histórico documentado en:

```text
resguardar el pan
```

donde `pan` designa cereal o mies y no el producto cocido.

### `entreparedes`

No se propone modificación sustantiva adicional salvo que una nueva fuente demuestre que puede precisarse su significado sin exceder el alcance del Glosario.

La distinción documental entre:

```text
entreparedes
```

y:

```text
entre paredes
```

debe conservarse.

---

## 5.3. Índice de medidas

Revisar:

- `legua`;
- `baras`.

No se propondrá ninguna equivalencia métrica automática.

### Requisito previo

Antes de convertir valores deberá encontrarse una fuente suficientemente específica para el patrón de medida aplicable al contexto geográfico y cronológico de la operación de 1752.

Si no puede demostrarse con seguridad, se mantendrá:

```text
equivalencia no fijada
```

La ausencia de una equivalencia es preferible a introducir una falsa precisión.

---

## Puerta de aprobación 3

Antes de publicar cambios de derivados se presentará una tabla con:

| Entrada | Estado actual | Fuente nueva | Cambio propuesto | Grado de seguridad |
|---|---|---|---|---|

Los cambios podrán aprobarse individualmente.

---

# 6. Fase 4 — Auditoría final de coherencia

Después de aplicar exclusivamente los cambios aprobados se realizará una auditoría final de solo lectura.

Deberá comprobarse:

1. que las transcripciones paleográficas ya validadas permanecen intactas;
2. que únicamente se han modificado las Notas históricas y derivados expresamente aprobados;
3. que no se ha introducido interpretación histórica de conjunto;
4. que el Estudio Histórico continúa sin activarse;
5. que no existe duplicación permanente innecesaria entre:
   - Notas históricas;
   - Glosario;
   - índices;
   - Diario Editorial;
6. que las referencias cruzadas siguen siendo coherentes;
7. que `last_validated_unit` y `last_closed_unit` no se han alterado como consecuencia de esta reparación retrospectiva, salvo que el procedimiento aprobado determine expresamente otra cosa;
8. que `current_unit` sigue siendo coherente con la secuencia posterior a `last_closed_unit`;
9. que el repositorio supera los controles técnicos;
10. que el PDF autoritativo sigue ausente del repositorio y sin modificación en Drive.

Solo después de esta auditoría se reanudará la edición ordinaria a partir del estado canónico posterior a `last_closed_unit`.

---

# 7. Información que debe reservarse para el futuro Estudio Histórico

No se incorporará a las Notas históricas de unidad la interpretación consolidada de:

- régimen señorial de Ordás;
- relaciones entre el territorio y la Casa de Luna;
- evolución completa del Concejo de Ordás hasta el municipio contemporáneo;
- reconstrucción territorial conjunta a partir de todos los linderos;
- estructura de propiedad y derechos;
- organización comunal de pastos, montes, eras y aprovechamientos;
- uso de madera para infraestructura;
- sistema agrario completo;
- rotaciones y clasificación de tierras;
- estructura social de peritos, oficiales de justicia y comparecientes;
- fiscalidad;
- interpretación climática o productiva del expediente;
- cualquier hipótesis que requiera relacionar múltiples unidades.

Todo ello deberá esperar al Estudio Histórico una vez habilitado y sustentarse exclusivamente en unidades validadas como base documental del expediente.

---

# 8. Secuencia recomendada de ejecución

El orden recomendado es:

## Paso 1

Aprobar y aplicar el refuerzo del procedimiento operativo.

## Paso 2

Preparar y aprobar las cuatro Notas históricas retrospectivas.

## Paso 3

Aplicar exclusivamente las Notas históricas aprobadas y sus cambios derivados directos.

## Paso 4

Revisar y aprobar las mejoras de grupo B en Glosario e índices.

## Paso 5

Aplicar los cambios B aprobados.

## Paso 6

Realizar la auditoría final de coherencia.

## Paso 7

Reanudar la edición ordinaria desde el estado canónico determinado por `last_closed_unit`.

---

# 9. Resultado esperado

Al finalizar el plan deberían cumplirse simultáneamente estas condiciones:

- el Manual Editorial permanece sin cambios salvo que aparezca una necesidad normativa real no detectada en la auditoría;
- el procedimiento de la skill obliga a evaluar explícitamente las Notas históricas;
- las unidades retrospectivamente afectadas contienen únicamente las Notas históricas C aprobadas;
- las demás unidades pueden mantener legítimamente `*(Sin notas históricas.)*` cuando la clasificación A/B/D así lo justifique;
- Glosario e índices contienen identificaciones y equivalencias mejor fundamentadas;
- no existe duplicación documental innecesaria;
- el Diario Editorial conserva solo lo que le corresponde;
- el Estudio Histórico permanece inactivo;
- la edición paleográfica validada no se altera;
- el proyecto puede continuar desde el estado gobernado por `last_closed_unit` sin reproducir el patrón de omisión detectado.

---

# 10. Regla de aprobación

Este plan es únicamente una propuesta de actuación.

Ninguna fase deberá ejecutarse automáticamente por la mera existencia de este documento.

Antes de cada bloque de escritura deberán presentarse para revisión:

- los cambios exactos;
- sus fuentes;
- los archivos afectados;
- el impacto esperado;
- cualquier duda metodológica nueva.

Si durante la ejecución aparece una situación no cubierta por el Manual o por este plan, deberá detenerse la operación y solicitar aprobación antes de publicar.
