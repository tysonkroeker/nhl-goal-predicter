import PySimpleGUI as sg
from .Api import makeRequest

def multiple_player_summary(names):
    message = ''
    first = True
    for name in names:
        if first:
            append = ''
            first = False
        else:
            append = '\n'

        message = message + append + print_player_summary(name.strip())
    
    return message

def print_player_summary(playerName):
    player = search_player(playerName)
    if player == None:
        return None

    scored_last_game = player_scored_last_game(player['playerId'])

    message = f"{player['skaterFullName']} @ {player['teamAbbrevs']}\n"
    goalsPerGame = player['goals'] / player['gamesPlayed']
    message = message + f"{goalsPerGame:.3f} Goals per game this season\n"
    
    if scored_last_game:
        message = message + 'Scored last game'
    else:
        message = message + 'Did not score last game'

    return message + '\n'

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
            playerObj = player
    return playerObj