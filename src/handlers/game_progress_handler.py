import pygame
import src.levels.settings as settings

green = (0, 255, 0)
blue = (0, 0, 128)

class GameProgressHandler:
    def __init__(self) -> None:
        self.cages_left = None
        self.player_health = None
        self.max_cages = None

    def update(self, screen):
        pass
        # font = pygame.font.Font(None, 32)

        # text = f'{self.player_health}'
        # textSurface = font.render(text, True, green, blue)
 
        # textRect = textSurface.get_rect()
 
        # textRect.center = (500, 500)
        # screen.blit(textSurface, textRect)
        # pygame.display.flip()