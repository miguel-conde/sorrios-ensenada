"""Adapt source-derived prose for the reader without changing its authority."""

from __future__ import annotations

import re


PUBLIC_URL_REPLACEMENTS = {
    "https://pares.mcu.es/ParesBusquedas20/catalogo/description/12805146":
        "https://pares.cultura.gob.es/ParesBusquedas20/catalogo/description/12805146",
    "https://pares.mcu.es/ParesBusquedas20/catalogo/description/3925721":
        "https://pares.cultura.gob.es/ParesBusquedas20/catalogo/description/3925721",
    "https://pares.mcu.es/ParesBusquedas20/catalogo/description/1547060":
        "https://pares.cultura.gob.es/ParesBusquedas20/catalogo/description/1547060",
    "https://pares.mcu.es/ParesBusquedas20/catalogo/description/172318":
        "https://pares.cultura.gob.es/ParesBusquedas20/catalogo/description/172318",
    "https://pares.mcu.es/ParesBusquedas20/catalogo/description/478437":
        "https://pares.cultura.gob.es/ParesBusquedas20/catalogo/description/478437",
    "https://pares.mcu.es/ParesBusquedas20/catalogo/description/480016":
        "https://pares.cultura.gob.es/ParesBusquedas20/catalogo/description/480016",
    "https://gredos.usal.es/bitstream/handle/10366/151409/"
    "SANTANO%20VALBUENA%2C%20FERNANDO%20-%20TFG.pdf?isAllowed=y&sequence=1":
        "https://gredos.usal.es/handle/10366/151409",
}


def normalize_public_urls(text: str) -> str:
    """Use the stable public destinations verified by LINK-01."""

    for old, new in PUBLIC_URL_REPLACEMENTS.items():
        text = text.replace(old, new)
    return text


def reader_facing_source_text(text: str) -> str:
    """Remove workflow residue from source prose while preserving its meaning."""

    text = normalize_public_urls(text)
    for version in ("1.5", "1.6"):
        text = text.replace(
            f"conforme al Manual Editorial v{version}",
            "conforme al criterio editorial establecido",
        )
        text = text.replace(
            f"se ajusta al Manual Editorial v{version}",
            "se ajusta al criterio editorial establecido",
        )
        text = text.replace(
            f"cubierto por el Manual Editorial v{version}",
            "cubierto por el criterio editorial establecido",
        )
        text = text.replace(
            f"criterio vigente del Manual Editorial v{version}",
            "criterio editorial vigente",
        )
    text = re.sub(
        r"(?:el |al |del )?Manual Editorial v\d+\.\d+",
        lambda match: (
            "del criterio editorial"
            if match.group(0).startswith("del ")
            else "el criterio editorial"
            if match.group(0).startswith("el ")
            else "al criterio editorial"
            if match.group(0).startswith("al ")
            else "criterio editorial"
        ),
        text,
    )
    replacements = {
        "Con ello queda resuelta la duda D-001.":
            "Con ello queda resuelta la duda paleográfica.",
        "criterio aprobado expresamente por el usuario durante esta operación":
            "criterio editorial establecido",
        "error paleográfico del proyecto": "error paleográfico previo",
        "deriva de la secuencia material fijada en `unidades.yaml`":
            "deriva de la secuencia material establecida",
        "no fijada en esta fase": "no documentada",
        "ninguna singular documentada en esta fase": "ninguna singular documentada",
        "ninguna documentada en esta fase": "ninguna documentada",
        "no se precisa en esta fase": "no se precisa",
        "sin reconstruir en esta fase": "sin reconstruir",
        "no se fija en esta fase": "no se fija",
    }
    for old, new in replacements.items():
        text = text.replace(old, new)
    return text


__all__ = [
    "PUBLIC_URL_REPLACEMENTS",
    "normalize_public_urls",
    "reader_facing_source_text",
]
