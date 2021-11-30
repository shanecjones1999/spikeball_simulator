from Player import *
from Team import *
from Game import *


# def __init__(self, name=str, hometown=str, power=int, accuracy=int, serve=int,
#                  defense=int, speed=int, agility=int, net_assembly=int,
#                  stingy=int, endurance=int, communication=int,
#                  temper_meter=int, tilt_factor=int):

def main():
    p1 = Player('Otis', 'Mazzulla', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    p2 = Spiker('Shane', 'Mazzulla', 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1)
    team1 = Team('Turtles', p1, p2)
    team1.team_chemistry()
    p1.to_string()
    team1.to_string()


main()
