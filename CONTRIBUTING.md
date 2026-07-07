# Contributing to RAG-Projects

Thank you for your interest in contributing! 🎉

## How to Contribute

### Reporting Bugs
- Open an issue with a clear title and description
- Include steps to reproduce the bug
- Attach relevant logs or screenshots if possible

### Suggesting Features
- Open an issue with the label `enhancement`
- Describe the feature and its use case

### Submitting Pull Requests

1. **Fork** the repository
2. **Clone** your fork locally:
   ```bash
   git clone https://github.com/<your-username>/RAG_projects_master.git
   ```
3. **Create a new branch** for your feature:
   ```bash
   git checkout -b feature/your-feature-name
   ```
4. **Make your changes** with clear, descriptive commits
5. **Push** your branch:
   ```bash
   git push origin feature/your-feature-name
   ```
6. Open a **Pull Request** against the `main` branch

## Code Style

- Follow PEP 8 for Python files
- Add docstrings to all functions and classes
- Keep imports organized (standard library → third-party → local)
- Use meaningful variable and function names

## Setting Up the Dev Environment

```bash
# Clone the repo
git clone https://github.com/anirudh1261/RAG_projects_master.git
cd RAG_projects_master

# Create a virtual environment
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Copy environment variables
cp .env.example .env
# Fill in your API keys in .env
```

## Project Structure

```
RAG-Projects-master/
├── Project 01 chatbot/       # Basic LangChain chatbot
├── Project 02 APIs/          # LLM as API with FastAPI
├── Project 03 RAG Pipeline/  # Starter RAG pipeline
├── Project 04 Retriever and Chain/
├── Project 05 Advanced RAG Q&A Project/
├── Project 06 Groq inference/
├── Project 07 Gen AI/
├── Project 08 Powerful Doc Q&A Chatbot/
├── Project 09 Advance Q&A Chatbot/
├── Project 10 On-Device AI/
├── Project 11 ImageEnhancer/
├── requirements.txt
└── README.md
```

## License

By contributing, you agree that your contributions will be licensed under the **MIT License**.
