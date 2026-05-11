import pygame

class Card:
    def __init__(self, image, pos, size, rank, player):
        self.rank = rank

        self.player = player
        self.image = pygame.image.load(image).convert_alpha()
        self.image = pygame.transform.smoothscale(self.image, size)

        self.rect = pygame.Rect(pos[0], pos[1], size[0], size[1])

        self.selected_atk = False

        self.selected_def = False

        self.atk_total = 0

        self.def_total = 0

    def draw(self, screen):
        screen.blit(self.image, self.rect)

        if self.selected_atk:
            pygame.draw.rect(screen, (255, 44, 44), self.rect, 3)
        
        if self.selected_def:
            pygame.draw.rect(screen, (0, 255, 0), self.rect, 3)

    def click(self, pos, atk_mode):

        if self.rect.collidepoint(pos):
            if atk_mode:
                self.selected_atk = not self.selected_atk
                self.atk_total += self.rank
                print("atk_total ", self.atk_total)
                print("def_total ", self.def_total)
                return True

            self.selected_def = not self.selected_def
            self.def_total += self.rank
            print("atk_total ", self.atk_total)
            print("def_total ", self.def_total)

        return False
    
    def get_atk(self):
        return self.atk_total

    def get_def(self):
        return self.def_total