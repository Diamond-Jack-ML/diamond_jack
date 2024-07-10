import requests

# Replace with your actual API key
api_key = '9f171058-58e0-41c6-81f3-52850faaf68f'

# API endpoint
url = 'https://api.bodygraphchart.com/v221006/hd-data'

# Data for the request (replace with actual values)
data = {
    'date': '1992-08-29 07:43',
    'timezone': 'America/New_York'
}

# Headers for the request
headers = {
    'Authorization': f'Bearer {api_key}',
    'Content-Type': 'application/json'
}

# Make the API request
response = requests.post(url, json=data, headers=headers)

# Check the response status
if response.status_code == 200:
    # Successfully generated the chart
    chart_data = response.json()
    print('Chart generated successfully:', chart_data)
else:
    # Handle errors
    print('Error generating chart:', response.status_code, response.text)
