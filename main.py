from app.langchain_pipeline import ask_rag

print("🔍 Insurance Chatbot (type 'exit' to quit)\n")
while True:
    query = input("❓ Your question: ")
    if query.lower() == "exit":
        break
    response = ask_rag(query)
    if "Connecting you to a human agent..." in response:
        print("🤝", response, "\n")
        break
    elif "Please ask another question." in response:
        print("🤔", response, "\n")
    else:
        # Print the answer from the RAG chain
        if len(response) > 0:
            print("🤖", response, "\n")
        else:
            print("🤖 Sorry, I couldn't find an answer to that.\n")