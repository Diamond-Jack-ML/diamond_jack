from jira import JIRA

# Set up your Jira server and credentials
jira_options = {'server': 'https://your_jira_server'}
jira = JIRA(options=jira_options, basic_auth=('your_username', 'your_password'))

# Get a specific issue
issue = jira.issue('PROJECT-123')
print(issue.fields.summary)

# Create a new issue
new_issue = jira.create_issue(project='PROJECT', summary='New issue from Python script',
                              description='Details of the issue', issuetype={'name': 'Task'})
print(new_issue)
