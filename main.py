import pygame
import sys, src.game as g, src.core.input as input,  src.core.update as update, src.core.render as render, src.core.camera_shifter as camera_shifter
import src.levels.settings as settings
from src.levels.level_loader import LevelLoader
from src.handlers.game_progress_handler import GameProgressHandler
import src.UI.ui_renderer as ui
import src.sound_mixer as sounds
from src.systems.bit_scaler_system import BitScalerSystem
pygame.init()

import moviepy.editor as moviepy

video = moviepy.VideoFileClip("resources/Videos/intro.mp4")
video.preview()

if not pygame.get_init():
        print("error initializing pygame", file=sys.stderr)
        exit(-1)

def main() -> None:
    game = g.Game()

    while game.is_running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game.is_running = False 
            elif event.type == pygame.VIDEORESIZE:
                game.set_size(event.w, event.h)

        if game.restarted:
            level_loader = LevelLoader() 
            created_objects = level_loader.setup_level(settings.level_map)
            player = created_objects.player_list.sprite
            game_progress = GameProgressHandler()

            sound_mixer = sounds.SoundMixer(game)
            action_updater = update.ActionUpdater(game, created_objects, game_progress, sound_mixer)
            camera = camera_shifter.CameraShifter(created_objects)
            ui_renderer = ui.UIRenderer(game_progress=game_progress, game=game, player=player)
            sound_mixer.play_background(game)
            bit_scaler = BitScalerSystem(created_objects)
            
            game.restarted = False

        input.check_input(game, player, sound_mixer)
        if game.state is game.mode.playing and not game.restarted:
            game_progress.update(game.screen)
            action_updater.update(bit_scaler)
            camera.update()
        render.render(game, created_objects, ui_renderer)
    pygame.quit()


if __name__ == "__main__":
    main()
