import streamlit as st
from google import genai

st.title("MY AI ASSISTANT")

client = genai.Client(api_key="AIzaSyDIVfqU4q_MA1gUkv5KboYR2iQYtDLydLM")

question = st.text_input("Ask me anything")

if st.button("Submit"):
    if question.strip() == "":
        st.warning("Please enter a question")
    else:
        response = client.models.generate_content(
            model="models/gemini-2.5-flash",   # safer free model
            contents=question
        )
        st.write(response.text)