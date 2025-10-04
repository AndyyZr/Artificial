import streamlit as st
from transformers import pipeline

st.title("🤖 My AI Helper")

@st.cache_resource
def load_model():
    return pipeline("text-generation", model="distilgpt2")

model = load_model()

user_input = st.text_input("Ask me something:")

if user_input:
    response = model(user_input, max_new_tokens=100, do_sample=True)
    st.write("**AI:**", response[0]["generated_text"])
