from jira import JIRA
import os

BASE_URL = os.getenv("ATLASSIAN_BASE_URL")
API_TOKEN = os.getenv("ATLASSIAN_API_TOKEN")
USER_EMAIL = os.getenv("ATLASSIAN_USER_EMAIL")

class JiraService:
    def __init__(self):
        self.jira = JIRA(
            server=BASE_URL,
            basic_auth=(USER_EMAIL,API_TOKEN)
        )


    def create_project(self, key, name, lead_email):
        lead_id = self.find_lead_id(lead_email)
        if not lead_id:
            raise ValueError("Lead not found")
        
        project = self.jira.create_project(
            key=key,
            name=name,
            projectTypeKey='software',
            projectTemplateKey='com.pyxis.greenhopper.jira:gh-simplified-agility-scrum',
            description=f'Project for {name}',
            lead=lead_id
        )
        return project

    def create_task(self, project_key, summary, description, issue_type='Task'):
        task = self.jira.create_issue(
            project=project_key,
            summary=summary,
            description=description,
            issuetype={'name': issue_type}
        )
        return task

    def create_subtask(self, parent_task_key, summary, description):
        subtask = self.jira.create_issue(
            project=parent_task_key.split('-')[0],
            summary=summary,
            description=description,
            issuetype={'name': 'Sub-task'},
            parent={'key': parent_task_key}
        )
        return subtask

    # Other existing methods
