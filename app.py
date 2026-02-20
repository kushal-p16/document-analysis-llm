import streamlit as st
from backend import PDFEngine
import tempfile

st.set_page_config(page_title="AI PDF Analyst", layout="wide")

st.title("📄 AI PDF Analysis System")
st.write("Upload any PDF and let the AI summarize it and answer your questions.")

engine = PDFEngine()

uploaded_pdf = st.file_uploader("Upload your PDF", type="pdf")

if uploaded_pdf:
    with tempfile.NamedTemporaryFile(delete=False, suffix=".pdf") as tmp:
        tmp.write(uploaded_pdf.read())
        pdf_path = tmp.name

    st.info("Processing PDF... Please wait ⏳")

    result = engine.load_pdf(pdf_path)

    st.success("PDF Processed Successfully ✔")

    # ============================
    # SUMMARY
    # ============================
    st.subheader("📌 Summary")
    st.write(result["summary"])

    # ============================
    # USER QUESTION
    # ============================
    st.subheader("💬 Ask Any Question About the PDF")
    user_q = st.text_input("Your Question:")

    if user_q:
        with st.spinner("Thinking... 🤖"):
            answer = engine.ask(user_q)

        st.write("### 🤖 Answer")
        st.success(answer["answer"])

        st.write("### 📌 Source")
        st.info(answer["passage"])