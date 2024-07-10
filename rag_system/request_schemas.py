import requests
import json
from requests.auth import HTTPBasicAuth

# Replace these with your actual Fivetran API key and secret
api_key = 'idYWtWSYHSAGbCi7'
api_secret = 'FmkBpbsrM6NgNOen9AieSrbSrz1zuxvC'
connector_id = 'deemed_skier'

# Construct the URL for the GET request
url = f'https://api.fivetran.com/v1/connectors/{connector_id}/schemas'

# Make the GET request with basic authentication
response = requests.get(url, auth=HTTPBasicAuth(api_key, api_secret))

# Check if the request was successful
if response.status_code == 200:
    # Parse the JSON response
    schema_info = response.json()
    
    # Define the output file path
    output_file_path = 'slack_schema_info.json'
    
    # Write the JSON response to a file
    with open(output_file_path, 'w') as json_file:
        json.dump(schema_info, json_file, indent=4)
    
    print(f"Schema information saved to {output_file_path}")
else:
    print("Failed to retrieve schema information")
    print("Status Code:", response.status_code)
    print("Response:", response.text)