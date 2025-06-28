"""
app.py - Streamlit chatbot UI for MOSDAC RAG
"""
import streamlit as st
from rag import RAGPipeline

st.set_page_config(page_title="MOSDAC RAG Chatbot")
st.title("MOSDAC RAG Chatbot")

st.sidebar.title("Instructions")
st.sidebar.write("""
- Ask questions about MOSDAC data (sample: About page)
- The bot retrieves relevant info and answers
- For best results, run the data pipeline first
""")

if "rag" not in st.session_state:
    st.session_state["rag"] = RAGPipeline()

user_input = st.text_input("Ask a question about MOSDAC data:")

if user_input:
    answer = st.session_state["rag"].answer(user_input)
    st.markdown(f"**Answer:**\n{answer}") 