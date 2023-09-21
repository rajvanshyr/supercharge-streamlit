import streamlit as st
import openai

st.title("📝 Music Generation")

txt = st.text_area('Text to analyze')
#st.button("Generate Music", type="primary")


if st.button("Generate Music"):
	st.write('Calling APi with following txt')
	st.write(txt)
	prom= "Generate the next line for a rap song for reference this is the previous line "+txt
	st.write(prom)
#st.write('Sentiment:', run_sentiment_analysis(txt))

