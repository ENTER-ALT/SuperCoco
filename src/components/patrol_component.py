from utilities import TIME_COUNTING_SPEED

class PatrolComponent:
    def __init__(self, switch_direction_delay) -> None:
        self.__patrol_activated = True
        self.switch_direction_delay = switch_direction_delay
        self.delay = 0
        self.delay_counter_speed = TIME_COUNTING_SPEED

    @property
    def patrol_activated(self):
        return self.__patrol_activated
    
    @patrol_activated.setter
    def patrol_activated(self, value):
        self.__patrol_activated = value