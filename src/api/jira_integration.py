import requests
import json
import os
import base64

# Jira API configuration
JIRA_BASE_URL = "https://agency-audia.atlassian.net"
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")
JIRA_USER_EMAIL = os.getenv("JIRA_USER_EMAIL")

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
        "leadAccountId": "your-account-id"  # Update with your actual lead account ID
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
            "description": description,
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
 
    # Example: Create a new project
    project_name = "Example Project"
    project_key = "EXMP"
    project = create_project(project_name, project_key)
    print(f"Created project: {project}")

    # Example: Create a new issue
    summary = "Example task"
    description = "This is an example task created via the Jira API."
    issue = create_issue(project_key, summary, description)
    print(f"Created issue: {issue}")

if __name__ == "__main__":
    main()
