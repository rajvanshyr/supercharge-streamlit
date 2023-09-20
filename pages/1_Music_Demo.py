import streamlit as st

st.title("📝 Music Generation")

txt = st.text_area('Text to analyze')
st.button("Generate Music", type="primary")


if st.button("Generate Music"):
	st.write('Calling APi')
#st.write('Sentiment:', run_sentiment_analysis(txt))

