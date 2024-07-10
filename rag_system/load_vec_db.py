from langchain_community.document_loaders.athena import AthenaLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

import os

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')  # Replace with your actual OpenAI API key

# Read the queries from the SQL files
with open('jira_query.sql', 'r') as q:
    jira_query = q.read()

with open('confluence_query.sql', 'r') as q:
    confluence_query = q.read()

with open('slack_query.sql', 'r') as q:
    slack_query = q.read()

# Load Jira data
jira_docs = AthenaLoader(
    query=jira_query,
    database="jira",
    s3_output_uri="s3://diamondjack/jira_query_results/",
    profile_name="datasharing",
    metadata_columns=["issue_id", "issue_summary", "issue_created"]
).load()

# Load Confluence data
confluence_docs = AthenaLoader(
    query=confluence_query,
    database="confluence",
    s3_output_uri="s3://diamondjack/confluence_query_results/",
    profile_name="datasharing",
    metadata_columns=["page_id", "page_title", "page_created"]
).load()

# Load Slack data
slack_docs = AthenaLoader(
    query=slack_query,
    database="slack",
    s3_output_uri="s3://diamondjack/slack_query_results/",
    profile_name="datasharing",
    metadata_columns=["channel_id", "channel_name"]
).load()

# Combine all documents
all_docs = jira_docs + confluence_docs + slack_docs

# Vectorize and load into Chroma
embeddings = OpenAIEmbeddings()
vecdb = Chroma.from_documents(all_docs, embeddings, persist_directory="./db")
vecdb.persist()
