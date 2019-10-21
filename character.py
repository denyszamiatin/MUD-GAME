character = {
    "email": "",
    "name": "",
    "race": "",
    "class": "",
}

# Races parameters (strength = stn, Endurance = end, agility = agl, intellect = inl)
STN, VIT, AGL, INL = range(4)


_race_stats = {
    'human': (3, 3, 3, 3),
    'elf': (2, 2, 4, 4),
    'dworf': (4, 4, 2, 2),
}


_class_stats = {
    'warrior': (2, 1, 0, 0),
    'archer': (0, 1, 2, 0),
    'wizard': (0, 0, 0, 3),
}


def get_race_stats(race: str):
    """Return race statistics
    """
    try:
        return _race_stats[race]
    except KeyError:
        raise TypeError("Unknown race")


def get_class_stats(klass: str):
    """Return class statistics
    """
    try:
        return _class_stats[klass]
    except KeyError:
        raise TypeError("Unknown class")


def get_classes() -> dict:
    """Return class statistics
    """
    return _class_stats.keys()
