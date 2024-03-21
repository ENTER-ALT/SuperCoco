import pygame
from src.utilities import TEXT_FONT
from src.game import Game
from src.game_objects.player import Player
from src.handlers.game_progress_handler import GameProgressHandler
from src.levels.settings import *

class UIRenderer:

    def __init__(self, game_progress: GameProgressHandler, game: Game, player: Player) -> None:
        self.cages_counter_image, self.cages_counter_text = self.load_cages_indicator()
        self.health_image = self.load_health_image()
        self.interaction_button = self.load_interaction_button()

        self.game_progress = game_progress
        self.game = game
        self.player = player
        self.y = self.cages_counter_text.get_height()

    def update(self):
        self.render_health_bar(self.game_progress, self.game)
        self.render_cages_indicator(self.game_progress, self.game)
        self.render_interaction_button(self.game, self.player)

    def load_health_image(self) -> pygame.Surface:
        image = pygame.image.load('resources/UI/UI_1.png')
        image = pygame.transform.scale(image, (tile_size*0.8,tile_size*0.8))
        rect = image.get_rect()

        return image

    def load_cages_indicator(self) -> tuple():
        image = pygame.image.load('resources/UI/UI_2.png')
        image = pygame.transform.scale(image, (tile_size*1,tile_size*1))
        cages_text = TEXT_FONT.render(f'{0}/{0}', True, 'Black')

        return image, cages_text
    
    def load_interaction_button(self) -> pygame.Surface:
        E_text = TEXT_FONT.render('E', True, 'Black')

        return E_text

    def render_health_bar(self, game_progress: GameProgressHandler, game: Game) -> None:
        if game_progress.player_health is None:
            return
        image = self.health_image
        for i in range(1, game_progress.player_health+1):
            game.screen.blit(image, (i*tile_size*1.1, self.y))

    def render_cages_indicator(self, game_progress: GameProgressHandler, game: Game) -> None:
        if game_progress.max_cages is None or game_progress.cages_left is None:
            return
        self.cages_counter_text = TEXT_FONT.render(f'{game_progress.max_cages-game_progress.cages_left}/{game_progress.max_cages}', True, 'Black')
        cages_text = self.cages_counter_text

        game.screen.blit(cages_text, (game.width - 2*cages_text.get_width(), self.y))
        game.screen.blit(self.cages_counter_image, (game.width - (2*cages_text.get_width()+tile_size*1.1), self.y-tile_size*0.2))
    
    def render_interaction_button(self, game: Game, player: Player):
        position = player.rect.x + player.rect.width/2, player.rect.y - player.rect.height/2
        if player.can_interact:
            game.screen.blit(self.interaction_button, position)
            


