# PKG-00 — Inventario y cuestionario de inputs editoriales

## 1. Baseline e integridad

- Rama: `feature/quarto-book`.
- HEAD: `c4bafd6e195c395f6b56189f90ac311445282733`.
- Upstream actual: `origin/feature/quarto-book` en el mismo commit.
- Ahead/behind actual: `0/0`. El upstream ha incorporado el commit que anteriormente estaba solo en local; no existe divergencia.
- `main`: `e81dc9239ac8dbabfe77168a50ef98c4d3b79170`.
- `origin/main`: `e81dc9239ac8dbabfe77168a50ef98c4d3b79170`.
- Árbol de trabajo: limpio.
- `project/`: intacto.
- PDFs versionados: ninguno.
- Candidata: 334 páginas, 73.994.496 bytes, SHA-256 `f1eee2f465f554d3bf2b506d23a622967d1b4f1013ac657a774868e525688183`; intacta.
- No se creó ni modificó ningún archivo. No hubo render, investigación externa, commit, push, tag ni release.

La skill del Catastro se aplicó en modo consulta/auditoría: se respetó la jerarquía de autoridades y la prohibición de escritura.

## 2. Resumen de lo ya documentado

| Elemento | Situación documental |
|---|---|
| Título de trabajo del libro | **Sorribos y Santibáñez de Ordás en 1752** |
| Subtítulo aprobado para desarrollar | **Estudio histórico y edición integral del Catastro de Ensenada** |
| Identidad general existente | **Sorríos — Catastro de Ensenada** |
| Autor personal | No consta |
| Roles asignados a personas | No constan |
| Transcripción y modernización | Obras y versiones perfectamente identificadas; responsables nominales pendientes |
| Colaboradores | No hay colaboradores contemporáneos explícitamente acreditados |
| Créditos | Aprobado el modelo basado en roles esenciales; faltan nombres y asignaciones |
| Copyright | Titular pendiente |
| Licencia | Pendiente |
| Fecha final | Pendiente |
| URL canónica pública | No existe |
| Prólogo | Personal, firmado, 900–1.500 palabras y situado después de créditos |
| Herramientas | Uso técnico de ChatGPT, Copilot, Codex, Quarto, Python, Git, LaTeX, Poppler y otras herramientas documentado; no son autores |

La composición 0.6 llevaba como autor PDF «Proyecto Sorríos - Catastro de Ensenada», pero la auditoría ya advierte que era una atribución colectiva de proyecto, no una autoría personal aprobada. La candidata Quarto tiene vacío el campo `Author` ([informe comparativo](INFORME_COMPARATIVO_PDF_0_6_Y_QUARTO.md)).

## 3. DAT-001 — autor

### Evidencia encontrada

No existe una propuesta explícita de nombre personal para el autor del libro.

- La candidata carece de campo de autor.
- `miguel-conde` es el propietario técnico del repositorio; constituye un indicio, no una atribución editorial.
- La autoría de commits tampoco prueba autoría intelectual.
- «Proyecto Sorríos - Catastro de Ensenada», usado en 0.6, identifica colectivamente el proyecto, no una persona.
- Los documentos de cierre declaran expresamente pendiente el nombre del autor ([alcance aprobado](ALCANCE_APROBADO_V1_0.md)).

### Decisión necesaria

El usuario debe indicar:

- nombre exacto para portada, créditos, metadatos y cita;
- forma abreviada, si desea otra para citas;
- inclusión o no del segundo apellido;
- ORCID, solo si desea mostrarlo;
- afiliación, solo si desea mostrarla.

### Recomendación

Usar una única firma pública coherente en portada, metadatos, créditos, colofón y modelos de cita. No añadir ORCID o afiliación si no aportan valor real a esta edición.

## 4. DAT-002 — roles editoriales

Están claramente documentadas como funciones del proyecto, pero no asignadas nominalmente:

- elaboración del estudio histórico;
- investigación histórica y documental;
- edición crítica y aparato;
- transcripción paleográfica;
- modernización para lectura;
- análisis cuantitativo y Registro D/C/I/E/L;
- diseño metodológico;
- coordinación de las capas del volumen;
- composición digital Quarto.

