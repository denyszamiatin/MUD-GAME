import pickle

character = {

    "name": "",
    "race": "",
    "klass": "",
    "health": "",
    "stats": (0, 0, 0, 0),
    "email": "",
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


def get_character_class():
    return character["klass"]


def get_character_race():
    return character["race"]


def get_character_health():
    return character["health"]


def set_character_health(amount):
    character["health"] = amount


def get_character_stats():
    return character["stats"]


def set_character_stats(stats):
    character["stats"] = stats


def get_character_stat(stat_name):
    return character["stats"][stat_name]


def set_character_stat(stat_name, stat_value):
    character["stats"] = stat_value
    #TODO - rewrite, it doesnt work


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


def save_game():
    with open('savefile.dat', 'wb') as f:
        pickle.dump([character, ], f, protocol=2)


def load_game() -> bool:
    global character
    try:
        with open('savefile.dat', 'rb') as f:
            character = pickle.load(f)
            return True
    except FileNotFoundError:
        return False
