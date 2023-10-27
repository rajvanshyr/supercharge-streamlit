import streamlit as st

form = st.form("my_form")
title = st.text_input('Movie title', 'Life of Brian')
form.slider("Inside the form")
st.slider("Outside the form")

# Now add a submit button to the form:
form.form_submit_button("Submit")


st.write('The current movie title is', title)