Son plausibles, pero requieren decisión humana, los títulos de:

- autor del volumen;
- autor del estudio histórico;
- director del proyecto;
- editor científico;
- editor crítico/documental;
- coordinador editorial;
- responsable de investigación histórica;
- responsable del análisis cuantitativo;
- responsable del diseño metodológico;
- responsable de la composición digital.

Recomendación: evitar acumular todos esos títulos. Una fórmula contenida podría combinar «autoría del volumen y del estudio histórico», «dirección editorial» y «edición crítica», dejando transcripción y modernización en créditos separados.

## 5. DAT-003 — transcripción

Lo documentado es:

- La [Edición Crítica 3.6](../project/20_TRABAJO_EDITORIAL/Edicion_Critica.md) contiene una transcripción paleográfica semidiplomática completa de 35 unidades.
- Las operaciones registran lectura visual, ampliación y validación paleográfica; con frecuencia declaran expresamente que no se utilizó OCR.
- El capítulo Quarto se genera automáticamente desde la Edición Crítica. Esa generación es una transformación técnica, no la creación intelectual de la transcripción.
- La transcripción está validada, pero no consta el nombre de su responsable ni de un revisor humano individual.
- Se documenta uso general de herramientas de IA en el proyecto, pero no una atribución específica y exhaustiva de qué pasajes transcribió o revisó cada herramienta.

Pendiente: determinar quién asume la responsabilidad intelectual y si deben separarse «transcripción», «revisión paleográfica» y «asistencia técnica».

Recomendación: acreditar a una persona como responsable solo si puede asumir la lectura y validación final; mencionar la ayuda digital por separado en el colofón.

## 6. DAT-004 — modernización

Lo documentado es:

- Existe una [edición modernizada 1.3](../project/30_RESULTADOS/EDICION_DIVULGATIVA/Catastro_Sorrios_1752_Version_Modernizada.md), íntegra y con cuarenta respuestas.
- Declara su naturaleza, fuente textual y criterios generales.
- Lleva la fecha interna «19 de septiembre de 2026», que corresponde a ese producto canónico, no a la fecha final del libro 1.0.
- Su traslado a Quarto se ejecuta mediante un generador determinista; el programa no es responsable intelectual de las decisiones de modernización.
- No consta quién debe figurar nominalmente como responsable, editor o revisor.

Recomendación: usar una fórmula única —«Edición modernizada y revisión»— si la misma persona tomó y validó las decisiones; separar responsabilidades si participaron varias.

## 7. DAT-005 — colaboradores

No se ha localizado ningún colaborador contemporáneo explícitamente identificado como tal.

- **Colaboradores humanos potenciales:** ninguno documentado nominalmente.
- **Instituciones/apoyos:** GitHub y Google Drive son infraestructura; archivos, bibliotecas, PARES y organismos citados son fuentes. No son colaboradores o patrocinadores por defecto.
- **Herramientas/software:** ChatGPT, Copilot, Codex, Quarto, Python, Git, Pandoc, LuaTeX, Poppler, Pillow y Chrome aparecen en el historial técnico. No son colaboradores ni autores.

Los declarantes de 1752, personajes históricos y autores de bibliografía tampoco son colaboradores del libro.

Recomendación: acreditar solo personas con una contribución concreta verificable. Usar «Créditos» para responsabilidades sustantivas y «Agradecimientos» para ayuda, acceso, orientación o apoyo informal.

## 8. DAT-006 — identidad del proyecto

Denominaciones diferenciadas:

| Ámbito | Denominación documentada |
|---|---|
| Repositorio | `miguel-conde/sorrios-ensenada` |
| Proyecto general | `Sorríos — Catastro de Ensenada` |
| ID técnico | `sorrios-ensenada-1752` |
| Plugin | `sorrios-ensenada` |
| Skill | `editar-catastro-sorrios` |
| Expediente | `Catastro de Ensenada de Sorribos y Santibáñez de Ordás` |
| Libro | `Sorribos y Santibáñez de Ordás en 1752` |
| Subtítulo | `Estudio histórico y edición integral del Catastro de Ensenada` |

