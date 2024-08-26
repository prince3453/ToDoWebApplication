import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
window = sg.Window("To-Do Application",
                   layout=[[label], [input_box], [add_button]],
                   font=('Helvetica', 20))
while True:
    event, value = window.read()
    if event == "Add":
        todos = functions.file_read()
        todos.append(value['todo']+"\n")
        functions.file_write(todos)
    elif event == "Show":
        todos = functions.file_read()
        functions.print_todo(todos)
    elif sg.WIN_CLOSED:
        break

window.close()