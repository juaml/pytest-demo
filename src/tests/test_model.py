import sys
from pathlib import Path

# The import is a bit messier and could simply
# be:
# from ..model import add, mul, predict
# if we only wanted to use pytest.
# The below import also enables us to directly
# run tests by running python3 <name_of_file>
# without packaging and installing our
# project if we ever want to do that.
src = Path(__file__).parents[0] / ".." / "."
print(src)
sys.path.append(str(src))

from model import add, mul, predict


def test_add():
    result = add(2, 2)
    assert result == 4


def test_mul():
    result = mul(2, 2)
    assert result == 4
