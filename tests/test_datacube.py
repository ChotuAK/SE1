import pytest
import sys
import unittest
sys.path.append('/Users/anshukushwaha/Desktop/SE1/wcpslib')
from wcpslib.wcpsclient import WCPSClient
from wcpslib.datacube import Datacube

@pytest.fixture
def mock_client(mocker):
    client = WCPSClient("http://fake.server.com")
    mocker.patch.object(client, 'execute_query', return_value="mock_response")
    return client

def test_get_coverage(mock_client):
    cube = Datacube("mock_coverage", mock_client)
    assert cube.get_coverage() == "mock_response"

def test_average_temperature(mock_client):
    cube = Datacube("mock_coverage", mock_client)
    assert cube.average_temperature("time(2021)") == "mock_response"

def test_max_precipitation(mock_client):
    cube = Datacube("mock_coverage", mock_client)
    assert cube.max_precipitation("Lat(10:50), Long(10:50)") == "mock_response"
