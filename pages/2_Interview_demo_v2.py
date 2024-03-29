import streamlit as st
import openai
from langchain.llms import OpenAI
import os
import langchain.agents

# Set up your environment variable
os.environ["SERPAPI_API_KEY"] = "99a28fd132fb487739324bbe3fa8fbf0a2dcebecd86cff841d4c79260aff5836"

def main():
	st.title("Interview Prep Assistant")
	st.markdown(
        """
        Need help prepping for an interview?
        Give us some details below and we will generate practice questions!!
    """
    )

	with st.sidebar:
		open_api_key = st.text_input("OpenAI API Key", key="file_qa_api_key", type="password")
		st.markdown("[View the source code](https://github.com/streamlit/llm-examples/blob/main/pages/1_File_Q%26A.py)")
		st.markdown("[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)")
	
	# Create a form for user input
	form = st.form("my_form")
	Company = form.text_input('Company', 'Google')
	Role = form.text_input('Position Interviewing For', 'Product Manager')
	Hm = form.text_input('Position of Interviewer', 'Engineering Manager')
	experience_level = form.slider("Years of Experience", 0, 25, 5)  # Assume experience level is from 0 to 10
	#submit = form.form_submit_button("Submit")
	if "Submit" not in st.session_state:
		st.session_state["Submit"] = False
	# if "Hit me1" not in st.session_state:
	# 	st.session_state["Hit me1"] = False
	# if "Hit me2" not in st.session_state:
	# 	st.session_state["Hit me2"] = False
	# if "Hit me3" not in st.session_state:
	# 	st.session_state["Hit me3"] = False
	if form.form_submit_button("Submit"):
		st.session_state["Submit"] = not st.session_state["Submit"]

	
	if open_api_key and st.session_state["Submit"]:
		try:
			llm = OpenAI(temperature=0.5, openai_api_key=open_api_key)
			d = langchain.agents.load_tools(['wikipedia', 'serpapi'], llm)
			os.environ["OPENAI_API_KEY"] = open_api_key
			p1 = f'Summarize what {Company} does in a simple way'
			a = langchain.agents.initialize_agent(d, llm, verbose=True)
			x = a.run(p1)
			prompt = f'I am interviewing as a {Role} position with the {Hm} at {Company}.I have {experience_level} years of experience. \
			What are the top 3 questions he is most likely to ask me? For reference, this is a quick description of what they do {x}'
			#st.write('The prompt output is', prompt)
			openai.api_key = open_api_key
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
						"content": prompt
					}
				]
			)
			reply = response['choices'][0]['message']['content']
			#st.write('The OpenAI response is', reply)
			questions = reply.split('\n\n')
			#form = st.form("my_form_2")
			for i, question in enumerate(questions, 1):
					st.markdown(f' {question}')  # Display each question
					user_answer = st.text_area(f'	 Answer for Question {i}') 
					# btext='Hit me'+str(i)
					# #f_name='my_form'+i
					# #st.button(btext)
					# # submit1 = form.form_submit_button("Submit1")
					# if st.button(btext):
					# 	st.session_state[btext] = not st.session_state[btext]

					# 	st.write('Ayyyyyy you clicked it my brotha')
					# 	prompt2 = f'Rank the answer in brackets to the question deliminated by the stars \
					# 	on a scale of 1-100: for someone interviewing as a {Role} at devops company.For \
					# 	reference, this is a quick description of what they do {x}: \n answer:*{user_answer}* \n \
					# 	question:*{question}*'
						
					# 	st.write(prompt2)
					# 	response = openai.ChatCompletion.create(
					# 		model="gpt-4",
					# 		temperature=0,
					# 		messages=[
					# 		{
					# 			"role": "system",
					# 			"content": "You are a proficient AI with a specialty in critiquing interview answers",
					# 		},
					# 		{
					# 			"role": "user",
					# 			"content": prompt2
					# 	}
					# 	]
					# 	)
					# 	reply = response['choices'][0]['message']['content']
					# 	st.write(reply)

					# 	st.write('Ayyyyyy you clicked it my brotha')



					#answer = form.form_submit_button("answer")
			#if st.button('Generate Questions'):
			# Assume `reply` is the string containing the questions
				#questions = reply.split('\n\n')  # Split the string into a list of questions based on two newline characters
		except Exception as e:
			st.error(f"An error occurred: {e}")
	else:
		if not open_api_key:
			st.warning('Please add your OpenAI API key to continue.')
	# if "Submit2" not in st.session_state:
	# 	st.session_state["Submit2"] = False
	# if "button2" not in st.session_state:
	# 	st.session_state["button2"] = False
	# if st.button("Submit2"):
	# 	st.session_state["Submit2"] = not st.session_state["Submit2"]
	# if st.session_state["Submit2"]:
	# 	if st.button("Button2"):
	# 		st.session_state["button2"] = not st.session_state["button2"]
	# 		st.write('Ayyyyyy you clicked it my brotha')


 # Create a text area for user to input their answer




if __name__ == "__main__":
	main()
