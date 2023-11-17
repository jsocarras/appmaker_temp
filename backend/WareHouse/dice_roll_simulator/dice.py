import random
class Dice:
    def __init__(self):
        self.id = random.randint(1, 100)  # Generate a unique ID for each dice
    def roll(self):
        return random.randint(1, 6)  # Simulate rolling the dice and return the result
    def __str__(self):
        return f"Dice {self.id}"