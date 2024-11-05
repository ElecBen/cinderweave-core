# cinderweave-core

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
