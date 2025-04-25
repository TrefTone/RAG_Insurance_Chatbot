from langchain_community.document_loaders import PyMuPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter

splitter = RecursiveCharacterTextSplitter(chunk_size=300, chunk_overlap=80)

def load_and_chunk_pdfs(pdf_paths):
    all_chunks = []
    for pdf, label in pdf_paths:
        docs = PyMuPDFLoader(pdf).load()
        for doc in docs:
            doc.metadata["source"] = label
        chunks = splitter.split_documents(docs)
        all_chunks.extend(chunks)
    return all_chunks