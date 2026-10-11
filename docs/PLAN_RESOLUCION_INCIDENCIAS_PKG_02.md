# Plan de resolución de incidencias PKG-02

## 1. Alcance

Este plan define las operaciones necesarias para cerrar `INC-BIB-001` e
`INC-BIB-002`. No ejecuta correcciones, no modifica fuentes canónicas o la
publicación y no autoriza investigación histórica ni sustitución de fuentes.

Ambas incidencias deben cerrarse antes de GATE-01. Pueden prepararse después de
PKG-03 porque no afectan a la cartografía y no ponen en duda los datos locales
de R21 o R29.

## 2. INC-BIB-001

### Evidencia

- R29, folio 319v: la taberna carece de arrendatario, «anda por vecera entre
  los vecinos» y no produce utilidad al común ni a particular.
- `TRA-005`: D, sustentado directamente por R29.
- `TRA-006`: E/I, paralelo atribuido a ordenanzas concejiles leonesas.
- BIB-012: URL no disponible; metadatos y correspondencia exacta no
  verificables; soporte S3.

### Diagnóstico

**BIB-A**, severidad **MEDIA**, bloqueo de 1.0 **CONDICIONAL**. El dato local
está sustentado; el problema reside en la amplitud del paralelo externo y en su
atribución bibliográfica.

### Operación canónica previa

Paquete apropiado: operación canónica independiente posterior a PKG-03 y
anterior a GATE-01/PKG-08, ejecutada con la skill local del Catastro.

Archivos que podrían requerir cambio, tras fijar el alcance exacto de la
operación:

- `project/30_RESULTADOS/ESTUDIO_HISTORICO/Registro_Afirmaciones_Calculos_v1.md`;
- `project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md`;
- `project/20_TRABAJO_EDITORIAL/Glosario.md`;
- controles y registro de operación canónica exigidos por el proyecto.

Autoridad: Edición Crítica/R29 para D; Registro para la clasificación y el uso
E/I. No requiere investigación externa para separar el dato local del paralelo.
No se buscará una fuente sustitutiva sin autorización expresa.

Decisión que deberá adoptar la operación: restringir `TRA-006` a lo realmente
verificado o retirar el paralelo E/I, manteniendo intactos R29 y `TRA-005`.

### Propagación posterior

Después del cierre canónico, PKG-08 deberá actualizar exclusivamente las
propagaciones afectadas, en particular el capítulo 11, el capítulo 13, la
matriz, las citas próximas y la bibliografía. BIB-012 solo se incorporará si su
uso final coincide con contenido verificable.

### Criterio de cierre

- R29 y `TRA-005` permanecen como autoridad del funcionamiento local.
- Ninguna formulación E/I afirma más de lo que acredita la fuente vinculada.
- Registro, Estudio y Glosario distinguen inequívocamente D de E/I.
- Las propagaciones editoriales y la referencia bibliográfica coinciden con la
  decisión canónica.
- La incidencia consta como cerrada antes de GATE-01.

## 3. INC-BIB-002

### Evidencia

- R21, folio 318r: ocho medios vecinos, «inclusas dos biudas».
- `DEM-001`: D, dato local sustentado por R21.
- BIB-015: sustenta libros de cabezas de casa/familias, composición de la
  familia y viudas con casa abierta como cabezas de casa; no contiene `medio
  vecino`.
- `DEM-005`: E/I, formulación compuesta que añade que en diversos lugares las
  viudas podían computarse como medio vecino; soporte S4 parcial.

### Diagnóstico

**MIX-B**, severidad **MEDIA**, bloqueo de 1.0 **CONDICIONAL**. Hay un dato
documental local válido y un contexto externo válido, pero la generalización
comparativa que los enlaza no está respaldada por BIB-015.

### Operación canónica previa

Paquete apropiado: operación canónica independiente posterior a PKG-03 y
anterior a GATE-01/PKG-08, ejecutada con la skill local del Catastro.

Archivos que podrían requerir cambio, tras fijar el alcance exacto de la
operación:

- `project/30_RESULTADOS/ESTUDIO_HISTORICO/Registro_Afirmaciones_Calculos_v1.md`;
- `project/30_RESULTADOS/ESTUDIO_HISTORICO/Estudio_Historico.md`;
- `project/20_TRABAJO_EDITORIAL/Glosario.md`;
- controles y registro de operación canónica exigidos por el proyecto.

Autoridad: Edición Crítica/R21 y `DEM-001` para D; BIB-015 solo para el contexto
general que contiene. No requiere nueva investigación externa para separar los
niveles y no autoriza una fuente sustitutiva.

Decisión que deberá adoptar la operación: conservar el dato local de las dos
viudas en D; limitar `DEM-005` al contexto demostrado por BIB-015; eliminar o
modular la generalización comparativa no sustentada.

### Propagación posterior

Después del cierre canónico, PKG-08 deberá propagar la separación al capítulo
6, al Glosario generado, a la matriz, a las citas próximas y a la bibliografía.
BIB-015 no podrá citarse como soporte de `medio vecino`.

### Criterio de cierre

- R21 y `DEM-001` conservan el dato local sin convertirlo en regla general.
- `DEM-005` contiene solo contexto efectivamente respaldado por BIB-015.
- Registro, Estudio y Glosario separan D de E/I.
- El capítulo 6 y la cita de BIB-015 no atribuyen a Camarero el cómputo de
  viudas como medio vecino.
- La incidencia consta como cerrada antes de GATE-01.

## 4. Secuencia y límites

1. Completar PKG-03 como pretrabajo independiente.
2. Abrir una operación canónica atómica para las dos incidencias, con base SHA
   y rutas permitidas explícitas.
3. Validar Registro, Estudio, Glosario y controles sin modificar
   `publication/`.
4. Revisar conjuntamente el resultado antes de GATE-01.
5. Propagarlo en PKG-08 mediante `references.bib`, bibliografía, citas próximas
   y enlaces E ↔ matriz.

No se añaden registros al placeholder preexistente `references.bib`, no se
corrigen ahora las entradas canónicas, no se regenera Quarto y no se abre una
investigación externa dirigida.
