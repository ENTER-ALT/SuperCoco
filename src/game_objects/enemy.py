import pygame
import src.utilities as utilities
import src.levels.settings as settings
from src.components.shift_component import ShiftComponent
from src.components.patrol_component import PatrolComponent
from src.components.attack_component import AttackComponent
from src.components.health_component import HealthComponent
from src.components.character_animator import CharacterAnimator
import random

class Enemy(pygame.sprite.Sprite, ShiftComponent, PatrolComponent, AttackComponent, HealthComponent, CharacterAnimator):
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.import_character_assets()
        switch_direction_delay = random.uniform(1.5,3.0)
        PatrolComponent.__init__(self, switch_direction_delay)
        HealthComponent.__init__(self, health=1)
        AttackComponent.__init__(self)

        self.is_attacking = True

        self.speed = random.randint(2,6)
        self.base_speed = 10

        self.runs = utilities.directions(0, 1, -1)
        self.__direction_x = random.choice([self.runs.RIGHT, self.runs.LEFT])

        self.is_attacking = False

        self.status = 'idle'
        self.facing_right = True
        self.on_right = False 
        self.on_left = False 
        self.on_ground = False
        self.on_ceiling = False
    
    @property
    def direction_x(self):
        return self.__direction_x
    
    @direction_x.setter
    def direction_x(self, value):
        if self.__direction_x < 0:
            self.facing_right = False
        if self.__direction_x > 0:
            self.facing_right = True
        self.__direction_x = value

    def import_character_assets(self) ->None:
        # self.image = pygame.image.load('resources/enemy/enemy.png').convert_alpha()
        # image_size = (settings.tile_size*4, settings.tile_size*3)
        # self.image = pygame.transform.scale(self.image, image_size)
        # self.rect = self.image.get_rect()
        character_path = 'resources/enemy/'
        animations = {'idle':[],'run':[]}
        image_size = (settings.tile_size*1.5, settings.tile_size*3)

        for animation in animations.keys():
            full_path = character_path + animation
            animations[animation] = utilities.import_folder(full_path, image_size)

        self.image = animations['idle'][0]
        self.rect = self.image.get_rect()
        # self.rect.size = (self.image.get_width()*0.2, self.image.get_height()*0.7)
        animation_speed = 1
        CharacterAnimator.__init__(self, animations, animation_speed)

    
    def update(self) -> None:
        self.get_status()
        self.animate()

    def shift(self, x_shift: int) -> None:
        super().shift(x_shift)
        # self.collider_relative_center.x += x_shift

    def get_damage(self) ->None:
        pass    
    
    def attack(self) ->None:
        self.is_attacking = False
        self.player.__health -= 1

    def set_speed(self, speed:float)->None:
        self.speed = speed

    def reset_speed(self) -> None:
        self.speed = self.base_speed

    def get_status(self):
        if self.direction_x != 0:
            self.status = 'run'
        else:
            self.status = 'idle'
    