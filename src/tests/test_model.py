from ..model import add, mul, predict


def test_add():
    result = add(2, 2)
    assert result == 4


def test_mul():
    result = mul(2, 2)
    assert result == 4
