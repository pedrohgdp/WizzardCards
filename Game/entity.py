import random
from Game import consts_variables

class Entity:
    def __init__(self):
        self.life = 20
        self.hand = ()
        
        self.seed = consts_variables.seed_random
        random.seed(self.seed)