import random
from enum import Enum
from copy import copy


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


class Cave:
    _drops = [None, Rarity.COMMON, Rarity.RARE, Rarity.EPIC, Rarity.LEGENDARY]

    _caves = [
        {
            'name': 'Developer Cave',
            'level_requirement': 1,
            'exp': 100,
            'drop_odds': [0, 1, 0, 0, 0],
            Rarity.COMMON: [(Drop.EQUIPMENT, 1000)],
            Rarity.RARE: [(Drop.GOLD, 5)],
            Rarity.EPIC: [(Drop.GOLD, 25)],
            Rarity.LEGENDARY: [(Drop.GOLD, 100), (Drop.EQUIPMENT, 1100)],
            'current_quantity': 0,
            'max_quantity': 0,
        },
        {
            'name': 'Beginner Cave',
            'level_requirement': 0,
            'exp': 3,
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
            'level_requirement': 2,
            'exp': 5,
            'drop_odds': [0.2, 0.4, 0.3, 0.09, 0.01],
            Rarity.COMMON: [(Drop.GOLD, 1)],
            Rarity.RARE: [(Drop.GOLD, 5)],
            Rarity.EPIC: [(Drop.GOLD, 25), (Drop.EQUIPMENT, 1100)],
            Rarity.LEGENDARY: [(Drop.GOLD, 100), (Drop.EQUIPMENT, 1200)],
            'current_quantity': -1,
            'max_quantity': -1,
        },
        {
            'name': 'Expert Cave',
            'level_requirement': 5,
            'exp': 7,
            'drop_odds': [0.2, 0.4, 0.3, 0.09, 0.01],
            Rarity.COMMON: [(Drop.GOLD, 1)],
            Rarity.RARE: [(Drop.GOLD, 5)],
            Rarity.EPIC: [(Drop.GOLD, 25), (Drop.EQUIPMENT, 1200)],
            Rarity.LEGENDARY: [(Drop.GOLD, 100), (Drop.EQUIPMENT, 1200)],
            'current_quantity': -1,
            'max_quantity': -1,
        },
        {
            'name': 'Dark Cave',
            'level_requirement': 10,
            'exp': 15,
            'drop_odds': [0.75, 0.10, 0.08, 0.05, 0.02],
            Rarity.COMMON: [(Drop.GOLD, 1), (Drop.EXP, 5)],
            Rarity.RARE: [(Drop.GOLD, 5), (Drop.EXP, 10)],
            Rarity.EPIC: [(Drop.GOLD, 150), (Drop.EQUIPMENT, 2100), (Drop.EQUIPMENT, 5100), (Drop.EQUIPMENT, 1200)],
            Rarity.LEGENDARY: [
                (Drop.GOLD, 200),
                (Drop.EQUIPMENT, 1300),
                (Drop.EQUIPMENT, 6100),
                (Drop.EQUIPMENT, 3100),
                (Drop.EQUIPMENT, 4100)
            ],
            'current_quantity': 10000,
            'max_quantity': 10000,
        },
        {
            'name': 'Talisman Cave',
            'level_requirement': 10,
            'exp': 10,
            'drop_odds': [0.85, 0.10, 0.03, 0.01, 0.01],
            Rarity.COMMON: [(Drop.GOLD, 15), (Drop.EXP, 15)],
            Rarity.RARE: [(Drop.GOLD, 100), (Drop.EXP, 100)],
            Rarity.EPIC: [(Drop.GOLD, 600), (Drop.EXP, 150), (Drop.EQUIPMENT, 1400), (Drop.EQUIPMENT, 1300)],
            Rarity.LEGENDARY: [(Drop.GOLD, 1000), (Drop.EXP, 200), (Drop.EQUIPMENT, 6300), (Drop.EQUIPMENT, 1400)],
            'current_quantity': 100,
            'max_quantity': 100,
        },
        {
            'name': 'Bogdan Cave',
            'level_requirement': 13,
            'exp': 6,
            'drop_odds': [0.4, 0.3, 0.20, 0.08, 0.02],
            Rarity.COMMON: [(Drop.GOLD, 3)],
            Rarity.RARE: [(Drop.GOLD, 8)],
            Rarity.EPIC: [(Drop.GOLD, 40)],
            Rarity.LEGENDARY: [(Drop.GOLD, 300), (Drop.EQUIPMENT, 1200)],
            'current_quantity': -1,
            'max_quantity': -1,
        },
        {
            'name': 'Ice Cave',
            'level_requirement': 20,
            'exp': 20,
            'drop_odds': [0.4, 0.3, 0.20, 0.095, 0.005],
            Rarity.COMMON: [(Drop.GOLD, 5)],
            Rarity.RARE: [(Drop.GOLD, 13)],
            Rarity.EPIC: [(Drop.GOLD, 60), (Drop.EQUIPMENT, 1200)],
            Rarity.LEGENDARY: [(Drop.GOLD, 600), (Drop.EQUIPMENT, 6200)],
            'current_quantity': 10000,
            'max_quantity': 10000,
        },
        {
            'name': 'Ice Cave 2',
            'level_requirement': 25,
            'exp': 25,
            'drop_odds': [0.4, 0.3, 0.285, 0.01, 0.005],
            Rarity.COMMON: [(Drop.GOLD, 5)],
            Rarity.RARE: [(Drop.GOLD, 13)],
            Rarity.EPIC: [(Drop.GOLD, 60), (Drop.EQUIPMENT, 6200)],
            Rarity.LEGENDARY: [(Drop.GOLD, 600), (Drop.EQUIPMENT, 6200), (Drop.EQUIPMENT, 1400)],
            'current_quantity': 10000,
            'max_quantity': 10000,
        },
        {
            'name': 'Beetle Cave',
            'level_requirement': 30,
            'exp': 30,
            'drop_odds': [0.4, 0.3, 0.20, 0.08, 0.02],
            Rarity.COMMON: [(Drop.EXP, 5)],
            Rarity.RARE: [(Drop.GOLD, 12)],
            Rarity.EPIC: [(Drop.GOLD, 60), (Drop.EQUIPMENT, 1200)],
            Rarity.LEGENDARY: [(Drop.GOLD, 600), (Drop.EQUIPMENT, 6200), (Drop.EQUIPMENT, 3200)],
            'current_quantity': 10000,
            'max_quantity': 10000,
        },
        {
            'name': 'Falcon Cave',
            'level_requirement': 40,
            'exp': 45,
            'drop_odds': [0.4, 0.3, 0.20, 0.08, 0.02],
            Rarity.COMMON: [(Drop.EXP, 7)],
            Rarity.RARE: [(Drop.GOLD, 15)],
            Rarity.EPIC: [(Drop.GOLD, 100)],
            Rarity.LEGENDARY: [(Drop.GOLD, 600), (Drop.EXP, 300), (Drop.EQUIPMENT, 2175), (Drop.EQUIPMENT, 1450)],
            'current_quantity': 10000,
            'max_quantity': 10000,
        },
        {
            'name': 'Hawk Cave',
            'level_requirement': 45,
            'exp': 50,
            'drop_odds': [0.4, 0.3, 0.19, 0.08, 0.03],
            Rarity.COMMON: [(Drop.EXP, 15)],
            Rarity.RARE: [(Drop.GOLD, 30)],
            Rarity.EPIC: [(Drop.GOLD, 100)],
            Rarity.LEGENDARY: [(Drop.GOLD, 600), (Drop.EQUIPMENT, 2175), (Drop.EQUIPMENT, 1450)],
            'current_quantity': 10000,
            'max_quantity': 10000,
        },
        {
            'name': 'Lillard Cave',
            'level_requirement': 50,
            'exp': 55,
            'drop_odds': [0.4, 0.3, 0.20, 0.08, 0.02],
            Rarity.COMMON: [(Drop.EXP, 10)],
            Rarity.RARE: [(Drop.GOLD, 14)],
            Rarity.EPIC: [(Drop.GOLD, 75)],
            Rarity.LEGENDARY: [(Drop.GOLD, 605), (Drop.EQUIPMENT, 5200), (Drop.EQUIPMENT, 4200)],
            'current_quantity': 10000,
            'max_quantity': 10000,
        },
        {
            'name': 'Trailblazer Cave',
            'level_requirement': 55,
            'exp': 60,
            'drop_odds': [0.4, 0.3, 0.20, 0.09, 0.01],
            Rarity.COMMON: [(Drop.EXP, 10)],
            Rarity.RARE: [(Drop.GOLD, 14)],
            Rarity.EPIC: [(Drop.GOLD, 75)],
            Rarity.LEGENDARY: [
                (Drop.GOLD, 605),
                (Drop.EQUIPMENT, 1600),
                (Drop.EQUIPMENT, 2300),
                (Drop.EQUIPMENT, 3300),
                (Drop.EQUIPMENT, 6500)
            ],
            'current_quantity': 1000,
            'max_quantity': 1000,
        },
        {
            'name': 'Volcanic Cave',
            'level_requirement': 60,
            'exp': 100,
            'drop_odds': [0.4, 0.3, 0.20, 0.0999, 0.0001],
            Rarity.COMMON: [(Drop.EXP, 30)],
            Rarity.RARE: [(Drop.GOLD, 15), (Drop.EXP, 50)],
            Rarity.EPIC: [(Drop.GOLD, 50), (Drop.EXP, 100)],
            Rarity.LEGENDARY: [(Drop.GOLD, 5000), (Drop.EXP, 2500), (Drop.EQUIPMENT, 1500)],
            'current_quantity': 10000,
            'max_quantity': 10000,
        },
        {
            'name': 'Molten Cave',
            'level_requirement': 65,
            'exp': 120,
            'drop_odds': [0.4, 0.3, 0.20, 0.099, 0.001],
            Rarity.COMMON: [(Drop.EXP, 30)],
            Rarity.RARE: [(Drop.GOLD, 15), (Drop.EXP, 50)],
            Rarity.EPIC: [(Drop.GOLD, 50), (Drop.EXP, 100)],
            Rarity.LEGENDARY: [(Drop.GOLD, 5000), (Drop.EXP, 2500), (Drop.EQUIPMENT, 1500)],
            'current_quantity': 10000,
            'max_quantity': 10000,
        },
        {
            'name': 'Royal Cave',
            'level_requirement': 70,
            'exp': 250,
            'drop_odds': [0, 0, 0.9, 0.0989, 0.0011],
            Rarity.COMMON: [],
            Rarity.RARE: [],
            Rarity.EPIC: [(Drop.GOLD, 100), (Drop.GOLD, 150), (Drop.GOLD, 75)],
            Rarity.LEGENDARY: [
                (Drop.GOLD, 7500),
                (Drop.GOLD, 7000),
                (Drop.EQUIPMENT, 6300),
                (Drop.EQUIPMENT, 2400),
                (Drop.EQUIPMENT, 4400),
                (Drop.EQUIPMENT, 3500)
            ],
            'current_quantity': 10000,
            'max_quantity': 10000,
        },
        {
            'name': 'Origin Cave',
            'level_requirement': 70,
            'exp': 250,
            'drop_odds': [0.4, 0.3, 0.25, 0.04, 0.01],
            Rarity.COMMON: [(Drop.EXP, 10)],
            Rarity.RARE: [(Drop.EXP, 100)],
            Rarity.EPIC: [(Drop.EXP, 250)],
            Rarity.LEGENDARY: [
                (Drop.EQUIPMENT, 1800),
                (Drop.EQUIPMENT, 3600),
                (Drop.EQUIPMENT, 4500),
                (Drop.EQUIPMENT, 5500),
                (Drop.EQUIPMENT, 6300)
            ],
            'current_quantity': 10000,
            'max_quantity': 10000,
        },
        {
            'name': 'Null Cave',
            'level_requirement': 80,
            'exp': 0,
            'drop_odds': [0, 0, 0, 0.9999, 0.0001],
            Rarity.COMMON: [],
            Rarity.RARE: [],
            Rarity.EPIC: [],
            Rarity.LEGENDARY: [
                (Drop.EXP, 100000),
                (Drop.EQUIPMENT, 5400),
            ],
            'current_quantity': 10000,
            'max_quantity': 10000,
        },
        {
            'name': 'Ender Cave',
            'level_requirement': 100,
            'exp': 1200,
            'drop_odds': [0.4, 0.3, 0.20, 0.09, 0.01],
            Rarity.COMMON: [(Drop.GOLD, 300)],
            Rarity.RARE: [(Drop.GOLD, 500)],
            Rarity.EPIC: [(Drop.GOLD, 1000)],
            Rarity.LEGENDARY: [(Drop.GOLD, 5000), (Drop.EQUIPMENT, 2200)],
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

    def mine_cave(self, luck=0):
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
        drop_odds = copy(self.cave['drop_odds'])
        drop_odds[4] += (luck / 100) * drop_odds[4]
        drop_odds[3] += (luck / 100) * drop_odds[3]
        drop_quality = random.choices(Cave._drops, drop_odds)[0]
        if drop_quality and self.cave[drop_quality]:
            drop = random.choice(self.cave[drop_quality])
            return drop
        else:
            return (None, None)

    @staticmethod
    def populate_caves():
        for cave in Cave._caves:
            cave['current_quantity'] = cave['max_quantity']

    @staticmethod
    def set_cave_quantity(cave_name: str, quantity: int):
        for cave in Cave._caves:
            if cave['name'].lower() == cave_name.lower():
                quantity = min(cave['max_quantity'], int(quantity))
                cave['current_quantity'] = quantity
                return True
        return False

    @staticmethod
    def list_caves_by_level(level=0):
        '''
            Returns a formatted string of all the caves that meet the level requirement.
        '''
        sorted_caves = sorted(Cave._caves, key=lambda cave: cave['level_requirement'])
        sorted_caves = filter(lambda cave: cave['level_requirement'] <= level, sorted_caves)
        caves_list = [
            f'`{cave["name"]}` **Level Requirement:** `{cave["level_requirement"]}`'
            for cave
            in sorted_caves
            if not cave['current_quantity'] == 0
        ]
        return caves_list

    @staticmethod
    def verify_cave(cave_name: str):
        for cave in Cave._caves:
            if cave['name'] == cave_name:
                return True
        return False
