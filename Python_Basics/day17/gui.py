import functions
import PySimpleGUI as sg


label = sg.Text("Type in To-Do")
input_box = sg.InputText(tooltip="Enter a todo", key='todo')
add_button = sg.Button("Add")
list_box = sg.Listbox(values=functions.get_todos(), key='todos',
                      enable_events=True, size=[45,10])
edit_button= sg.Button("Edit")
layout = [[label], [input_box, add_button], [list_box, edit_button]]

window = sg.Window('My To-Do App', layout=layout, font=('Helvetica', 20))

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Add':
            todos = functions.get_todos()
            new_todo = values['todo'] + "\n"
            todos.append(new_todo)
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'Edit':
            todo_to_edit = values['todos'][0]
            new_todo = values['todo'] + '\n'
            todos = functions.get_todos()
            index = todos.index(todo_to_edit)
            todos[index] = new_todo
            functions.write_todos(todos)
            window['todos'].update(values=todos)
        case 'todos':
            item = values['todos'][0]
            window['todo'].update(value=item)
        case sg.WIN_CLOSED:
            break


window.close()
