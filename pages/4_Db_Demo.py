import streamlit as st
import openai

def create_connection(path):
    connection = None
    try:
        connection = sqlite3.connect(path)
        st.write("Connection to SQLite DB successful")
    except Error as e:
    	st.write('Below is error:', e, 'Above is a error.')
        st.write("The error '{e}' occurred")

    return connection

with st.sidebar:
    anthropic_api_key = st.text_input("Openai API Key", key="file_qa_api_key", type="password")
    "[View the source code](https://github.com/streamlit/llm-examples/blob/main/pages/1_File_Q%26A.py)"
    "[![Open in GitHub Codespaces](https://github.com/codespaces/badge.svg)](https://codespaces.new/streamlit/llm-examples?quickstart=1)"

st.title("📝 Meeting Summarization")

connection = create_connection("E:\\sm_app.sqlite")


def execute_query(connection, query):
    cursor = connection.cursor()
    try:
        cursor.execute(query)
        connection.commit()
        print("Query executed successfully")
    except Error as e:
        print(f"The error '{e}' occurred")



create_users_table = """
CREATE TABLE IF NOT EXISTS users (
  id INTEGER PRIMARY KEY AUTOINCREMENT,
  name TEXT NOT NULL,
  age INTEGER,
  gender TEXT,
  nationality TEXT
);
"""

execute_query(connection, create_users_table)  

