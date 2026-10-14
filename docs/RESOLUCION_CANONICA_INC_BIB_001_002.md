# Resolución canónica de INC-BIB-001 e INC-BIB-002

## 1. Base

- Base exacta: `d4153c60489f4df24cdadf75d7740ec85b9406dd`.
- Rama aislada: `canonical/inc-bib-001-002-v1`, sin upstream.
- Fecha de resolución: 14 de octubre de 2026.
- Operación atómica de estudio histórico; no es PKG-08 ni una operación de
  publicación.

## 2. Autoridad

La Edición Crítica v3.6 sigue siendo la única autoridad sobre el expediente.
R21 y R29 no presentan errores de lectura y permanecen intactas. Las fuentes
externas solo pueden aportar contexto E delimitado; no respaldan artificialmente
los datos locales D.

| Archivo | Pasaje | ID | Nivel previo | Fuente previa | Cambio | Motivo |
|---|---|---|---|---|---|---|
| Registro v1.2 | paralelo de ordenanzas y vecera | `TRA-006` | E/I | BIB-012 / Cuadros de León | retirar fila | correspondencia exacta no verificada; R29 basta para el dato local |
| Estudio v1.2 §13 | paralelo taberna/carnicería/panadería/mesón | `TRA-006` | E/I | BIB-012 | retirar párrafo, URL y cita final | no es contexto autorizable |
| Glosario, `vecera` | confirmación por ordenanzas leonesas | `TRA-006` | E/I | BIB-012 | sustituir por apoyo local | el sentido local consta directamente en R29/`TRA-005` |
| Registro v1.2 | viudas como medio vecino en diversos lugares | `DEM-005` | E/I | BIB-015 | restringir | BIB-015 no contiene esa equivalencia |
| Estudio v1.2 §3 | práctica comparada sobre viudas | `DEM-005` | E/I | BIB-015 | separar D local y E general | evita atribuir a la bibliografía lo que solo documenta R21 |
| Glosario, `medio vecino` | práctica comparada sobre viudas | `DEM-005` | E/I | BIB-015 | limitar al expediente | no existe apoyo para la generalización comparada |
| Glosario, `hijo de familia` | organización doméstica | `DEM-005` | E/I | BIB-015 | conservar | la formulación reducida sigue respaldando este uso doméstico |

Las restantes apariciones auditadas en `project/` corresponden a datos locales
válidos, cálculos intactos, registros/diagnósticos históricos o planes de
publicación anteriores. No constituyen afirmaciones nuevas autorizadas por el
Registro v1.3.

## 3. INC-BIB-001

### problema

`TRA-006` atribuía a unas ordenanzas concejiles leonesas una formulación amplia
sobre servicios por vecera. BIB-012 no permite comprobar con seguridad la
correspondencia exacta, la autoría ni la fecha.

### dato D preservado

R29 y `TRA-005` conservan sin cambios el dato local: la taberna carece de
arrendatario, funciona por vecera entre los vecinos y no rinde utilidad al común
ni a particular.

### E/I retirado o restringido

Se retira por completo el paralelo externo. No se busca una fuente sustitutiva,
no se amplía el mecanismo a otros servicios y no se debilita el dato local.

### Registro

La fila `TRA-006` se elimina sin renumerar ningún ID. Esta es la convención más
limpia disponible: el Registro solo define `Admitida`, `Condicionada` y
`Excluida`, y no existe una categoría establecida de afirmación retirada.

### Estudio

Se conserva el párrafo sustentado por R29/`TRA-005`. Se eliminan el párrafo de
ordenanzas, la URL de Cuadros de León y `TRA-006`/`vecera` de la síntesis de
contextos regionales externos.

### Glosario

La definición de `vecera` permanece. Su contexto se apoya únicamente en R29 y
`TRA-005`, con el límite de no generalizar el turno a otras actividades.

### resultado

`INC-BIB-001: CERRADA EN CAPA CANÓNICA`

## 4. INC-BIB-002

### problema

La formulación compuesta de `DEM-005` atribuía a BIB-015 que en diversos lugares
las viudas podían computarse como medio vecino. La verificación de PKG-02 mostró
que la obra no contiene esa equivalencia.

### dato D preservado

R21 y `DEM-001` conservan íntegramente el dato local: 18 vecinos, 8 medios
vecinos —incluidas dos viudas— y 8 residentes no considerados vecinos.

### DEM-005 antes/después

**Antes:** «Los libros personales del Catastro se articulaban en torno a cabezas
de casa y familias, con cónyuges, hijos, criados y otros convivientes; en
diversos lugares las viudas podían computarse como medio vecino».

**Después:** «Los libros personales del Catastro se articulaban en torno a
cabezas de casa o familias y registraban cónyuges, hijos, criados y otros
convivientes; las viudas con casa abierta podían figurar como cabezas de casa».

