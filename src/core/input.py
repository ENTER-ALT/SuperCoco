import pygame, src.game, src.game_objects.player as player
import src.sound_mixer as sounds

def check_input(game: src.game.Game, player: player.Player, sound_mixer: sounds.SoundMixer) -> None:
    
    key = pygame.key.get_pressed()
    if game.state == game.mode.playing:
        check_playing(key, player, game)

    elif game.state == game.mode.main_menu:
        check_main_menu(key, game, sound_mixer)

    elif game.state == game.mode.paused:
        check_paused(key, game, sound_mixer)

    elif game.state == game.mode.dead:
        check_dead(key, game, sound_mixer)

    elif game.state == game.mode.win:
        check_win(key, game, sound_mixer)
    

def check_main_menu(key, game, sound_mixer: sounds.SoundMixer) -> None:
    if key[pygame.K_SPACE]:
        game.state = game.mode.playing 
        sound_mixer.play_background(game)

    if key[pygame.K_q]:
        game.is_running = False

def check_playing(key, player, game)-> None:
    if key[pygame.K_a] or key[pygame.K_LEFT]:
        player.direction_x = player.runs.LEFT   
    elif key[pygame.K_d] or key[pygame.K_RIGHT]:
        player.direction_x = player.runs.RIGHT
    else:
        player.direction_x = player.runs.STILL

    if key[pygame.K_SPACE] or key[pygame.K_UP]:
        player.jump()

    if key[pygame.K_e]:
        player.interact()

    if key[pygame.K_ESCAPE]:
        game.state = game.mode.paused

def check_paused(key, game, sound_mixer) -> None:
    if key[pygame.K_SPACE]:
        game.state = game.mode.playing

    if key[pygame.K_q]:
        game.state = game.mode.main_menu
        sound_mixer.play_background(game)
        game.restarted = True

def check_dead(key, game, sound_mixer) -> None:
    if key[pygame.K_SPACE]:
        game.state = game.mode.main_menu
        sound_mixer.play_background(game)
        game.restarted = True

    if key[pygame.K_q]:
        game.is_running = False

def check_win(key, game, sound_mixer) -> None:
    if key[pygame.K_SPACE]:
        game.state = game.mode.main_menu
        sound_mixer.play_background(game)
        game.restarted = True

    if key[pygame.K_q]:
        game.is_running = False
