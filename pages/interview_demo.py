import streamlit as st

form = st.form("my_form")
Company = form.text_input('Company', 'Google')
Role = form.text_input('Position Interviwing For', 'Product manager')
Hm = form.text_input('Position of Interviwer', 'Engineering Manager')


form.slider("Level of Experience")
st.slider("Outside the form")

# Now add a submit button to the form:
form.form_submit_button("Submit")


st.write('The current movie title is', Role)
