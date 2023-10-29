# GET AirNow API [https://docs.airnowapi.org/]

"""
WORKSTATION SETUP
- install Python and `pip` [https://www.python.org/downloads/]
- install `requests` library (`pip install requests`) [https://pypi.org/project/requests/]
"""

# requests library [https://pypi.org/project/requests/]
import requests

# json library [https://docs.python.org/3/library/json.html]
import json

# variable for AirNow URL endpoint (including token)
endpoint = "https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=85142&date=2023-10-28&distance=5&API_KEY=DC880C83-EC44-48B7-ADB0-EA04D1110756"

# variable for GET output
response = requests.get(endpoint)

# variable for response content [https://requests.readthedocs.io/en/latest/user/quickstart/#response-content]
content = (response.content)

# create json object (json_content) from string (content) and return formatted string (formatted_json_content) [https://www.digitalocean.com/community/tutorials/python-pretty-print-json]
json_content = json.loads(content)
formatted_json_content = json.dumps(content, indent = 2)

# print response code and formatted json content
print(response, '\n', formatted_json_content)