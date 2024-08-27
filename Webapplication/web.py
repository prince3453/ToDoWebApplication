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

for index,todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.file_write(todos)
        del st.session_state[todo]
        st.rerun()

st.text_input(label="", placeholder="Add new Todo...", on_change=add_todo, key='new_todo')