from src.components.interactive_component import InteractiveComponent

class InteractComponent:
    def __init__(self) -> None:
        self.__interact_target = None
        self.__can_interact = False

    @property
    def can_interact(self) -> None:
        return self.__can_interact

    @property
    def interact_target(self) ->None:
        return self.__interact_target

    @interact_target.setter
    def interact_target(self, value: InteractiveComponent) ->None:
        if value != None:
            self.__can_interact = True
        else:
            self.__can_interact = False
        self.__interact_target = value

    def interact(self) ->None:
        if self.__can_interact:
            self.interact_target.use()
            
