import pygame
from enum import Enum

from Game import consts_and_variables
from Game.enemy import Enemy
from Game.player import Player
from Game.deck_controller import DeckController
from Game.card import Card


class GameStates(Enum):
    FILLING_HANDS = 1
    DRAWING_CARDS = 2
    PLAYER_SELECTING_ATK_CARDS = 3
    PLAYER_SELECTING_DEF_CARDS = 4
    ENEMY_SELECTING_CARDS = 5
    ATTACK_AND_DEFENSE_MODE = 6

class IDLE(Enum):
    ATK = 1
    DEF = 2
class JogoScreen:
    def __init__(self, game_controller):

        self.game_controller = game_controller

        self.player = Player()
        self.enemy = Enemy()

        self.deck_controller = DeckController()
        self.deck_controller.fill_deck()

        self.player_cards = []
        self.enemy_cards = []

        self.actual_state = GameStates.FILLING_HANDS

        self.timer_next_card = 0
        self.visible_cards = 0
        self.delay_next_card = 0.2

        self.create_board()

        self.create_hands()

        self.actual_state = GameStates.DRAWING_CARDS

        self.player_atk = 0
        self.player_def = 0

        self.enemy_atk = 0
        self.enemy_def = 0

        self.idle_state = IDLE.ATK


    def create_board(self):
        self.screen_width = consts_and_variables.WIDTH
        self.screen_height = consts_and_variables.HEIGHT

        self.board = pygame.image.load('Game/Sprites/Board.png').convert_alpha()
        self.board = pygame.transform.smoothscale(self.board, (self.screen_width, self.screen_height))

        self.card_enemy = pygame.image.load('Game/Sprites/EnemyCard.png').convert_alpha()
        self.card_enemy = pygame.transform.smoothscale(self.card_enemy, (consts_and_variables.CARD_ENEMY_WIDTH, consts_and_variables.CARD_ENEMY_HEIGHT))

        self.life_ui = pygame.image.load('Game/Sprites/LifeImage.png').convert_alpha()
        self.life_ui = pygame.transform.smoothscale(self.life_ui, (consts_and_variables.LIFE_IMAGE_WIDTH, consts_and_variables.LIFE_IMAGE_HEIGHT))

        self.button_select = pygame.image.load('Game/Sprites/SelectButton.png').convert_alpha()
        self.rect_button_select = pygame.Rect(375, 500, self.button_select.get_width() / 3, self.button_select.get_height() / 3)
        self.button_select = pygame.transform.smoothscale(self.button_select, (self.button_select.get_width() / 3, self.button_select.get_height() / 3))

    def create_hands(self):
        player_hand = self.deck_controller.fill_hand(5)
        enemy_hand = self.deck_controller.fill_hand(5)

        for i, (rank, code) in enumerate(player_hand):

            pos = consts_and_variables.CARD_POSITIONS_PLAYER[i]
            size = (consts_and_variables.CARD_PLAYER_WIDTH, consts_and_variables.CARD_PLAYER_HEIGHT)

            self.player_cards.append(Card(f'Game/Sprites/Cards/{code}.png', pos, size, rank, self.player))

        for i, (rank, code) in enumerate(enemy_hand):

            pos = consts_and_variables.CARD_POSITIONS_ENEMY[i]
            size = (consts_and_variables.CARD_ENEMY_WIDTH, consts_and_variables.CARD_ENEMY_HEIGHT)

            self.enemy_cards.append(Card(f'Game/Sprites/Cards/{code}.png', pos, size, rank, self.player))

    def handle_events(self, events):

        if self.actual_state in (GameStates.PLAYER_SELECTING_ATK_CARDS, GameStates.PLAYER_SELECTING_DEF_CARDS):

            for event in events:

                if event.type == pygame.MOUSEBUTTONDOWN:

                    pos = pygame.mouse.get_pos()

                    if self.rect_button_select.collidepoint(pos):

                        if self.actual_state == GameStates.PLAYER_SELECTING_ATK_CARDS:

                            self.actual_state = GameStates.PLAYER_SELECTING_DEF_CARDS
                            self.idle_state = IDLE.DEF

                            print("Agora selecionando DEF")
                            return

                        elif self.actual_state == GameStates.PLAYER_SELECTING_DEF_CARDS:

                            self.actual_state = GameStates.ENEMY_SELECTING_CARDS

                            print("Agora inimigo seleciona")
                            return

                    for card in self.player_cards:

                        if self.idle_state == IDLE.ATK:

                            value = card.click(pos, True, False)

                            if value:

                                self.player_atk += value

                                print("player atk:", self.player_atk)
                                print("player def:", self.player_def)

                                return

                        elif self.idle_state == IDLE.DEF:

                            value = card.click(pos, False, True)

                            if value:

                                self.player_def += value

                                print("player atk:", self.player_atk)
                                print("player def:", self.player_def)

                                return


    def update(self, dt):

        if self.actual_state == GameStates.DRAWING_CARDS:

            if self.visible_cards < len(self.enemy_cards):

                self.timer_next_card += dt

                if self.timer_next_card >= self.delay_next_card:
                    self.timer_next_card = 0
                    self.visible_cards += 1

            else:
                self.actual_state = GameStates.PLAYER_SELECTING_ATK_CARDS

    def draw(self, screen):

        screen.blit(self.board, (0, 0))

        player_text = self.game_controller.font.render(str(self.player.life), True, (255, 255, 255))
        enemy_text = self.game_controller.font.render(str(self.enemy.life), True, (255, 255, 255))

        screen.blit(self.life_ui, consts_and_variables.LIFE_IMAGE_ENEMY_POSITION)
        screen.blit(self.life_ui, consts_and_variables.LIFE_IMAGE_PLAYER_POSITION)

        screen.blit(player_text, (155, consts_and_variables.HEIGHT - 87))
        screen.blit(enemy_text, (155, 73))

        screen.blit(self.button_select, self.rect_button_select)

        for i in range(self.visible_cards):
            screen.blit(self.card_enemy, consts_and_variables.CARD_POSITIONS_ENEMY[i])
            self.player_cards[i].draw(screen)

    def next_round(self):

        self.player_cards.clear()
        self.enemy_cards.clear()

        self.visible_cards = 0
        self.timer_next_card = 0

        self.create_hands()

        self.actual_state = GameStates.DRAWING_CARDS