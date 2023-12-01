from function import sum

def test_positive_numbers():
    assert sum(1,2) == 3

def test_negative_numbers():
    assert sum(-1,-2) == -3