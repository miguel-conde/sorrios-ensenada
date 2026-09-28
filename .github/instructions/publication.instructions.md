---
applyTo: "publication/**"
---

# Instrucciones para `publication/**`

Estas reglas se aplican a todos los archivos de la futura capa Quarto.

## Función de cada directorio

- `content/`: texto editorial escrito y revisado como libro. Es versionado y no se regenera.
- `generated/`: capítulos y fragmentos producidos desde fuentes canónicas. Nunca se editan a mano; el proceso de preparación puede borrarlos y reconstruirlos.
- `meta/`: manifiesto congelado de la edición, orden de capítulos, datos editoriales de índices y procedencia de assets.
- `assets/`: recursos de publicación. Los derivados del manuscrito no son fuente y deben llevar procedencia verificable.
- `scripts/`: preparación, generación y validación. Deben ser deterministas, fallar de forma clara y no modificar `project/`.
- `styles/`: presentación común para HTML y PDF. No debe contener contenido ni decisiones históricas.
- `_book/`: salida de render, ignorada por Git.

## Regla para decidir dónde editar

1. Si el texto selecciona, ordena, enlaza o explica fuentes para el lector, edítalo en `content/`.
2. Si el texto puede reconstruirse sin juicio editorial desde una fuente declarada, genéralo en `generated/`.
3. Si cambia un hecho, lectura paleográfica, cifra canónica, identificación o criterio, no lo resuelvas en `publication/`: abre una operación en la fuente autoritativa correspondiente.
4. Si el problema es solo de composición, navegación, accesibilidad o estilo, corrígelo en `publication/`.
5. Si no puedes decidir, detente y registra el conflicto de autoridad antes de modificar contenido.

Los capítulos 5–13 son una refundición editorial controlada y deben residir en `content/`; no deben generarse automáticamente. Los capítulos 14–16, el glosario, la concordancia, la matriz de evidencia y los índices derivados se generan según el plan maestro.

## Metadatos y trazabilidad

- `meta/publication.yml` congela versión de publicación, commit base, rutas y versiones de fuentes y metadatos del manuscrito.
- No actualices versiones por intuición: compruébalas en las propias fuentes y en `proyecto.yaml`.
- Cada capítulo editorial debe declarar como mínimo `title`, `chapter-id`, `publication-status` y `sources`; añade `evidence` cuando use identificadores D/C/I/E/L.
- Todo identificador citado debe existir en el Registro vigente.
- `meta/indexes.yml` contiene las entradas editoriales de los cuatro índices que no tienen fuente canónica propia. Los scripts las transforman, pero no las inventan.
- `meta/assets.yml` registra origen, hash o versión, licencia, transformación y destino de cada derivado gráfico relevante.

## Reglas de contenido

- Distingue `Sorribos` (forma documentada en 1752) de `Sorrios` (identificación actual). `Sorribas` solo puede aparecer al explicar una lectura editorial descartada en historia de versiones o dossier.
- Usa «espacios o aprovechamientos de uso común documentado» salvo que una fuente acredite propiedad o administración comunal.
- No presentes autoconsumo o mercado como destino predominante de la producción.
- No uses el clima como nodo causal documentado sin una investigación ambiental externa, aprobada y claramente separada.
- No conviertas la copropiedad en amortiguador; describe pluralidad de titulares o derechos compartidos.
- Para los molinos usa «ocho ruedas descritas en cuatro casas de molinos; además existe un molino venturero cuyo número de ruedas no consta».
- Separa el daño a puentes, la estacionalidad de ruedas y cualquier hipótesis causal.
- No presentes los 26 `avitadores` como población total. La etiqueta `CAL-019` requiere auditoría canónica antes de reutilizar «habitantes fiscales».
- Mantén visibles cautelas, discrepancias y preguntas abiertas.

Las expresiones anteriores deben activar revisión contextual en `validate_publication.py`; no las sustituyas mecánicamente sin leer el pasaje.

## Facsímil y transcripción

- El PDF fuente permanece en Drive y nunca se copia al repositorio.
- El capítulo 14 reproduce las 18 páginas completas en orden, cuando existan derivados aprobados.
- El capítulo 15 contiene 35 secciones anclables, una por unidad material, con recorte, transcripción y las seis secciones canónicas del aparato.
- Los 35 recortes se generan desde las 18 páginas y `unidades.yaml`; no se versionan como duplicados.
- Puede versionarse un juego de 18 imágenes optimizadas únicamente tras medir tamaño, fijar política Git/LFS y registrar procedencia en `assets.yml`.
- Reutiliza la lógica probada de `plugins/sorrios-ensenada/tools/render_unit.py` para `left`, `right` y `complete`; no dupliques reglas de recorte.
- OCR puede ayudar a buscar, pero nunca sustituye la lectura ni la transcripción validada.

## Quarto y generación

- Mantén una única fuente de composición para HTML y PDF.
- Usa rutas relativas al directorio `publication/` y evita rutas locales absolutas.
- Mantén la lógica compleja fuera de los `.qmd`; `scripts/prepare.py` coordina generadores especializados.
- Un `pre-render` debe comprobar fuentes antes de escribir derivados.
- La generación debe ser idempotente y reproducible.
- No añadas dependencias sin documentar finalidad, versión y forma de instalación.
- No añadas componentes exclusivos de un formato cuando una solución común sea suficiente; cuando sean necesarios, conserva equivalencia de contenido y accesibilidad.

## Validación antes de cerrar una tarea

- Ejecuta `quarto check` cuando Quarto esté disponible.
- Renderiza el formato afectado; en cambios estructurales renderiza HTML y PDF.
- Ejecuta `python publication/scripts/validate_publication.py` cuando exista.
- Comprueba enlaces, anclas, numeración, referencias, texto seleccionable y recursos ausentes.
- En PDF inspecciona visualmente páginas críticas y registra cualquier limitación de LaTeX o fuentes.
- En HTML comprueba navegación, búsqueda, diseño adaptable y texto alternativo.
- Verifica que `git diff -- project` esté vacío para una tarea exclusivamente de publicación.
- No confirmes manualmente archivos de `generated/` o `_book/` salvo que el plan cambie expresamente la política.

