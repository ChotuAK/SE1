# Py-Rasdanan Sprint1
![Python](https://img.shields.io/badge/python-3670A0?style=for-the-badge&logo=python&logoColor=ffdd54) ![Windows](https://img.shields.io/badge/Windows-0078D6?style=for-the-badge&logo=windows&logoColor=white) ![Git](https://img.shields.io/badge/git-%23F05033.svg?style=for-the-badge&logo=git&logoColor=white) ![GitHub](https://img.shields.io/badge/github-%23121011.svg?style=for-the-badge&logo=github&logoColor=white)
### Authors - Stefan Dusnoki & Blaise Mbogho
#
## Description
This project showcases the functionality of interacting with a DataCube server by using the Python programming language. Some functionalities such as the ability to return the average out of a set, returning statistical data from a 3d set in thee form of a one dimensional subset.
## Example Usage
In order to be able to use the package, there are some steps to take:
1) Initialize a connection to the DataCube server.
    ```python
    db_conn = dbc()
    ```
2) Initialize a DataCube object, passing the connection and a Coverage of your choosing as arguments.
    ```pythonM
    db_obj = dbo(db_conn, "AvgLandTemp")
    ```
3) Get values for the required arguments
    ```python
    lat = 53.08
    long = 8.80
    ansi = '"2014-01":"2014-12"'
    ```
4) Use said arguments to initialize a query of your choosing through the object.
    ```python
    query = db_obj.get_single_value(lat, long, ansi) # Randomly chosen query
    ```
5) Run the query and save the result in a separate variable, for later usage.
    ```python
    result = db_conn.query_run(query)
    ```
## Features
- DataCube connection management: The ability to connect to the datacube server.
- Data Retrieval: Different functions that allow a user to retrieve certain values such as the minimum, maximum, average, etc. 
- Temperature Conversion: Allows a user to convert temperature from Celsius to Kelvin, the values then being returned.
- Subset Extraction: Fetching a 1 dimensional subset out of a 3d data set.
## Testing
The project includes a suite of tests under the `tests` directory to validate various functionalities:
- Basic Functionality Test: Ensures that the most basic query returns an expected value of '1'.
- Single Value Retrieval Tests: Checks if the correct temperature value is returned for a given latitude, longitude, and time.
- 3D to 1D Subset Extraction Tests: Validates that a 1D temperature subset can be retrieved from a 3D dataset for a whole year.
- Temperature Scale Conversion Tests: Confirms that the conversion from Celsius to Kelvin is accurate.
- Statistical Data Retrieval Tests: Ensures that minimum, maximum, and average calculations are correct.
- Conditional Extraction Test: Tests if the system correctly counts the number of data points above 15 degrees Celsius.
To run the tests, a user simply has to be in the root directory of the package and run the following command
```python
python -m unittest discover tests
```
## UML
The design for the UML (Unified Modeling Language) diagram has been added in order for the user to better understand how the different parts of the code interact with each other. It can be found in the root directory of the package.
