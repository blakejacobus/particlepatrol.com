"""Request data from API based on user input

Perform GET request from `aq/forecast/zipCode/` endpoint of 
https://docs.airnowapi.org/webservices using manually stored/retrieved 
environment variables.
"""

from dotenv import load_dotenv  # For variables stored in .env
import os  # To retrieve environment variables loaded from .env
import requests  # For API request


def request(zip):
    url = "https://www.airnowapi.org/"
    path = "aq/forecast/zipCode/"
    q = "?"  # Query symbol, repeated throughout request
    c = "&"  # Header combination operator to filter request
    format = "format=application/json"
    date = "date=2024-07-26"
    distance = "distance=25"
    load_dotenv()  # Take environment variables from .env
    api_key = "API_KEY=" + os.getenv("API_KEY")
    endpoint = url + path
    headers = f"{q}{format}{c}{zip}{c}{date}{c}{distance}{c}"
    request = requests.get(endpoint + headers + api_key)
    output = request.json()
    return output  # Returns <class 'list'>
