from dotenv import load_dotenv
import streamlit as st
import os
import google.generativeai as genai

# Load environment variables
load_dotenv()

# Configure Gemini AI with API Key
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# Load Gemini model
model = genai.GenerativeModel("models/gemini-1.5-pro")
chat = model.start_chat(history=[])

# Function to get response from Gemini
def get_gemini_response(question):
    response = chat.send_message(question, stream=True)
    return response

# Initialize Streamlit app
st.set_page_config(page_title="Gemini Chatbot")
st.header("Gemini Chatbot")

# Initialize session state for chat history
if "chat_history" not in st.session_state:
    st.session_state["chat_history"] = []

# User input
input_question = st.text_input("Ask a question...")
submit = st.button("Ask the question...")

if submit and input_question:
    response = get_gemini_response(input_question)
    st.session_state["chat_history"].append(("You:", input_question))
    
    st.subheader("The Response is")
    
    response_text = ""
    for chunk in response:
        response_text += chunk.text
        st.write(chunk.text)

    # Store bot's response in session state
    st.session_state["chat_history"].append(("Bot:", response_text))

# Display chat history
st.subheader("Chat History")
for role, text in st.session_state["chat_history"]:
    st.write(f"{role} {text}")
