from Game.cutscene_screen import CutsceneScreen

class Game:
    def __init__(self):
        self.current_screen = CutsceneScreen(self)

    def handle_events(self, events):
        self.current_screen.handle_events(events)

    def update(self, dt):
        self.current_screen.update(dt)

    def draw(self, screen):
        self.current_screen.draw(screen)