import sys
import numpy
import pandas
import urllib.request
import json
import pprint
import PySimpleGUI as sg
import api

layout = [
    [sg.Text("Hello TEST")],
    [sg.InputText()],
    [sg.Button("Search")]
    ]

# Create the window
window = sg.Window("Demo", layout)



# Create an event loop
while True:
    event, values = window.read()
    if event == sg.WIN_CLOSED:
        break
    if event == "Search":
        player = api.search_player(values[0])
        api.player_scored_last_game(player['playerId'])

window.close()