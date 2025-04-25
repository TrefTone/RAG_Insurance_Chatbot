from langchain_core.runnables import RunnableLambda
from langchain.schema.runnable import RunnableSequence

import os
from utils.loader import load_and_chunk_pdfs
from utils.embedder import build_or_load_vectorstore, get_retriever
from utils.llm_config import llm, prompt_template

# Source PDFs
pdf_paths = [
    ("C:/System/TCS project/data/Life.pdf", "Life Insurance document"),
    ("C:/System/TCS project/data/Life_detailed.pdf", "Life Insurance document"),
    ("C:/System/TCS project/data/Health.pdf", "Health Insurance document"),
    ("C:/System/TCS project/data/Health_detailed.pdf", "Health Insurance document"),
    ("C:/System/TCS project/data/Motor.pdf", "Motor Insurance document"),
    ("C:/System/TCS project/data/Motor_detailed.pdf", "Motor Insurance document"),
    ("C:/System/TCS project/data/Property.pdf", "Home Insurance document"),
    ("C:/System/TCS project/data/Home.pdf", "Home Insurance document"),
]


def get_rag_chain():
    # Injest and chunk
    chunks = load_and_chunk_pdfs(pdf_paths)

    #Build vector space
    vectorstore = build_or_load_vectorstore(chunks)
    
    #RAG chain
    retriever = get_retriever(vectorstore)
    return (
        {"context": retriever, "question": RunnableLambda(lambda x: x)}
        | prompt_template
        | llm
    )

rag_chain = get_rag_chain()

def ask_rag(query: str) -> str:
    try:
        result = rag_chain.invoke(query)
        answer = result.content.strip()
        if not answer or len(answer) < 10:
            return "🤖 Sorry, I couldn't understand that. Please ask an insurance-related question."
        if "I'm not sure" in answer or "I'm sorry" in answer:
            return "Please ask another question."
        return f"{answer}\n\n"
    except Exception as e:
        return f"⚠️ Error: {e}"
