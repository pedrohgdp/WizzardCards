import pygame
from Game.game_state_controller import Game
from Game import consts_variables

pygame.init()

screen = pygame.display.set_mode((consts_variables.WIDTH, consts_variables.HEIGHT))

clock = pygame.time.Clock()

game = Game()

running = True
while running:
    dt = clock.tick(consts_variables.FPS) / 1000

    events = pygame.event.get()
    for event in events:
        if event.type == pygame.QUIT:
            running = False

    game.handle_events(events)
    game.update(dt)
    game.draw(screen)

    pygame.display.flip()

pygame.quit()