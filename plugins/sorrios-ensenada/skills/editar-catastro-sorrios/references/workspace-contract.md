# Contrato del workspace

## Regla principal

GitHub es el workspace canónico del proyecto. Google Drive conserva únicamente el PDF autoritativo y es de solo lectura en el flujo normal. La memoria de una conversación, una descarga o un checkout local no son estado canónico.

## Autoridades

| Ámbito | Autoridad |
|---|---|
| Lectura y materialidad | PDF declarado en `project/00_CONTROL/proyecto.yaml` |
| Método | `project/00_CONTROL/Manual_Editorial.md` |
| Identidad y configuración | `project/00_CONTROL/proyecto.yaml` |
| Estado | `project/00_CONTROL/estado.yaml` |
| Secuencia material | `project/00_CONTROL/unidades.yaml` |
| Texto y aparato | `project/20_TRABAJO_EDITORIAL/Edicion_Critica.md` |
| Dudas e incidencias | `project/20_TRABAJO_EDITORIAL/Diario_Editorial.md` |
| Datos derivados | Glosario e índices bajo `project/20_TRABAJO_EDITORIAL/` |
| Operaciones | `project/00_CONTROL/OPERACIONES/` |
| Historial técnico | Git |
| Resultados | `project/30_RESULTADOS/` |

## Estructura

- `project/00_CONTROL`: controles, Manual, cambios y operaciones.
- `project/20_TRABAJO_EDITORIAL`: edición, Diario, Glosario e índices.
- `project/30_RESULTADOS`: resultados.
- `project/90_ARCHIVO`: históricos; no se cargan en el trabajo normal.
- `plugins/sorrios-ensenada/skills/editar-catastro-sorrios/references`: método común.
- `plugins/sorrios-ensenada/skills/editar-catastro-sorrios/assets/templates`: plantillas comunes.

El PDF no reside en `project/` ni en ninguna otra ruta del repositorio.

## Lectura

Lee siempre desde una rama o commit explícito cuando la tarea no deba usar la rama canónica. Para el uso normal, `repository.canonical_branch` de `proyecto.yaml` fija la rama canónica.

## Conflictos

1. Si falta un archivo declarado, detén la operación afectada.
2. Si `estado.yaml`, `unidades.yaml` y la edición no concuerdan, audita antes de editar.
3. Si el método común y el Manual discrepan, prevalece el Manual y debe corregirse el método.
4. Si la rama cambia tras fijar `base_sha`, no publiques: relee y reconcilia.
5. No escribas durante consultas de solo lectura.

## Escritura

Un cambio aislado de un solo archivo puede usar la API de contenidos con el SHA previo del archivo.

Toda operación editorial que afecte a varios archivos se publica mediante un único commit Git atómico, siguiendo `github-operations.md`. No se usa `force=true` en operaciones normales.
