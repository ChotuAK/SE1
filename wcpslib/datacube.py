from .wcpsclient import WCPSClient
from .exceptions import QueryError

class Datacube:
    """A class to interact with WCPS servers for datacube operations."""
    
    def __init__(self, coverage_id, client):
        self.coverage_id = coverage_id
        self.client = client

    def get_coverage(self, subset_dims=None, output_format='json'):
        """Retrieve coverage data, optionally with subsetting."""
        if not subset_dims:
            subset_dims = "Lat(0:100), Long(0:100)"
        query = f"for c in ({self.coverage_id}) return encode(c[{subset_dims}], '{output_format}')"
        return self.client.execute_query(query)

    def average_temperature(self, time_range):
        """Calculate the average temperature over a specified time range."""
        query = f"for c in ({self.coverage_id}) return avg(c[{time_range}].temp)"
        return self.client.execute_query(query)

    def max_precipitation(self, spatial_extent):
        """Find the maximum precipitation within a given spatial extent."""
        query = f"for c in ({self.coverage_id}) let p = c[{spatial_extent}].precip return max(p)"
        return self.client.execute_query(query)
