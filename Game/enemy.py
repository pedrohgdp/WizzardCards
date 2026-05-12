from Game.entity import Entity

class Enemy(Entity):

    def __init__(self):
        super().__init__()

    def get_card_value(self, rank):

        if rank in ["K", "Q", "J"]:
            return 10

        return int(rank)

    def calculate_best_attack_and_defense(self, enemy_cards):

        cards_values = []

        for card in enemy_cards:

            value = self.get_card_value(card.rank)

            cards_values.append({
                "card": card,
                "value": value
            })

        cards_values.sort(
            key=lambda item: item["value"],
            reverse=True
        )

        enemy_attack = 0
        enemy_defense = 0

        for i in range(2):
            enemy_attack += cards_values[i]["value"]
            
        for i in range(2, 5):
            enemy_defense += cards_values[i]["value"]

        return enemy_attack, enemy_defense