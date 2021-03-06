import random


class Player:
    def __init__(self, name=str, hometown=str, power=int, accuracy=int, serve=int,
                 defense=int, speed=int, agility=int, net_assembly=int,
                 stingy=int, endurance=int, communication=int,
                 temper_meter=int, tilt_factor=int):
        self.name = name
        self.ready = False
        self.power = power
        self.accuracy = accuracy
        self.serve = serve
        self.defense = defense
        self.speed = speed
        self.agility = agility
        self.net_assembly = net_assembly
        self.stingy = stingy
        self.endurance = endurance
        self.communication = communication
        self.temper_meter = temper_meter
        self.tilt_factor = tilt_factor

    def to_string(self):
        print('Name:\t\t', self.name)
        print('Ready:\t\t', self.ready)
        print('Power:\t\t', self.power)
        print('Accuracy:\t', self.accuracy)
        print('Serve:\t\t', self.serve)
        print('Defense:\t', self.defense)
        print('Speed:\t\t', self.speed)
        print('Agility:\t', self.agility)
        print('Net assembly:\t', self.net_assembly)
        print('Stingy:\t\t', self.stingy)
        print('Endurance:\t', self.endurance)
        print('Communication:\t', self.communication)
        print('Temper meter:\t', self.temper_meter)
        print('Tilt factor:\t', self.tilt_factor)

    def ready_up(self):
        self.ready = True

    def cool_down(self):
        self.ready = False

    def spike(self, previous_hit=int):
        # probability of a successful spike is linear combination of:
        #   1) accuracy (50%)
        #   2) previous hit (or set) (50%)
        #       if previous_hit is large (close to 100), current hit is harder
        #       if previous_hit is small (close to 1), current hit is easier
        # accuracy directly increases probability of spike landing
        # previous_hit inversely increases the probability of landing spike

        acc_bonus = 0.5*random.randint(1, self.accuracy)
        ph_bonus = 0.5*(2000/random.randint(1, previous_hit))
        ph_bonus = min(ph_bonus, 50)
        total_bonus = acc_bonus + ph_bonus
        return int(total_bonus*self.power/100)
        # ph = 100 --> 20
        # ph = 20 --> 100

    def set(self):
        pass

    def serve(self):
        pass


class Spiker(Player):
    def super_spike(self):
        print('Spike!')


class Setter(Player):
    def super_set(self):
        print('Set!')


class Defender(Player):
    def super_defense(self):
        print('Defense!')
