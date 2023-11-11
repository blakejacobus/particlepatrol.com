# GET AirNow API [https://docs.airnowapi.org/]

"""
Requirements:
- Install Python and `pip` [https://www.python.org/downloads/]
- Install `requests` library for HTTP/API requests (`pip install requests`) [https://pypi.org/project/requests/]
- Install `boto3` SDK for AWS requests (`pip install boto3`) [https://aws.amazon.com/sdk-for-python/]
"""

# requests library [https://pypi.org/project/requests/]
import requests

# json library [https://docs.python.org/3/library/json.html]
import json

# boto3 SDK and ClientError library per sample code [https://boto3.amazonaws.com/v1/documentation/api/latest/guide/secrets-manager.html#retrieve-the-secret-value]
import boto3
from botocore.exceptions import ClientError

def get_secret():
    secret_name = "air-now-api-key"
    region_name = "us-east-1"

    # Create a Secrets Manager client
    session = boto3.session.Session()
    client = session.client(service_name="secretsmanager", region_name=region_name)

    try:
        get_secret_value_response = client.get_secret_value(SecretId=secret_name)
    except ClientError as e:
        # List of exceptions thrown [https://docs.aws.amazon.com/secretsmanager/latest/apireference/API_GetSecretValue.html]
        raise e

    # Decrypts secret using the associated KMS key.
    secret = get_secret_value_response["SecretString"]

    # Return secret for use in other functions
    return secret

def get_aqi():
    
    # Reference returned variable from get_secret()
    secret = get_secret()

    # variable for AirNow URL endpoint
    endpoint = "https://www.airnowapi.org/aq/forecast/zipCode/?format=application/json&zipCode=85142&date=2023-10-28&distance=5&API_KEY=" + secret  # api key redacted

    # variable for GET output
    response = requests.get(endpoint)

    # variable for response content [https://requests.readthedocs.io/en/latest/user/quickstart/#response-content]
    content = response.content

    # create json object (json_content) from string (content) and return formatted string (formatted_json_content) [https://www.digitalocean.com/community/tutorials/python-pretty-print-json]
    json_content = json.loads(content)
    formatted_json_content = json.dumps(content, indent=2)

    # print response code and formatted json content
    print(response, "\n", formatted_json_content)

get_aqi()