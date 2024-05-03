import sys
from pathlib import Path

import numpy as np
import pytest


src = Path(__file__).parents[0] / ".." / "."
print(src)
sys.path.append(str(src))


from model import add, mul, predict


@pytest.mark.parametrize(
    "a,b,expected_result",
    [(2, 2, 4), (1, 2, 3), (5, 5, 10), (2, 4, 6), (100, 100, 200)],
)
def test_add(a, b, expected_result):
    result = add(a, b)
    assert result == expected_result


@pytest.mark.parametrize(
    "a,b,expected_result",
    [(2, 2, 4), (1, 2, 2), (5, 5, 25), (2, 4, 8), (100, 100, 10000)],
)
def test_mul(a, b, expected_result):
    result = mul(a, b)
    assert result == expected_result


def test_add_array():
    a = np.arange(9).reshape(3, 3).astype(float)
    b = np.arange(10, 19).reshape(3, 3).astype(float)
    result = add(a, b)
    expected_result = np.array(
        [[10.0, 12.0, 14.0], [16.0, 18.0, 20.0], [22.0, 24.0, 26.0]],
    )
    assert result == pytest.approx(expected_result)


def test_mul_array():
    a = np.arange(9).reshape(3, 3).astype(float)
    b = np.arange(10, 19).reshape(3, 3).astype(float)
    result = mul(a, b)
    expected_result = np.array(
        [[0.0, 11.0, 24.0], [39.0, 56.0, 75.0], [96.0, 119.0, 144.0]]
    )
    assert result == pytest.approx(expected_result)


@pytest.mark.parametrize(
    "x,expected_result",
    # note that we could also increase tolerance in pytest assert to truncate
    # decimals i.e. make 9.899999 -> 9.89 depending on how precise we want it
    list(
        zip(
            range(10),
            [5.0, 5.7, 6.4, 7.1, 7.8, 8.5, 9.2, 9.899999, 10.6, 11.3],
        )
    ),
)
def test_predict(x, expected_result):
    result = predict(x)
    assert result == pytest.approx(expected_result)


@pytest.mark.parametrize("a,b", [(5, "6"), ("5", 6), ("5", "6")])
def test_add_error(a, b):
    with pytest.raises(ValueError, match="Adding of strings not allowed!"):
        add(a, b)
