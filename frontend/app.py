import streamlit as st

from api import upload_pdf, ask_question
from components import show_message
from styles import load_css

st.set_page_config(
    page_title="FinInsight AI",
    page_icon="📊",
    layout="wide"
)

load_css()

if "messages" not in st.session_state:
    st.session_state.messages = []

if "uploaded" not in st.session_state:
    st.session_state.uploaded = False

st.title("📊 FinInsight AI")
st.caption("AI Financial Document Intelligence")

st.divider()

st.subheader("📄 Upload PDF")

uploaded_file = st.file_uploader(
    "Choose a PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    if st.button("Upload Document", use_container_width=True):

        with st.spinner("Uploading and indexing PDF..."):

            response = upload_pdf(uploaded_file)

            if response:

                st.success("PDF indexed successfully.")

                st.session_state.uploaded = True

st.divider()

st.subheader("💬 Ask Questions")

if st.session_state.uploaded:

    question = st.text_input(
        "Ask anything about the uploaded PDF"
    )

    if st.button("Ask AI", use_container_width=True):

        if question.strip():

            st.session_state.messages.append(
                {
                    "role": "user",
                    "content": question
                }
            )

            with st.spinner("Thinking..."):

                result = ask_question(question)

            st.session_state.messages.append(
                {
                    "role": "assistant",
                    "content": result["answer"],
                    "sources": result["sources"]
                }
            )

else:

    st.info("Upload a PDF first.")

st.divider()

st.subheader("Conversation")

for message in st.session_state.messages:

    show_message(message)

st.divider()

if st.button("🗑 Clear Chat"):

    st.session_state.messages = []

    st.rerun()