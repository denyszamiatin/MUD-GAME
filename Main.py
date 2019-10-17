import re
# from validate_email import validate_email
# is_valid = validate_email('example@example.com')


def is_valid_email(email):
    # Implemented:
    # len: <= 320
    # name: len > 0
    # name: len < 64
    # @ between name and domain
    # domain: [A-Z, a-z, 0-9, - .]
    # domain: at least one .

    # TODO - Not implemented:
    # name: - ! # $ % & ‘ * + — / =? ^ _ ` { | } ~ a-zA-Z0-9-.
    # name: . ! # $ % & ‘ * + — / =? ^ _ ` { | } ~  cant be first or last.
    # name: . ! # $ % & ‘ * + — / =? ^ _ ` { | } ~  cant appear twice or more in row
    # name: only one .
    # domain: at least 2 [a-zA-Z] after last dot
    #Races parameters (strength = str, wisdom = wis, agility = agl, intellect = agl)

    pattern = r"^.{1,64}@[A-Za-z0-9\._-]+\.[a-zA-Z]*$"
    if len(email) <= 320:
        if re.match(pattern, email):
            return True
    return False

#race block
human_stats = {'str':3, 'wis':3, 'agl':3, 'int':3}
elf_stats = {'str':2, 'wis':4, 'agl':4, 'int':2}
dworf_stats = {'str':4, 'wis':2, 'agl':3, 'int':3}

def race(n):
    if n == ("human"):
        return human_stats
    elif n == ("elf"):
        return elf_stats
    elif n == ('dworf'):
        return dworf_stats
