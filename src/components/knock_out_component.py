from utilities import TIME_COUNTING_SPEED

class KnockOutComponent:
    def __init__(self) -> None:
        self.__is_knockout = False
        self.knock_out_time = 0.8
        self.time_counter = 0

    @property
    def is_knockout(self):
        return self.__is_knockout
    
    @is_knockout.setter
    def is_knockout(self, value):
        if value:
            self.time_counter = self.knock_out_time
        self.__is_knockout = value

    def update(self) -> None:
        if not self.is_knockout:
            return
        if self.time_counter <= 0:
            self.time_counter = 0
            self.is_knockout = False
        self.time_counter -= TIME_COUNTING_SPEED
        