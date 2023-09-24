import streamlit as st
import openai
import requests
import random
import syllables
from streamlit_text_rating.st_text_rater import st_text_rater



with st.sidebar:
    anthropic_api_key = st.text_input("Openai API Key", key="file_qa_api_key", type="password")
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/pages/1_File_Q%26A.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("📝 Music Generation")

txt = st.text_area('Text to analyze')
#st.button("Generate Music", type="primary")


if st.button("Generate Music"):
	#st.write('Calling APi with following txt')
	#st.write(txt)
	
	#st.write(prom)
#st.write('Sentiment:', run_sentiment_analysis(txt))
	openai.api_key= anthropic_api_key
	word_list = txt.split() 
	last=word_list[-1]
	url = "https://api.datamuse.com/words?rel_rhy="+last

	payload={}
	headers = {}

	response = requests.request("GET", url, headers=headers, data=payload)
	st.write(url)
	#word=response.json()[0]["word"]
	li=response.json()
	word=random.choice(li)
	st.write(word)
	word=word["word"]
	nS=syllables.estimate(txt)
	#prom= "Generate the next line for a rap song for reference this is the previous line "+txt+" "
	prom= f'Generate the next line for a rap song that ends with {word} and has {nS} syllables. Make sure to extract the theme and reference \
	it in the line you generate \
	for reference this is the previous line: {txt} . '
	st.write(prom)
	response = openai.Completion.create(
		engine="text-davinci-003",
		prompt=prom,
		temperature=0.6,
		max_tokens=60,
		top_p=1,
		frequency_penalty=0,
		presence_penalty=0
	)
	st.write(response["choices"][0]['text'])
	values = st.slider('Rate this line:', 0, 100, 25)
	st.write('Rating:', values)
	#response = st_text_rater(text=response["choices"][0]['text'])
	#st.write(response)
	#st.write(f"response --> {response}")
	st.write('Rating:', values)
	

st.write('Staying')
if st.button("Stay Music"):
	st.write('Hiii')

