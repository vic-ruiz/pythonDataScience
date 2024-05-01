import streamlit as st
import functions


def add_todo():
    todo = st.session_state['new_todo']
    todos = functions.get_todos('Python_Basics/day19/todos.txt')
    todos.append(todo + "\n")
    functions.write_todos(todos, 'Python_Basics/day19/todos.txt')


todos = functions.get_todos('Python_Basics/day19/todos.txt')
print(todos)

st.title("My Todo App")
st.subheader('This is my todo app')

for todo in todos:
    st.checkbox(todo)

st.text_input(label="", placeholder="Add a new todo",
              on_change=add_todo, key='new_todo')

st.session_state