`Sorribos` es la forma histórica de 1752; `Sorrios` es la forma actual. «Sorríos» se usa como identidad gráfica del proyecto, no como transcripción documental.

Formulaciones posibles:

1. **Recomendada:** título y subtítulo aprobados, con una línea secundaria «Proyecto Sorríos — Catastro de Ensenada».
2. Título y subtítulo sin identidad superior de proyecto; en créditos, «Edición digital del Catastro de Ensenada de Sorribos y Santibáñez de Ordás».
3. «Sorríos — Catastro de Ensenada» como cabecera de colección/proyecto y debajo el título del libro.

Ninguna fórmula implica sello editorial, empresa o titularidad jurídica.

## 9. DAT-007 — copyright

Requieren tratamiento separado:

| Componente | Situación |
|---|---|
| Estudio, introducciones y texto editorial nuevo | Titular no documentado |
| Edición crítica y aparato | Responsable y titular no documentados |
| Transcripción paleográfica | Responsable y titular no documentados |
| Edición modernizada | Responsable y titular no documentados |
| Selección y composición del volumen | Titular no documentado |
| Texto manuscrito de 1752 | Naturaleza histórica distinta; no confundir con derechos sobre su reproducción |
| Imágenes/facsímil | No consta autorización o régimen de reproducción pública |
| Cartografía futura | Fuentes todavía no seleccionadas |
| Citas, imágenes y fuentes externas | Conservan sus propios derechos y condiciones |

La decisión pedida ahora es únicamente quién debe figurar como titular del copyright del contenido original de la edición, sujeto a los derechos aplicables a materiales externos.

## 10. DAT-008 — licencia

- **L1 — Todos los derechos reservados.** No concede un permiso general de reutilización más allá de los límites legales o permisos particulares. Ofrece máximo control, pero dificulta redistribución, adaptación y reutilización académica.

- **L2 — CC BY 4.0.** Permite copiar, redistribuir y adaptar, incluso comercialmente, exigiendo atribución, enlace a la licencia e indicación de cambios. Es la opción más abierta y sencilla para difusión y reutilización.

- **L3 — CC BY-SA 4.0.** Ofrece permisos semejantes a CC BY, pero obliga a publicar las adaptaciones bajo la misma licencia. Favorece que las obras derivadas permanezcan abiertas, aunque reduce compatibilidad con otros proyectos.

- **L4 — CC BY-NC 4.0.** Permite reutilización y adaptación no comercial con atribución. Restringe explotación comercial, pero la frontera de «uso comercial» puede generar dudas prácticas.

- **L5 — Otra.** Permite adoptar otra licencia o una formulación propia, pero exige comprobar compatibilidad, claridad y alcance. No conviene redactar condiciones improvisadas sin revisión adecuada.

Recomendación editorial: si se desea máxima difusión y el titular controla los derechos, valorar L2 con una nota que limite expresamente su alcance al contenido original. Si los derechos no están suficientemente aclarados, mantener L1 provisionalmente.

Ninguna de estas elecciones relicencia automáticamente facsímiles, cartografía, imágenes o materiales externos. Será necesaria una nota de derechos por componentes.

## 11. DAT-009 — fecha editorial

Existen varias fechas de trabajo —19 de septiembre para la modernización, 9 de octubre para la candidata y 10 de octubre para el cierre del alcance—, pero ninguna es la fecha de publicación de la edición 1.0.

Modelos posibles:

- año solamente;
- mes y año;
- fecha completa.

Recomendación: mostrar el **año efectivo de publicación** en portada legal y modelos de cita; conservar la fecha completa de liberación en metadatos técnicos y colofón. No se fija ahora ningún valor.

## 12. DAT-010 — URL canónica

No existe una URL pública/canónica aprobada:

- el repositorio privado no es la URL del libro;
- el preview local `127.0.0.1` fue temporal;
- no existe configuración de Netlify, GitHub Pages u otro proveedor;
- Netlify es una preferencia de planificación, no una decisión de publicación.

Estado: **PENDIENTE HASTA PKG-12/13**. No debe inventarse dominio ni reutilizarse una URL de trabajo.

## 13. DAT-AI-01 — herramientas digitales/IA

