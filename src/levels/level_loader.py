import pygame
import utilities
from game_objects.scene_objects.cage import CoconutCage
from game_objects.scene_objects.enemy_border import EnemyBorder
from game_objects.scene_objects.tile import Tile
from game_objects.player import Player
from game_objects.enemy import Enemy
import levels.settings as settings

TILES = 'tiles'
CAGES = 'cages'
PLAYER ='player'
ENEMIES = 'enemies'
ENEMY_BORDERS = 'borders'
CAGE_WITH_PRISONER_INDEX = 1

class LevelLoader:
    def setup_level(self, layout) -> utilities.level_objects:
        objects_data = self.collect_objects_data(layout)
        tiles = self.create_tiles(objects_data[TILES])
        player = self.create_player(objects_data[PLAYER])
        cages = self.create_cages(objects_data[CAGES])
        enemies = self.create_enemies(objects_data[ENEMIES])
        enemy_borders = self.create_enemy_borders(objects_data[ENEMY_BORDERS])
        return utilities.level_objects(tiles, player, cages, enemies, enemy_borders)

    def collect_objects_data(self, layout) -> dict:
        objects_data = {
            TILES:[], CAGES:[], PLAYER:[], ENEMIES:[], ENEMY_BORDERS:[]
        }
        tile_size = settings.tile_size
        for row_index, row in enumerate(layout):
            for col_index, cell_number in enumerate(row):
                if cell_number in range(1,5):
                    spawn_position = pygame.math.Vector2(col_index * tile_size, row_index * tile_size)
                    objects_data[TILES].append(utilities.tile_info(spawn_position, cell_number))
                elif cell_number == 'P':
                    spawn_position = pygame.math.Vector2(col_index * tile_size, row_index * tile_size)
                    objects_data[PLAYER].append(spawn_position)
                elif cell_number == 'C':
                    spawn_position = pygame.math.Vector2(col_index * tile_size, row_index * tile_size)
                    objects_data[CAGES].append(spawn_position)
                elif cell_number == 7:
                    spawn_position = pygame.math.Vector2(col_index * tile_size, row_index * tile_size)
                    objects_data[ENEMIES].append(spawn_position)
                elif cell_number == 9:
                    spawn_position = pygame.math.Vector2(col_index * tile_size, row_index * tile_size)
                    objects_data[ENEMY_BORDERS].append(spawn_position)
        return objects_data

    def create_enemy_borders(self, spawn_info) ->pygame.sprite.Group:
        borders = pygame.sprite.Group()
        for spawn in spawn_info:
            border =  EnemyBorder((spawn.x,spawn.y),(settings.tile_size, settings.tile_size))
            borders.add(border)
        return borders


    def create_cages(self, spawn_info) ->pygame.sprite.Group:
        cages = pygame.sprite.Group()
        for spawn in spawn_info:
            cage =  CoconutCage(CAGE_WITH_PRISONER_INDEX,(spawn.x,spawn.y),(settings.tile_size*2.3, settings.tile_size*2))
            half_height = cage.rect.height//2
            cage.rect.x = spawn.x
            cage.rect.y = spawn.y - half_height
            cages.add(cage)
        return cages
    
    def create_enemies(self, spawn_info) ->pygame.sprite.Group:
        enemies = pygame.sprite.Group()
        for spawn in spawn_info:
            enemy =  Enemy()

            half_height = enemy.image.get_height()//2
            enemy.rect.x = spawn.x
            enemy.rect.y = spawn.y - half_height - settings.tile_size*0.5

            enemies.add(enemy)
        return enemies

    def create_player(self, spawn_info) ->pygame.sprite.GroupSingle:
        player_list = pygame.sprite.GroupSingle()
        for spawn in spawn_info:
            character = Player()
            half_height = character.rect.height//2
            character.rect.x = spawn.x
            character.rect.y = spawn.y - half_height
            player_list.add(character)
        return player_list

    def create_tiles(self, spawn_info) ->pygame.sprite.Group:
        tiles = pygame.sprite.Group()
        for spawn, cell_number in spawn_info:
            tile =  Tile(cell_number,(spawn.x,spawn.y),(settings.tile_size, settings.tile_size))
            tiles.add(tile)
                    
        return tiles
