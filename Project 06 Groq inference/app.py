"""
Project 06: Chat-Groq Agent with RAG
======================================
A RAG-powered chatbot using:
- Groq API with Llama3-70b for ultra-fast inference
- FAISS as the vector store
- Ollama Embeddings for local embeddings
- LangChain for document loading, splitting, and retrieval
- Streamlit for interactive UI

Author: Ganji Anirudh
"""

import streamlit as st
import os
import time
from langchain_groq import ChatGroq
from langchain_community.document_loaders import WebBaseLoader
from langchain_community.embeddings import OllamaEmbeddings
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain.chains import create_retrieval_chain
from langchain_community.vectorstores import FAISS
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Load the Groq API key
groq_api_key = os.environ.get("GROQ_API_KEY")
if not groq_api_key:
    st.error("❌ GROQ_API_KEY not found. Please set it in your .env file.")
    st.stop()

# ---------------------------------------------------------
# Initialize vector store (cached in session state)
# ---------------------------------------------------------
if "vector" not in st.session_state:
    with st.spinner("🔄 Loading and embedding documents..."):
        st.session_state.embeddings = OllamaEmbeddings()
        st.session_state.loader = WebBaseLoader("https://docs.smith.langchain.com/")
        st.session_state.docs = st.session_state.loader.load()

        st.session_state.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000, chunk_overlap=200
        )
        st.session_state.final_documents = st.session_state.text_splitter.split_documents(
            st.session_state.docs
        )
        st.session_state.vectors = FAISS.from_documents(
            st.session_state.final_documents,
            st.session_state.embeddings
        )
        st.session_state.vector = True
    st.success("✅ Vector store ready!")

# ---------------------------------------------------------
# Streamlit UI
# ---------------------------------------------------------
st.set_page_config(page_title="Chat-Groq RAG Agent", page_icon="⚡")
st.title("⚡ Chat-Groq RAG Agent")
st.markdown("Powered by **Groq + Llama3-70b** for blazing fast responses.")

# ---------------------------------------------------------
# LLM and RAG Chain
# ---------------------------------------------------------
llm = ChatGroq(groq_api_key=groq_api_key, model="llama3-70b-8192")

prompt_template = ChatPromptTemplate.from_template(
    """
    Answer the questions based on the provided context only.
    Please provide the most accurate response based on the question.
    <context>
    {context}
    </context>
    Question: {input}
    """
)

document_chain = create_stuff_documents_chain(llm, prompt_template)
retriever = st.session_state.vectors.as_retriever()
retrieval_chain = create_retrieval_chain(retriever, document_chain)

# ---------------------------------------------------------
# User Input
# ---------------------------------------------------------
user_prompt = st.text_input("💬 Enter your question here:")

if user_prompt:
    with st.spinner("⚡ Generating response..."):
        start = time.process_time()
        response = retrieval_chain.invoke({"input": user_prompt})
        elapsed = round(time.process_time() - start, 3)

    st.success(f"✅ Response (in {elapsed}s):")
    st.write(response["answer"])

    # Show relevant document chunks in expander
    with st.expander("📄 Document Similarity Search"):
        for i, doc in enumerate(response["context"]):
            st.markdown(f"**Chunk {i+1}:**")
            st.write(doc.page_content)
            st.divider()