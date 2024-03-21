import utilities
import pygame
import game
import UI.ui_renderer as ui

def render_main_menu(game):
    game.background = pygame.image.load('resources/mainmenu.png').convert_alpha()
    game.background = pygame.transform.scale(game.background, (game.width, game.height))
    game.screen.blit(game.background, (0,0))

def render_pause(game):
    game.background = pygame.image.load('resources/pausemenu.png').convert_alpha()
    game.background = pygame.transform.scale(game.background, (game.width, game.height))
    game.screen.blit(game.background, (0,0))

def render_dead(game):
    game.background = pygame.image.load('resources/died.png').convert_alpha()
    game.background = pygame.transform.scale(game.background, (game.width, game.height))
    game.screen.blit(game.background, (0,0))

def render_win(game):
    game.background = pygame.image.load('resources/win.png').convert_alpha()
    game.background = pygame.transform.scale(game.background, (game.width, game.height))
    game.screen.blit(game.background, (0,0))

def render_playing(game, created_objects: utilities.level_objects, ui_renderer: ui.UIRenderer):
    game.background = pygame.image.load('resources/beach.png').convert_alpha()
    game.background = pygame.transform.scale(game.background, (game.width, game.height))
    game.screen.blit(game.background, (0,0))
    
    created_objects.player_list.draw(game.screen)
    created_objects.tiles.draw(game.screen)
    created_objects.cages.draw(game.screen)
    created_objects.enemies.draw(game.screen)
    # created_objects.enemy_borders.draw(game.screen)

    ui_renderer.update()

def render(game: game.Game, created_objects: utilities.level_objects, ui_renderer: ui.UIRenderer) -> None:
    if game.state == game.mode.main_menu:
        render_main_menu(game)
    elif game.state == game.mode.playing:
        render_playing(game, created_objects, ui_renderer)
    elif game.state == game.mode.paused:
        render_pause(game)
    elif game.state == game.mode.dead:
        render_dead(game)
    elif game.state == game.mode.win:
        render_win(game)

    pygame.display.flip()
