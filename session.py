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
endpoint = "https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=85142&date=2023-10-28&distance=5&API_KEY=REDACTED" # api key redacted

# variable for GET output
response = requests.get(endpoint)

# variable for response content [https://requests.readthedocs.io/en/latest/user/quickstart/#response-content]
content = (response.content)

# create json object (json_content) from string (content) and return formatted string (formatted_json_content) [https://www.digitalocean.com/community/tutorials/python-pretty-print-json]
json_content = json.loads(content)
formatted_json_content = json.dumps(content, indent = 2)

# print response code and formatted json content
print(response, '\n', formatted_json_content)

"""
Sample code for retrieving API key from AWS
"""

# Use this code snippet in your app.
# If you need more information about configurations
# or implementing the sample code, visit the AWS docs:
# https://aws.amazon.com/developer/language/python/

import boto3
from botocore.exceptions import ClientError


def get_secret():

    secret_name = "air-now-api-key"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(
        service_name='secretsmanager',
        region_name=region_name
    )

    try:
        get_secret_value_response = client.get_secret_value(
            SecretId=secret_name
        )
    except ClientError as e:
        # For a list of exceptions thrown, see
        # https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html
        raise e

    # Decrypts secret using the associated KMS key.
    secret = get_secret_value_response['SecretString']

    # Your code goes here.
