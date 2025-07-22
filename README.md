# Alzheimers-Biomedical-RAG-System
A Retrieval-Augmented Generation (RAG) system for answering domain-specific questions on Alzheimer’s using LangChain, FAISS, Sentence-Transformers, and Streamlit.
## ✨ Features

- 🔍 PDF-based biomedical document ingestion
- 🧠 Domain-specific RAG pipeline
- 🗃️ Biomedical embeddings using S-PubMedBERT (MS MARCO)
- 📊 Answer evaluation using semantic similarity
- 🧪 Tested on curated Alzheimer's QA dataset

- ## 🧱 Tech Stack

- 🦙 `Mistral-7B-Instruct` (LLM via HuggingFace)
- 📚 `pritamdeka/S-PubMedBERT-MS-MARCO` for embeddings
- 🔎 FAISS vector store
- 🧠 LangChain RAG pipeline
- 📄 PDF loading via PyMuPDF
- 🧪 Evaluation using Sentence Transformers
- 🌐 Streamlit

- ## 🗂️ Project Structure
📁 alzheimers-rag-qa/
├── Alzheimer's PDFs/ # Input biomedical documents
├── app.py # Streamlit frontend
├── rag_pipeline.py # Main RAG pipeline
├── alzheimers_test_set.py # Evaluation dataset
├── .env # API keys (not tracked)
├── .gitignore # Ignore sensitive files
└── README.md # Project documentation

