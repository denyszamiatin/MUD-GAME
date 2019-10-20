character = {
    "email": "",
    "name": "",
    "race": "",
    "class": "",
}

# Races parameters (strength = stn, Endurance = end, agility = agl, intellect = inl)
race_stats = {
    'human': {'stn': 3, 'vit': 3, 'agl': 3, 'inl': 3},
    'elf': {'stn': 2, 'vit': 2, 'agl': 4, 'inl': 4},
    'dworf': {'stn': 4, 'vit': 4, 'agl': 2, 'inl': 2},
}

class_stats = {
    'warrior': {'stn': 2, 'vit': 1, 'agl': 0, 'inl': 0},
    'archer': {'stn': 0, 'vit': 1, 'agl': 2, 'inl': 0},
    'wizard': {'stn': 0, 'vit': 0, 'agl': 0, 'inl': 3},
}


def get_race_stats(race: str):
    """Return race statistics
    """
    try:
        return race_stats[race]
    except KeyError:
        raise TypeError("Unknown race")


def get_class_stats(_class: str):
    """Return class statistics
    """
    try:
        return class_stats[_class]
    except KeyError:
        raise TypeError("Unknown class")
