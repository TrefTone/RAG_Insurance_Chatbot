import streamlit as st
from app.langchain_pipeline import ask_rag

st.set_page_config(page_title="Insurance Chatbot", page_icon="🤖", layout="centered")

st.title("🔍 Insurance Chatbot")
st.markdown("Ask anything related to **Life**, **Health**, **Motor**, or **Property Insurance**.\n\nSource: Retrieved from https://irdai.gov.in/")
# Reset Chat Button
if st.button("🔄 Reset Chat"):
    st.session_state.messages = []
    st.session_state.awaiting_agent_confirmation = False
    st.session_state.last_user_query = ""
    st.rerun()

# Initialize session state
if "messages" not in st.session_state:
    st.session_state.messages = []

if "awaiting_agent_confirmation" not in st.session_state:
    st.session_state.awaiting_agent_confirmation = False
    st.session_state.last_user_query = ""

# Chat UI function
def chat_interface():
    # Display welcome message only at the start
    if not st.session_state.messages:
        with st.chat_message("assistant"):
            st.markdown("Hello! I'm your Insurance Assistant. How can I help you today?")

    # Display chat history
    for msg in st.session_state.messages:
        with st.chat_message(msg["role"]):
            st.markdown(msg["content"])

    # Chat input
    user_input = st.chat_input("Type your insurance question here...")

    # Main conversation handler
    if user_input and not st.session_state.awaiting_agent_confirmation:
        # Append user message
        st.session_state.messages.append({"role": "user", "content": user_input})
        st.session_state.last_user_query = user_input

        with st.chat_message("user"):
            st.markdown(user_input)

        # Get bot response
        with st.chat_message("assistant"):
            with st.spinner("Thinking..."):
                try:
                    response = ask_rag(user_input).strip()
                except Exception as e:
                    response = f"⚠️ Error while processing your request. Please try again later.\n\nDetails: {e}"

            # Fallback if model hangs or returns nothing
            if not response or response.lower() in ["", "none"]:
                response = "🤖 Sorry, I couldn't understand that. Please ask an insurance-related question."

            st.markdown(response)
            st.session_state.messages.append({"role": "assistant", "content": response})

            # Trigger fallback interaction
            if "Please ask another question." in response:
                st.session_state.awaiting_agent_confirmation = True


    # If bot was unsure, offer human help
    if st.session_state.awaiting_agent_confirmation:
        st.markdown("Would you like to speak with a human agent?")
        user_choice = st.radio(
            "Select one option:",
            ["Yes", "No"],
            key="agent_radio"
        )

        if st.button("Submit"):
            if user_choice == "Yes":
                final_msg = (
                    "📞 Please contact our personnel for further assistance:\n\n"
                    "- 📧 Email: support@insureassist.com\n"
                    "- 📱 Phone: +91-98-xxxx-10"
                )
                with st.chat_message("assistant"):
                    st.markdown(final_msg)
                st.session_state.messages.append({"role": "assistant", "content": final_msg})
                st.session_state.awaiting_agent_confirmation = False

            elif user_choice == "No":
                # Just reset confirmation and let user continue chatting
                st.session_state.awaiting_agent_confirmation = False
                st.rerun()  # Refresh UI to re-enable chat input

# Launch chatbot
chat_interface()
