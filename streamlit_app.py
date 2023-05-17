import streamlit as st
from langchain.llms import OpenAI

st.title('🦜🔗 Langchain - Basic App')

llm = OpenAI(model_name='text-davinci-003')

with st.form:
  text_input = st.text_input('Enter your prompt:', '')
  submitted = st.form_submit_button('Submit')
  if submitted:
    llm(text_input)
