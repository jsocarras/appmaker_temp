# random_number_guesser.py
import streamlit as st
from game_logic import GameLogic  # Assuming game_logic.py contains the GameLogic class
import sys
import os
import streamlit as st

from game_logic import GameLogic
def play_game():
    st.title("Guessing Game")
    st.write("Guess a number between 1 and 10 in 3 guesses or fewer.")

    if 'game_logic' not in st.session_state:
        st.session_state.game_logic = GameLogic()

    guess = st.text_input("Enter your guess:")

    if st.button("Guess"):
        result = st.session_state.game_logic.check_guess(guess)
        st.write(result)

        if st.session_state.game_logic.is_game_over():
            st.write(f"Game Over. The correct number was {st.session_state.game_logic.secret_number}.")
            del st.session_state.game_logic  # Reset the game

# The main function is removed or modified so it's not automatically executed
