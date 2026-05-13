from random import randint, seed, shuffle
import json
from Game import consts_and_variables

class DeckController:
    def __init__(self):
        seed(consts_and_variables.seed_random)
        self.deck = []
        self.discard = []

    def fill_deck(self):
        with open("Game/Data/cards_json.json", "r") as file:
            data = json.load(file)

        self.deck = [(c["rank"], c["code"]) for c in data["deck"]]
        self.discard = []

        self.shuffle_deck()

    def shuffle_deck(self):
        shuffle(self.deck)

    def refill_if_needed(self):
        if len(self.deck) == 0:
            self.deck = self.discard
            self.discard = []
            self.shuffle_deck()

    def draw_from_deck(self):
        self.refill_if_needed()

        if not self.deck:
            return None

        return self.deck.pop()

    def fill_hand(self, size):
        hand = []

        for _ in range(size):
            card = self.draw_from_deck()
            if card is None:
                break
            hand.append(card)

        return hand
    
    def discard_cards(self, cards):
        self.discard.extend(cards)