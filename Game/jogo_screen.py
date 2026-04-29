import pygame
from enum import Enum
from Game import consts_variables

class GameStates(Enum):
    pass
class JogoScreen():
    def __init__(self, game_controller):
        self.game_controller = game_controller

        self.create_variables()
        self.load_images()

    def handle_events(self, events):
        pass

    def update(self, dt):
        pass

    def draw(self, screen):
        screen.blit(self.board, (0, 0))

        for pos in consts_variables.CARD_POSITIONS:
            screen.blit(self.card, pos)

    def load_images(self):
        self.board = pygame.image.load('Game/Sprites/Board.png').convert()
        self.board = pygame.transform.scale(self.board, (self.screen_width, self.screen_height))

        self.card = pygame.image.load('Game/Sprites/EnemyCard.png').convert_alpha()
        self.card = pygame.transform.scale(self.card, (self.card_width, self.card_height))


    def create_variables(self):
        self.screen_width = consts_variables.WIDTH
        self.screen_height = consts_variables.HEIGHT

        self.card_width = consts_variables.CARD_WIDTH
        self.card_height = consts_variables.CARD_HEIGHT