Está documentado el uso operativo de ChatGPT Web/Desktop, Copilot, Codex CLI y la skill del proyecto. También está ampliamente documentada la cadena Quarto/Python/Pandoc/LaTeX/Poppler.

No está documentado con precisión suficiente:

- qué herramienta intervino en cada texto;
- qué proporción de redacción, transcripción o revisión corresponde a cada una;
- una política pública ya aprobada sobre IA.

Las herramientas no son autoras. La responsabilidad humana final debe quedar separada de automatización, generación técnica y asistencia digital.

Opciones:

- **A.** Declararlas en el colofón o metodología de producción.
- **B.** Enumerarlas en créditos técnicos.
- **C.** Declarar asistencia digital sin marcas o productos concretos.
- **D.** Otra formulación aprobada por el usuario.

Recomendación: A, porque DEC-008 ya reserva las herramientas para el colofón y mantiene limpios los créditos intelectuales.

## 14. Prólogo — guion para el usuario

1. **Origen del proyecto:** cómo apareció el documento y cuándo surgió la idea de editarlo.
2. **Relación personal:** vínculo con Sorrios/Sorribos, Santibáñez, Ordás, el manuscrito o las personas relacionadas.
3. **Motivación:** por qué merecía una edición integral y qué se quería poner al alcance del lector.
4. **Evolución:** del primer contacto con el documento a la transcripción, el estudio y el libro actual.
5. **Personas y apoyos:** contribuciones, conversaciones, ayuda familiar, local, académica o técnica.
6. **Invitación al lector:** cómo espera el autor que se lea, consulte o continúe este trabajo.

**NO meter en el prólogo:**

- historia general del Catastro de Ensenada;
- metodología paleográfica detallada;
- arquitectura técnica del repositorio;
- bibliografía o discusión historiográfica extensa;
- explicación detallada de D/C/I/E/L;
- changelog, versiones, pruebas o herramientas.

## 15. Asuntos LEGAL-PENDIENTE

- Régimen de reproducción y redistribución pública del facsímil.
- Condiciones aplicables a las reproducciones digitales del manuscrito.
- Compatibilidad entre la futura licencia del contenido original y materiales externos.
- Derechos, licencia y atribución de cada futura base cartográfica.
- Alcance de cualquier imagen externa que se incorpore a cubierta o interiores.
- Redacción final de la nota de derechos por componentes.

Estos asuntos no bloquean el inventario, pero sí pueden condicionar la candidata final.

## 16. Estado de preparación de PKG-01–PKG-05

| Paquete | Estado | Motivo |
|---|---|---|
| PKG-01 — Glosario canónico | **READY** | No depende de DAT-001–010. Requiere una operación canónica separada, la skill y su propio commit. |
| PKG-02 — Verificación bibliográfica | **READY** | Puede comenzar independientemente de los datos personales. Las fórmulas finales de cita sí esperarán autor, fecha y URL. |
| PKG-03 — Cartografía | **READY CON DEPENDENCIA** | Puede iniciar selección y elaboración, pero la aceptación exige licencias, atribuciones y derechos de redistribución comprobados. |
| PKG-04 — Prototipo F3 | **READY** | No necesita autoría, copyright, licencia general ni prólogo. Su adopción final exige decisión humana en GATE-01. |
| PKG-05 — Correcciones técnicas | **READY CON DEPENDENCIA** | Puede empezar sin DAT. El cierre de REV-024 deberá validarse con el resultado de PKG-01, y la medición de peso debe coordinarse con F3. |

Ningún paquete está bloqueado por los DAT de PKG-00.

## 17. Cuestionario final del usuario

### 1. DAT-001

- **Pregunta:** ¿Qué firma exacta debe aparecer como autor? Indica nombre completo, forma corta, uso del segundo apellido, ORCID opcional y afiliación opcional.
- **Recomendación:** una sola forma pública coherente; ORCID y afiliación solo si se desean realmente.
- **Respuesta del usuario:** `PENDIENTE`

### 2. DAT-002

- **Pregunta:** ¿Qué roles personales quieres declarar?
- **Opciones:**  
  R1 — autoría del volumen y estudio + dirección editorial + edición crítica;  
  R2 — desglose amplio: investigación, análisis, método, coordinación y composición;  
  R3 — formulación propia.
