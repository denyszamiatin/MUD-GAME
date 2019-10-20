





# Races parameters (strength = stn, Endurance = end, agility = agl, intellect = inl)
race_stats = {
    'human': {'stn': 3, 'vit': 3, 'agl': 3, 'inl': 3},
    'elf': {'stn': 2, 'vit': 2, 'agl': 4, 'inl': 4},
    'dworf': {'stn': 4, 'vit': 4, 'agl': 2, 'inl': 2},
}


def get_race_stats(race: str):
    """Return race statistics
    """
    try:
        return race_stats[race]
    except KeyError:
        raise TypeError("Unknown race")