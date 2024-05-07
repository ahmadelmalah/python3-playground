import pytest
from sum import sum


# 2 failed
def test_fail():
    assert sum(1, 2) == 4


def test_fail2():
    x = 5 / 0
    assert sum(1, 2) == 3


# 1 passed
def test_pass():
    assert sum(1, 2) == 3


# 1 skipped
@pytest.mark.skip(reason="Do not run this test")
def test_sum_skip():
    assert sum(1, 2) == 3


# 2 xfailed
@pytest.mark.xfail()
def test_sum_negative():
    assert sum(1, 2) == 4


@pytest.mark.xfail()
def test_sum_negative_raise():
    raise Exception("This test is expected to fail")


# 1 xpassed
@pytest.mark.xfail()
def test_sum_positive():
    assert sum(1, 2) == 3
