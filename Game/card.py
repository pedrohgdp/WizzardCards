import pygame

class Card:
    def __init__(self, image, pos, size):
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, size)

        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])
        self.selected = False

    def draw(self, screen):
        screen.blit(self.image, self.rect)

        if self.selected:
            pygame.draw.rect(screen, (0, 255, 0), self.rect, 3)

    def click(self, pos):
        if self.rect.collidepoint(pos):
            self.selected = not self.selected