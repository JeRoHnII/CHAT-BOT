import google.generativeai as genai
import os
import streamlit as st
import os
os.environ["GOOGLE_API_KEY"] ="AIzaSyAxuRrd_dF349H9rwQynLLDp1WwzvbUOq0"

# Configure API Key
genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

def translate_role_for_streamlit(user_role):
    if user_role == "model":
        return "assistant"
    else:
        return user_role

# Initialize chat session in Streamlit if not already present
if "chat_session" not in st.session_state:
    # Create a new chat session
    model = genai.GenerativeModel("gemini-1.5-flash-latest")  # Best for free users
    st.session_state.chat_session = model.start_chat(history=[])

# Display the chatbot's title on the page
st.title("🤖 Gemini Pro - ChatBot")

# Display the chat history
for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role_for_streamlit(message.role)):
        st.markdown(message.parts[0].text)

# Input field for user's message
user_prompt = st.chat_input("Ask Gemini-Pro...")
if user_prompt:
    # Add user's message to chat and display it
    st.chat_message("user").markdown(user_prompt)

    # Send user's message to Gemini-Pro and get the response
    gemini_response = st.session_state.chat_session.send_message(user_prompt)

    # Display Gemini-Pro's response
    with st.chat_message("assistant"):
        st.markdown(gemini_response.text)
  
