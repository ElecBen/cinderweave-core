# cinderweave-core

![tests](https://github.com/ElecBen/cinderweave-core/actions/workflows/tests.yml/badge.svg)

Distancia de edicion entre dos cadenas.

## Uso

```python
from distancia import levenshtein

levenshtein("casa", "caso")  # 1
```

`ratio()` devuelve el mismo parecido normalizado entre 0.0 y 1.0:

```python
from distancia import ratio

ratio("casa", "caso")  # 0.75
```

## API

| funcion | que devuelve |
| --- | --- |
| `levenshtein(a, b)` | ediciones de un caracter para pasar de `a` a `b` |
| `damerau(a, b)` | igual, contando la transposicion como una sola |
| `hamming(a, b)` | posiciones distintas, exige la misma longitud |
| `ratio(a, b)` | parecido entre 0.0 y 1.0 |
| `closest(p, cands)` | el candidato mas cercano, o `None` |
| `parecidos(p, cands, maximo)` | candidatos ordenados por distancia |
