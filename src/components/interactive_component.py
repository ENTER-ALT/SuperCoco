class InteractiveComponent:
    def __init__(self) -> None:
        self.__interactable = True

    def use(self):
        self.__interactable = False

    @property
    def used(self) ->None:
        return not self.__interactable