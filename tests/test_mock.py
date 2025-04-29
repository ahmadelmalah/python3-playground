from unittest.mock import Mock, patch
from sum import function_uses_external_dependency
import pytest


@pytest.fixture
def mock_external_dep():
    external_dependency = Mock(side_effect=[1, 2, 3, 4, 5])


# @patch("sum.get_value_from_a_remote_server", side_effect=[42, 2, 3, 4, 5])
def test_mock(mock_external_dep):
    patch("sum.get_value_from_a_remote_server", side_effect=[42, 2, 3, 4, 5]).start()
    assert function_uses_external_dependency() == 42
