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
        5: discord.Color.red(),
    }

    _equipment = [
        {
            'id': 1000,
            'name': 'Developer Pickaxe',
            'type': EquipmentType.PICKAXE,
            'stats': {
                'speed|+': 70,
                'crit|+': 50,
            },
            'level': 0,
            'set': None,
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
            'level': 0,
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
            'level': 3,
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
                'crit|+': 5,
            },
            'level': 10,
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
            'level': 20,
            'set': None,
            'value': 1000,
            'max_stars': 18
        },
        {
            'id': 1450,
            'name': 'Sky Pickaxe',
            'type': EquipmentType.PICKAXE,
            'stats': {
                'speed|+': 30,
                'speed|%': 7,
            },
            'level': 30,
            'set': None,
            'value': 1250,
            'max_stars': 18
        },
        {
            'id': 1500,
            'name': 'Obsidian Pickaxe',
            'type': EquipmentType.PICKAXE,
            'stats': {
                'exp|+': 60,
                'power|+': 45,
                'exp|%': 5,
            },
            'level': 50,
            'set': None,
            'value': 1500,
            'max_stars': 24
        },
        {
            'id': 1600,
            'name': 'Trailblazer Pickaxe',
            'type': EquipmentType.PICKAXE,
            'stats': {
                'power|+': 30,
            },
            'level': 40,
            'set': 'Damian',
            'value': 2000,
            'max_stars': 24
        },
        {
            'id': 1700,
            'name': 'Ancient Pickaxe',
            'type': EquipmentType.PICKAXE,
            'stats': {
                'power|+': 90,
                'exp|+': 30,
            },
            'level': 40,
            'set': 'Ancient',
            'value': 25000,
            'max_stars': 18
        },
        {
            'id': 1800,
            'name': 'Origin Pickaxe',
            'type': EquipmentType.PICKAXE,
            'stats': {
                'exp|+': 120,
                'speed|+': 20,
            },
            'level': 60,
            'set': 'Origin',
            'value': 40000,
            'max_stars': 32
        },
        {
            'id': 2100,
            'name': 'Dark Helmet',
            'type': EquipmentType.HELMET,
            'stats': {
                'power|+': 1,
            },
            'level': 10,
            'set': 'Dark',
            'value': 400,
            'max_stars': 12
        },
        {
            'id': 2150,
            'name': 'Ancient Helmet',
            'type': EquipmentType.HELMET,
            'stats': {
                'power|+': 30,
                'exp|+': 30,
                'crit|+': 30,
                'luck|+': 30,
                'luck|%': 20,
            },
            'level': 40,
            'set': 'Ancient',
            'value': 25000,
            'max_stars': 18
        },
        {
            'id': 2175,
            'name': 'Brave Helmet',
            'type': EquipmentType.HELMET,
            'stats': {
                'power|+': 30,
            },
            'level': 30,
            'set': None,
            'value': 1000,
            'max_stars': 18
        },
        {
            'id': 2200,
            'name': 'Absolute Helmet',
            'type': EquipmentType.HELMET,
            'stats': {
                'power|+': 67,
                'power|%': 5,
            },
            'level': 100,
            'set': 'Absolute',
            'value': 10000,
            'max_stars': 24
        },
        {
            'id': 2300,
            'name': 'Damian Helmet',
            'type': EquipmentType.HELMET,
            'stats': {
                'power|+': 10,
                'power|%': 5,
            },
            'level': 40,
            'set': 'Damian',
            'value': 2000,
            'max_stars': 24
        },
        {
            'id': 2400,
            'name': 'Royal Crown Helmet',
            'type': EquipmentType.HELMET,
            'stats': {
                'power|+': 150,
                'luck|+': 50,
                'power|%': 20,
            },
            'level': 60,
            'set': 'Royal',
            'value': 10000,
            'max_stars': 32
        },
        {
            'id': 3100,
            'name': 'Dark Vest',
            'type': EquipmentType.VEST,
            'stats': {
                'power|+': 3,
                'exp|+': 2,
            },
            'level': 10,
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
            'level': 30,
            'set': None,
            'value': 400,
            'max_stars': 18
        },
        {
            'id': 3300,
            'name': 'Blazer Vest',
            'type': EquipmentType.VEST,
            'stats': {
                'power|+': 25,
            },
            'level': 40,
            'set': 'Damian',
            'value': 2000,
            'max_stars': 24
        },
        {
            'id': 3400,
            'name': 'Ancient Vest',
            'type': EquipmentType.VEST,
            'stats': {
                'power|+': 50,
                'exp|+': 50,

            },
            'level': 40,
            'set': 'Ancient',
            'value': 25000,
            'max_stars': 18
        },
        {
            'id': 3500,
            'name': 'Royal Vest',
            'type': EquipmentType.VEST,
            'stats': {
                'power|+': 150,
                'luck|+': 20,
                'power|%': 10
            },
            'level': 60,
            'set': 'Royal',
            'value': 10000,
            'max_stars': 32
        },
        {
            'id': 3600,
            'name': 'Origin Vest',
            'type': EquipmentType.VEST,
            'stats': {
                'exp|+': 75,
            },
            'level': 50,
            'set': 'Origin',
            'value': 40000,
            'max_stars': 32
        },
        {
            'id': 4100,
            'name': 'Dark Pants',
            'type': EquipmentType.PANTS,
            'stats': {
                'power|+': 2,
                'exp|+': 3,
            },
            'level': 10,
            'set': 'Dark',
            'value': 400,
            'max_stars': 12
        },
        {
            'id': 4200,
            'name': 'Damian Pants',
            'type': EquipmentType.PANTS,
            'stats': {
                'power|+': 32,
                'exp|+': 5,
                'speed|+': 5,
            },
            'level': 40,
            'set': 'Damian',
            'value': 4500,
            'max_stars': 24
        },
        {
            'id': 4300,
            'name': 'Ancient Pants',
            'type': EquipmentType.PANTS,
            'stats': {
                'power|+': 50,
                'luck|+': 30,
                'power|%': 10,
            },
            'level': 40,
            'set': 'Ancient',
            'value': 25000,
            'max_stars': 18
        },
        {
            'id': 4400,
            'name': 'Royal Pants',
            'type': EquipmentType.PANTS,
            'stats': {
                'power|+': 100,
                'luck|+': 40,
                'luck|%': 10
            },
            'level': 60,
            'set': 'Royal',
            'value': 10000,
            'max_stars': 32
        },
        {
            'id': 4500,
            'name': 'Origin Pants',
            'type': EquipmentType.PANTS,
            'stats': {
                'exp|+': 50,
                'speed|+': 25,
            },
            'level': 50,
            'set': 'Origin',
            'value': 40000,
            'max_stars': 32
        },
        {
            'id': 5100,
            'name': 'Dark Boots',
            'type': EquipmentType.BOOTS,
            'stats': {
                'exp|+': 1,
            },
            'level': 10,
            'set': 'Dark',
            'value': 400,
            'max_stars': 12
        },
        {
            'id': 5200,
            'name': 'Damian Boots',
            'type': EquipmentType.BOOTS,
            'stats': {
                'power|+': 20,
                'exp|%': 10,
            },
            'level': 40,
            'set': 'Damian',
            'value': 4500,
            'max_stars': 24
        },
        {
            'id': 5300,
            'name': 'Ancient Boots',
            'type': EquipmentType.BOOTS,
            'stats': {
                'power|+': 10,
                'exp|+': 10,
                'power|%': 10,
                'exp|+': 10,
            },
            'level': 40,
            'set': 'Ancient',
            'value': 25000,
            'max_stars': 18
        },
        {
            'id': 5400,
            'name': 'Void Walker Boots',
            'type': EquipmentType.BOOTS,
            'stats': {
                'exp|+': 200,
                'exp|%': 25,
            },
            'level': 100,
            'set': None,
            'value': 50000,
            'max_stars': 12
        },
        {
            'id': 5500,
            'name': 'Origin Boots',
            'type': EquipmentType.BOOTS,
            'stats': {
                'exp|+': 75,
                'exp|%': 10,
            },
            'level': 50,
            'set': 'Origin',
            'value': 40000,
            'max_stars': 32
        },
        {
            'id': 6100,
            'name': 'Dark Gloves',
            'type': EquipmentType.GLOVES,
            'stats': {
                'power|%': 5,
                'crit|+': 5,
            },
            'level': 10,
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
            'level': 30,
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
            'level': 60,
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
            'level': 100,
            'set': None,
            'value': 20000,
            'max_stars': 32
        },
        {
            'id': 6500,
            'name': 'Damian Gloves',
            'type': EquipmentType.GLOVES,
            'stats': {
                'power|+': 15,
                'speed|+': 5,
            },
            'level': 40,
            'set': 'Damian',
            'value': 2000,
            'max_stars': 24
        },
        {
            'id': 6600,
            'name': 'Ancient Gloves',
            'type': EquipmentType.GLOVES,
            'stats': {
                'power|+': 50,
                'exp|+': 50,
            },
            'level': 40,
            'set': 'Ancient',
            'value': 25000,
            'max_stars': 18
        },
    ]

    sets = {
        'Origin': [
            {
                'exp|%': 5
            },
            {
                'exp|%': 10
            },
            {
                'exp|%': 15
            },
            {
                'exp|+': 200
            }
        ],
        'Ancient': [
            {
            },
            {
                'power|+': 20,
            },
            {
                'power|+': 20,
            },
            {
                'power|%': 5,
            },
            {
                'luck|+': 5,
            },
            {
                'power|%': 10,
                'luck|+': 50,
            }
        ],
        'Damian': [
            {
            },
            {
                'power|%': 5,
            },
            {
                'power|%': 5,
            },
            {
                'power|%': 5,
            },
            {
                'exp|+': 10,
                'power|%': 5,
            },
            {
                'power|%': 10,
                'exp|%': 10,
            }
        ],
        'Dark': [
            {
            },
            {
                'exp|+': 5,
            },
            {
                'exp|+': 5,
            },
            {
                'exp|+': 10,
            },
            {
                'exp|+': 10,
            },
            {
                'exp|%': 10,
                'crit|+': 10,
            }
        ],
        'Royal': [
            {
            },
            {
                'power|+': 250,
            },
            {
                'power|%': 50,
            },
        ],
    }

    # Rollable stat types from bonuses. Does not represent all available stats in game.
    stat_types = ['power', 'speed', 'luck', 'exp', 'crit', 'drill power', 'drill exp']

    def __init__(self):
        pass

    @staticmethod
    def get_set_bonus_str(set_name: str, set_count: int):
        if set_name not in Equipment.sets:
            return ''
        set = Equipment.sets[set_name]
        set_str = f'-----{set_name} Set Bonuses-----\n'
        for i in range(len(set)):
            if set[i].items():
                if i < set_count:
                    set_str += f'** - {i + 1} - **\n'
                else:
                    set_str += f'**{i + 1}**\n'
                for key, value in set[i].items():
                    stat, modifier = key.split('|')
                    if modifier == '+':
                        set_str += f'`{modifier}{value} {stat}`\n'
                    elif modifier == '%':
                        set_str += f'`{value}{modifier} {stat}`\n'
        return set_str

    @staticmethod
    def get_base_equipment_stats_str(equipment_name: str):
        base_equipment = Equipment.get_equipment_from_name(equipment_name)
        stats_str = f'**__{base_equipment["name"]}__**\n'
        stats_str += f'`Lv: {base_equipment["level"]}`\n'
        for i in range(base_equipment['max_stars']):
            if i % 5 == 0:
                stats_str += ' '
            stats_str += '☆'
        stats_str += '\n'
        for key, value in base_equipment['stats'].items():
            stat, modifier = key.split('|')
            if modifier == '+':
                stats_str += f'`{stat}: {modifier}{value}`\n'
            elif modifier == '%':
                stats_str += f'`{stat}: {value}{modifier}`\n'
        return stats_str

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
        adder = 0
        star_bonus = 0
        for i in range(stars):
            if i % 5 == 0:
                adder += 1 * (i // 10 + 1)
            star_bonus += adder
        return star_bonus

    @staticmethod
    def get_bonus_for_weapon(name: str, current_lines: int):
        '''
            Bonuses formatted as: stat|modifier|value,...,

            Returns string representing equipment bonus.
        '''
        # Amount of lines in a bonus
        upgrade_odds = {
            1: 1,
            2: .1,
            3: .05,
            4: .025,
            5: .01,
            6: 0,
        }
        base_equipment = Equipment.get_equipment_from_name(name)
        lines = random.choices(
            [current_lines, current_lines + 1],
            [1 - upgrade_odds[current_lines + 1], upgrade_odds[current_lines + 1]])
        bonus = ''
        for i in range(lines[0]):
            stat = random.choice(Equipment.stat_types)
            modifier = random.choices(['+', '%'], [.65, .35])[0]
            if modifier == '+':
                if stat == 'crit' or stat == 'speed' or stat == 'luck':
                    value = random.randint(max(int(base_equipment['level'] / 8), 1), max(int(base_equipment['level'] / 4), 1))
                else:
                    value = random.randint(int(base_equipment['level'] / 2), int(base_equipment['level']))
            else:
                value = random.randint(int(base_equipment['level'] / 4), int(base_equipment['level'] / 2))
            bonus += f'{stat}|{modifier}|{value},'
        return bonus
