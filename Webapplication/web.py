import streamlit as st
import functions

st.title("My Todo App")
st.subheader("My Todo App")
st.write("The app is for everyday work")
todos = functions.file_read()
for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add new Todo...")