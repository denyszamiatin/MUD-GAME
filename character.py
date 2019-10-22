import pickle
import typing

character = {
    "name": "",
    "race": "",
    "klass": "",
    "health": "",
    "stats": [0, 0, 0, 0],
    "email": "",
}

# Races parameters
# (strength = STN, Endurance = VIT, agility = AGL, intellect = INL)
STN, VIT, AGL, INL = range(4)


_RACE_STATS = {
    'human': (3, 3, 3, 3),
    'elf': (2, 2, 4, 4),
    'dworf': (4, 4, 2, 2),
}


_CLASS_STATS = {
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


def update_character_stats(stats):
    character['stats'] = [sum(x) for x in zip(get_character_stats(), stats, )]


def get_character_stat(stat_name):
    return character["stats"][stat_name]


def set_character_stat(stat_name, stat_value):
    character["stats"][stat_name] = stat_value


def get_race_stats(race: str):
    """Return race statistics
    """
    try:
        return _RACE_STATS[race]
    except KeyError:
        raise TypeError("Unknown race")


def get_class_stats(klass: str):
    """Return class statistics
    """
    try:
        return _CLASS_STATS[klass]
    except KeyError:
        raise TypeError("Unknown class")


def get_classes() -> typing.Iterable[str]:
    """Return class statistics
    """
    return _CLASS_STATS.keys()


def get_races() -> typing.Iterable[str]:
    """Return class statistics
    """
    return _RACE_STATS.keys()


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
