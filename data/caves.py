import random
from enum import Enum

class Drop(Enum):
    GOLD = 'gold'
    ITEM = 'item'
    EQUIPMENT = 'equipment'
    EXP = 'exp'

class Rarity(Enum):
    COMMON = 'common'
    RARE = 'rare'
    EPIC = 'epic'
    LEGENDARY = 'legendary'

'''
drops are formated in a two tuple of (type, id/amount)
'''

class Cave:
    _drops = [None, Rarity.COMMON, Rarity.RARE, Rarity.EPIC, Rarity.LEGENDARY]

    _caves = [
        # {
        #     'name': 'Developer Cave',
        #     'level_requirement': 1,
        #     'exp': 100,
        #     'drop_odds': [0, 1, 0, 0, 0],
        #     Rarity.COMMON: [(Drop.EQUIPMENT, 1000)],
        #     Rarity.RARE: [(Drop.GOLD, 5)],
        #     Rarity.EPIC: [(Drop.GOLD, 25)],
        #     Rarity.LEGENDARY: [(Drop.GOLD, 100), (Drop.EQUIPMENT, 1100)],
        #     'current_quantity': -1,
        #     'max_quantity': -1,
        # },
        {
            'name': 'Beginner Cave',
            'level_requirement': 1,
            'exp': 1,
            'drop_odds': [0.4, 0.3, 0.20, 0.08, 0.02],
            Rarity.COMMON: [(Drop.GOLD, 1)],
            Rarity.RARE: [(Drop.GOLD, 5)],
            Rarity.EPIC: [(Drop.GOLD, 25)],
            Rarity.LEGENDARY: [(Drop.GOLD, 100), (Drop.EQUIPMENT, 1100)],
            'current_quantity': -1,
            'max_quantity': -1,
        },
        {
            'name': 'Amateur Cave',
            'level_requirement': 5,
            'exp': 4,
            'drop_odds': [0.2, 0.4, 0.3, 0.09, 0.01],
            Rarity.COMMON: [(Drop.GOLD, 1)],
            Rarity.RARE: [(Drop.GOLD, 5)],
            Rarity.EPIC: [(Drop.GOLD, 25)],
            Rarity.LEGENDARY: [(Drop.GOLD, 100), (Drop.EQUIPMENT, 1200)],
            'current_quantity': -1,
            'max_quantity': -1,
        },
        {
            'name': 'Dark Cave',
            'level_requirement': 10,
            'exp': 10,
            'drop_odds': [0.85, 0.10, 0.03, 0.01, 0.01],
            Rarity.COMMON: [(Drop.GOLD, 10)],
            Rarity.RARE: [(Drop.GOLD, 100)],
            Rarity.EPIC: [(Drop.GOLD, 150), (Drop.EQUIPMENT, 2100), (Drop.EQUIPMENT, 5100)],
            Rarity.LEGENDARY: [(Drop.GOLD, 300), (Drop.EQUIPMENT, 1300), (Drop.EQUIPMENT, 6100), (Drop.EQUIPMENT, 3100), (Drop.EQUIPMENT, 4100)],
            'current_quantity': 10000,
            'max_quantity': 10000,
        },
        {
            'name': 'Ender Cave',
            'level_requirement': 100,
            'exp': 1200,
            'drop_odds': [1, 0, 0, 0, 0],
            Rarity.COMMON: [(Drop.GOLD, 10)],
            Rarity.RARE: [(Drop.GOLD, 100)],
            Rarity.EPIC: [(Drop.GOLD, 150), (Drop.EQUIPMENT, 2100), (Drop.EQUIPMENT, 5100)],
            Rarity.LEGENDARY: [(Drop.GOLD, 300), (Drop.EQUIPMENT, 1300), (Drop.EQUIPMENT, 6100), (Drop.EQUIPMENT, 3100), (Drop.EQUIPMENT, 4100)],
            'current_quantity': 10000,
            'max_quantity': 10000,
        },
    ]

    def __init__(self, cave):
        self.cave = cave

    @classmethod
    def from_cave_name(cls, cave_name: str):
        for cave in Cave._caves:
            if cave['name'] == cave_name:
                return cls(cave)
        return None

    def mine_cave(self):
        '''
            Returns a two tuple of the drop.
            (DropType, DropValue)
            or
            (None, None)
        '''
        if self.cave['current_quantity'] > 0:
            self.cave['current_quantity'] -= 1
        elif self.cave['current_quantity'] == 0:
            return (None, None)
        drop_quality = random.choices(Cave._drops, self.cave['drop_odds'])[0]
        if drop_quality:
            drop = random.choice(self.cave[drop_quality])
            return drop
        else:
            return (None, None)

    @staticmethod
    def populate_caves():
        for cave in Cave._caves:
            cave['current_quantity'] = cave['max_quantity']

    @staticmethod
    def list_caves_by_level(level=0):
        '''
            Returns a formatted string of all the caves that meet the level requirement.
        '''
        sorted_caves = sorted(Cave._caves, key=lambda cave: cave['level_requirement'])
        sorted_caves = filter(lambda cave: cave['level_requirement'] <= level, sorted_caves)
        caves_str = '\n'.join([f'`{cave["name"]}` **Level Requirement:** `{cave["level_requirement"]}`' for cave in sorted_caves])
        return caves_str

    @staticmethod
    def verify_cave(cave_name:str):
        for cave in Cave._caves:
            if cave['name'] == cave_name:
                return True
        return False
