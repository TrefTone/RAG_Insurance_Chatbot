import os
from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.prompts import PromptTemplate

load_dotenv()

llm = ChatGoogleGenerativeAI(
    model="gemini-2.0-flash",
    google_api_key=os.getenv("GOOGLE_API_KEY")
)
prompt_str = os.getenv("LLM_TUNING")
template = (
    f"{prompt_str}\n"
    "Context:\n{context}\n\n"
    "Question: {question}\n"
    "Answer: (be specific and complete, use bullets if needed):"
)

prompt_template = PromptTemplate(
    input_variables=["context", "question"],
    template=template
)


