import streamlit as st
from dice import Dice

def play_game():
    # Create a session state to maintain the dice count and dice objects between interactions
    if 'dice_count' not in st.session_state:
        st.session_state['dice_count'] = 1
        st.session_state['dice_list'] = [Dice() for _ in range(st.session_state['dice_count'])]
    # Display the dice count selection
    st.sidebar.header("Dice Count")
    dice_count = st.sidebar.slider("Select the number of dice", 1, 6, st.session_state['dice_count'])
    if dice_count != st.session_state['dice_count']:
        # Update the dice count and recreate or remove dice objects if necessary
        if dice_count > st.session_state['dice_count']:
            extra_dice_count = dice_count - st.session_state['dice_count']
            extra_dice_list = [Dice() for _ in range(extra_dice_count)]
            st.session_state['dice_list'].extend(extra_dice_list)
        else:
            excess_dice_count = st.session_state['dice_count'] - dice_count
            st.session_state['dice_list'] = st.session_state['dice_list'][:-excess_dice_count]
        st.session_state['dice_count'] = dice_count
    # Get the dice objects from the session state
    dice_list = st.session_state['dice_list']
    # Display the dice roll button
    if st.button("Roll Dice"):
        # Roll each dice and display the result
        for dice in dice_list:
            result = dice.roll()
            st.write(f"Dice: {dice}, Result: {result}")
