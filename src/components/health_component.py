class HealthComponent:
    def __init__(self, health: int) -> None:
        self.max_health = health
        self.health = self.max_health
        self.on_recover = False
        self.recover_time = 2.0
        self.timer = 0
        self.timer_speed = 0.1
    
    def get_damage(self, value: int) ->None:
        self.health -= value
        if self.health <= 0:
            return
        self.on_recover = True
        self.timer = self.recover_time
    
    def update(self):
        self.timer -= self.timer_speed
        if self.timer <= 0:
            self.timer = 0
            self.on_recover = False

        