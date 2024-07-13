from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
import streamlit as st
import os
import sqlite3
import json

# Ensure the OpenAI API key is set
openai_api_key = os.getenv('OPENAI_API_KEY')
if not openai_api_key:
    raise ValueError("The OpenAI API key is not set. Please set the environment variable 'OPENAI_API_KEY'.")

# Declare the foundational model and prompt template
template = """
You are an assistant tasked with answering questions about Confluence pages.
Refer to the following Confluence pages as reference.
Keep your answer concise, using a maximum of three sentences.
Question: {question}
Chat Threads: {page_content}
Answer:
"""
prompt = ChatPromptTemplate.from_template(template)
llm = ChatOpenAI(model="gpt-4-0125-preview")

# Function to get Confluence page content from SQLite database
def get_confluence_pages():
    conn = sqlite3.connect('./confluence_db/chroma.sqlite3')
    cursor = conn.cursor()
    cursor.execute("SELECT metadata FROM embeddings_queue")
    rows = cursor.fetchall()
    conn.close()
    
    # Extract page content assuming 'page_content' is the correct key
    return [json.loads(row[0])['page_title'] + ": " + json.loads(row[0]).get('page_content', '') for row in rows]

# Function to get answer
def get_answer(question):
    db = Chroma(persist_directory="./confluence_db", embedding_function=OpenAIEmbeddings(openai_api_key=openai_api_key))
    retriever = db.as_retriever()
    pages = get_confluence_pages()
    
    # Prepare the page content as a single string
    page_content = "\n\n".join(pages)
    
    # Prepare inputs for the RAG chain
    inputs = {"page_content": page_content, "question": question}
    rag_chain = (prompt | llm | StrOutputParser())
    
    # Fetch the answer using the RAG chain
    answer = rag_chain.invoke(inputs)
    return answer

# Streamlit UI
st.title("Confluence - Q&A Bot")

with st.form("my_form"):
    sample_question = "What is the most discussed topic in Confluence?"
    question = st.text_area("Enter text:", sample_question)
    submitted = st.form_submit_button("Submit")
    if submitted:
        answer = get_answer(question)
        st.info(answer)
