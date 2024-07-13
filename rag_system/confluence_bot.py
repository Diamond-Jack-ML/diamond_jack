from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from langchain_community.vectorstores import Chroma
from langchain_openai import OpenAIEmbeddings
import streamlit as st
import os

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


# Function to get answer
def get_answer(question):
    db = Chroma(persist_directory="./confluence_db", embedding_function=OpenAIEmbeddings(openai_api_key=os.getenv('OPENAI_API_KEY')))
    inputs = {"page_content": db.as_retriever(), "question": RunnablePassthrough()}
    rag_chain = (inputs | prompt | llm | StrOutputParser())
    return rag_chain.invoke(question)

# Streamlit UI
st.title("Confluence - Q&A Bot")

with st.form("my_form"):
    sample_question = "What is the most discussed topic in Confluence?"
    question = st.text_area("Enter text:", sample_question)
    submitted = st.form_submit_button("Submit")
    if submitted:
        answer = get_answer(question)
        st.info(answer)
