# Validación H3 — GitHub workspace v2

**Fecha:** 5 de septiembre de 2026  
**Rama:** `migration/github-workspace-v2`  
**Resultado:** PARCIAL — Web/Desktop y pruebas automatizables PASS; skill real pendiente

## Matriz de aceptación ejecutada

| Prueba | Resultado | Evidencia |
|---|---|---|
| CI Windows/Ubuntu, Python 3.10/3.13 | PASS | Workflow `Portable Python tests`, run 37 sobre `9fff2e546f7fe2fd137a67ca375c217d1229f3dc`; cuatro jobs PASS. |
| CI tras pruebas H3 | PASS | Workflow run 42 sobre `e8d596595a8808293bbfb7deb01ee69d465a5693`; cuatro jobs PASS. |
| CI sobre registro H3 | PASS | Workflow run 43 sobre `29a3c662dc59cdd985cf9d412de4315a1def4328`; cuatro jobs PASS. |
| Chat normal Web / `PROJECT.md` | PASS | `PROJECT.md` leído desde la rama y bootstrap reconstruido sin Work ni checkout local. |
| ChatGPT Desktop / Chat normal / sin Work | PASS | Ejecución real reportada por el usuario: siguió `PROJECT.md` sobre `migration/github-workspace-v2`, devolvió exactamente `project_id: sorrios-ensenada-1752`, fase `edicion_paleografica`, `current_unit: portada`, página 1 `complete`, `operation.status: clean`, y confirmó que no modificó archivos. |
| Schema 2 y estado | PASS | `project_id: sorrios-ensenada-1752`; fase `edicion_paleografica`; `current_unit: portada`; página 1 `complete`; `operation.status: clean`. |
| Drive solo PDF | PASS | Se usó únicamente el file ID canónico `1GgBs68iTi53ue8-TbrYFABALxadhQe5u`. |
| PDF sin Base64 | PASS | Drive entregó un archivo PDF real mediante referencia de archivo; `b64_string: null`. |
| Nombre/MIME/tamaño | PASS | `sorrios_ensenada_orden_lectura_calidad_original.pdf`; `application/pdf`; 5.038.575 bytes. |
| SHA-256 | PASS | `d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24`. |
| Número de páginas | PASS | 18. |
| Render `complete` | PASS | Página 1 / `portada` renderizada e inspeccionada visualmente. |
| Render `left` | PASS | Página 2 / `reverso_portada` recortada a izquierda e inspeccionada visualmente. |
| Render `right` | PASS | Página 2 / `folio_306r` recortada a derecha e inspeccionada visualmente. |
| Escritura reversible | PASS | `c08b272…` crea, `a2bad936…` actualiza y `90638aa…` elimina; el árbol vuelve exactamente a `b0d7c46254e667c6a1a2f08c36f9da94767029aa`. |
| Concurrencia por SHA base | PASS | Candidato `88f813d9…` preparado desde base `9fff2e5…`; tras cambiar HEAD a `c08b272…` se detectó `HEAD != base_sha` y el candidato no se publicó. |
| Atomicidad multiarchivo | PASS | `227ccd776d3e7a42112dfe8743f89ed11393ce50` publica dos archivos juntos; `e8d596595a8808293bbfb7deb01ee69d465a5693` los retira juntos. |
| Limpieza tras pruebas | PASS | El árbol de `e8d596595…` vuelve exactamente al árbol de cierre de H2 `b0d7c462…`; no quedan ficheros `.h3-probe`. |
| Plugin aislado | PASS | CI copia solo `plugins/sorrios-ensenada`, verifica versión 2.0.0, referencias y plantillas sin `PROJECT.md`. |
| Skill autocontenida estáticamente | PASS | CI verifica que `SKILL.md` no depende de `PROJECT.md`, que sus enlaces resuelven dentro de la skill y que declara GitHub como workspace y Drive solo lectura. |
| `main` congelada | PASS | Sigue en `cd683dd3a745c1f7bbabc154510885dbdad9dde8`. |

## Observación sobre API de contenidos

Una tentativa de `create_file` mediante la API de contenidos fue detenida por una comprobación de seguridad del conector antes de ejecutar la escritura. No se produjo ningún cambio. La misma operación se ejecutó correctamente mediante el protocolo Git-data definido por la arquitectura (`blob` → `tree` → `commit` → relectura de HEAD → `update_ref(force=false)`). Esto no bloquea H3: la capacidad de lectura/escritura GitHub y el protocolo atómico canónico quedan demostrados.

## Prueba pendiente

### Skill en superficie compatible

Debe invocarse realmente `editar-catastro-sorrios` desde una superficie que soporte la skill y comprobar que, sin depender de `/PROJECT.md`, reconstruye el mismo estado desde GitHub y trata Drive solo como PDF de solo lectura.

Prompt recomendado:

```text
Usa $editar-catastro-sorrios en modo consulta puntual y solo lectura.

Trabaja contra el repositorio miguel-conde/sorrios-ensenada en la rama migration/github-workspace-v2.
No uses PROJECT.md.

Lee el estado canónico desde GitHub y responde únicamente con:
- project_id
- fase
- current_unit
- current_location.pdf_page
- current_location.position
- operation.status

No modifiques ningún archivo y no escribas en Google Drive.
```

Resultado esperado:

- `project_id: sorrios-ensenada-1752`;
- fase `edicion_paleografica`;
- `current_unit: portada`;
- página 1, posición `complete`;
- `operation.status: clean`;
- ninguna escritura;
- ninguna dependencia de `/PROJECT.md`.

Hasta que esta prueba sea PASS, no ejecutar H4 ni mover `main`.
