# main Streamlit app.py
import streamlit as st
import os
import random
import sys
import importlib
from ..backend.chatdev import chat_chain

time, directory = chat_chain.get_logfilepath()
 
GAMES_DIR = directory

def load_game_module(game_name):
    # Clear previous game directories from sys.path
    for folder in game_folders:
        folder_path = os.path.join(GAMES_DIR, folder)
        if folder_path in sys.path:
            sys.path.remove(folder_path)
            
    # Add the current game directory to sys.path
    game_dir = os.path.join(GAMES_DIR, game_name)
    if game_dir not in sys.path:
        sys.path.append(game_dir)

    # Load the game module
    module_name = game_name.replace(" ", "_") + "_main"
    sys.modules.pop(module_name, None)
    spec = importlib.util.spec_from_file_location(module_name, os.path.join(game_dir, "main.py"))
    module = importlib.util.module_from_spec(spec)
    sys.modules[module_name] = module
    spec.loader.exec_module(module)
    return module

game_folders = [folder for folder in sorted(os.listdir(GAMES_DIR))
                if os.path.isdir(os.path.join(GAMES_DIR, folder)) and not folder.startswith('.')]

st.title("Welcome to the Python Game Collection")

if 'selected_game_index' not in st.session_state or 'current_game' not in st.session_state:
    st.session_state.selected_game_index = 0
    st.session_state.current_game = None
    st.session_state.current_game_module_name = ""

selected_game_index = st.session_state.selected_game_index

# Game selection buttons
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("< Previous"):
        selected_game_index = max(0, selected_game_index - 1)
with col2:
    if st.button("Random"):
        selected_game_index = random.randint(0, len(game_folders) - 1)
with col3:
    if st.button("Next >"):
        selected_game_index = min(len(game_folders) - 1, selected_game_index + 1)

st.session_state.selected_game_index = selected_game_index
new_selected_game_name = game_folders[selected_game_index]

st.write(f"Selected Game: {new_selected_game_name}")

# Load the game module when a new game is selected
if new_selected_game_name != st.session_state.current_game_module_name:
    st.session_state.current_game = load_game_module(new_selected_game_name)
    st.session_state.current_game_module_name = new_selected_game_name

# Display the play button for the loaded game
if st.session_state.current_game:
    st.session_state.current_game.play_game()
