import pygame

from game_objects.scene_objects.scene_object import SceneObject


class Tile(SceneObject):
    def __init__(self, num, position, size):
        super().__init__(size)
        self.image = pygame.image.load(f'resources/tiles/tile-{num}.png')
        self.image = pygame.transform.scale(self.image, self.image_size)
        self.rect = self.image.get_rect(topleft=position)
