'''
Game Logic
This module contains the logic for the guessing game.
'''
import random
class GameLogic:
    def __init__(self):
        self.secret_number = random.randint(1, 10)
        self.remaining_guesses = 3
    def check_guess(self, guess):
        try:
            guess = int(guess)
        except ValueError:
            return "Invalid input. Please enter a number."
        if guess < 1 or guess > 10:
            return "Invalid input. Please enter a number between 1 and 10."
        self.remaining_guesses -= 1
        if guess == self.secret_number:
            return "Congratulations! You guessed the correct number."
        elif guess < self.secret_number:
            return "Too low. Guess higher."
        else:
            return "Too high. Guess lower."
        if self.is_game_over():
            return f"Game over. The correct number was {self.secret_number}."
    def is_game_over(self):
        return self.remaining_guesses == 0