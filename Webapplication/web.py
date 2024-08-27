import streamlit as st
import functions

todos = functions.file_read()
def add_todo():
    todo = st.session_state['new_todo'] + "\n"
    todos.append(todo)
    functions.file_write(todos)

st.title("My Todo App")
st.subheader("My Todo App")
st.write("The app is for everyday work")

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new Todo...", on_change=add_todo, key='new_todo')