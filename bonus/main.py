import FreeSimpleGUI as sg


label1 = sg.Text("Select File to Compress")
input1 = sg.Input()
choose_button = sg.FilesBrowse("Choose")

label2 = sg.Text("Select destination Folder")
input2 = sg.Input()
choose_button2 = sg.FolderBrowse("Choose")

button = sg.Button("Compress")

window = sg.Window("File Compressor", layout=[[label1, input1, choose_button], [label2, input2, choose_button2], [button]])

window.read()
window.close()