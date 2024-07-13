from langchain_community.document_loaders.athena import AthenaLoader
import os

os.environ['OPENAI_API_KEY'] = os.getenv('OPENAI_API_KEY')  # Ensure your environment variable is set

# Read the query from the SQL file
with open('confluence_query.sql', 'r') as q:
    confluence_query = q.read()

# Execute Athena query
athena_loader = AthenaLoader(
    query=confluence_query,
    database="confluence",
    s3_output_uri="s3://diamondjack/confluence_query_results/",
    profile_name="datasharing",
    metadata_columns=["page_id", "page_title", "page_created", "page_content", "page_details"]
)

with open("athena_test_output.txt", "w") as output_file:
    output_file.write("Executing Athena query...\n")
    confluence_docs = athena_loader.load()
    output_file.write(f"Number of documents loaded: {len(confluence_docs)}\n")

    # Check the contents of the loaded documents
    for doc in confluence_docs:
        output_file.write(f"Document: page_content='{doc.page_content}' metadata={doc.metadata}\n")
