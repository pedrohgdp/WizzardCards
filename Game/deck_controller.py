from random import randint, seed
import json
from Game import consts_and_variables

class DeckController():
    def __init__(self):
        seed(consts_and_variables.seed_random)

    def fill_deck(self):
        with open("Game/Data/cards_json.json", "r") as file:
            data = json.load(file)
        
        consts_and_variables.deck = [
            (card["rank"], card["code"])
            for card in data["deck"]
        ]

    def fill_player_hand(self):
        for i in range(5):
            random_number = randint(0, len(consts_and_variables.deck) - 1)
            card = consts_and_variables.deck.pop(random_number)
            consts_and_variables.player_cards.append(card)

    def fill_enemy_hand(self):
        for i in range(5):
            random_number = randint(0, len(consts_and_variables.deck) - 1)
            card = consts_and_variables.deck.pop(random_number)
            consts_and_variables.enemy_cards.append(card)