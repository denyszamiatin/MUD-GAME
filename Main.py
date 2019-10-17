import re


def is_valid_email(email):
    # Implemented:
    # len: <= 320
    # name: len > 0
    # name: len < 64
    # @ between name and domain

    # Not implemented
    # name: - ! # $ % & ‘ * + — / =? ^ _ ` { | } ~ a-zA-Z0-9-.
    # name: . ! # $ % & ‘ * + — / =? ^ _ ` { | } ~  cant be first or last.
    # name: . ! # $ % & ‘ * + — / =? ^ _ ` { | } ~  cant appear twice or more in row
    # name: only one .
    # domain: [A-Z, a-z, 0-9, - .]
    # domain: at least one .
    # domain: at least 2 [a-zA-Z] after last dot

    pattern = r"^.{1,64}@[A-Za-z0-9\._-]+\.[a-zA-Z]*$"
    if len(email) <= 320:
        if re.match(pattern, email):
            return True
    return False

