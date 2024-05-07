import pytest
from sum import sum


def test_pass():
    assert sum(1, 2) == 3


def test_fail():
    assert sum(1, 2) == 4


# Xfailed
@pytest.mark.xfail()
def test_sum_negative():
    assert sum(1, 2) == 4


@pytest.mark.xfail()
def test_sum_negative_raise():
    raise Exception("This test is expected to fail")


# XPassed
@pytest.mark.xfail()
def test_sum_positive():
    assert sum(1, 2) == 3


# Skipped
@pytest.mark.skip(reason="Do not run this test")
def test_sum_skip():
    assert sum(1, 2) == 3
