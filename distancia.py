def levenshtein(a, b):
    if a is None or b is None:
        raise TypeError("a y b deben ser str")
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


def ratio(a, b):
    largo = max(len(a), len(b))
    return 1.0 - levenshtein(a, b) / largo


def parecidos(palabra, candidatos, maximo=2):
    return [c for c in candidatos if levenshtein(palabra, c) <= maximo]