La cautela prohíbe expresamente usar BIB-015 como soporte de `medio vecino`, de
una equivalencia viuda → medio vecino, de coeficientes vecinos → habitantes, de
equivalencias de hogar o de reglas generales aplicables a Sorribos.

### Registro

`DEM-005` mantiene nivel E/I, usa la edición institucional ya verificada de
BIB-015 y queda limitado a la organización general de los libros personales.

### Estudio

El párrafo local de R21 permanece. A continuación se separan expresamente el
dato D local, el contexto E general y los límites I/L que impiden equivalencias
demográficas.

### Glosario

`medio vecino` conserva su definición local y declara que las dos viudas son un
dato exclusivo de este expediente, no una regla comparada. `hijo de familia`
mantiene su referencia a `DEM-005`, pues el contexto doméstico continúa
legítimamente respaldado.

### resultado

`INC-BIB-002: CERRADA EN CAPA CANÓNICA`

## 5. Auditoría de propagaciones

`publication/` no se modifica en esta operación. Siguen reflejando el estado
anterior:

- capítulo 6, `06-vecinos-hogares-viviendas-trabajo.qmd`: prosa que atribuye a
  distintos lugares el cómputo de viudas como medios vecinos y metadato E de
  `DEM-005`;
- capítulo 11, `11-hacienda-concejil-servicios-colectivos.qmd`: localizadores,
  metadatos y párrafo externo de `TRA-006`;
- capítulo 13,
  `13-economia-rural-integrada-vulnerabilidades-resiliencia-limites.qmd`:
  metadatos, síntesis regional y cita de `TRA-006`;
- `generated/glosario.qmd`: vista todavía derivada del Glosario previo;
- `generated/matriz-evidencia.qmd`: formulaciones previas completas de
  `DEM-005` y `TRA-006`;
- `scripts/validate_publication.py`: conjuntos E y expectativas que todavía
  exigen `TRA-006` y el estado previo del capítulo 6;
- `references.bib`: solo contiene el marcador de bibliografía futura; aún no
  incorpora ni resuelve BIB-012/BIB-015.

Las copias generadas de la transcripción y la edición modernizada conservan
correctamente los datos locales y no requieren corrección histórica; solo
deberán regenerarse cuando PKG-08 sincronice procedencia y derivados.

## 6. Trabajo pendiente para PKG-08

### INC-BIB-001

- corregir los capítulos 11 y 13;
- regenerar la matriz de evidencia y el glosario si su derivación lo requiere;
- retirar las citas próximas y metadatos de `TRA-006`;
- revisar las expectativas del validador de publicación;
- decidir el tratamiento bibliográfico final de BIB-012, sin uso histórico
  sustantivo salvo dato residual legítimo.

### INC-BIB-002

- corregir el capítulo 6 con separación D/E/I/L;
- regenerar el glosario y la matriz de evidencia;
- actualizar citas próximas y metadatos de `DEM-005`;
- incorporar a la bibliografía la ficha correcta de BIB-015 y su edición
  institucional, con alcance restringido;
- sincronizar procedencia, hashes y derivados solo dentro de PKG-08.

## 7. Validación

- Validador canónico 2.0.2: PASS.
- Pruebas focalizadas de la capa canónica: PASS (32 pruebas).
- Identificadores definidos y referencias del Estudio: PASS.
- Estructura de tablas Markdown y sintaxis documental: PASS.
- Auditoría posterior de residuos: PASS con supervivencias clasificadas como
  historial diagnóstico o propagación editorial pendiente.
- R21, R29, `DEM-001`, `TRA-005`, `DEM-002`, cantidades, cálculos y lineación:
  preservados.
- `publication/`: sin cambios.
- `operation.status`: `clean`.

La suite general obtiene 585 pruebas superadas, nueve fallos y 36 errores, todos
limitados a `publication/` desincronizada por diseño:

- `apparatus_sources.py` exige aún el Registro 1.2 y rechaza la versión 1.3;
- `publication.yml` conserva el blob anterior del Glosario, lo que bloquea las
  pruebas de generación de aparatos y las comprobaciones PKG-05 asociadas;
- los capítulos 11 y 13 todavía declaran `TRA-006`, ya retirado del Registro
  vigente;
- la candidata conserva el snapshot exacto del árbol canónico anterior.

No existe un fallo adicional de contenido o controles canónicos. Resolver esos
contratos, regenerar aparatos y sincronizar procedencia pertenece a PKG-08.

## 8. Cierre

- `INC-BIB-001: CERRADA EN CAPA CANÓNICA`
- `INC-BIB-002: CERRADA EN CAPA CANÓNICA`
- `PROPAGACIÓN EDITORIAL PENDIENTE DE PKG-08`

La corrección queda preparada para revisión independiente antes de su
integración y antes de cualquier evaluación formal de GATE-01.
