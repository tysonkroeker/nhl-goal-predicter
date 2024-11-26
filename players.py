import PySimpleGUI as sg
from services.PlayerService import multiple_player_summary

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
    if event == "Search" or event == "PlayerInput" + "_Enter":
        names = values['PlayerInput'].split(',')
        message = multiple_player_summary(names)
        window['PlayerStats'].update(message)

window.close()