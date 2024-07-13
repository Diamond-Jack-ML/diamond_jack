import os
import requests
from requests.auth import HTTPBasicAuth
import base64
import json

# Jira API configuration
BASE_URL = 'https://agency-audia.atlassian.net/wiki/rest/api'
API_TOKEN = os.getenv("ATLASSIAN_API_TOKEN")
USER_EMAIL = os.getenv("ATLASSIAN_USER_EMAIL")


def get_spaces():
    url = f'{BASE_URL}/space'
    response = requests.get(url, auth=HTTPBasicAuth(USER_EMAIL, API_TOKEN))
    response.raise_for_status()
    return response.json()['results']

def get_pages_in_space(space_key):
    url = f'{BASE_URL}/space/{space_key}/content'
    response = requests.get(url, auth=HTTPBasicAuth(USER_EMAIL, API_TOKEN))
    response.raise_for_status()
    return response.json()['page']['results']

def get_page_content(page_id):
    url = f'{BASE_URL}/content/{page_id}?expand=body.storage'
    response = requests.get(url, auth=HTTPBasicAuth(USER_EMAIL, API_TOKEN))
    response.raise_for_status()
    return response.json()['body']['storage']['value']

def save_to_text_file(content, filename):
    os.makedirs(os.path.dirname(filename), exist_ok=True)
    with open(filename, 'w', encoding='utf-8') as f:
        f.write(content)

def process_confluence_space(space_key, output_dir):
    pages = get_pages_in_space(space_key)
    for page in pages:
        page_id = page['id']
        page_title = page['title']
        content = get_page_content(page_id)
        filename = os.path.join(output_dir, f'{page_title}.txt')
        save_to_text_file(content, filename)

def fetch_and_store_confluence_data(output_dir):
    spaces = get_spaces()
    for space in spaces:
        space_key = space['key']
        space_name = space['name']
        space_dir = os.path.join(output_dir, space_name)
        process_confluence_space(space_key, space_dir)

def load_text_files(directory):
    text_data = []
    for root, _, files in os.walk(directory):
        for file in files:
            with open(os.path.join(root, file), 'r', encoding='utf-8') as f:
                text_data.append(f.read())
    return text_data