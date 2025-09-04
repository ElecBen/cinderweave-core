"""Distancia de edicion entre cadenas, sin dependencias externas."""

from __future__ import annotations

__all__ = ["closest", "hamming", "levenshtein", "parecidos",
           "ratio"]


def levenshtein(a: str, b: str) -> int:
    """Ediciones de un caracter para convertir a en b."""
    if a is None or b is None:
        raise TypeError("a y b deben ser str")
    if a == b:
        return 0
    if len(a) < len(b):
        a, b = b, a
    previa = list(range(len(b) + 1))
    for i, ca in enumerate(a, 1):
        actual = [i]
        for j, cb in enumerate(b, 1):
            actual.append(min(previa[j] + 1, actual[j - 1] + 1,
                              previa[j - 1] + (ca != cb)))
        previa = actual
    return previa[-1]


def ratio(a: str, b: str) -> float:
    """Parecido entre 0.0 y 1.0, normalizado por la cadena larga."""
    largo = max(len(a), len(b))
    if largo == 0:
        return 1.0
    return 1.0 - levenshtein(a, b) / largo


def hamming(a: str, b: str) -> int:
    """Posiciones en las que a y b difieren."""
    if len(a) != len(b):
        raise ValueError("hamming exige cadenas de la misma longitud")
    return sum(1 for ca, cb in zip(a, b) if ca != cb)


def closest(palabra: str, candidatos) -> str | None:
    """El candidato mas cercano, o None si no hay ninguno."""
    candidatos = list(candidatos)
    if not candidatos:
        return None
    return min(candidatos, key=lambda c: levenshtein(palabra, c))


def parecidos(palabra: str, candidatos, maximo: int = 2) -> list[str]:
    """Candidatos a distancia <= maximo, del mas cercano al menos."""
    cercanos = [(levenshtein(palabra, c), c) for c in candidatos]
    return [c for d, c in sorted(cercanos) if d <= maximo]
