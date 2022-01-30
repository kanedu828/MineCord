import random
from copy import copy


class Dungeon:

    _dungeons = [
        {
            'name': 'Abyssal Dungeon',
            'level_requirement': 75,
            'durability': 50000,
            'exp': 10000,
            'gold': 5000,
            'drop_rate': 0.35,
            'fragment_drop': 0,
            'clear_rate': 'daily',
        },
        {
            'name': 'Nami Dungeon',
            'level_requirement': 80,
            'durability': 10000000,
            'exp': 500000,
            'gold': 20000,
            'drop_rate': 0.5,
            'fragment_drop': 1,
            'clear_rate': 'weekly',
        },
    ]

    @classmethod
    def from_dungeon_name(cls, dungeon_name: str):
        for dungeon in Dungeon._dungeons:
            if dungeon['name'] == dungeon_name:
                return dungeon
        return None

    @staticmethod
    def list_dungeons_by_level(level=0):
        '''
            Returns a formatted string of all the caves that meet the level requirement.
        '''
        sorted_dungeons = sorted(Dungeon._dungeons, key=lambda dungeon: dungeon['level_requirement'])
        sorted_dungeons = filter(lambda dungeon: dungeon['level_requirement'] <= level, sorted_dungeons)
        dungeons_list = [
            f'`{dungeon["name"]}` **Level Requirement:** `{dungeon["level_requirement"]}`'
            for dungeon
            in sorted_dungeons
        ]
        return dungeons_list
