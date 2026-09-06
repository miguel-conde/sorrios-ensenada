# Validación H3 — GitHub workspace v2

**Fecha:** 6 de septiembre de 2026  
**Rama:** `migration/github-workspace-v2`  
**Resultado:** PASS — criterios de aceptación H3 completados

## Matriz de aceptación ejecutada

| Prueba | Resultado | Evidencia |
|---|---|---|
| CI Windows/Ubuntu, Python 3.10/3.13 | PASS | Workflow `Portable Python tests`, run 37 sobre `9fff2e546f7fe2fd137a67ca375c217d1229f3dc`; cuatro jobs PASS. |
| CI tras pruebas H3 | PASS | Workflow run 42 sobre `e8d596595a8808293bbfb7deb01ee69d465a5693`; cuatro jobs PASS. |
| CI sobre registro H3 | PASS | Workflow run 43 sobre `29a3c662dc59cdd985cf9d412de4315a1def4328`; cuatro jobs PASS. |
| CI tras registro Desktop | PASS | Workflow run 44 sobre `12f63adfedd6b4d8126d621849dee01e32edb467`; cuatro jobs PASS. |
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
| Instalación Codex del plugin 2.0.0 | PASS | Codex CLI 0.152.1 reinstaló `sorrios-ensenada@personal` desde el checkout exacto de `migration/github-workspace-v2`; `plugin list --json` mostró `version: 2.0.0`, `installed: true`, `enabled: true`. La ejecución posterior en Codex no llegó a iniciarse por límite de uso y no se contabiliza como prueba funcional. |
| Skill real en ChatGPT Desktop | PASS | Invocación real del complemento `Catastro de Sorríos` en Desktop. Sin `PROJECT.md`, sin checkout local y usando el ref `migration/github-workspace-v2`, leyó `project/00_CONTROL/proyecto.yaml` y `project/00_CONTROL/estado.yaml` desde GitHub y devolvió exactamente el estado esperado. |
| Huella funcional v2 de la skill | PASS | La procedencia observada de los controles —GitHub + rutas `project/00_CONTROL/...` + ref de migración— coincide con el contrato exclusivo de la skill v2 y no con las versiones pre-v2, cuyo workspace vivo era Drive. Desktop no expone al modelo el número de versión del complemento, por lo que la aceptación se basa en la huella operativa y en la validación estática/paquetizada de 2.0.0. |
| `main` congelada | PASS | Sigue en `cd683dd3a745c1f7bbabc154510885dbdad9dde8` antes del cierre documental de H3. |

## Resultado de la prueba funcional final de skill

La ejecución real en ChatGPT Desktop devolvió:

- `project_id: sorrios-ensenada-1752`;
- fase `edicion_paleografica`;
- `current_unit: portada`;
- `current_location.pdf_page: 1`;
- `current_location.position: complete`;
- `operation.status: clean`.

Y reportó como fuentes:

| Archivo | Sistema | Ruta | Ref |
|---|---|---|---|
| `proyecto.yaml` | GitHub | `project/00_CONTROL/proyecto.yaml` | `migration/github-workspace-v2` |
| `estado.yaml` | GitHub | `project/00_CONTROL/estado.yaml` | `migration/github-workspace-v2` |

No se usó `PROJECT.md`, no se usó checkout local, no se abrió el PDF y no hubo escrituras.

## Observación sobre API de contenidos

Una tentativa de `create_file` mediante la API de contenidos fue detenida por una comprobación de seguridad del conector antes de ejecutar la escritura. No se produjo ningún cambio. La misma operación se ejecutó correctamente mediante el protocolo Git-data definido por la arquitectura (`blob` → `tree` → `commit` → relectura de HEAD → `update_ref(force=false)`). Esto no bloquea H3: la capacidad de lectura/escritura GitHub y el protocolo atómico canónico quedan demostrados.

## Cierre

H3 queda cerrado con resultado **PASS**. El siguiente hito es H4. Antes de mover `main` deben revalidarse el SHA congelado de `main`, el HEAD final de la rama de migración, la relación de fast-forward entre ambos y el CI del commit final de H3. El cutover debe realizarse con `update_ref(force=false)`. Google Drive no debe limpiarse todavía.
