import sys
import numpy
import pandas
import urllib.request
import json
import pprint
import PySimpleGUI as sg


def all_teams():
    data = makeRequest("https://api.nhle.com/stats/rest/en/team")
    return data['data']

def player_scored_last_game(playerId):
    data = makeRequest('https://api-web.nhle.com/v1/player/{0}/game-log/20242025/2'.format(playerId))
    return data['gameLog'][0]['goals'] > 0

def player_games(playerId):
    data = makeRequest('https://api-web.nhle.com/v1/player/{0}/game-log/20242025/2'.format(playerId))
    return data['gameLog']

def search_player(name):
    playerData = makeRequest("https://api.nhle.com/stats/rest/en/skater/summary?limit=-1&start=17&sort=points&cayenneExp=seasonId=20242025")
    playerObj = None
    for player in playerData['data']:
        if(name == player['teamAbbrevs'] or name in player['skaterFullName']):
            print(player['goals'] / player['gamesPlayed'])
            print(player['playerId'])
            print(player['skaterFullName'])
            playerObj = player
    return playerObj


def makeRequest(url):
    req = urllib.request.Request(url)
    req.add_header('User-Agent', 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:106.0) Gecko/20100101 Firefox/106.0')
    req.add_header('Accept', 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8')
    req.add_header('Accept-Language', 'en-US,en;q=0.5')
    f = urllib.request.urlopen(req)
    data = f.read()
    jsonData = json.loads(data)
    return jsonData