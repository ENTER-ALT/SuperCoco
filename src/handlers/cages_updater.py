class CagesUpdater:
    def __init__(self, cages) -> None:
        self.cages = cages

    def update(self) -> None:
        for cage in self.cages:
            cage.update()