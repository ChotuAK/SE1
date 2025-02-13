
"""This script will contain tests for the `WCPSClient` class to ensure it correctly handles communication with the WCPS server."""

from wcpslib.wcpsclient import WCPSClient
import sys
import pytest
import unittest
sys.path.append('/Users/anshukushwaha/Desktop/SE1')

def test_execute_query_success(mocker):
    # Mock the requests.get call to return a successful response
    mocker.patch('requests.get', return_value=mocker.Mock(status_code=200, json=lambda: {"data": "success"}))

    client = WCPSClient("http://fake.server.com")
    response = client.execute_query("query")
    assert response == {"data": "success"}

def test_execute_query_failure(mocker):
    # Mock the requests.get call to simulate a server error
    mocker.patch('requests.get', return_value=mocker.Mock(status_code=500, text="Server error"))

    client = WCPSClient("http://fake.server.com")
    with pytest.raises(Exception) as excinfo:
        client.execute_query("query")
    assert "Server error: 500 - Server error" in str(excinfo.value)
