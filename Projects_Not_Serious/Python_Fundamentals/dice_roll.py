import random


class Dice:
    def roll(self):
        generated_roll = (random.randint(1,10), random.randint(1,10))
        return generated_roll
