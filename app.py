import streamlit as st
import tempfile
import os
from utils.retriever import load_pdf, load_docx, load_xls, load_txt, create_vector_store

from langchain_community.chat_models import ChatOpenAI
from langchain.chains import ConversationalRetrievalChain
from langchain.memory import ConversationBufferMemory

def get_documents_from_uploaded(uploaded_file):
    # Write the uploaded file to a temporary file, then load using the appropriate loader.
    filename = uploaded_file.name
    suffix = "." + filename.split('.')[-1]
    with tempfile.NamedTemporaryFile(delete=False, suffix=suffix) as tmp:
        tmp.write(uploaded_file.getvalue())
        temp_path = tmp.name

    if filename.endswith('.pdf'):
        documents = load_pdf(temp_path)
    elif filename.endswith('.doc') or filename.endswith('.docx'):
        documents = load_docx(temp_path)
    elif filename.endswith('.xls'):
        documents = load_xls(temp_path)
    elif filename.endswith('.txt'):
        documents = load_txt(temp_path)
    else:
        documents = []
    os.remove(temp_path)
    return documents

def get_content_from_documents(documents):
    # Combine all document page_content into one string
    return "\n".join([doc.page_content for doc in documents])

def main():
    st.title("RAG Chat with Your Document")
    st.write("Upload a document (PDF, DOC/DOCX, XLS, TXT) and ask questions about its content.")

    uploaded_file = st.file_uploader("Upload Document", type=["pdf", "doc", "docx", "xls", "txt"])
    if uploaded_file is not None:
        with st.spinner("Processing document..."):
            documents = get_documents_from_uploaded(uploaded_file)
        if not documents:
            st.error("Could not process the document.")
            return

        # Display the extracted content (optional)
        content = get_content_from_documents(documents)
        st.subheader("Extracted Document Content")
        st.text_area("", content, height=200)

        # Create vector store for retrieval
        with st.spinner("Creating vector store..."):
            vector_store = create_vector_store(documents)

        # Initialize OpenAI chat model and conversational retrieval chain
        llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
        memory = ConversationBufferMemory(memory_key="chat_history", return_messages=True)
        qa_chain = ConversationalRetrievalChain.from_llm(llm, retriever=vector_store.as_retriever(), memory=memory)

        st.subheader("Chat with Your Document")
        query = st.text_input("Enter your question:")

        if query:
            with st.spinner("Generating answer..."):
                result = qa_chain({"question": query})
            st.write(result["answer"])

if __name__ == "__main__":
    main()