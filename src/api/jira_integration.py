import requests
import json
import os
import base64

# Jira API configuration
JIRA_BASE_URL = "https://agency-audia.atlassian.net"
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")
JIRA_USER_EMAIL = os.getenv("JIRA_USER_EMAIL")
JIRA_LEAD_ID = os.getenv("JIRA_LEAD_ID")

def get_headers():
    auth = f"{JIRA_USER_EMAIL}:{JIRA_API_TOKEN}"
    auth_bytes = auth.encode('ascii')
    auth_base64 = base64.b64encode(auth_bytes).decode('ascii')

    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/json"
    }
    
    print(f"Authorization Header: {headers['Authorization']}")
    return headers

def create_project(project_name, project_key, project_type="software"):
    url = f"{JIRA_BASE_URL}/rest/api/3/project"
    payload = {
        "key": project_key,
        "name": project_name,
        "projectTypeKey": project_type,
        "leadAccountId": JIRA_LEAD_ID  # Update with your actual lead account ID
    }

    response = requests.post(url, headers=get_headers(), data=json.dumps(payload))
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Body: {response.text}")
    return response.json()

def create_issue(project_key, summary, description, issue_type="Task"):
    url = f"{JIRA_BASE_URL}/rest/api/3/issue"
    payload = {
        "fields": {
            "project": {
                "key": project_key
            },
            "summary": summary,
            "description": {
                "type": "doc",
                "version": 1,
                "content": [
                    {
                        "type": "paragraph",
                        "content": [
                            {
                                "type": "text",
                                "text": description
                            }
                        ]
                    }
                ]
            },
            "issuetype": {
                "name": issue_type
            }
        }
    }

    response = requests.post(url, headers=get_headers(), data=json.dumps(payload))
    print(f"Response Status Code: {response.status_code}")
    print(f"Response Body: {response.text}")
    return response.json()

def main():
    # Example: Use an existing project key
    project_key = "MVP"  # Replace with an actual project key that exists in your Jira instance

    # Check if the project already exists
    url = f"{JIRA_BASE_URL}/rest/api/3/project/{project_key}"
    response = requests.get(url, headers=get_headers())
    if response.status_code == 200:
        print(f"Project {project_key} already exists.")
    else:
        # Create a new project
        project_name = "Example Project"
        project = create_project(project_name, project_key)
        print(f"Created project: {project}")

    # Create a new issue in the existing project
    summary = "Example task"
    description = "This is an example task created via the Jira API."
    issue = create_issue(project_key, summary, description)
    print(f"Created issue: {issue}")

if __name__ == "__main__":
    main()
