import pygame
from game_objects.player import *
import utilities
from game_objects.scene_objects.cage import CoconutCage

class CharacterAnimator:
    def __init__(self, animations: dict, animation_speed: float) ->None:
        self.animations = animations
        
        self.frame_index = 0
        self.animation_speed = animation_speed

    def animate(self) -> None:
        if len(self.animations.keys()) < 1:
            return
        animation = self.animations[self.status]

		# loop over frame index 
        self.frame_index += utilities.TIME_COUNTING_SPEED * len(animation) *  self.animation_speed
        if self.frame_index >= len(animation):
            self.frame_index = 0

        image = animation[int(self.frame_index)]
        if isinstance(self, CoconutCage):
            self.image = image
            return
        
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image,True,False)
            self.image = flipped_image

		# set the rect
        if self.on_ground and self.on_right:
            self.rect = self.image.get_rect(bottomright = self.rect.bottomright)
        elif self.on_ground and self.on_left:
            self.rect = self.image.get_rect(bottomleft = self.rect.bottomleft)
        elif self.on_ground:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.on_ceiling and self.on_right:
            self.rect = self.image.get_rect(topright = self.rect.topright)
        elif self.on_ceiling and self.on_left:
            self.rect = self.image.get_rect(topleft = self.rect.topleft)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)

