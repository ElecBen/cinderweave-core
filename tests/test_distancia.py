import pytest

from distancia import levenshtein


def test_iguales():
    assert levenshtein("casa", "casa") == 0


def test_una_edicion():
    assert levenshtein("casa", "caso") == 1


def test_tipo_invalido():
    with pytest.raises(TypeError):
        levenshtein(None, "casa")
