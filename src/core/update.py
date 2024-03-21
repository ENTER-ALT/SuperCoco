from src.handlers.collision_handler import CollisionHandler
from src.handlers.interaction_detection_handler import InteractionDetectionHandler
from src.handlers.win_condition_check_handler import WinConditionChecker
from src.handlers.lose_condition_check_handler import LoseConditionChecker
from src.systems.player.character_move_system import CharacterMoveSystem
from src.systems.attack_collision_system import AttackCollisionSystem
from src.systems.enemy.patrol_system import PatrolSystem
from src.handlers.game_progress_handler import GameProgressHandler
from src.handlers.enemy_collision_handler import EnemyCollisionHandler
from src.handlers.cages_updater import CagesUpdater
import src.sound_mixer as sounds
import src.utilities as utilities
import src.game as game

FPS = 60
FRAME_TARGET_TIME = 1000/FPS

class ActionUpdater:
    def __init__(self, game: game.Game, created_objects: utilities.level_objects, game_progress: GameProgressHandler, sound_mixer: sounds.SoundMixer) -> None:
        self.collision_handler = CollisionHandler(created_objects.tiles)
        self.enemy_collision_handler = EnemyCollisionHandler(created_objects.enemy_borders)
        self.interaction_detection_handler = InteractionDetectionHandler(created_objects.cages)
        self.character_move_system = CharacterMoveSystem()
        self.player = created_objects.player_list.sprite
        self.win_condition_checker = WinConditionChecker(created_objects.cages, game_progress)
        self.lose_condition_checker = LoseConditionChecker(self.player, game_progress)
        self.attack_collision_system = AttackCollisionSystem(created_objects)
        self.patrol_system = PatrolSystem()
        self.cages_updater = CagesUpdater(created_objects.cages)
        self.sound_mixer = sound_mixer
        self.game = game
        self.created_objects = created_objects

    def update(self, bit_scaler) -> None:
        game = self.game
        player = self.player

        delta_time = (game.clock.tick(FPS) * .001 * FRAME_TARGET_TIME)
        if delta_time > 2:
            delta_time = 2
        utilities.TIME_COUNTING_SPEED = delta_time/10
        #time_to_wait = int(FRAME_TARGET_TIME - delta_time)
        # if 0 < time_to_wait <= FRAME_TARGET_TIME:
        #     pygame.time.delay(time_to_wait)
        if game.state == game.mode.playing: 
            self.character_move_system.horizontal_movement(player, delta_time)
            self.collision_handler.horizontal_movement_collision(player)
            self.character_move_system.vertical_movement(player, delta_time)
            self.collision_handler.vertical_movement_collision(player)
            self.interaction_detection_handler.update(player)

            player.update()

            for enemy in self.created_objects.enemies:
                # self.patrol_system.update(enemy)
                self.character_move_system.horizontal_movement(enemy, delta_time)
                self.enemy_collision_handler.horizontal_movement_collision(enemy)
                enemy.update()

            self.attack_collision_system.detectAttackCollision(self.sound_mixer)
            bit_scaler.update(delta_time)
            self.cages_updater.update()

            game_won = self.win_condition_checker.check_condition()
            if game_won:
                game.state = game.mode.win
                self.sound_mixer.play_background(game)
            game_lost = self.lose_condition_checker.check_condition()
            if game_lost:
                game.state = game.mode.dead
                self.sound_mixer.play_background(game)
            
