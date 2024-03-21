import pygame
from game_objects.scene_objects.scene_object import SceneObject

SOURCE = 'resources/enemy_borders/border_1.png'

class EnemyBorder(SceneObject):
    def __init__(self, position, size):
        super().__init__(size)
        self.image = pygame.image.load('resources/win.png')
        self.image = pygame.transform.scale(self.image, self.image_size)
        self.rect = self.image.get_rect(topleft=position)
        
