
class Player:
    def __init__(self, name, color, socketId):
        self.name = name
        self.color = color
        self.alive = True
        self.role = 'crewmate'
        self.id = socketId
        self.voting = 0

