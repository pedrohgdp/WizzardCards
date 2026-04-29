import pygame
from enum import Enum
from Game import consts_variables


class JogoScreen():
    def __init__(self, game_controller):
        self.game_controller = game_controller

        self.width = consts_variables.WIDTH
        self.height = consts_variables.HEIGHT

        self.board = pygame.image.load('Game/Sprites/Board.png')
        self.board = pygame.transform.scale(self.board, (self.width, self.height))

    def handle_events(self, events):
        pass

    def update(self, dt):
        pass

    def draw(self, screen):
        pygame.Surface.blit(screen, self.board, (0, 0))