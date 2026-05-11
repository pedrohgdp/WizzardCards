from random import randint, seed
import json
from Game import consts_and_variables

class DeckController:
    def __init__(self):
        seed(consts_and_variables.seed_random)
        self.deck = []

    def fill_deck(self):
        with open("Game/Data/cards_json.json", "r") as file:
            data = json.load(file)

        self.deck = [(c["rank"], c["code"]) for c in data["deck"]]

    def fill_hand(self, size):
        hand = []

        for _ in range(size):
            idx = randint(0, len(self.deck) - 1)
            hand.append(self.deck.pop(idx))

        return hand