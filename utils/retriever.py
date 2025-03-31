from langchain_community.document_loaders import PyPDFLoader, Docx2txtLoader, UnstructuredExcelLoader, TextLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings import OpenAIEmbeddings
from langchain_community.vectorstores import FAISS

def load_pdf(file_path):
    loader = PyPDFLoader(file_path)
    return loader.load()

def load_docx(file_path):
    # Supports both .doc and .docx by using the same loader
    loader = Docx2txtLoader(file_path)
    return loader.load()

def load_xls(file_path):
    loader = UnstructuredExcelLoader(file_path)
    return loader.load()

def load_txt(file_path):
    loader = TextLoader(file_path)
    return loader.load()

def retrieve_documents(file_paths):
    documents = []
    for file_path in file_paths:
        if file_path.endswith('.pdf'):
            documents.extend(load_pdf(file_path))
        elif file_path.endswith('.doc') or file_path.endswith('.docx'):
            documents.extend(load_docx(file_path))
        elif file_path.endswith('.xls'):
            documents.extend(load_xls(file_path))
        elif file_path.endswith('.txt'):
            documents.extend(load_txt(file_path))
    return documents

def create_vector_store(documents):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=1000, chunk_overlap=100)
    split_docs = text_splitter.split_documents(documents)
    embeddings = OpenAIEmbeddings()
    vector_store = FAISS.from_documents(split_docs, embeddings)
    return vector_store