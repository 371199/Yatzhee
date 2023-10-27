import random

class Dice():
    def __init__(self) -> None:
        Die_1 = Die()
        Die_2 = Die()
        Die_3 = Die()
        Die_4 = Die()
        Die_5 = Die()
        


class Die():
    def __init__(self) -> None:
        self.value = None
        self.rolling = True

    def roll(self):
        if self.rolling:
            self.value = random.randint(1,6)