from src.components.patrol_component import PatrolComponent
from src.game_objects.enemy import Enemy

class PatrolSystem:
    def update(self, enemy):
        if enemy is None or not isinstance(enemy, PatrolComponent) or not enemy.patrol_activated:
            return  
        self.get_direction(enemy)

    def get_direction(self, enemy: Enemy):
        if enemy.on_left:
            enemy.direction_x = enemy.runs.RIGHT
        elif enemy.on_right:
            enemy.direction_x = enemy.runs.LEFT


