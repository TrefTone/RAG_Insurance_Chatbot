# Insurance Chatbot

A conversational AI chatbot built with **LangChain**, **Gemini**, **FAISS**, and **Streamlit** that answers questions about **Life**, **Health**, **Motor**, and **Property Insurance** based on documents from [IRDAI](https://irdai.gov.in/).

---

## Features

- RAG-based Question Answering using Google Gemini
- PDF ingestion and document chunking
- Semantic search powered by FAISS vectorstore
- Streamlit frontend for interactive Q&A
- Fallback to human agent if LLM is unsure

---

## How It Works

1. **PDF Loading & Chunking**  
   PDF documents are loaded using `PyMuPDFLoader` and split using `RecursiveCharacterTextSplitter`.

2. **Embeddings & Vectorstore**  
   Documents are embedded with `HuggingFaceEmbeddings` (`all-MiniLM-L6-v2`) and stored in a FAISS index.

3. **Prompt & LLM**  
   Questions are routed through a context-enhanced prompt to Gemini 2.0 Flash via `ChatGoogleGenerativeAI`.

4. **Interactive UI**  
   Users interact with a Streamlit chatbot interface.

---

## Project Structure

```
.
├── streamlit_app.py              # Main chatbot UI
├── app/
│   └── langchain_pipeline.py     # Core RAG pipeline
├── utils/
│   ├── loader.py                 # PDF loading & chunking
│   ├── embedder.py               # Embedding & vectorstore
│   └── llm_config.py             # Gemini config & prompt
├── data/                         # Source documents
│   ├── Life.pdf
│   ├── Health.pdf
│   ├── Motor.pdf
│   ├── Property.pdf
│   └── ...
├── requirements.txt              # Dependencies
└── .env                          # API keys and prompt config
```

---

## ⚙️ Setup Instructions

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/insurance-chatbot.git
cd insurance-chatbot
```

### 2. Install Dependencies
```bash
pip install -r requirements.txt
```

### 3. Add Your Environment Variables

Create a `.env` file with:
```
GOOGLE_API_KEY=your_google_api_key
LLM_TUNING=Answer the question using the following context. Be clear, concise, and professional.
```

### 4. Add Your PDF Files
Place the documents in the `data/` folder (as already listed above).

### 5. Run the Chatbot
```bash
streamlit run streamlit_app.py
```

---

## Example Questions

- What is covered under a health insurance policy?
- How do I file a motor insurance claim?
- What’s excluded in life insurance?
- Can I transfer home insurance?

---

## DEMO
![Insurance Chatbot-1](https://github.com/user-attachments/assets/39d750e8-8e96-43d9-a883-bb0d0899575f)
![Insurance Chatbot-2](https://github.com/user-attachments/assets/244a8a72-2615-427b-b6c9-83bd57cfe617)

## Fall-back mechanism
![image](https://github.com/user-attachments/assets/e7584cb3-e7e4-4e1c-8d6b-43f5eba09d38)

