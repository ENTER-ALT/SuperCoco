import pygame

from src.components.shift_component import ShiftComponent


class SceneObject(pygame.sprite.Sprite, ShiftComponent):
    def __init__(self, size):
        super().__init__()
        self.image_size = size
