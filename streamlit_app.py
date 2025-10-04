import streamlit as st
from gpt4all import GPT4All

st.title("🤖 My AI Helper")

@st.cache_resource
def load_model():
    return GPT4All("./ggml-gpt4all-j-v1.bin")  # path to uploaded model in repo

model = load_model()

user_input = st.text_input("Ask me something:")

if user_input:
    response = model.generate(user_input)
    st.write("**AI:**", response)
