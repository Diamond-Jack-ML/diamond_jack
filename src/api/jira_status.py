import os
import requests
import json
import base64

# Jira API configuration
JIRA_BASE_URL = "https://agency-audia.atlassian.net"
JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")
JIRA_USER_EMAIL = os.getenv("JIRA_USER_EMAIL")

def get_jira_headers():
    auth = f"{JIRA_USER_EMAIL}:{JIRA_API_TOKEN}"
    auth_base64 = base64.b64encode(auth.encode('ascii')).decode('ascii')
    headers = {
        "Authorization": f"Basic {auth_base64}",
        "Content-Type": "application/json"
    }
    return headers

def fetch_jira_project_state():
    url = f"{JIRA_BASE_URL}/rest/api/3/search"
    query = {
        'jql': 'project = MVP ORDER BY created DESC',
        'fields': 'summary,status,assignee,issuetype',
        'maxResults': 50
    }
    issues = []
    start_at = 0

    while True:
        query['startAt'] = start_at
        response = requests.get(url, headers=get_jira_headers(), params=query)
        data = response.json()
        issues.extend(data.get('issues', []))
        if len(data.get('issues', [])) < query['maxResults']:
            break
        start_at += query['maxResults']

    return issues

def format_jira_data(issues):
    formatted_data = []
    for issue in issues:
        summary = issue['fields'].get('summary', 'No summary')
        status = issue['fields'].get('status', {}).get('name', 'No status')
        issue_type = issue['fields'].get('issuetype', {}).get('name', 'No type')
        assignee_field = issue['fields'].get('assignee')
        assignee = assignee_field['displayName'] if assignee_field else 'Unassigned'
        formatted_data.append(f"Issue Type: {issue_type}, Summary: {summary}, Status: {status}, Assignee: {assignee}")
    return "\n".join(formatted_data)

def save_jira_data_to_file(issues, filename="jira_data.txt"):
    formatted_data = format_jira_data(issues)
    with open(filename, 'w') as file:
        file.write(formatted_data)

def main():
    # Fetch current Jira project state
    issues = fetch_jira_project_state()

    # Save Jira data to a text file
    save_jira_data_to_file(issues)
    print(f"Jira data saved to jira_data.txt")

if __name__ == "__main__":
    main()
