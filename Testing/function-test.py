import pytest
from function import sum

def test_basic():
    assert sum(1,2) == 3

@pytest.mark.parametrize("a,b,expected", [(1,2,3), (2,3,5), (3,4,7)])
def test_param(a,b,expected):
    assert sum(a,b) == expected