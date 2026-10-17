# Checkpoint de reanudación hasta PKG-12

**Base registrada:** `feature/quarto-book@9d80c60bd338aae7d6bd966b55e36073717e11dc`
**Función:** congelar el orden de reanudación sin iniciar ninguna operación.

## Estado actual

- PKG-01–PKG-11 están completados según su estado vigente.
- `GATE-01 = PASS` y `GATE-02 = PASS`.
- La candidata 1.0 fue validada integralmente por PKG-11.
- HUM-01B está completado: prólogo definitivo y declaración sobre
  IA/herramientas cerrados.
- E1 — REV-LECTOR-01 está **COMPLETADA**.
- E2 — LINK-01 está **COMPLETADA**.
- E3 — REV-LECTOR-02 está **COMPLETADA** en rama aislada, pendiente de revisión
  e integración.
- La validación integral y los renders posteriores a HUM-01B están
  deliberadamente diferidos.
- PKG-12 **NO** se ha iniciado.

## Línea principal editorial congelada

### E1 — REV-LECTOR-01

**COMPLETADA.** Sus 23 hallazgos se aplicaron conjuntamente en E3.

Auditoría editorial orientada al lector, previa a cualquier corrección. Debe
cubrir:

- repetición excesiva del nombre del autor en Créditos;
- «dos operaciones» y su sustitución por una formulación más natural;
- versiones internas visibles de Edición Crítica, modernizada, Estudio y
  Registro;
- uso innecesario de «Quarto» en el discurso dirigido al lector;
- referencias públicas a `publication/content/`, `publication/generated/` y
  rastros técnicos similares;
- presentación adecuada de herramientas/IA;
- ubicación de «Correcciones y contacto»;
- referencia pública al repositorio.

### E2 — LINK-01

**COMPLETADA.** Sus correcciones localizadas se aplicaron conjuntamente en E3.

Auditoría de **todos** los enlaces externos e internos, bibliografía, anchors,
facsímil ↔ transcripción y matriz/retornos. Debe comprobar expresamente
`https://hdl.handle.net/10366/151409` y clasificar cada resultado como
`válido`, `redirigido`, `roto` o `no verificable automáticamente`.

### E3 — REV-LECTOR-02

**COMPLETADA EN RAMA AISLADA.** Resultado: `E3: APTO PARA REVISIÓN E
INTEGRACIÓN`.

Aplicación conjunta de las correcciones resultantes de E1 y E2. Debe incluir:

- sección pública «Correcciones y contacto»;
- `EMAIL DE CONTACTO — PLACEHOLDER PENDIENTE`;
- GitHub Issues como canal complementario;
- referencia al repositorio público si ya está preparado.

Puede usarse provisionalmente un placeholder para email o repositorio. No se
ejecutará todavía la validación integral mientras sigan abiertas observaciones.

### E4 — REV-FINAL-PREVIEW

Solo cuando estén cerradas **todas** las observaciones editoriales:

- ejecutar una vez la suite completa y los validadores integrales;
- realizar un render HTML completo y un render PDF completo;
- registrar los nuevos hashes;
- completar una revisión final representativa.

El resultado será el objeto que pase a PKG-12.

### E5 — PKG-12

Preview y aceptación humana. No se ejecutará antes de E4.

## Línea paralela — repositorio público

### R1 — AUD-REPO-01

**COMPLETADA.** Resultado:

`REPO NO APTO TODAVÍA PARA APERTURA PÚBLICA`

Bloqueantes actuales:

1. tratamiento de privacidad de terceros vivos en el prólogo;
2. estructura de licencias.

Otros asuntos: README raíz, NOTICE/atribuciones, correo de contacto, rutas
locales, metadatos de correo Git, ramas temporales, Actions, referencias al
repositorio privado y dependencia externa del manuscrito.

### R2 — Decisiones humanas de apertura

Antes de modificar, decidir el tratamiento de los nombres de terceros y las
licencias del contenido editorial, código, documentación y materiales de
terceros. El email permanece como placeholder.

### R3 — PUB-REPO-01

Preparación controlada del repositorio público. **No** cambia todavía su
visibilidad.

### R4 — AUD-REPO-02

Nueva auditoría de HEAD e historial. Debe resultar `APTO` antes de la apertura.

### R5 — Cambio de visibilidad

Operación explícita, separada y únicamente con autorización humana.

## Relación entre líneas

- La preparación del repositorio no sustituye ni reordena la línea editorial.
- E1 y E2 pueden ejecutarse aunque R2 o R3 sigan pendientes.
- E3 puede usar provisionalmente placeholders de email o repositorio.
- Antes de cerrar la versión destinada a publicación debe existir una URL
  pública válida del repositorio si el libro la presenta como pública.
- La apertura debe completarse antes del release si la edición final enlaza al
  repositorio.
- PKG-12 no debe convertirse en una auditoría del repositorio.

## Observaciones editoriales conocidas

1. Simplificar Créditos.
2. Cambiar «operaciones».
3. Revisar el enlace GREDOS/handle.
4. Revisar todos los enlaces.
5. Retirar versiones internas visibles innecesarias.
6. Retirar «Quarto» cuando sea jerga innecesaria.
7. Eliminar rutas internas del discurso dirigido al lector.
8. La declaración IA/herramientas ya fue revisada en HUM-01B.
9. Añadir un canal para reportar errores.
10. Añadir una referencia al repositorio público.
11. Mantener el email como placeholder hasta decisión humana.

Nuevas observaciones humanas pueden incorporarse antes de REV-FINAL-PREVIEW.

## Reanudación

- **Siguiente operación de la línea principal, tras revisar e integrar E3:**
  `E4 — REV-FINAL-PREVIEW`.
- **Siguiente operación posible de la línea paralela:**
  `R2 — DECISIONES HUMANAS DE PRIVACIDAD Y LICENCIAS`.

Ninguna de estas operaciones se inicia en este checkpoint.
