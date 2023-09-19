import streamlit as st
import openai


def transcribe_audio(audio_file_path):
    with open(audio_file_path, 'rb') as audio_file:
        transcription = openai.Audio.transcribe("whisper-1", audio_file)
    return transcription['text']

with st.sidebar:
    anthropic_api_key = st.text_input("Openai API Key", key="file_qa_api_key", type="password")
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/pages/1_File_Q%26A.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("📝 Meeting Summarization")
uploaded_file = st.file_uploader("Upload an Meeting FIle", type=("txt", "wav"))

if uploaded_file and anthropic_api_key:
    openai.api_key= anthropic_api_key
    transcription = openai.Audio.transcribe("whisper-1", uploaded_file)
    print(transcription)


# if uploaded_file and question and not anthropic_api_key:
#     st.info("Please add your Openai API key to continue.")

def key_points_extraction(transcription):
    response = openai.ChatCompletion.create(
        model="gpt-4",
        temperature=0,
        messages=[
            {
                "role": "system",
                "content": "You are a proficient AI with a specialty in distilling information into key points in bullet format. Based on the following text, identify and list the main points that were discussed or brought up. These should be the most important ideas, findings, or topics that are crucial to the essence of the discussion in bullet format."
            },
            {
                "role": "user",
                "content": transcription
            }
        ]
    )
    return response['choices'][0]['message']['content']

option = st.selectbox(
    'How would you like to be contacted?',
    ('Email', 'Summarize', 'Mobile phone'))

if uploaded_file and option =='Summarize' and anthropic_api_key:
    openai.api_key= anthropic_api_key
    response=key_points_extraction(transcription['text'])
    st.write("### Answer")
    st.write(response)