from langchain_community.document_loaders.athena import AthenaLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

import os

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')  # Make sure your environment variable is set

# Read the query from the SQL file
with open('slack_query.sql', 'r') as q:
    slack_query = q.read()

# Load Slack data
slack_docs = AthenaLoader(
    query=slack_query,
    database="slack",
    s3_output_uri="s3://diamondjack/slack_query_results/",
    profile_name="datasharing",
    metadata_columns=["channel_id", "channel_name"]
).load()

# Combine all documents
all_docs = slack_docs

# Vectorize and load into Chroma
embeddings = OpenAIEmbeddings()
vecdb = Chroma.from_documents(all_docs, embeddings, persist_directory="./db")
vecdb.persist()
