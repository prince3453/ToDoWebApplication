import functions
import FreeSimpleGUI as sg

label = sg.Text("Type in a to-do")
input_box = sg.InputText(tooltip="Enter todo", key="todo")
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.file_read(),
                      key = 'todos', enable_events=True,
                      size= [45,15])
edit_button = sg.Button("Edit")
window = sg.Window("To-Do Application",
                   layout=[[label], [input_box], [add_button], [list_box,edit_button]],
                   font=('Helvetica', 20))
while True:
    event, values = window.read()
    print(values['todos'])
    if event == "Add":
        todos = functions.file_read()
        todos.append(values['todo'] + "\n")
        functions.file_write(todos)
        window['todos'].update(values=todos)
    elif event == "Edit":
        todo_to_edit = values['todos'][0]
        ntodo = values['todo']
        todos = functions.file_read()
        todos[todos.index(todo_to_edit)] = ntodo+'\n'
        functions.file_write(todos)
        window['todos'].update(values=todos)
    elif event == 'todo':
        window['todo'].update(value=values['todos'][0])
    elif event == "Show":
        todos = functions.file_read()
        functions.print_todo(todos)
    elif sg.WIN_CLOSED:
        break

window.close()