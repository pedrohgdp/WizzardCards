import pygame
from Game.cutscene_screen import CutsceneScreen


class MainMenu:
    def __init__(self, game_controller):
        pygame.mixer.music.load('Game/Music/Menu-UndetaleCopy.ogg')
        pygame.mixer.music.set_volume(0.3)
        pygame.mixer.music.play(-1)
        self.game_controller = game_controller
        self.timer = 0.0
        self.blink_interval = 1.0

        self.font_menu = pygame.font.Font('Game/Font/PressStart2P-Regular.ttf', 10)

        self.width = 600
        self.height = 600
        
        self.main_menu_image = pygame.image.load('Game/Sprites/MainMenuImage.png').convert_alpha()
        self.main_menu_image = pygame.transform.scale(self.main_menu_image, (self.width, self.height))

        self.show_text = True

        self.static_texts = [
            "Selecione cartas de ataque e aperte selecionado.",
            "Selecione cartas de defesa e aperte selecionado.",
            "Após isso os danos são computados."
        ]

        self.blink_text = "Aperte qualquer botão para continuar..."

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

        self.draw_static_texts(screen)

        if self.show_text:
            self.draw_blink_text(screen)

    def draw_static_texts(self, screen):
        margin_bottom = 290
        line_height = 14

        start_y = self.height - margin_bottom

        for i, line in enumerate(self.static_texts):
            text_surface = self.font_menu.render(line, True, (255, 190, 50))
            text_rect = text_surface.get_rect()

            text_rect.centerx = self.width // 2
            text_rect.y = start_y + i * line_height

            screen.blit(text_surface, text_rect)

    def draw_blink_text(self, screen):
        text_surface = self.font_menu.render(self.blink_text, True, (255, 190, 50))
        text_rect = text_surface.get_rect()

        text_rect.centerx = self.width // 2

        text_rect.y = self.height - 200

        screen.blit(text_surface, text_rect)