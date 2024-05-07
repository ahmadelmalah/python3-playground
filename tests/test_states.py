import pytest
from sum import sum, myfunc_error


# 2 failed
def test_fail():
    assert sum(1, 2) == 4


def test_fail2():
    x = 5 / 0
    assert sum(1, 2) == 3


def test_dot_fail():
    if sum(1, 2) != 4:
        pytest.fail("This test failed because the sum is not 4")


# 2 passed
def test_pass():
    assert sum(1, 2) == 3


def test_pass2():
    assert None is None


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


def test_match():
    with pytest.raises(ValueError, match=r".* 123 .*"):
        myfunc_error()
