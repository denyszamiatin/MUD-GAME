import registration
import character

if character.load_game():
    print(character.character)
else:
    registration.registration()
    print(character.character)
