import pickle

import registration
import character

if character.load_game():
    print(character.character)
else:
    registration.registration()
    character.save_game()
    print(character.character)


