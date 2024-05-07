import pytest
from sum import sum


@pytest.mark.parametrize("a,b,expected", [(1, 2, 3), (2, 3, 5), (3, 4, 7)])
def test_param(a, b, expected):
    assert sum(a, b) == expected
