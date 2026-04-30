import random
from Game import consts_variables

class Enemy:
    def __init__(self):
        self.seed = consts_variables.seed_random
        random.seed(self.seed)