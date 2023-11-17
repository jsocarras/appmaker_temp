# main Streamlit app.py
import streamlit as st
import os
import random
import sys
import importlib
import requests
import inspect

FLASK_BACKEND_URL = 'http://localhost:9000'
filepath = os.path.dirname(__file__)
root = os.path.dirname(filepath)
backend = os.path.join(root, "backend")
directory_name = os.path.join(backend, "WareHouse")

GAMES_DIR = directory_name
form = False

def buttonSubmit(name, desc):
    print("Submitting form")
    print("name is: ", name, " description is ", desc)
    form_data = {'name': name, 'desc': desc}
    response = requests.post(f'{FLASK_BACKEND_URL}/api/data', data=form_data)

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

    # Find and return the last defined method in the module
    methods = []
    for func in dir(module):
        try:
            attr = getattr(module, func)
            if callable(attr):
                methods.append(attr)
        except TypeError as e:
            print(f"Error processing {func}: {e}")

    sorted_methods = sorted(methods, key=lambda f: inspect.getsourcelines(f)[1])
    last_method = sorted_methods[-1] if sorted_methods else None

    return last_method

game_folders = [folder for folder in sorted(os.listdir(GAMES_DIR))
                if os.path.isdir(os.path.join(GAMES_DIR, folder)) and not folder.startswith('.')]

st.title("Welcome to the Python Game Collection")

if 'selected_game_index' not in st.session_state or 'current_game' not in st.session_state:
    st.session_state.selected_game_index = 0
    st.session_state.current_game = None
    st.session_state.current_game_module_name = ""

selected_game_index = st.session_state.selected_game_index

# Game selection buttons
col1, col2, col3, col4 = st.columns(4)
with col1:
    if st.button("< Previous"):
        selected_game_index = max(0, selected_game_index - 1)
with col2:
    if st.button("Random"):
        selected_game_index = random.randint(0, len(game_folders) - 1)
with col3:
    if st.button("Next >"):
        selected_game_index = min(len(game_folders) - 1, selected_game_index + 1)
with col4:
    with st.expander("Create Game"):
        with st.form("Label"):
            name = st.text_input("Name")
            desc = st.text_input("Task")
            if st.form_submit_button("Submit"):
                buttonSubmit(name, desc)

st.session_state.selected_game_index = selected_game_index
new_selected_game_name = game_folders[selected_game_index]

st.write(f"Selected Game: {new_selected_game_name}")

# Load the game module when a new game is selected
if new_selected_game_name != st.session_state.current_game_module_name:
    st.session_state.current_game = load_game_module(new_selected_game_name)
    st.session_state.current_game_module_name = new_selected_game_name

# Display the play button for the loaded game
if st.session_state.current_game:
    st.session_state.current_game()
