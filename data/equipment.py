from enum import Enum
import random
import discord

class EquipmentType(Enum):
    PICKAXE = 'pickaxe'
    HELMET = 'helmet'
    VEST = 'vest'
    PANTS = 'pants'
    BOOTS = 'boots'
    GLOVES = 'gloves'


class Equipment:

    lines_to_color = {
        0: discord.Color.light_gray(),
        1: discord.Color.green(),
        2: discord.Color.blue(),
        3: discord.Color.purple(),
        4: discord.Color.orange(),
    }

    _equipment = [
        {
            'id': 1000,
            'name': 'Developer Pickaxe',
            'type': EquipmentType.PICKAXE,
            'stats': {
                'speed|+': 100,
            },
            'level_requirement': 0,
            'set': 'Developer',
            'value': 0,
            'max_stars': 24
        },
        {
            'id': 1100,
            'name': 'Beginner Pickaxe',
            'type': EquipmentType.PICKAXE,
            'stats': {
                'power|+': 1,
            },
            'level_requirement': 0,
            'set': None,
            'value': 100,
            'max_stars': 5
        },
        {
            'id': 1200,
            'name': 'Amateur Pickaxe',
            'type': EquipmentType.PICKAXE,
            'stats': {
                'power|+': 3
            },
            'level_requirement': 3,
            'set': None,
            'value': 150,
            'max_stars': 7
        },
        {
            'id': 1300,
            'name': 'Dark Pickaxe',
            'type': EquipmentType.PICKAXE,
            'stats': {
                'power|+': 10,
                'exp|+': 5,
            },
            'level_requirement': 10,
            'set': 'Dark',
            'value': 400,
            'max_stars': 12
        },
        {
            'id': 1400,
            'name': 'Ice Pickaxe',
            'type': EquipmentType.PICKAXE,
            'stats': {
                'power|+': 15,
                'speed|+': 5,
            },
            'level_requirement': 20,
            'set': 'Ice',
            'value': 1000,
            'max_stars': 18
        },
        {
            'id': 2100,
            'name': 'Dark Helmet',
            'type': EquipmentType.HELMET,
            'stats': {
                'power|+': 1,
            },
            'level_requirement': 10,
            'set': 'Dark',
            'value': 400,
            'max_stars': 12
        },
        {
            'id': 2200,
            'name': 'Absolute Helmet',
            'type': EquipmentType.HELMET,
            'stats': {
                'power|+': 67,
                'power|%': 5,
            },
            'level_requirement': 100,
            'set': 'Absolute',
            'value': 10000,
            'max_stars': 24
        },
        {
            'id': 3100,
            'name': 'Dark Vest',
            'type': EquipmentType.VEST,
            'stats': {
                'power|+': 3,
                'exp|+': 2,
            },
            'level_requirement': 10,
            'set': 'Dark',
            'value': 400,
            'max_stars': 12
        },
        {
            'id': 3200,
            'name': 'Beetle Armor Vest',
            'type': EquipmentType.VEST,
            'stats': {
                'power|+': 20,
                'exp|+': 4,
            },
            'level_requirement': 30,
            'set': None,
            'value': 400,
            'max_stars': 18
        },
        {
            'id': 4100,
            'name': 'Dark Pants',
            'type': EquipmentType.PANTS,
            'stats': {
                'power|+': 2,
                'exp|+': 3,
            },
            'level_requirement': 10,
            'set': 'Dark',
            'value': 400,
            'max_stars': 12
        },
        {
            'id': 5100,
            'name': 'Dark Boots',
            'type': EquipmentType.BOOTS,
            'stats': {
                'exp|+': 1,
            },
            'level_requirement': 10,
            'set': 'Dark',
            'value': 400,
            'max_stars': 12
        },
        {
            'id': 6100,
            'name': 'Dark Gloves',
            'type': EquipmentType.GLOVES,
            'stats': {
                'power|%': 5,
            },
            'level_requirement': 10,
            'set': 'Dark',
            'value': 400,
            'max_stars': 12
        },
        {
            'id': 6200,
            'name': 'Pure Gloves',
            'type': EquipmentType.GLOVES,
            'stats': {
            },
            'level_requirement': 20,
            'set': None,
            'value': 400,
            'max_stars': 18
        },
        {
            'id': 6300,
            'name': 'Superior Pure Gloves',
            'type': EquipmentType.GLOVES,
            'stats': {
            },
            'level_requirement': 50,
            'set': None,
            'value': 8000,
            'max_stars': 24
        },
        {
            'id': 6400,
            'name': 'Mastercrafted Pure Gloves',
            'type': EquipmentType.GLOVES,
            'stats': {
            },
            'level_requirement': 100,
            'set': None,
            'value': 20000,
            'max_stars': 32
        },
    ]

    stat_types = ['power', 'speed', 'luck', 'exp']

    def __init__(self):
        pass

    @staticmethod
    def get_equipment_from_id(id: int):
        for e in Equipment._equipment:
            if e['id'] == id:
                return e
        return None

    @staticmethod
    def get_equipment_from_name(name: str):
        for e in Equipment._equipment:
            if e['name'] == name:
                return e
        return None

    @staticmethod
    def get_star_bonus(stars: int):
        adder = 1
        star_bonus = 0
        while stars > 0:
            stars -= 1
            star_bonus += adder
            if stars % 5 == 0:
                adder += 1
        return star_bonus

    @staticmethod
    def get_bonus_for_weapon(name: str, current_lines: int):
        '''
            Bonuses formatted as: stat|modifier|value,...,

            Returns string representing equipment bonus.
        '''
        #Amount of lines in a bonus
        upgrade_odds = {
            1: 1,
            2: .1,
            3: .05,
            4: .025,
            5: .01
        }
        base_equipment = Equipment.get_equipment_from_name(name)
        lines = random.choices([current_lines, current_lines + 1], [1 - upgrade_odds[current_lines + 1], upgrade_odds[current_lines + 1]])[0]
        bonus = ''
        for i in range(lines):
            stat = random.choice(Equipment.stat_types)
            modifier = random.choices(['+', '%'], [.65, .35])[0]
            if modifier == '+':
                value = random.randint(int(base_equipment['level_requirement'] / 2), base_equipment['level_requirement'])
            else:
                value = random.randint(int(base_equipment['level_requirement'] / 4), base_equipment['level_requirement'] / 2)
            bonus += f'{stat}|{modifier}|{value},'
        return bonus
