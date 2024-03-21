import pygame, utilities
import levels.settings as settings

class Game:
    def __init__(self, width=settings.screen_width, height=settings.screen_height) -> None:
        self.is_running = True
        self.set_size(width, height)
        self.clock = pygame.time.Clock()
        self.mode = utilities.game_state(0, 1, 2, 3, 4)
        self.state = self.mode.main_menu
        self.restarted = True
        self.background = None
    
    def set_size(self, width, height):
        self.width = width
        self.height = height
        settings.screen_width = width
        settings.screen_height = height
        settings.tile_size = width//30
        self.screen = pygame.display.set_mode((width, height), pygame.RESIZABLE)
