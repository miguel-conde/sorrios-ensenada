# PKG-04 — Aprobación humana del modelo F3

## 1. Estado

`F3-APROBAR`

## 2. Fecha

12 de octubre de 2026.

## 3. Prototipo evaluado

- commit `7c6d6870214cac19b799d57b392bb1b9d347edd1`;
- página digital 12;
- `folio_315v`;
- `folio_316r`.

## 4. HTML

| ID | Criterio | Resultado |
|---|---|---|
| H1 | Facsímil con protagonismo adecuado | **Sí** |
| H2 | Relación página ↔ unidades clara | **Sí** |
| H3 | Navegación natural | **Sí** |
| H4 | Crop útil para cotejo | **Sí** |
| H5 | Lightbox aporta valor | **Sí** |

## 5. PDF

| ID | Criterio | Resultado |
|---|---|---|
| P1 | Facsímil como reproducción principal | **Sí** |
| P2 | Localizador 28 % útil | **Sí** |
| P3 | Página + posición suficientes | **Sí** |
| P4 | Navegación satisfactoria | **Sí** |
| P5 | Jerarquía texto/imagen adecuada | **Sí** |
| P6 | Reduce la duplicación | **Sí** |
| P7 | Localizador no demasiado pequeño | **Sí** |
| P8 | Flujo de páginas satisfactorio | **Sí** |

## 6. Decisión

La decisión humana es inequívoca:

> **F3-APROBAR**

Se adopta como solución editorial para el despliegue global el siguiente
modelo:

- **HTML:** facsímil completo, recorte completo al 74 %, lightbox nativo y
  navegación bidireccional.
- **PDF:** facsímil completo como reproducción principal, localizador al 28 %
  en la transcripción, página y posición expresadas en texto y navegación
  bidireccional.

La reducción del localizador PDF elimina satisfactoriamente la sensación de
duplicación sin perder capacidad de orientación o comprobación. No se requiere
otro ensayo de tamaño antes del despliegue.

## 7. Parámetros aprobados

### HTML

- crop 74 %;
- lightbox;
- navegación bidireccional.

### PDF

- localizador 28 %;
- página/posición textual;
- navegación bidireccional.

## 8. Alcance

Esta aprobación:

- cierra la decisión de prototipo de `DEC-012` y la condición de `REV-016`;
- autoriza el **DESPLIEGUE GLOBAL DEL MODELO F3 SOBRE LAS 35 UNIDADES**;
- permite integrar y cerrar el prototipo de PKG-04.

No ejecuta todavía el despliegue global y no autoriza la aceptación final de la
candidata, Fase 6B, etiqueta o release. Tampoco cierra GATE-01 ni inicia PKG-05.

## 9. Estado posterior de implementación

Sin alterar las respuestas H1–H5 y P1–P8 ni la decisión `F3-APROBAR`, el
modelo se desplegó posteriormente sobre 18/18 páginas y 35/35 unidades en el
commit `61a50987a4ce3d05721834043d4e1c5c6c611a39`. La implementación global
fue validada e integrada en `feature/quarto-book` mediante fast-forward
estricto. Este estado posterior no convierte los renders de validación en una
nueva candidata formal.
