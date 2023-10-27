import streamlit as st
import openai
from langchain.llms import OpenAI



with st.sidebar:
    open_api_key = st.text_input("Openai API Key", key="file_qa_api_key", type="password")
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/pages/1_File_Q%26A.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"
st.title("Interview Help")

form = st.form("my_form")
Company = form.text_input('Company', 'Google')
Role = form.text_input('Position Interviwing For', 'Product manager')
Hm = form.text_input('Position of Interviwer', 'Engineering Manager')


form.slider("Level of Experience")
st.slider("Outside the form")

# Now add a submit button to the form:
x=form.form_submit_button("Submit")



if open_api_key and x:
	st.write("submitted")

#st.write('The current movie title is', Role)
