import random

class die:

    def __init__(self, valueRange):
        self.value = None
        self.valueRange = valueRange

    def roll(self):
        holdRandom = random.randrange(1, self.valueRange, 1)
        self.value = holdRandom
        return holdRandom