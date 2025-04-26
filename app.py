import streamlit as st
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain_core.prompts import ChatPromptTemplate
from langchain_groq import ChatGroq
from langchain.chains import create_retrieval_chain
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import CharacterTextSplitter
import tempfile
import os

# ----- Function to create docs and retrieval chain -----
def create_retrieval_chain_from_pdf(pdf_file):
    # Save uploaded PDF to a temp file
    temp_dir = tempfile.TemporaryDirectory()
    temp_pdf_path = os.path.join(temp_dir.name, pdf_file.name)
    with open(temp_pdf_path, "wb") as f:
        f.write(pdf_file.read())

    # Load and split PDF
    loader = PyPDFLoader(temp_pdf_path)
    pages = loader.load_and_split()

    # Create embeddings and vector store
    embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vector = FAISS.from_documents(pages, embeddings)

    # Create prompt
    template = """
    You are a helpful and knowledgeable product assistant. 
    Your job is to answer user questions about our products clearly, concisely, and politely, using the provided product documents.

    Context:
    {context}

    User Question:
    {input}

    Instructions:
    - If the answer is in the context, use it directly.
    - If the answer is not in the context, politely say you don't have enough information.
    - Keep responses short, friendly, and informative.
    - Offer to assist with related products if needed.
    """
    prompt = ChatPromptTemplate.from_template(template)

    # Load model
    llm = ChatGroq(model_name="llama3-8b-8192", groq_api_key="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")

    # Create document chain
    document_chain = create_stuff_documents_chain(llm, prompt)

    retriever = vector.as_retriever()
    retriever_chain = create_retrieval_chain(retriever, document_chain)

    return retriever_chain

# ----- Streamlit Frontend -----
st.title("📚 Product Info Chatbot")

uploaded_file = st.file_uploader("Upload your product PDF", type=["pdf"])

if uploaded_file is not None:
    st.success("PDF Uploaded Successfully!")
    # Create chain
    retrieval_chain = create_retrieval_chain_from_pdf(uploaded_file)

    # Chat input
    user_question = st.text_input("Ask your question:")

    if st.button("Get Answer") and user_question:
        with st.spinner("Searching for the answer..."):
            response = retrieval_chain.invoke({"input": user_question})
            answer = response['answer']
            st.markdown("### 📢 Answer:")
            st.write(answer)


