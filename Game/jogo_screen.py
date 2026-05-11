import pygame
from enum import Enum
from Game import consts_and_variables
from Game.enemy import Enemy
from Game.player import Player
from Game.deck_controller import DeckController

class GameStates(Enum):
    FILLING_HANDS = 1
    DRAWING_CARDS = 2
    PLAYER_SELECTING_ATK_CARDS = 3
    PLAYER_SELECTING_DEF_CARDS = 4
    ENEMY_SELECTING_CARDS = 5
    ATTACK_AND_DEFENSE_MODE = 6

class JogoScreen():
    def __init__(self, game_controller):
        self.game_controller = game_controller
        self.deck_controller = DeckController()
        self.deck_controller.fill_deck()

        self.create_variables()
        self.load_images()

        if self.actual_state == GameStates.FILLING_HANDS:
            self.deck_controller.fill_player_hand()
            self.deck_controller.fill_enemy_hand()
            self.actual_state = GameStates.DRAWING_CARDS

    def handle_events(self, events):
        if self.actual_state == GameStates.PLAYER_SELECTING_ATK_CARDS:
            pass

    def update(self, dt):
        if self.actual_state == GameStates.DRAWING_CARDS:

            if self.visible_cards < len(consts_and_variables.CARD_POSITIONS_ENEMY):
                self.timer_next_card += dt

                if self.timer_next_card >= self.delay_next_card:
                    self.timer_next_card = 0
                    self.visible_cards += 1

            else:
                self.actual_state = GameStates.PLAYER_SELECTING_ATK_CARDS

    def draw(self, screen):
        player_life_text = self.game_controller.font.render(str(self.player.life), True, (255, 255, 255))
        enemy_life_text = self.game_controller.font.render(str(self.enemy.life), True, (255, 255, 255))

        screen.blit(self.board, (0, 0))
        screen.blit(self.life_ui, (consts_and_variables.LIFE_IMAGE_ENEMY_POSITION_WIDTH, consts_and_variables.LIFE_IMAGE_ENEMY_POSITION_HEIGHT))
        screen.blit(self.life_ui, (consts_and_variables.LIFE_IMAGE_PLAYER_POSITION_WIDTH, consts_and_variables.LIFE_IMAGE_PLAYER_POSITION_HEIGHT))
        screen.blit(player_life_text, self.player_life_text_pos)
        screen.blit(enemy_life_text, self.enemy_life_text_pos)

        for i in range(self.visible_cards):
            pos = consts_and_variables.CARD_POSITIONS_ENEMY[i]
            screen.blit(self.card, pos)
            self.draw_player_cards(screen)

    def draw_player_cards(self, screen):
        for i in range(self.visible_cards):
            card = consts_and_variables.player_cards[i]

            self.image_card = pygame.image.load(f'Game/Sprites/Cards/{card[1]}.png').convert_alpha()

            self.image_card = pygame.transform.smoothscale(self.image_card, (self.card_player_width, self.card_player_height))

            pos = consts_and_variables.CARD_POSITIONS_PLAYER[i]

            rect = pygame.Rect(pos[0], pos[1], self.card_player_width, self.card_player_height)

            self.player_cards_rects.append(rect)

            screen.blit(self.image_card, pos)

    def load_images(self):
        self.board = pygame.image.load('Game/Sprites/Board.png').convert_alpha()
        self.board = pygame.transform.smoothscale(self.board, (self.screen_width, self.screen_height))

        self.card = pygame.image.load('Game/Sprites/EnemyCard.png').convert_alpha()
        self.card = pygame.transform.smoothscale(self.card, (self.card_enemy_width, self.card_enemy_height))

        self.life_ui = pygame.image.load('Game/Sprites/LifeImage.png').convert_alpha()
        self.life_ui = pygame.transform.smoothscale(self.life_ui, (consts_and_variables.LIFE_IMAGE_WIDTH, consts_and_variables.LIFE_IMAGE_HEIGHT))

    def create_variables(self):
        self.player = Player()

        self.enemy = Enemy()
        
        self.screen_width = consts_and_variables.WIDTH
        self.screen_height = consts_and_variables.HEIGHT

        self.card_enemy_width = consts_and_variables.CARD_ENEMY_WIDTH
        self.card_enemy_height = consts_and_variables.CARD_ENEMY_HEIGHT

        self.card_player_width = consts_and_variables.CARD_PLAYER_WIDTH
        self.card_player_height = consts_and_variables.CARD_PLAYER_HEIGHT

        self.player_life_text_pos = (155,  consts_and_variables.HEIGHT - 87)
        self.enemy_life_text_pos = (155, 87)

        self.timer_next_card = 0
        self.visible_cards = 0
        self.delay_next_card = 0.2

        self.actual_state = GameStates.FILLING_HANDS

        self.player_cards_rects = []
