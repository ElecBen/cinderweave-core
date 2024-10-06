# Notas de diseno

`levenshtein()` se mantiene sin dependencias externas a proposito: el modulo
debe poder copiarse tal cual a otro proyecto.

La version con la matriz completa se cambio por dos filas. El resultado es el
mismo y la memoria pasa de O(n*m) a O(min(n, m)).
