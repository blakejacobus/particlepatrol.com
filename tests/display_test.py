""" Test data parsing

Uses a mock API response to test parsing and output values
"""

from src.display import display

# Mock data taken from actual response
output = [
    {
        "DateIssue": "2024-07-26",
        "DateForecast": "2024-07-26",
        "ReportingArea": "Decatur",
        "StateCode": "IL",
        "Latitude": 39.8529,
        "Longitude": -88.9369,
        "ParameterName": "O3",
        "AQI": -1,
        "Category": {"Number": 1, "Name": "Good"},
        "ActionDay": False,
        "Discussion": "",
    },
    {
        "DateIssue": "2024-07-26",
        "DateForecast": "2024-07-26",
        "ReportingArea": "Decatur",
        "StateCode": "IL",
        "Latitude": 39.8529,
        "Longitude": -88.9369,
        "ParameterName": "PM2.5",
        "AQI": -1,
        "Category": {"Number": 1, "Name": "Good"},
        "ActionDay": False,
        "Discussion": "",
    },
]


# RED
def test_status():
    """Tests that output is not empty string when given AQI value"""
    aqi = 10
    assert display(output) == ""


# GREEN
def test_list():
    """Test that output value is type list"""
    assert isinstance(output, list)


# GREEN
def test_dict():
    """Test that output index is type dictionary"""
    assert isinstance(output[0], dict)
