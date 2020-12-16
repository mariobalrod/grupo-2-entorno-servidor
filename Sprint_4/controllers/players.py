from models.player import Player
from utils.event import *
from utils.random import *

players = []
votes = []
colors = ['red', 'blue', 'yellow', 'green', 'orange', 'purple']

#funcion para crear jugador y asignarle un color aleatorio
def join(name, socketId):
    if len(colors) > 0:
        color = get_random_color(colors)
        colors.remove(color)
        newPlayer = Player(name, color, socketId)
        players.append(newPlayer.__dict__)

        emitAll('players', players)

    else:
        emitOne('full', True)

#funcion a partir de la cual comienza la partida y asigna el rango impostor a un jugador.
def start():
    if len(players) > 0:
        impostor = get_random_impostor(players)
        impostor['role'] = 'impostor'
    
    data = { "players": players, "vote": True, "playing": True }
    emitAll('start', data)

#funcion por la que se puede votar a los jugadores.
def vote(id):
    for player in players:
        if player['id'] == id:
            player['voting'] = player['voting'] + 1
            votes.append(player)

    if len(votes) == len(player):
        for player in votes:
            player['voting'] = 0

        emitAll('finish', players)

    else:
        emitAll('players', players)

#funcion para terminar la partida tras los votos, determina si el eliminado es impostor o no, y según el resultado se sigue con la partida o se acaba.
def end_game():
    temp = True
    max_voting = players[0]

    for player in players:
        if player['voting'] > max_voting['voting']:
            max_voting = player

    for player in players:
        if player['id'] == max_voting['id']:
            player['alive'] = False

            if player['role'] == 'impostor':
                temp = False
                emitAll('impostor', 'Tripulantes habeis matado al Impostor')

    if temp == True:
        emitAll('players', players)
        
#funcion para empezar nueva partida.
def clear():
    players.clear()
    votes.clear()
    colors = ['red', 'blue', 'yellow', 'green', 'orange', 'purple']
    emitAll('players', players)