import PySimpleGUI as sg
from services.PlayerService import print_player_summary

layout = [
    [sg.Text("Enter player name to find out how likely they are to score!")],
    [sg.Text('', key='PlayerStats')],
    [sg.InputText("", key="PlayerInput")],
    [sg.Button("Search")]
    ]

# Create the window
window = sg.Window("NHL Goal Predicter", layout, finalize=True)
window['PlayerInput'].bind("<Return>", "_Enter")


# Create an event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Search":
        message = print_player_summary(values['PlayerInput'])
        window['PlayerStats'].update(message)
    if event == "PlayerInput" + "_Enter":
        message = print_player_summary(values['PlayerInput'])
        window['PlayerStats'].update(message)

window.close()