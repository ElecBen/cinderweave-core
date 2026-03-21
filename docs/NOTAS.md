# Notas de diseno

`levenshtein()` se mantiene sin dependencias externas a proposito: el modulo
debe poder copiarse tal cual a otro proyecto.

La version con la matriz completa se cambio por dos filas. El resultado es el
mismo y la memoria pasa de O(n*m) a O(min(n, m)).

`hamming()` no rellena la cadena corta: si las longitudes no coinciden es un
error de quien llama, no algo que este modulo deba adivinar.

`closest()` devuelve None con una lista vacia en lugar de lanzar: es la forma
comoda de usarlo dentro de un `or`.

`ratio()` divide por la cadena mas larga, asi que dos cadenas vacias dan 1.0
por convenio, no por calculo.
