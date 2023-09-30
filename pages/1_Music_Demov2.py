import streamlit as st
import openai
import requests
import random
import syllables
import time

# Check if 'rating' key is in the session state
if 'rating' not in st.session_state:
    st.session_state.rating = None

with st.sidebar:
    anthropic_api_key = st.text_input("Openai API Key", key="file_qa_api_key", type="password")
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/pages/1_File_Q%26A.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("📝 Music Generation")

txt = st.text_area('Text to analyze')

if st.button("Generate Music") or st.session_state.rating is not None:
    openai.api_key = anthropic_api_key
    word_list = txt.split() 
    last = word_list[-1]
    url = "https://api.datamuse.com/words?rel_rhy=" + last
    response = requests.get(url)
    word = random.choice(response.json())
    nS = syllables.estimate(txt)
    prom = f'Generate the next line for a rap song that ends with {word["word"]} and has {nS} syllables. Make sure to extract the theme and reference it in the line you generate for reference this is the previous line: {txt} . '
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
    st.session_state.rating = values
    time.sleep(1)

if st.button("Stay Music"):
    st.write('Hiii')