- **Recomendación:** R1, ajustándolo a las responsabilidades reales y dejando DAT-003/004 separados.
- **Respuesta del usuario:** `PENDIENTE`

### 3. DAT-003

- **Pregunta:** ¿Cómo debe acreditarse la transcripción paleográfica?
- **Opciones:**  
  T1 — «Transcripción paleográfica y revisión: [nombre]»;  
  T2 — separar transcripción y revisión entre personas;  
  T3 — dirección/revisión humana más asistencia técnica declarada.
- **Recomendación:** T1 si una sola persona asume la responsabilidad final; en caso contrario, T2.
- **Respuesta del usuario:** `PENDIENTE`

### 4. DAT-004

- **Pregunta:** ¿Quién debe figurar como responsable de la edición modernizada?
- **Opciones:**  
  M1 — «Edición modernizada y revisión: [nombre]»;  
  M2 — separar edición y revisión;  
  M3 — otra formulación.
- **Recomendación:** M1 si las decisiones y su validación pertenecen a la misma persona.
- **Respuesta del usuario:** `PENDIENTE`

### 5. DAT-005

- **Pregunta:** ¿Hay personas que deban acreditarse? Para cada una, indica nombre, contribución y destino: `CRÉDITOS` o `AGRADECIMIENTOS`. Puede responderse `NINGUNO`.
- **Recomendación:** reservar créditos para contribuciones sustantivas y agradecimientos para apoyos puntuales.
- **Respuesta del usuario:** `PENDIENTE`

### 6. DAT-006

- **Pregunta:** ¿Qué identidad visible debe acompañar al título?
- **Opciones:** I1 — «Proyecto Sorríos — Catastro de Ensenada» como línea secundaria; I2 — solo título/subtítulo; I3 — proyecto como cabecera de colección.
- **Recomendación:** I1.
- **Respuesta del usuario:** `PENDIENTE`

### 7. DAT-007

- **Pregunta:** ¿Quién debe figurar como titular del copyright del contenido original de esta edición?
- **Opciones:** persona autora; varias personas; entidad; otra fórmula expresamente indicada.
- **Recomendación:** usar el titular real del contenido original sin extender la declaración a materiales externos.
- **Respuesta del usuario:** `PENDIENTE`

### 8. DAT-008

- **Pregunta:** ¿Qué licencia debe aplicarse al contenido original?
- **Opciones:** L1, L2, L3, L4 o L5 según la comparación anterior.
- **Recomendación:** L2 — CC BY 4.0, si se desea difusión abierta y el titular controla los derechos; de lo contrario, L1 hasta aclararlos.
- **Respuesta del usuario:** `PENDIENTE`

### 9. DAT-009

- **Pregunta:** ¿Qué modelo de fecha editorial prefieres?
- **Opciones:** F1 — año; F2 — mes/año; F3 — fecha completa.
- **Recomendación:** F1 para la mención editorial visible, conservando fecha completa en metadatos y colofón.
- **Respuesta del usuario:** `PENDIENTE`

### 10. DAT-010

- **Pregunta:** ¿Existe ya una URL pública que quieras declarar como canónica?
- **Opciones:** U1 — no; aplazar hasta PKG-12/13. U2 — sí; proporcionar la URL exacta.
- **Recomendación:** U1.
- **Respuesta del usuario:** `PENDIENTE`

### 11. DAT-AI-01

- **Pregunta:** ¿Cómo debe declararse el uso de herramientas digitales/IA?
- **Opciones:** A — colofón/metodología de producción; B — créditos técnicos; C — declaración genérica; D — otra fórmula.
- **Recomendación:** A.
- **Respuesta del usuario:** `PENDIENTE`

### 12. PROLOGO-01

- **Pregunta:** ¿Proporcionarás un borrador completo de 900–1.500 palabras o primero respuestas breves a los seis apartados del guion?
- **Opciones:** P1 — borrador completo; P2 — seis respuestas preparatorias.
- **Recomendación:** P1 para conservar plenamente tu voz personal.
- **Respuesta del usuario:** `PENDIENTE`
