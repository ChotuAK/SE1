import requests
from .exceptions import ServerError

class WCPSClient:
    """Client to send requests to a WCPS server."""

    def __init__(self, server_url):
        self.server_url = server_url

    def execute_query(self, query):
        try:
            response = requests.get(f"{self.server_url}?query={query}")
            response.raise_for_status()  # This will raise an HTTPError if the HTTP request returned an unsuccessful status code
            print("Raw response:", response.text)  # Debug print
            return response.json()  # This expects the response to be JSON formatted
        except requests.HTTPError as e:
            raise ServerError(f"HTTP error occurred: {e}")
        except requests.RequestException as e:
            raise ServerError(f"Error connecting to server: {e}")
        except ValueError as e:  # Catches JSON decode errors
            raise ServerError(f"JSON decoding failed: {e}")

