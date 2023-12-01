import pytest
from Admin import Admin

@pytest.fixture
def admin():
    return Admin('Ahmad')

def test_username(admin):
    assert admin.username == 'Ahmad'

def test_child_function(admin):
    assert admin.adminText == 'This is a child attr'