import pygame
import src.utilities as utilities
from src.components.character_animator import  CharacterAnimator
from src.components.interact_component import InteractComponent
from src.components.knock_out_component import KnockOutComponent
from src.components.health_component import HealthComponent
import src.levels.settings as settings

class Player(pygame.sprite.Sprite, CharacterAnimator, InteractComponent, HealthComponent, KnockOutComponent):
    def __init__(self) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.import_character_assets()
        InteractComponent.__init__(self)
        HealthComponent.__init__(self, health=5)
        KnockOutComponent.__init__(self)

        self.base_speed = 20
        self.reset_speed()
        self.jump_force = -35
        self.gravity = 3

        self.runs = utilities.directions(0, 1, -1)
        self.__direction_x = self.runs.STILL
        self.velocity_y = 0.0

        self.status = 'idle'
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False
    
    @property
    def direction_x(self):
        return self.__direction_x
    
    @direction_x.setter
    def direction_x(self, value):
        if self.is_knockout:
            return
        if self.__direction_x < 0:
            self.facing_right = False
        if self.__direction_x > 0:
            self.facing_right = True
        self.__direction_x = value

    def import_character_assets(self) ->None:
        character_path = 'resources/character/'
        animations = {'idle':[],'run':[],'jump':[],'fall':[],'knock_out':[]}
        image_size = (settings.tile_size*2, settings.tile_size*2)

        for animation in animations.keys():
            full_path = character_path + animation
            animations[animation] = utilities.import_folder(full_path, image_size)

        self.image = animations['idle'][0]
        self.rect = self.image.get_rect()
        animation_speed = 1
        CharacterAnimator.__init__(self, animations, animation_speed)
    
    def update(self) ->None:
        HealthComponent.update(self)
        KnockOutComponent.update(self)
        self.apply_gravity()
        self.get_status()
        self.animate()

    def jump(self) ->None:
        if not self.on_ground or self.is_knockout:
            return
        self.velocity_y = self.jump_force

    def apply_gravity(self) ->None:
        self.velocity_y += self.gravity

    def set_speed(self, speed:float)->None:
        self.speed = speed

    def reset_speed(self) ->None:
        self.speed = self.base_speed

    def get_status(self) ->None:
        if self.is_knockout:
            self.status = 'knock_out'
        elif self.velocity_y < 0:
            self.status = 'jump'
        elif self.velocity_y > 3.4:
            self.status = 'fall'
        else:
            if (self.direction_x > 0 and not self.on_right) or (self.direction_x < 0 and not self.on_left):
                self.status = 'run'
            else:
                self.status = 'idle'
