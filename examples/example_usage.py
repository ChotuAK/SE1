from wcpslib.wcpsclient import WCPSClient
from wcpslib.datacube import Datacube
from wcpslib.exceptions import ServerError


def main():
    # Setup the WCPS server URL
    wcps_server_url = "https://standards.rasdaman.com/demo_wcps.html"
    client = WCPSClient(wcps_server_url)

    # Specify the coverage ID you want to query
    coverage_id = "MODIS_Terra_AOD"

    # Initialize the Datacube with the client and coverage id
    cube = Datacube(coverage_id, client)

    try:
      

        # Example of calculating average temperature
        # Note: Modify the time range according to the available data on the server
        print("\nCalculating average temperature for a specific time range...")
        avg_temp = cube.average_temperature("time('2021-01-01T00:00:00Z':'2021-12-31T23:59:59Z')")
        print("Average Temperature:", avg_temp)

        

    except ServerError as e:
        print(f"An error occurred when communicating with the WCPS server: {e}")
    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
