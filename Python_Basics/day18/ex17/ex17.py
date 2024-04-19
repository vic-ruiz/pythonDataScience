import PySimpleGUI as sg
import converter

sg.theme('black')

label1 = sg.Text("Enter feet")
input1 = sg.InputText(key="feet")

label2 = sg.Text("Enter inches")
input2 = sg.InputText(key="inches")

convert_button = sg.Button("Convert", key="Convert")
exit_button = sg.Button('Exit')
output = sg.Text("", key="output")

layout = [[label1, input1],
          [label2, input2],
          [convert_button,exit_button, output]]

window = sg.Window("Converter", layout=layout)

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "Convert":
            try:
                feet = values['feet']
                inches = values['inches']
                meters = converter.convert(feet, inches)
                window["output"].update(value=meters)
            except ValueError:
                sg.popup('Please proveide two numbers')
        case 'Exit':
            break
        case sg.WIN_CLOSED:
            break

window.close()


