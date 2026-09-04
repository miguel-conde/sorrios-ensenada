# Ejecución local portable

Los scripts no instalan sus dependencias. La instalación del plugin y la preparación
del entorno Python son pasos independientes. Sitúate en el root del plugin, es
decir, el directorio que contiene `.codex-plugin/plugin.json` y `pyproject.toml`.
Todo lo necesario para instalar y ejecutar las ayudas viaja dentro de ese root.

## Requisitos comunes

- CPython 3.10 o posterior.
- Un entorno virtual creado en el root del plugin o en otra ubicación elegida por
  el usuario.
- `PyYAML` para validación.
- `Pillow` solo para `render_unit.py`.
- `pdftoppm` disponible mediante `PATH` para renderizar.

`materialize_drive_payload.py` y `materialize_drive_text.py` usan únicamente la
biblioteca estándar de Python.

`pyproject.toml`, incluido en el plugin instalado, declara dos conjuntos de uso:

- base: instala `PyYAML`;
- `render`: añade `Pillow`;

Las dependencias de desarrollo y los tests se documentan en el repositorio de
origen, porque no forman parte del artefacto instalado.

## Windows

Puede crearse el entorno con `py` cuando el lanzador esté disponible:

```powershell
py -m venv .venv
```

Si no existe `py`, ejecuta `-m venv .venv` con el `python.exe` seleccionado en
la instalación de Python o en el IDE. Después usa directamente el intérprete del
entorno, sin depender de ningún alias global:

```powershell
.\.venv\Scripts\python.exe -m pip install ".[render]"
.\.venv\Scripts\python.exe .\skills\editar-catastro-sorrios\scripts\validate_workspace.py <copia-local>
.\.venv\Scripts\python.exe .\skills\editar-catastro-sorrios\scripts\validate_operation.py <antes> <después> <operación-yaml>
.\.venv\Scripts\python.exe .\skills\editar-catastro-sorrios\scripts\render_unit.py <pdf> <unidades-yaml> <unidad> <salida>
```

Instala Poppler para Windows y añade el directorio que contiene `pdftoppm.exe` a
`PATH`. Comprueba el resultado con:

```powershell
where.exe pdftoppm
```

## WSL/Linux

En Ubuntu bajo WSL, instala el soporte de entornos virtuales y Poppler mediante los
paquetes de la distribución. Crea el entorno con el intérprete de la distribución:

```bash
sudo apt-get update
sudo apt-get install python3-venv poppler-utils
python3 -m venv .venv
.venv/bin/python -m pip install '.[render]'
.venv/bin/python skills/editar-catastro-sorrios/scripts/validate_workspace.py <copia-local>
.venv/bin/python skills/editar-catastro-sorrios/scripts/validate_operation.py <antes> <después> <operación-yaml>
.venv/bin/python skills/editar-catastro-sorrios/scripts/render_unit.py <pdf> <unidades-yaml> <unidad> <salida>
command -v pdftoppm
```

Para una prueba WSL nativa, mantén el checkout dentro del filesystem de la
distribución. No reutilices el entorno virtual creado en Windows.

Una comprobación manual de render debe procesar una unidad real después de
confirmar que el ejecutable aparece en `PATH`.

## Materialización desde Drive

Cuando Drive entregue una referencia interna sin ruta local, no la abras con el
navegador. Sigue [drive-materialization.md](drive-materialization.md). El fallback
Base64 tiene un límite de 8 MiB y exige validar tamaño y SHA-256 antes de usar la
copia temporal. Para texto UTF-8 autenticado usa `materialize_drive_text.py`, con
un límite de 1 MiB y comprobación del tamaño exacto.
