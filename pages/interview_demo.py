import streamlit as st
import openai
from langchain.llms import OpenAI
import os
import langchain.agents



os.environ["SERPAPI_API_KEY"]="99a28fd132fb487739324bbe3fa8fbf0a2dcebecd86cff841d4c79260aff5836"

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
	o=open_api_key
	st.write("submitted")
	llm = OpenAI(temperature=0.5,openai_api_key=o)
	d=langchain.agents.load_tools(['wikipedia','serpapi'],llm)
	os.environ["OPENAI_API_KEY"]=open_api_key
	a=langchain.agents.initialize_agent(d,llm,verbose=True)
	x=a.run("Summarize what Opsera does to a non-techincal person")
	prom= f'I am interviewing as a {Role} position with the {Hm} at {Company}. \
	What are the top 3 questions he is most likely to ask me? For reference this is a quick description of what they do {x}\
	'
	st.write('The prompt output is', prom)
	openai.api_key= o
	response = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "You are a proficient AI with a specialty in coming up with interview questions",
               },
            {
                "role": "user",
                "content": prom
            }
        ]
    )
     re=response['choices'][0]['message']['content']
     st.write('The Open ai response is', re)

#st.write('The current movie title is', Role)
