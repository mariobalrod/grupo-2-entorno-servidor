from models.player import Player
from utils.event import *
from utils.random import *
import random

class Controllers:
    def __init__(self):
        self.players = []
        self.alives = [0]
        self.votes = []
        self.colors = ['red', 'blue', 'yellow', 'green', 'orange', 'purple']

    #funcion para crear jugador y asignarle un color aleatorio
    def join(self, name, socketId):
        if len(self.colors) > 0:
            color = get_random_color(self.colors)
            self.colors.remove(color)
            newPlayer = Player(name, color, socketId)
            self.players.append(newPlayer.__dict__)

            emitAll('players', self.players)

        else:
            emitOne('full', True)

    #funcion a partir de la cual comienza la partida y asigna el rango impostor a un jugador.
    def start(self):
        if len(self.players) > 0:
            impostor = get_random_impostor(self.players)
            impostor['role'] = 'impostor'

        self.alives.append(len(self.players))
        
        data = { "players": self.players, "playing": True }
        emitAll('start', data)

    #funcion por la que se puede votar a los jugadores.
    def vote(self, id):
        for player in self.players:
            if player['id'] == id:
                player['voting'] = player['voting'] + 1
                self.votes.append(player)

        emitAll('players', self.players)

    #funcion para terminar la partida tras los votos, determina si el eliminado es impostor o no, y según el resultado se sigue con la partida o se acaba.
    def end_game(self):
        if len(self.votes) == self.alives[len(self.alives) - 1]:
            self.votes.clear()
            self.alives.append(self.alives[len(self.alives) - 1] - 1)

            random_player = self.players[random.randint(0, len(self.players) - 1)]

            while random_player['alive'] == False:
                random_player = self.players[random.randint(0, len(self.players) - 1)]
                
            max_voting = [random_player]

            for player in self.players:
                if player['alive'] == True and player['voting'] > max_voting[len(max_voting) - 1]['voting']:
                    max_voting.append(player)

            # reset voting
            for player in self.players:
                player['voting'] = 0

            for player in self.players:
                if player['id'] == max_voting[len(max_voting) - 1]['id']:
                    player['alive'] = False

                    # muerto el impostor ?¿
                    if player['role'] == 'impostor':
                        emitAll('impostor', 'Tripulantes habeis matado al Impostor')
                        return 'null'

            # solo quedan 2
            if self.alives[len(self.alives) - 1] == 2:
                for player in self.players:
                    if player['alive'] == True and player['role'] == 'impostor':
                        emitAll('defeat', 'El impostor ha ganado!')
                        return 'null'

            # solo queda 1
            if self.alives[len(self.alives) - 1] == 1:
                for player in self.players:
                    if player['alive'] == True and player['role'] == 'impostor':
                        emitAll('defeat', 'El impostor ha ganado!')
                        return 'null'
                    
                    if player['alive'] == True and player['role'] == 'crewmate':
                        emitAll('impostor', 'Tripulantes habeis matado al Impostor')
                        return 'null'

            # muerto un tripulante
            emitAll('kill', self.players)
            return 'null'
            
    #funcion para empezar nueva partida.
    def clear(self):
        self.alives = [0]
        self.players.clear()
        self.votes.clear()
        self.colors = ['red', 'blue', 'yellow', 'green', 'orange', 'purple']

        emitAll('players', self.players)