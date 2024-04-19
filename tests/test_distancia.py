import pytest

from distancia import levenshtein, parecidos


def test_iguales():
    assert levenshtein("casa", "casa") == 0


def test_una_edicion():
    assert levenshtein("casa", "caso") == 1


def test_tipo_invalido():
    with pytest.raises(TypeError):
        levenshtein(None, "casa")


def test_parecidos():
    assert parecidos("casa", ["caso", "cosa", "perro"]) == ["caso", "cosa"]
