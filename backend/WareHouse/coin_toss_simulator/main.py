'''
Build a coin toss simulator for Streamlit. The script should allow the user to 'flip' a coin and display whether it lands on heads or tails.
'''
import streamlit as st
import random
import time
def coin_toss():
    result = random.choice(['Heads', 'Tails'])
    return result
def play_game():
    st.title("Coin Toss Simulator")
    st.write("Click the button to flip the coin!")
    if st.button("Flip Coin"):
        result = coin_toss()
        time.sleep(1)  # Add a short delay
        st.write(f"The coin landed on: {result}")
