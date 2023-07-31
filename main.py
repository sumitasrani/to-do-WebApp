import streamlit as st
import functions

todos = functions.get_todos()

def add_todo():
    todo = st.session_state["new_todo"] + "\n"
    todos.append(todo)
    functions.write_todos(todos)

st.title("Simple To-do App")
st.subheader("Add to-do. Mark check on completion. Download list.")
st.write("Focus. Streamline. Prioritize. Increase your daily productivity.")

for index, todo in enumerate(todos):
    checkbox = st.checkbox(todo, key=todo)
    if checkbox:
        todos.pop(index)
        functions.write_todos(todos)
        del st.session_state[todo]
        st.experimental_rerun()

st.text_input(label="", placeholder="Add to-do...",
              on_change=add_todo, key='new_todo')

with open("todos.txt", "r") as file:
    download_btn = st.download_button(
            label="Download to-do list",
            data=file,
            file_name="My_todo_list.txt",
            mime="text/plain"
          )