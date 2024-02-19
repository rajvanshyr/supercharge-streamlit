import streamlit as st
import openai
import requests
import random
import syllables
import time

# Check if 'rating' key is in the session state
if 'rating' not in st.session_state:
    st.session_state.rating = None

# Introducing new session state flag for music generation
if 'music_generated' not in st.session_state:
    st.session_state.music_generated = False

with st.sidebar:
    anthropic_api_key = st.text_input("Openai API Key", key="file_qa_api_key", type="password")
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/pages/1_File_Q%26A.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("📝 Music Generation")

st.markdown(
        """
        Make lyrics like your favorite rappers!
        Type a line below and then click the button to generate the next line!

    """
    )

txt = st.text_area('Text to analyze')

if st.button("Next Line") and not st.session_state.music_generated:
    openai.api_key = anthropic_api_key
    word_list = txt.split() 
    last = word_list[-1]
    url = "https://api.datamuse.com/words?rel_rhy=" + last
    response = requests.get(url)
    word = random.choice(response.json())
    nS = syllables.estimate(txt)
    prom = f'Generate the next line for a rap song that ends with {word["word"]} and has {nS} syllables. Make sure to extract the theme and reference it in the line you generate for reference this is the previous line: {txt} . '
    response = openai.Completion.create(
        engine="gpt-3.5-turbo-instruct",
        prompt=prom,
        temperature=0.6,
        max_tokens=60,
        top_p=1,
        frequency_penalty=0,
        presence_penalty=0
    )
    st.write(response["choices"][0]['text'])
    st.session_state.music_generated = True

# Separating slider logic from button logic
if st.session_state.music_generated:
    #st.write(response["choices"][0]['text'])
    values = st.slider('Rate this line:', 0, 100, 25)
    #st.session_state.rating = values
    # The sleep is likely unnecessary but you can uncomment it if needed
    # time.sleep(1)

