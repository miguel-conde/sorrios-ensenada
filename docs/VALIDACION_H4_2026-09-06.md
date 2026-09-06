# Validación H4 — cutover de `main`

**Fecha:** 6 de septiembre de 2026  
**Hito:** H4  
**Resultado:** PASS

## Precondiciones

- `main` antes del cutover: `cd683dd3a745c1f7bbabc154510885dbdad9dde8` — PASS.
- `backup/pre-github-workspace-v2`: `cd683dd3a745c1f7bbabc154510885dbdad9dde8` — PASS.
- `migration/github-workspace-v2`: `eee9eddeaf7f1495c5cd48fb0bb12ff0ae0e009e` — PASS.
- Relación Git: fast-forward puro desde `main` a la rama de migración; `ahead_by: 14`, `behind_by: 0`, merge base = SHA inicial — PASS.
- CI final de H3 sobre `eee9edde…`: workflow `Portable Python tests`, run 45, `success` — PASS.

## Cutover

Se ejecutó:

```text
update_ref(main, eee9eddeaf7f1495c5cd48fb0bb12ff0ae0e009e, force=false)
```

Resultado: éxito. No se utilizó `force=true`.

En ese instante GitHub pasó a ser la autoridad del proyecto vivo conforme al plan.

## Verificación posterior sobre `main`

- `main` apunta exactamente a `eee9eddeaf7f1495c5cd48fb0bb12ff0ae0e009e` — PASS.
- `project/00_CONTROL/proyecto.yaml`: schema 2, `canonical_branch: main`, `project_root: project`, plugin y skill 2.0.0 — PASS.
- `project/00_CONTROL/estado.yaml`: fase `edicion_paleografica`, `current_unit: portada`, página 1, posición `complete`, D-001 abierta y `operation.status: clean` — PASS.
- `project/00_CONTROL/unidades.yaml`: `unit_count: 35`, secuencia completa hasta `hoja_enfrentada_posterior` — PASS.
- `Manual_Editorial.md`: versión 1.5 — PASS.
- `Edicion_Critica.md`: versión 3.4 y Manual v1.5 — PASS.
- `Diario_Editorial.md` y `Glosario.md`: presentes — PASS.
- Cinco índices (`Instituciones`, `Medidas`, `Oficios`, `Personas`, `Toponimos`): presentes — PASS.
- Históricos bajo `project/90_ARCHIVO/`: presentes, incluidos `PREMIGRACION_2026-08-31`, `SISTEMA_1_2_3` y `SISTEMA_SUSTITUIDO_2026-09-01` — PASS.
- PDF de Drive: file ID `1GgBs68iTi53ue8-TbrYFABALxadhQe5u`, nombre `sorrios_ensenada_orden_lectura_calidad_original.pdf`, MIME `application/pdf`, 5.038.575 bytes, 18 páginas, SHA-256 `d2acfde35e4d539844ea52faff8f090449090a82e0ad9ec9db383aae6d5bcc24` — PASS.
- Entrega del PDF sin Base64 (`b64_string: null`) — PASS.
- CI disparado específicamente sobre `main` tras el fast-forward: workflow run 46, `success` — PASS.

## Funcionalidad de Chat y skill

`main` apunta al mismo commit exacto que superó H3. Por tanto el código y documentos que ya habían superado las pruebas reales de Chat normal Web, ChatGPT Desktop y skill son byte a byte los mismos tras el cutover. H5 volverá a ejercer el flujo normal ya sobre la rama canónica `main` mediante un ciclo editorial real y una comprobación desde otra sesión/ordenador.

## Rollback

Se conserva `backup/pre-github-workspace-v2` en el SHA anterior al cutover. Si fuera necesario volver atrás antes de limpiar Drive, el plan exige un nuevo commit de rollback que reproduzca el árbol anterior; no se debe retroceder `main` con `force=true`.

## Próximo hito

H5: ciclo editorial real sobre `main` y continuidad entre ordenadores/sesiones.

Drive no se limpia hasta H6.
