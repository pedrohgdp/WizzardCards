import pygame
import random
from Game import consts_and_variables
from Game.jogo_screen import JogoScreen
from enum import Enum

class States(Enum):
    INTRO = 1
    ASKING_NAME = 2

class CutsceneScreen:
    def __init__(self, game_controller):
        self.game_controller = game_controller
        
        self.timer = 0
        self.actual_state = States.INTRO
        self.intern_name = ""

        self.width = consts_and_variables.WIDTH
        self.height = consts_and_variables.HEIGHT
    

    def handle_events(self, events):
        for event in events:
            if self.actual_state == States.ASKING_NAME:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.intern_name = self.intern_name[:-1]
                    elif event.key == pygame.K_RETURN:
                        self.convert_name_to_seed()
                    else:
                        self.intern_name += event.unicode

    def update(self, dt):
        if self.actual_state == States.INTRO:
            self.timer += dt
            if self.timer >= 2:
                self.actual_state = States.ASKING_NAME
                self.timer = 0

    def draw(self, screen):
        screen.fill((0, 0, 0))

        if self.actual_state == States.INTRO:
            self.write_text_1_on_screen(screen)
        elif self.actual_state == States.ASKING_NAME:
            self.write_text_2_on_screen(screen)
        

    def write_text_1_on_screen(self, screen):
        text = self.game_controller.font.render("Ola mago. Bem-vindo ao jogo! ", True, (255, 255, 255))
        rect = text.get_rect(center=(self.width/2, self.height/2))
        screen.blit(text, rect)

    def write_text_2_on_screen(self, screen):
        text = self.game_controller.font.render("Conte para a gente o seu nome: ", True, (255, 255, 255))
        rect = text.get_rect(center=(self.width/2, self.height/2))
        screen.blit(text, rect)

        text_name = self.game_controller.font.render(self.intern_name, True, (255,255,255))
        rect_text_name = text_name.get_rect(center=(self.width/2 - 30, self.height/2 + 50))
        screen.blit(text_name, rect_text_name)
    
    def convert_name_to_seed(self):
        value = 0
        for c in self.intern_name:
            value += ord(c)
        self.intern_name = ""
        self.change_to_game()
        consts_and_variables.seed_random = value + random.randint(0, 50)
        print("seed_random: ", consts_and_variables.seed_random)

    def change_to_game(self):
        self.game_controller.current_screen = JogoScreen(self.game_controller)