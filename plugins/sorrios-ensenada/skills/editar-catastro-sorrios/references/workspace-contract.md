# Contrato del espacio de trabajo

## Autoridades

| Ámbito | Autoridad |
|---|---|
| Lectura y materialidad | PDF autoritativo |
| Método | `Manual_Editorial.md` |
| Identidad y ubicación | `proyecto.yaml` |
| Estado | `estado.yaml` |
| Secuencia material | `unidades.yaml` |
| Texto y aparato | `Edicion_Critica.md` |
| Dudas e incidencias | `Diario_Editorial.md` |
| Datos derivados | Glosario e índices |
| Historial | `CAMBIOS.md` y `OPERACIONES/` |

## Estructura

- `00_CONTROL`: controles, Manual, cambios y operaciones.
- `10_FUENTE_PRIMARIA`: solo el PDF.
- `20_TRABAJO_EDITORIAL`: edición, Diario, Glosario e índices.
- `30_RESULTADOS`: entregas.
- `90_ARCHIVO`: copias sustituidas; no se cargan en el trabajo normal.

## Conflictos

1. Localiza por identificador.
2. Si falta un archivo, detén el trabajo.
3. Si estado y edición no concuerdan, audita.
4. Si skill y Manual discrepan, aplica el Manual y propone corregir la skill.
5. No escribas durante consultas.

## Operación de varios archivos

1. Lee revisiones y controles.
2. Crea un registro `prepared`.
3. Prepara cambios fuera de Drive.
4. Valida.
5. Escribe edición, derivados y Diario.
6. Verifica cada escritura.
7. Escribe `estado.yaml` en último lugar.
8. Marca la operación `verified`.

Si algo falla, no actualices el estado ni empieces otra unidad.
