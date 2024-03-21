from src.components.interactive_component import InteractiveComponent

class WinConditionChecker:
    def __init__(self, cages, game_progress) -> None:
        self.cages = cages
        self.cages_left = len(cages)

        self.game_progress = game_progress
        game_progress.max_cages = len(cages)
    def check_condition(self) -> bool:
        self.cages_left = 0
        for cage in self.cages:
            if not isinstance(cage, InteractiveComponent):
                continue
            if not cage.used:
                self.cages_left += 1
        self.game_progress.cages_left = self.cages_left
        if self.cages_left <= 0:  
            return True
        return False