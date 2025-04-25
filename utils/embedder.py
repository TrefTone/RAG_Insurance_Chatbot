from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
import os

embedding_model = HuggingFaceEmbeddings(model_name="all-MiniLM-L6-v2")

def build_or_load_vectorstore(documents, persist_dir="embeddings"):
    index_path = os.path.join(persist_dir, "index.faiss")
    if os.path.exists(index_path):
        return FAISS.load_local(persist_dir, embedding_model, allow_dangerous_deserialization=True)
    else:
        vectorstore = FAISS.from_documents(documents, embedding_model)
        vectorstore.save_local(persist_dir)
        return vectorstore

def get_retriever(vectorstore, k=5):
    return vectorstore.as_retriever(search_type="similarity", search_kwargs={"k": k})