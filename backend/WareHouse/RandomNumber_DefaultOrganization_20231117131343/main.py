'''
main.py
'''
import random
import streamlit as st
import time
def main():
    st.title("Random Number Generator")
    # Create an empty placeholder
    random_number_placeholder = st.empty()
    # Initialize the random_number key in the session state
    if 'random_number' not in st.session_state:
        st.session_state.random_number = None
    # Generate a new random number if it doesn't exist or if the button is pressed
    if st.button("Generate Random Number") or st.session_state.random_number is None:
        random_number = random.randint(1, 100)
        st.session_state.random_number = random_number
    # Update the placeholder with the current random number
    random_number_placeholder.write("Random Number:", st.session_state.random_number)
    # Update the random number every 5 seconds
    while True:
        time.sleep(5)
        random_number = random.randint(1, 100)
        st.session_state.random_number = random_number
        random_number_placeholder.write("Random Number:", st.session_state.random_number)
if __name__ == "__main__":
    main()