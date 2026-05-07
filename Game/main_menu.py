import pygame
from Game.cutscene_screen import CutsceneScreen
from Game import consts_and_variables

class MainMenu:
    def __init__(self, game_controller):
        self.game_controller = game_controller
        self.timer = 0.0
        self.blink_interval = 1.0

        self.font_menu = pygame.font.Font("Game/Font/PressStart2P-Regular.ttf", 10)

        self.width = consts_and_variables.WIDTH
        self.height = consts_and_variables.HEIGHT
        
        self.main_menu_image = pygame.image.load('Game/Sprites/MainMenuImage.png').convert_alpha()
        self.main_menu_image = pygame.transform.scale(self.main_menu_image, (self.width, self.height))

        self.show_text = True

    def handle_events(self, events):
        for event in events:
            if event.type == pygame.KEYDOWN:
                self.game_controller.current_screen = CutsceneScreen(self.game_controller)

    def update(self, dt):
        self.timer += dt
        
        if self.timer > self.blink_interval:
            self.show_text = not self.show_text
            self.timer = 0.0

    def draw(self, screen):
        screen.blit(self.main_menu_image, (0, 0))
        
        if self.show_text:
            self.draw_text_to_press_button(screen)

    def draw_text_to_press_button(self, screen):
        text = self.font_menu.render("Aperte qualquer botao para continuar...", True, (255, 190, 50))
        rectText = text.get_rect(center=(self.width/2 + 15, self.height/2 + 95))
        screen.blit(text, rectText)