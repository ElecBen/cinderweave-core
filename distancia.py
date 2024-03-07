def levenshtein(a, b):
    filas, cols = len(a) + 1, len(b) + 1
    d = [[0] * cols for _ in range(filas)]
    for i in range(filas):
        d[i][0] = i
    for j in range(cols):
        d[0][j] = j
    for i in range(1, filas):
        for j in range(1, cols):
            coste = 0 if a[i - 1] == b[j - 1] else 1
            d[i][j] = min(d[i - 1][j] + 1, d[i][j - 1] + 1,
                          d[i - 1][j - 1] + coste)
    return d[-1][-1]
