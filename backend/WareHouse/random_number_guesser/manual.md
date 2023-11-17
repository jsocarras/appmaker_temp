# Guessing Game User Manual

## Introduction

Welcome to the Guessing Game! This application allows you to play a fun game where you have to guess a random number between 1 and 10 in 3 guesses or fewer. The game is built using Python and utilizes the tkinter library for the graphical user interface.

## Installation

To install and run the Guessing Game, please follow these steps:

1. Make sure you have Python installed on your computer. You can download Python from the official website: [https://www.python.org/downloads/](https://www.python.org/downloads/)

2. Clone or download the project files from the GitHub repository: [https://github.com/your-repository](https://github.com/your-repository)

3. Open a terminal or command prompt and navigate to the project directory.

4. Install the required dependencies by running the following command:

   ```
   pip install -r requirements.txt
   ```

   This will install the necessary packages, including tkinter.

## Usage

To start the Guessing Game, follow these steps:

1. Open a terminal or command prompt and navigate to the project directory.

2. Run the following command to start the game:

   ```
   python main.py
   ```

3. The game window will appear with a label asking you to guess a number between 1 and 10.

4. Enter your guess in the entry field and click the "Guess" button.

5. A message box will appear with the result of your guess. If you guessed the correct number, you will see a congratulatory message. If your guess was too high or too low, you will receive a hint.

6. Continue guessing until you either guess the correct number or run out of guesses.

7. If you run out of guesses, a message box will appear with the correct number.

8. Click the "OK" button to close the message box and end the game.

## Game Logic

The game logic is implemented in the `game_logic.py` module. It generates a random number between 1 and 10 as the secret number and allows the user to make up to 3 guesses. The logic checks each guess and provides feedback on whether the guess is too high, too low, or correct.

## Customization

If you want to customize the game, you can modify the code in the `main.py` and `game_logic.py` files. For example, you can change the range of numbers or the number of guesses allowed.

## Conclusion

Congratulations! You have successfully installed and played the Guessing Game. Have fun guessing the random number and enjoy the game! If you have any questions or encounter any issues, please don't hesitate to contact our support team.