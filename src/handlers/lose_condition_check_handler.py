
class LoseConditionChecker:
    def __init__(self, player, game_progress) -> None:
        self.player = player
        self.game_progress = game_progress

    def check_condition(self) -> bool:
        self.game_progress.player_health = self.player.health
        if self.player.rect.y > 1920 or self.player.health <= 0:
            return True
        return False