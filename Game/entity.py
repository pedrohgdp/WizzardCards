import random
from Game import consts_and_variables

class Entity:
    def __init__(self):
        self.life = 20
        self.hand = ()
        
        self.seed = consts_and_variables.seed_random
        random.seed(self.seed)