"""
Project 01: Langchain Chatbot with OpenAI
==========================================
A simple conversational chatbot built using:
- LangChain for prompt chaining
- OpenAI GPT-3.5-turbo as the LLM backend
- Streamlit for the web UI
- LangSmith for tracing and monitoring

Author: Ganji Anirudh
"""

from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser

import streamlit as st
from dotenv import load_dotenv
import os

# Load environment variables from .env file
load_dotenv()
os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

# LangSmith tracking for observability
os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")

# ---------------------------------------------------------
# Prompt Template
# ---------------------------------------------------------
prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "You are a helpful assistant. Please respond to the user queries."),
        ("user", "Question: {question}")
    ]
)

# ---------------------------------------------------------
# Streamlit UI
# ---------------------------------------------------------
st.set_page_config(page_title="LangChain Chatbot", page_icon="🤖")
st.title("🤖 Langchain Demo with OpenAI API")
st.markdown("Ask me anything! Powered by GPT-3.5-turbo & LangChain.")

input_text = st.text_input("🔍 Search the topic you want:")

# ---------------------------------------------------------
# LLM Chain
# ---------------------------------------------------------
llm = ChatOpenAI(model="gpt-3.5-turbo")
output_parser = StrOutputParser()
chain = prompt | llm | output_parser

if input_text:
    with st.spinner("Thinking..."):
        response = chain.invoke({"question": input_text})
    st.success("Response:")
    st.write(response)