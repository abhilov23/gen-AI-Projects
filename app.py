from dotenv import load_dotenv
load_dotenv() #loading all the environment variables

import streamlit as st
import os
import google.generativeai as genai

# Load your Google Cloud project ID
genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

##function to load gemini model
model=genai.GenerativeModel("models/gemini-1.5-pro")
def get_gemini_response(question):
    response=model.generate_content(question)
    return response.text



#initializing the streamlit app
st.set_page_config(page_title="Q&A demo")
st.header("Gemini LLM Application")

input=st.text_input("Input", key="input")
submit=st.button("Ask a question")

#when submit is clicked

if submit:
    response=get_gemini_response(input)
    st.write(response)