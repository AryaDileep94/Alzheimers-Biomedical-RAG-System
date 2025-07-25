# -*- coding: utf-8 -*-
"""app

Automatically generated by Colab.

Original file is located at
    https://colab.research.google.com/drive/1rEG6pztSYkO0iQsPyvWAVuk3BgYrozea
"""

import streamlit as st
from rag_pipeline import load_rag_chain, query_rag

# --- 🌐 Page Setup ---
st.set_page_config(
    page_title="Alzheimer's QnA App",
    page_icon="🧠",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# --- 🌈 Styling ---
st.markdown("""
    <style>
        .stApp {
            background-color: #f3f4f6;
            padding-top: 2rem;
        }
        .title-text {
            font-size: 40px;
            text-align: center;
            font-weight: bold;
            color: #4a4a4a;
        }
        .subtitle-text {
            font-size: 20px;
            text-align: center;
            color: #6c757d;
            margin-bottom: 30px;
        }
        .answer-box {
            background-color: #ffffff;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0px 0px 10px rgba(0, 0, 0, 0.1);
            font-size: 18px;
            color: #333333;
        }
    </style>
""", unsafe_allow_html=True)

# --- 🧠 Header ---
st.markdown('<div class="title-text">🧠 Alzheimer\'s Disease Q&A</div>', unsafe_allow_html=True)
st.markdown('<div class="subtitle-text">Powered by Mistral + LangChain RAG + BioMed Embeddings</div>', unsafe_allow_html=True)

# --- 📦 Load RAG Pipeline ---
with st.spinner("Loading RAG system. Please wait..."):
    rag_chain = load_rag_chain()

st.success("✅ Enter your query below.")

# --- 💬 Input Box ---
query = st.text_input(
    "💬 Ask a medical question",
    placeholder="e.g., What are the early symptoms of Alzheimer?"
)

# --- 🚀 Answer Area ---
if query:
    with st.spinner("🔍 Retrieving answer..."):
        answer = query_rag(rag_chain, query)

    st.markdown("### ✅ Answer:")
    st.markdown(f'<div class="answer-box">{answer}</div>', unsafe_allow_html=True)