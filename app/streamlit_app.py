import streamlit as st
import requests

from utils.translator import (
    translate_to_english,
    translate_from_english
)

API_URL = "http://127.0.0.1:8000"

# -------------------------------------------------
# Page Configuration
# -------------------------------------------------

st.set_page_config(
    page_title="AI Document Assistant",
    page_icon="📄",
    layout="wide"
)

# -------------------------------------------------
# Sidebar
# -------------------------------------------------

with st.sidebar:

    st.title("📄 AI Document Assistant")

    st.markdown("---")

    st.subheader("Project Features")

    st.write("✅ Ask Questions")
    st.write("✅ Compare Documents")
    st.write("✅ Multilingual Support")
    st.write("✅ Gemini AI")
    st.write("✅ ChromaDB")

    st.markdown("---")

    st.subheader("Supported Languages")

    st.write("🇬🇧 English")
    st.write("🇮🇳 Hindi")
    st.write("🇮🇳 Marathi")
    st.write("🇫🇷 French")
    st.write("🇪🇸 Spanish")

    st.markdown("---")

    try:
        requests.get(API_URL, timeout=3)
        st.success("🟢 FastAPI Connected")

    except:
        st.error("🔴 FastAPI Not Running")

    st.markdown("---")

    st.caption("Potens AI/ML Internship Assignment")

# -------------------------------------------------
# Title
# -------------------------------------------------

st.title("📄 AI Document Assistant (RAG)")

st.caption(
    "Retrieval-Augmented Generation using FastAPI, ChromaDB, Sentence Transformers & Google Gemini"
)

st.write(
    "Ask questions about your PDF documents or compare two documents."
)

# -------------------------------------------------
# Tabs
# -------------------------------------------------

tab1, tab2 = st.tabs(
    [
        "📄 Ask Questions",
        "📑 Compare Documents"
    ]
)

# ===========================================================
# ASK QUESTIONS
# ===========================================================

with tab1:

    st.header("Ask a Question")

    language = st.selectbox(
        "Select Language",
        [
            "English",
            "Hindi",
            "Marathi",
            "French",
            "Spanish"
        ]
    )

    question = st.text_input(
        "Enter your question"
    )

    st.info(
        """
### Example Questions

• What is the leave policy?

• What is the work from home policy?

• What is the code of conduct?

• What are the security policies?
"""
    )

    if st.button("Get Answer"):

        if question.strip() == "":

            st.warning("Please enter a question.")

        else:

            with st.spinner("Generating answer..."):

                try:

                    english_question = translate_to_english(question)

                    response = requests.post(
                        f"{API_URL}/ask",
                        json={
                            "question": english_question
                        }
                    )

                    if response.status_code == 200:

                        result = response.json()

                        translated_answer = translate_from_english(
                            result["answer"],
                            language
                        )

                        st.success("Answer Generated Successfully!")

                        st.subheader("Answer")

                        st.write(translated_answer)

                        st.subheader("Citations")

                        for citation in result["citations"]:

                            with st.expander(
                                f"📄 {citation['file']} | Page {citation['page']}"
                            ):

                                st.write(citation["snippet"])

                    else:

                        st.error("Unable to get response from API.")

                except Exception as e:

                    st.error(f"Error: {e}")

# ===========================================================
# DOCUMENT COMPARISON
# ===========================================================

with tab2:

    st.header("Compare Documents")

    document1 = st.text_input(
        "Document 1",
        placeholder="Leave-Policy.pdf"
    )

    document2 = st.text_input(
        "Document 2",
        placeholder="Employee-Handbook.pdf"
    )

    topic = st.text_input(
        "Topic",
        placeholder="Leave Policy"
    )

    if st.button("Compare Documents"):

        if (
            document1.strip() == ""
            or document2.strip() == ""
            or topic.strip() == ""
        ):

            st.warning("Please fill all fields.")

        else:

            with st.spinner("Comparing documents..."):

                try:

                    response = requests.post(
                        f"{API_URL}/contradict",
                        json={
                            "document1": document1,
                            "document2": document2,
                            "topic": topic
                        }
                    )

                    if response.status_code == 200:

                        result = response.json()

                        st.success("Comparison Completed!")

                        st.subheader("Comparison")

                        st.write(result["answer"])

                        st.subheader("Evidence")

                        for evidence in result["evidence"]:

                            with st.expander(
                                f"📄 {evidence['file']} | Page {evidence['page']}"
                            ):

                                st.write(evidence["snippet"])

                    else:

                        st.error("Unable to compare documents.")

                except Exception as e:

                    st.error(f"Error: {e}")