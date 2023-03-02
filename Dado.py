import random
class Dice:
    def __init__(self):
        self.caras=[1,2,3,4,5,6]

    def roll(self):
        return self.caras[random.randrange(0,5)]
