# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

---

## [1.1.0] - 2024-07-07

### Added
- `LICENSE` file (MIT License)
- `CONTRIBUTING.md` with setup guide and PR instructions
- `.env.example` template for environment variable configuration
- `CHANGELOG.md` to track project changes
- "Project Made By" section in README with author details

### Changed
- `Project 01 chatbot/app.py`: Fixed typos, added docstring, improved Streamlit UI with spinner and page config
- `Project 06 Groq inference/app.py`: Fixed typos, improved error handling, refactored variable names, improved UI
- `requirements.txt`: Added version pins, organized into categories with comments

### Fixed
- Fixed typo in system prompt: "You are ahelpful assistant" → "You are a helpful assistant"
- Fixed typo in expander label: "Documnet Similarity Search" → "Document Similarity Search"
- Fixed variable naming conflict in Project 06 (`prompt` used twice)

---

## [1.0.0] - 2024-06-01

### Added
- Initial release of RAG Projects repository
- Project 01: LangChain Chatbot with OpenAI
- Project 02: Production Grade LLM as API with FastAPI
- Project 03: Getting Started with RAG Pipeline (ChromaDB + FAISS)
- Project 04: Advanced RAG Q&A with Retriever and Chain
- Project 05: Advanced RAG Q&A with Multiple Data Sources
- Project 06: End-to-End RAG with Groq Inference Engine
- Project 07: Gen AI Powered App with HuggingFace + Mistral
- Project 08: Powerful Document Q&A Chatbot with Llama3 + Groq
- Project 09: Advanced Q&A Chatbot with RAGStack + AstraDB
- Project 10: On-Device AI RAG with ObjectBox Vector Database
- Project 11: Image Enhancer App
