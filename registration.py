import random
import re
import character

email_pattern = re.compile(r"^.{1,64}@[A-Za-z0-9\._-]+\.[a-zA-Z]*$")
EMAIL_MAX_LENGTH = 320


def registration() -> dict:

    character.character["email"] = input_email()

    character.character["name"] = generate_name()

    character.character["race"] = choose_race()

    character.character["class"] = choose_class()

    # TODO - add method to count result of stats race + class

    return character.character


def input_email():
    print("Welcome to our game. Lets create your character")
    while True:
        email = input("Please input your email\n")
        if is_valid_email(email):
            return email
        print("Incorrect email. Please try again")


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


def input_class():
    print("Please choose you class")
    for klass in character.get_classes():
        print("Do you want to be a {} with bonuses: {}?".format(
            klass.capitalize(),
            character.get_class_stats(klass)
        ))
        answer = input("type ok to accept or anything else to decline\n")
        if answer == "ok":
            print("Congratulations, you are", klass)
            return klass
    return None


def get_random_class():
    klass = random.choice(character.get_classes())
    print("You got a random class, its", klass)
    return klass


def choose_class() -> str:
    klass = input_class()
    if klass is None:
        klass = get_random_class()
    return klass


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

