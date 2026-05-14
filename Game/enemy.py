from Game.entity import Entity

from Game.entity import Entity
import random

class Enemy(Entity):

    def __init__(self):
        super().__init__()

    def get_card_value(self, rank):

        if rank in ["K", "Q", "J"]:
            return 10

        return int(rank)

    def calculate_best_attack_and_defense(self, enemy_cards, player_cards):
        enemy_values = []
        player_values = []

        for card in enemy_cards:

            value = self.get_card_value(card.rank)

            enemy_values.append({
                "card": card,
                "value": value
            })

        for card in player_cards:

            value = self.get_card_value(card.rank)

            player_values.append(value)

        enemy_values.sort(
            key=lambda item: item["value"],
            reverse=True
        )

        player_values.sort(reverse=True)

        player_best_attack = sum(player_values[:2])

        player_best_defense = sum(player_values[2:5])

        total_enemy_power = sum(value["value"] for value in enemy_values)

        enemy_attack = 0
        enemy_defense = 0

        attack_cards = []
        defense_cards = []

        if player_best_defense < 15:
            aggression = 0.8
        elif player_best_attack > 15:
            aggression = 0.45
        else:
            aggression = 0.6

        attack_target = int(total_enemy_power * aggression)

        for card in enemy_values:

            if enemy_attack < attack_target:

                attack_cards.append(card)
                enemy_attack += card["value"]

            else:

                defense_cards.append(card)
                enemy_defense += card["value"]


        if len(defense_cards) == 0:

            weakest_attack = attack_cards[-1]

            attack_cards.pop()

            enemy_attack -= weakest_attack["value"]

            defense_cards.append(weakest_attack)

            enemy_defense += weakest_attack["value"]

        if random.random() < 0.15:
            enemy_attack = max(enemy_attack - random.randint(1, 4),0)

        return enemy_attack + random.randint(1, 5), enemy_defense