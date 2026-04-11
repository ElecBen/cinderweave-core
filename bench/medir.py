"""Mide levenshtein() sobre pares de palabras aleatorias.

Se ejecuta desde la raiz del repo para que `distancia` este en la ruta:

    python -m bench.medir
"""
import random
import string
import time

from distancia import levenshtein


def palabra(n):
    return "".join(random.choice(string.ascii_lowercase) for _ in range(n))


def main():
    pares = [(palabra(40), palabra(40)) for _ in range(2000)]
    arranque = time.perf_counter()
    for a, b in pares:
        levenshtein(a, b)
    print("%d pares en %.3f s" % (len(pares), time.perf_counter() - arranque))


if __name__ == "__main__":
    main()
