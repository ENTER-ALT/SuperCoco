import pygame

class ColliderComponent:
    def __init__(self, collider_size, collider_relative_center=pygame.Vector2(0,0)) -> None:
        self.collider_size = collider_size
        self.collider_relative_center = collider_relative_center

    @property
    def collider_center(self):
        return pygame.Vector2(self.rect.centerx + self.collider_relative_center.x, self.rect.centery + self.collider_relative_center.y)
    @property
    def collider_left(self):
        return self.collider_center.x - self.collider_size.x//2
    @property
    def collider_right(self):
        return self.collider_center.x + self.collider_size.x//2
    @property
    def collider_top(self):
        return self.collider_center.y - self.collider_size.y//2
    @property
    def collider_bottom(self):
        return self.collider_center.y + self.collider_size.y//2