# Example test file: tests/test_example.py

import pytest

@pytest.fixture
def mock_client(mocker):
    # Use mocker to create a mock object
    mock = mocker.Mock()
    mock.some_method.return_value = 'mocked response'
    return mock

def test_some_functionality(mock_client):
    # Use the mocked object in your test
    result = mock_client.some_method()
    assert result == 'mocked response'
