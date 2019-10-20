import random
import re
import character as character

email_pattern = re.compile(r"^.{1,64}@[A-Za-z0-9\._-]+\.[a-zA-Z]*$")
EMAIL_MAX_LENGTH = 320


def registration() -> dict:

    print("Welcome to our game. Lets create your character")
    while True:
        email = input("Please input your email\n")
        if is_valid_email(email):
            character.character["email"] = email
            break
        print("Incorrect email. Please try again")

    character.character["name"] = generate_name()

    character.character["race"] = choose_race()

    character.character["class"] = choose_class()

    return character.character


def generate_name() -> str:

    """TODO - implement generation of name:
    Имя начинается с большой буквы
    Длина имени - 5-9 символов
    Имя не должно содержать более 2-х гласных или согласных подряд"""
    print("You got name: DummyName")
    return "DummyName"


def choose_race() -> str:

    """TODO - implement race choice :
    При регистрации новый игрок должен выбрать расу, к которой будет принадлежать.
    Необходимо реализовать функцию,
    которая позволит пользователю выбрать расу и произвести валидацию выбора"""
    print("You got race: Elf")
    return "elf"


def choose_class() -> str:

    print("Please choose you class")
    answer_msg = "type ok to accept or anything else to decline\n"

    for i in character.class_stats:
        print("Do you want to be a ", i.capitalize(), "with bonuses: ", character.class_stats[i], "?")
        answer = input(answer_msg)
        if answer == "ok":
            print("Congratulations, you are", i)
            return i

    rand_class = random.choice(character.class_stats)
    print("You got a random class, its", rand_class)
    return rand_class


def is_valid_email(string: str) -> bool:
    """Return True if string is valid email

    TODO - Not implemented:
    name: - ! # $ % & ‘ * + — / =? ^ _ ` { | } ~ a-zA-Z0-9-.
    name: . ! # $ % & ‘ * + — / =? ^ _ ` { | } ~  cant be first or last.
    name: . ! # $ % & ‘ * + — / =? ^ _ ` { | } ~  cant appear twice or more in row
    name: only one .
    domain: at least 2 [a-zA-Z] after last dot

    >>> is_valid_email("A"*(EMAIL_MAX_LENGTH + 1))
    False
    >>> is_valid_email("@example.org")
    False
    >>> is_valid_email('a'*65 + "@example.org")
    False
    >>> is_valid_email("a@ABCabc-123.org")
    True
    >>> is_valid_email("a@a.b.com")
    True
    """
    return len(string) <= EMAIL_MAX_LENGTH and bool(email_pattern.match(string))

