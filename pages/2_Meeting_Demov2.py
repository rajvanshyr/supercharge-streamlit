import streamlit as st
import openai
from pydub.utils import make_chunks
from pydub import AudioSegment

# Function to transcribe audio
def transcribe_audio(audio_file_path):
    with open(audio_file_path, 'rb') as audio_file:
        transcription = openai.Audio.transcribe("whisper-1", audio_file)
    return transcription['text']

# Sidebar with API key input and links to source code
with st.sidebar:
    anthropic_api_key = st.text_input("OpenAI API Key", key="file_qa_api_key", type="password")
    st.markdown("[View the source code](https://github.com/streamlit/llm-examples/blob/main/pages/1_File_Q%26A.py)")
    st.markdown("[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)")

# Title and file uploader
st.title("📝 Meeting Summarization")
st.markdown(
        """
        Need to summarize a meeting? 
        Drop the wav file in below.(Currently only supports small wav files)
    """)
uploaded_file = st.file_uploader("Upload a Meeting File", type=("txt", "wav"))

# Function to extract key points from transcription
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

# Option selector
option = st.selectbox(
    'What do you want to do?',
    ('Get More Details on Topic', 'Summarize Action Items'))

# Handling file upload and summarization
if uploaded_file and option == 'Summarize Action Items' and anthropic_api_key:
    with st.spinner('Transcribing and summarizing...'):
        openai.api_key = anthropic_api_key
        transcription_text = ""
        
        chunk_length_ms = 20000
        myaudio = AudioSegment.from_file(uploaded_file, "wav") 
        chunks = make_chunks(myaudio, chunk_length_ms)
        
        progress_bar = st.progress(0)
        for i, chunk in enumerate(chunks):
            chunk_name = f"chunk{i}.wav"
            chunk.export(chunk_name, format="wav")
            transcription_text += transcribe_audio(chunk_name)
            progress_bar.progress(i / len(chunks))

        st.write("### Transcription")
        st.write(transcription_text)
        
        response = key_points_extraction(transcription_text)
        st.write("### Answer")
        st.write(response)
else:
    if not anthropic_api_key:
        st.warning('Please add your OpenAI API key to continue.')
