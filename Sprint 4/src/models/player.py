import json

class Player:
    def __init__(self, name, color, sockedId):
        self.name = name
        self.color = color
        self.alive = True
        self.role = 'crewmate'
        self.id = socketId
        self.voting = 0

    def vote(olayer):
        player.voting.append(self)

    def die():
        self.alive = False

    def toJSON(self):
        return json.dumps(self, default=lambda o: o.__dict__, sort_keys = True, indent=4)
        