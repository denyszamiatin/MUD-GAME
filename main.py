import pickle

import registration
import character
from character import character


def load_game() -> (bool, str):
    global character # TODO - rewrite from global, return character
    try:
        with open('savefile.dat', 'rb') as f:
            return True, pickle.load(f)
    except FileNotFoundError:
        return False, None


def save_game():
    with open('savefile.dat', 'wb') as f:
        pickle.dump([character, ], f)


game_loaded, character_load = load_game()


if game_loaded:
    character.character = character_load
    print(character.character)
else:
    registration.registration()
    save_game()
    print(character.character)


