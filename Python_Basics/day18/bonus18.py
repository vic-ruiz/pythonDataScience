import PySimpleGUI as sg
from zip_extractor import extract_archive

sg.theme('black')


label_archive = sg.Text('Select archive')
input_archive = sg.InputText()
button_archive = sg.FileBrowse('Choose', key='archive')

label_dest = sg.Text('Select destination directory')
input_dest = sg.InputText()
button_dest = sg.FolderBrowse('Choose', key='dest')

button_extract = sg.Button('Extract')
output = sg.Text("", key='output')

layout = [[label_archive, input_archive, button_archive],
          [label_dest, input_dest, button_dest],
          [button_extract, output]]

window = sg.Window('Archive Extractor', layout=layout)

while True:
    event, values = window.read()
    print(event)
    print(values)
    match event:
        case 'Extract':
            try:
                extract_archive(values['archive'], values['dest'])
                window['output'].update(value='Extraction completed')
            except FileNotFoundError:
                sg.popup('Please select archive and destination')
        case sg.WIN_CLOSED:
            break


window.close()

