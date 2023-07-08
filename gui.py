import functions
import PySimpleGUI as sg

label =sg.Text("type in to-do")
input_box= sg.InputText(tooltip="Enter todo")
add_button = sg.Button("Add",tooltip="click to add todo")

window=sg.Window('my to do app', layout=[[label],[input_box, add_button]])
window.read()
window.close()