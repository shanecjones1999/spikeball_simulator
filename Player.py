class Player:
    def __init__(self, name=str, power=int, accuracy=int, defense=int):
        self.name = name
        self.ready = False
        self.power = power
        self.accuracy = accuracy
        self.defense = defense

    def ready_up(self):
        self.ready = True

    def cool_down(self):
        self.ready = False
