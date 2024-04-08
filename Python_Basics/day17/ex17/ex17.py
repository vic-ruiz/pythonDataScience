import PySimpleGUI as sg
import converter

label1 = sg.Text("Enter feet")
input1 = sg.InputText(key="feet")

label2 = sg.Text("Enter inches")
input2 = sg.InputText(key="inches")

convert_button = sg.Button("Convert", key="Convert")
output = sg.Text("", key="output")

layout = [[label1, input1],
          [label2, input2],
          [convert_button, output]]

window = sg.Window("Converter", layout=layout)

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "Convert":
            feet = values['feet']
            inches = values['inches']
            meters = converter.convert(feet, inches)
            window["output"].update(value=meters)
        case sg.WIN_CLOSED:
            break

window.close()


