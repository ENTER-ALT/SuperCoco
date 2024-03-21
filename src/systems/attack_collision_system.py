import utilities
from components.health_component import HealthComponent
from components.knock_out_component import KnockOutComponent
import sound_mixer as sounds

class AttackCollisionSystem:
    def __init__(self, created_objects: utilities.level_objects) -> None:
        self.enemies = created_objects.enemies
        self.player = created_objects.player_list.sprite 
    
    def detectAttackCollision(self, sound_mixer: sounds.SoundMixer) ->None:
        player = self.player
        if not isinstance(player, HealthComponent) or player.on_recover:
            return
        for enemy in self.enemies:
            if enemy.rect.colliderect(player.rect):
                player.get_damage(enemy.damage)
                sound_mixer.play_sound(sounds.DAMAGE_SOUND)
                if not isinstance(player, KnockOutComponent):
                    continue
                knock_out_forceY = -14
                knock_out_directionX = self.get_difference(player.rect.x, enemy.rect.x)
                self.knock_out(player, knock_out_forceY, knock_out_directionX)
                    

    
    def knock_out(self, character: KnockOutComponent, forceY, directionX) -> None:
        if character.is_knockout:
            return
        character.velocity_y = forceY
        character.direction_x = directionX
        character.is_knockout = True

    def is_looking_at(self, character1, character2) -> bool:
        difference = self.get_difference(character1.rect.x, character2.rect.x)
        
        return difference == character1.direction_x
    
    def get_difference(self, x1, x2) ->int:
        difference = x1 - x2
        if difference > 0:
            difference = 1
        elif difference < 0:
            difference = -1
        else:
            difference = 0
        return difference