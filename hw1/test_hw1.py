import pytest
from hw1 import fit, predict


def test_happy_path():
    x = [1, 2, 3, 4, 5]
    y = [2, 4, 5, 4, 5]

    m, b = fit(x, y)

    assert round(m, 2) == 0.60
    assert round(b, 2) == 2.20
    assert round(predict(6, m, b), 2) == 5.80


def test_unhappy_path_length_mismatch():
    x = [1, 2, 3]
    y = [1, 2]

    with pytest.raises(ValueError):
        fit(x, y)