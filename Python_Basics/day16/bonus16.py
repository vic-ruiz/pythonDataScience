import PySimpleGUI as sg

label1 = sg.Text("Select files to compress: ")
label2 = sg.Text("Select destination folder: ")
input1 = sg.InputText()
input2 = sg.InputText()
button1 = sg.FileBrowse("Choose")
button2 = sg.FolderBrowse("Choose")
compress_button = sg.Button("Compress")


window = sg.Window("File Zipper", layout=[[label1, input1, button1],
                                          [label2, input2, button2],
                                          [compress_button]])
window.read()
window.close()