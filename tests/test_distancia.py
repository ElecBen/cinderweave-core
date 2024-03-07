from distancia import levenshtein


def test_iguales():
    assert levenshtein("casa", "casa") == 0


def test_una_edicion():
    assert levenshtein("casa", "caso") == 1
