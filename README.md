# MOSDAC Retrieval-Augmented Generation (RAG) System

## Overview
This project implements a Retrieval-Augmented Generation (RAG) system using data from [MOSDAC](https://www.mosdac.gov.in). It crawls, processes, and indexes MOSDAC data, enabling semantic search and conversational Q&A via a Streamlit chatbot UI.

## Features
- Data crawling and extraction (web, PDF, DOCX, XLSX)
- Text cleaning, chunking, and entity extraction
- Knowledge graph construction
- Embedding generation and FAISS vector search
- Retrieval-augmented generation with LangChain
- Streamlit-based conversational interface

## Setup
1. **Clone the repository**
2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```
3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```
4. **Download NLTK and spaCy models**
   ```python
   import nltk; nltk.download('punkt')
   import spacy; spacy.cli.download('en_core_web_sm')
   ```

## Usage
- Run each script in order:
  1. `crawl.py` - Crawl and extract data
  2. `process.py` - Clean and chunk text
  3. `embed.py` - Generate embeddings and build FAISS index
  4. `rag.py` - Retrieval-augmented generation logic
  5. `app.py` - Launch Streamlit chatbot UI

## File Structure
- `crawl.py` - Data crawling and extraction
- `process.py` - Text cleaning and chunking
- `embed.py` - Embedding generation and vector store
- `rag.py` - RAG pipeline
- `app.py` - Streamlit UI
- `utils.py` - Shared utilities

## Notes
- For geospatial queries, see the optional section in `rag.py`.
- Use GitHub or Google Drive for version control/collaboration. 