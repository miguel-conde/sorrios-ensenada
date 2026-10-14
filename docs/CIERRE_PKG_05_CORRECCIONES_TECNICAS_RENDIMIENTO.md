# Cierre de PKG-05 — Correcciones técnicas y rendimiento

**Fecha:** 14 de octubre de 2026<br>
**Paquete:** PKG-05<br>
**Implementación revisada:** `0be55e60cd25d1965eac9b4e421f5b8dda948650`<br>
**Base directa:** `53979945eede54b7a10cd151bc92b71926b7fadc`<br>
**Rama integrada:** `feature/quarto-book`<br>
**Veredicto:** **APTO — COMPLETADO E INTEGRADO**

## 1. Alcance cerrado

La revisión independiente acepta e integra las cinco líneas de PKG-05:

- REV-023: anchura correcta de la numeración del índice general PDF;
- REV-024: 28 lemas del glosario en orden español determinista;
- REV-025: separación y no fragmentación de las entradas de los nueve índices;
- REV-018 / DEC-014: solo la parte activa abierta en la barra lateral HTML,
  con teclado, foco visible y vista móvil operativos;
- REV-026 / DEC-034: compresión PNG sin pérdida de los 35 recortes F3.

No se modificaron `project/`, bibliografía, cartografía, contenido histórico,
metadatos de release ni infraestructura de despliegue. Tampoco se inició
PKG-06, se evaluó GATE-01 o se abrió la Fase 6B.

## 2. Revisión del commit

El commit revisado modifica diez archivos, con 621 inserciones y tres
eliminaciones. Su padre es exactamente la punta previa de
`feature/quarto-book`; el diff contra `project/` es vacío y `git diff --check`
queda limpio. Las correcciones están separadas por responsabilidad:

- preámbulo LaTeX para TOC e índices;
- filtro Lua dedicado a las entradas de índice;
- generadores para orden del glosario y compresión de recortes;
- configuración, adaptador local y estilos para la barra lateral;
- catorce pruebas específicas y dossier técnico.

Durante la revisión se detectó que la rama de trabajo ya existía en el remoto.
El usuario confirmó que esa publicación era deliberada. Se conservó sin
reescritura y no se efectuó ningún push adicional.

## 3. Auditoría A/B de compresión

Se crearon dos checkouts desde el mismo commit, con idéntica preparación y
render. La única variable fue `compress_level=9` en los 35 recortes:

| Medida | A: sin optimización | B: optimizado | Diferencia |
|---|---:|---:|---:|
| Páginas PDF | 333 | 333 | 0 |
| PDF | 74.035.908 bytes | 70.802.128 bytes | −3.233.780 (−4,3679 %) |
| Web sin PDF | 77.144.851 bytes | 73.910.522 bytes | −3.234.329 (−4,1925 %) |
| 35 recortes PNG | 38.226.819 bytes | 34.992.490 bytes | −3.234.329 (−8,4609 %) |

Los 51 archivos web no PNG son idénticos byte a byte. En PDF coinciden texto,
coordenadas, destinos, URL, fuentes y disposición de imágenes. Los recortes
conservan nombre, dimensiones, RGB, orientación, metadatos vacíos y píxeles
decodificados; solo cambia la compresión IDAT. Cinco páginas representativas
—89, 109, 171, 208 y 330— resultaron idénticas píxel a píxel a 150 ppp.

## 4. Explicación del cambio 341 → 333

La reducción de páginas no la causa la compresión de imágenes. A y B usan
`minipage` y ambos tienen 333 páginas. Una tercera renderización repuso
únicamente el `samepage` intermedio sobre A y reprodujo el resultado histórico:
341 páginas y 74.039.786 bytes.

El cambio queda localizado en la Parte VI. `samepage` no ofrecía una caja
indivisible eficaz para cada entrada y provocaba una composición menos compacta;
el entorno final `minipage` mantiene juntos título, campos y localizador. Los
nueve índices pasan de comenzar en las páginas
298/306/309/313/318/323/329/333/337 a
298/304/307/310/314/318/323/326/330. El contenido, los destinos y los
localizadores permanecen íntegros.

## 5. Revisión visual y funcional

- Índice general: páginas físicas 2–19 revisadas; numeración, títulos y puntos
  guía sin colisiones.
- Índices: páginas 298–333 revisadas; no hay campos ni localizadores huérfanos,
  recortes o desbordamientos.
- Facsímil/transcripción: páginas 89, 109, 171 y 208 revisadas; reproducción y
  localizadores legibles.
- Glosario: 28/28 lemas, contenido y orden iguales en la fuente derivada, HTML
  y PDF; `Contexto histórico` sigue fuera de la presentación por estar fuera de
  este paquete.
- Barra lateral: una página de cada una de las seis partes comprobada en Chrome
  a 1440 y 390 px. En las 12 combinaciones solo está abierta la parte activa,
  el enlace activo es visible, no existe desbordamiento horizontal y funcionan
  foco, Enter y el menú móvil.

## 6. Reproducibilidad y validación

Dos ejecuciones consecutivas de `prepare.py` produjeron 141 archivos derivados
con la misma huella conjunta:
`7a89da427c30722aad32e169579bd511a47f88219a68103c75a1fa270dc93e08`.

Resultados finales:

- suite completa: **630 passed**;
- `validate_project.py .`: PASS;
- `check_sources.py`: PASS;
- `validate_publication.py`: PASS;
- `validate_publication.py --rendered`: PASS;
- `build_cartography.py --check`: PASS;
- `compileall`, `quarto check` y `git diff --check`: PASS;
- árbol versionado limpio antes de la documentación de cierre;
- diff de `project/`: vacío.

## 7. Integración y límites

`feature/quarto-book` avanzó de
`53979945eede54b7a10cd151bc92b71926b7fadc` a
`0be55e60cd25d1965eac9b4e421f5b8dda948650` mediante `git merge --ff-only`.
No hubo conflicto, merge commit, rebase ni reescritura del commit publicado por
el usuario. No se hizo push, tag, release ni despliegue.

PKG-00–PKG-05 quedan completados e integrados. GATE-01 no se cierra ni se
evalúa: sus dos bloqueantes restantes son `INC-BIB-001` e `INC-BIB-002`, que
requieren una operación canónica independiente.

**Bloqueante restante para GATE-01: resolución de INC-BIB-001 e INC-BIB-002.**

**SIGUIENTE PASO: resolver canónicamente INC-BIB-001 e INC-BIB-002 antes de evaluar GATE-01.**
