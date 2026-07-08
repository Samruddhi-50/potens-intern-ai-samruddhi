# 📄 AI Document Assistant (RAG)

## Overview

The AI Document Assistant is a Retrieval-Augmented Generation (RAG) application that enables users to ask questions about PDF documents and compare documents for contradictions using semantic search and Google Gemini.

The system extracts text from PDF files, generates vector embeddings using Sentence Transformers, stores them in ChromaDB, retrieves relevant information, and generates accurate responses using Google Gemini.

---

## Features

- 📄 PDF document ingestion
- ✂️ Intelligent text chunking
- 🔍 Semantic search using ChromaDB
- 🤖 AI-powered question answering using Google Gemini
- ⚖️ Document contradiction detection
- 📚 Source citations with page numbers
- 🌍 Multilingual support
- 🖥️ Interactive Streamlit interface
- 🚀 REST API using FastAPI

---

## Tech Stack

- Python
- FastAPI
- Streamlit
- ChromaDB
- Sentence Transformers
- Google Gemini API
- PyMuPDF
- Deep Translator

---

## Project Structure

```
potens-intern-ai-samruddhi/
│
├── api/
│   └── main.py
│
├── app/
│   └── streamlit_app.py
│
├── utils/
│   ├── pdf_loader.py
│   ├── chunker.py
│   ├── embedding.py
│   ├── retriever.py
│   ├── gemini.py
│   ├── contradiction.py
│   └── translator.py
│
├── documents/
├── chroma_db/
├── requirements.txt
├── README.md
└── .env
```

---

## Installation

### Clone Repository

```bash
git clone <repository_url>
cd potens-intern-ai-samruddhi
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Configure Environment Variables

Create a `.env` file in the project root.

```text
GEMINI_API_KEY=YOUR_API_KEY
```

---

## Run FastAPI

```bash
python -m uvicorn api.main:app --reload
```

Swagger UI:

```
http://127.0.0.1:8000/docs
```

---

## Run Streamlit

```bash
python -m streamlit run app/streamlit_app.py
```

---

## API Endpoints

### GET /

Returns API status.

### POST /ask

Ask questions from uploaded PDF documents.

Example:

```json
{
  "question": "What is the leave policy?"
}
```

---

### POST /contradict

Compare two documents.

Example:

```json
{
  "document1": "Leave-Policy.pdf",
  "document2": "Employee-Handbook.pdf",
  "topic": "Leave Policy"
}
```

---

## Workflow

1. Upload PDF documents
2. Extract text
3. Split into chunks
4. Generate embeddings
5. Store in ChromaDB
6. Retrieve relevant chunks
7. Generate answer using Gemini
8. Display citations

---

## Future Improvements

- OCR support
- Confidence score
- Better document filtering
- Conversation memory
- Support for more file formats

---

## AI Usage

AI assistance was used for:

- Debugging
- FastAPI development
- Prompt engineering
- Streamlit UI improvements
- Code refactoring

All generated code was reviewed, modified, and tested before submission.

---

## Author

Samruddhi Londhe