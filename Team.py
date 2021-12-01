import math

from Player import *


class Team:
    def __init__(self, team_name=str, p1=Player, p2=Player):
        self.team_name = team_name
        self.p1 = p1
        self.p2 = p2
        self.chemistry = int(100/p1.tilt_factor + 100/p2.tilt_factor)

    def to_string(self):
        print('Team name:\t', self.team_name)
        print('Player 1:\t', self.p1.name)
        print('Player 2:\t', self.p2.name)

    def team_chemistry(self):
        print(self.chemistry)
