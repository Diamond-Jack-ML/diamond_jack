from langchain_community.document_loaders.athena import AthenaLoader
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings

import os

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')  # Make sure your environment variable is set

# Read the query from the SQL file
with open('confluence_query.sql', 'r') as q:
    confluence_query = q.read()

# Load Confluence data
confluence_docs = AthenaLoader(
    query=confluence_query,
    database="confluence",
    s3_output_uri="s3://diamondjack/confluence_query_results/",
    profile_name="datasharing",
    metadata_columns=["page_id", "page_title", "page_created", "page_content", "page_details"]
).load()

# Combine all documents
all_docs = confluence_docs

# Vectorize and load into Chroma
embeddings = OpenAIEmbeddings()
vecdb = Chroma.from_documents(all_docs, embeddings, persist_directory="./confluence_db")
