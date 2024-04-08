import PySimpleGUI as sg
import zip_creator

label1 = sg.Text("Select files to compress: ")
input1 = sg.InputText()
button1 = sg.FilesBrowse("Choose", key='files')

label2 = sg.Text("Select destination folder: ")
input2 = sg.InputText()
button2 = sg.FolderBrowse("Choose", key='folder')

compress_button = sg.Button("Compress")
output = sg.Text("", key='output')


window = sg.Window("File Zipper", layout=[[label1, input1, button1],
                                          [label2, input2, button2],
                                          [compress_button, output]])

while True:
    event, values = window.read()
    print(event)
    print(values)

    match event:
        case "Compress":
            filepaths = values['files']
            filepaths = filepaths.split(';')
            folder = values['folder']
            zip_creator.make_archive(filepaths, folder)
            window['output'].update(value='Compression completed')

        case sg.WIN_CLOSED:
            break


window.close()