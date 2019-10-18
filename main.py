import re


email_pattern = re.compile(r"^.{1,64}@[A-Za-z0-9\._-]+\.[a-zA-Z]*$")
EMAIL_MAX_LENGTH = 320


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


# Races parameters (strength = stn, wisdom = wis, agility = agl, intellect = inl)
race_stats = {
    'human': {'stn': 3, 'end': 3, 'agl': 3, 'inl': 3},
    'elf': {'stn': 2, 'end': 2, 'agl': 4, 'inl': 4},
    'dworf': {'stn': 4, 'end': 4, 'agl': 2, 'inl': 2},
}


def get_race_stats(race: str):
    """Return race statistics
    """
    try:
        return race_stats[race]
    except KeyError:
        raise TypeError("Unknown race")