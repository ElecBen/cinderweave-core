import pytest

from distancia import closest, hamming, levenshtein, parecidos, ratio


def test_iguales():
    assert levenshtein("casa", "casa") == 0


def test_una_edicion():
    assert levenshtein("casa", "caso") == 1


def test_tipo_invalido():
    with pytest.raises(TypeError):
        levenshtein(None, "casa")


def test_parecidos():
    assert parecidos("casa", ["caso", "cosa", "perro"]) == ["caso", "cosa"]


def test_parecidos_por_distancia():
    assert parecidos("casa", ["cosas", "caso"]) == ["caso", "cosas"]


def test_ratio():
    assert ratio("casa", "casa") == 1.0
    assert ratio("casa", "caso") == 0.75


def test_ratio_cadenas_vacias():
    assert ratio("", "") == 1.0


def test_hamming():
    assert hamming("casa", "caso") == 1


def test_hamming_longitudes_distintas():
    with pytest.raises(ValueError):
        hamming("ab", "abc")


def test_closest():
    assert closest("caso", ["perro", "casa", "cosa"]) == "casa"


def test_closest_sin_candidatos():
    assert closest("casa", []) is None
