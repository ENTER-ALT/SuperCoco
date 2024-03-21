import levels.settings as settings
import utilities

class CameraShifter:
    def __init__(self, created_objects: utilities.level_objects) -> None:
        self.following_target = created_objects.player_list.sprite
        self.world_shift = 0 #the speed of camera(world) shifting
        self.level_objects = created_objects

    def update(self) ->None:
        for tile in self.level_objects.tiles:
            tile.shift(self.world_shift)
        for cage in self.level_objects.cages:
            cage.shift(self.world_shift)
        for enemy in self.level_objects.enemies:
            enemy.shift(self.world_shift)
        for border in self.level_objects.enemy_borders:
            border.shift(self.world_shift)
        self.scroll_x()

    def scroll_x(self):
        target = self.following_target
        target_x = target.rect.centerx
        direction_x = target.direction_x

        #if moving to the left screen
        if target_x < settings.screen_width / 3 and direction_x < 0:
            self.world_shift = 20
            target.set_speed(0)

        #if moving to the right screen
        elif target_x > settings.screen_width - (settings.screen_width / 3) and direction_x > 0:
            self.world_shift = -20
            target.set_speed(0)

        else:
            self.world_shift = 0
            target.reset_speed()