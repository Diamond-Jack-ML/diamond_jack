import requests
import os
from requests.auth import HTTPBasicAuth

# Configuration for Confluence API
BASE_URL = os.getenv('CONFLUENCE_BASE_URL')
API_TOKEN = os.getenv('ATLASSIAN_API_TOKEN')
USER_EMAIL = os.getenv('ATLASSIAN_USER_EMAIL')

def create_confluence_page(space_key, parent_page_id, page_title, content_body):
    """
    Create a new Confluence page.

    Args:
    - space_key (str): The key of the Confluence space.
    - parent_page_id (str): The ID of the parent page.
    - page_title (str): The title of the new page.
    - content_body (str): The content of the new page in HTML format.

    Returns:
    - response: The response from the Confluence API.
    """
    payload = {
        "type": "page",
        "title": page_title,
        "space": {"key": space_key},
        "ancestors": [{"id": parent_page_id}],
        "body": {
            "storage": {
                "value": content_body,
                "representation": "storage"
            }
        }
    }

    response = requests.post(
        BASE_URL,
        json=payload,
        auth=HTTPBasicAuth(USER_EMAIL, API_TOKEN)
    )

    if response.status_code == 200:
        print("Page created successfully.")
    else:
        print(f"Failed to create page. Status code: {response.status_code}")
        print(response.text)

    return response

# Add other necessary Confluence methods here
