import pygame
from Game.main_menu import MainMenu

class Game:
    def __init__(self):
        self.font = pygame.font.Font("Game/Font/PressStart2P-Regular.ttf", 15)
        self.current_screen = MainMenu(self)

    def handle_events(self, events):
        self.current_screen.handle_events(events)

    def update(self, dt):
        self.current_screen.update(dt)

    def draw(self, screen):
        self.current_screen.draw(screen)