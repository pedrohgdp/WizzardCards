import pygame
import random
from Game import consts_and_variables
from Game.jogo_screen import JogoScreen
from enum import Enum

class Estado(Enum):
    INTRO = 1
    PEDIR_NOME = 2
    JOGO = 3

class CutsceneScreen:
    def __init__(self, game_controller):
        self.game_controller = game_controller
        
        self.timer = 0
        self.estado = Estado.INTRO
        self.nome_interno = ""

        self.width = consts_and_variables.WIDTH
        self.height = consts_and_variables.HEIGHT
    

    def handle_events(self, events):
        for event in events:
            if self.estado == Estado.PEDIR_NOME:
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_BACKSPACE:
                        self.nome_interno = self.nome_interno[:-1]
                    elif event.key == pygame.K_RETURN:
                        self.converter_nome_para_seed()
                    else:
                        self.nome_interno += event.unicode

    def update(self, dt):
        if self.estado == Estado.INTRO:
            self.timer += dt
            if self.timer >= 2:
                self.estado = Estado.PEDIR_NOME
                self.timer = 0

        if self.estado == Estado.JOGO:
            self.trocar_para_estado_jogo()

    def draw(self, screen):
        screen.fill((0, 0, 0))

        if self.estado == Estado.INTRO:
            self.escrever_texto_1_tela(screen)
        elif self.estado == Estado.PEDIR_NOME:
            self.escrever_texto_2_tela(screen)
        

    def escrever_texto_1_tela(self, screen):
        texto = self.game_controller.font.render("Ola mago. Bem-vindo ao jogo! ", True, (255, 255, 255))
        rect = texto.get_rect(center=(self.width/2, self.height/2))
        screen.blit(texto, rect)

    def escrever_texto_2_tela(self, screen):
        texto = self.game_controller.font.render("Contenos o seu nome: ", True, (255, 255, 255))
        rect = texto.get_rect(center=(self.width/2, self.height/2))
        screen.blit(texto, rect)

        texto_nome = self.game_controller.font.render(self.nome_interno, True, (255,255,255))
        rect_texto_nome = texto_nome.get_rect(center=(self.width/2 - 30, self.height/2 + 50))
        screen.blit(texto_nome, rect_texto_nome)
    
    def converter_nome_para_seed(self):
        valor = 0
        for c in self.nome_interno:
            valor += ord(c)
        self.nome_interno = ""
        self.estado = Estado.JOGO
        consts_and_variables.seed_random = valor + random.randint(0, 50)
        print("seed_random: ", consts_and_variables.seed_random)

    def trocar_para_estado_jogo(self):
        self.game_controller.current_screen = JogoScreen(self.game_controller)