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
    DRILL = 'drill'
    BELT = 'belt'
    CAPE = 'cape'


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
                'exp|+': 2,
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
                'power|+': 3,
                'exp|+':5,
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
                'exp|+': 10,
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
                'exp|+': 20,
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
                'exp|+': 15
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
                'exp|+': 30
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
                'exp|+': 150,
                'speed|+': 20,
            },
            'level': 60,
            'set': 'Origin',
            'value': 40000,
            'max_stars': 32
        },
        {
            'id': 1810,
            'name': 'Abyssal Pickaxe',
            'type': EquipmentType.PICKAXE,
            'stats': {
                'exp|+': 250,
                'power|+': 500,
                'crit|+': 10,
                'speed|+': 10
            },
            'level': 100,
            'set': 'Abyssal',
            'value': 50000,
            'max_stars': 37
        },
        {
            'id': 1820,
            'name': 'Nami Pickaxe',
            'type': EquipmentType.PICKAXE,
            'stats': {
                'exp|+': 850,
                'power|+': 1000,
                'crit|+': 10,
                'speed|+': 25,
                'power|%': 25,
                'exp|%': 25
            },
            'level': 150,
            'set': 'Nami',
            'value': 100000,
            'max_stars': 42
        },
        {
            'id': 2100,
            'name': 'Dark Helmet',
            'type': EquipmentType.HELMET,
            'stats': {
                'power|+': 5,
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
                'power|+': 1000,
                'exp|+': 1000,
                'crit|+': 100,
                'power|%': 25,
            },
            'level': 100,
            'set': 'Absolute',
            'value': 25000,
            'max_stars': 48
        },
        {
            'id': 2300,
            'name': 'Damian Helmet',
            'type': EquipmentType.HELMET,
            'stats': {
                'power|+': 22,
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
                'power|+': 250,
                'luck|+': 50,
                'power|%': 20,
            },
            'level': 60,
            'set': 'Royal',
            'value': 10000,
            'max_stars': 32
        },
        {
            'id': 2410,
            'name': 'Abyssal Helmet',
            'type': EquipmentType.HELMET,
            'stats': {
                'power|+': 250
            },
            'level': 100,
            'set': 'Abyssal',
            'value': 50000,
            'max_stars': 37
        },
        {
            'id': 2420,
            'name': 'Nami Helmet',
            'type': EquipmentType.HELMET,
            'stats': {
                'power|+': 500,
                'exp|+': 250,
                'luck|+': 20,
                'exp|%': 25
            },
            'level': 150,
            'set': 'Nami',
            'value': 100000,
            'max_stars': 42
        },
        {
            'id': 3100,
            'name': 'Dark Vest',
            'type': EquipmentType.VEST,
            'stats': {
                'power|+': 5,
                'exp|+': 5,
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
                'power|+': 12,
                'exp|+': 20,
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
                'exp|+': 28
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
                'power|+': 300,
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
            'id': 3610,
            'name': 'Abyssal Vest',
            'type': EquipmentType.VEST,
            'stats': {
                'power|+': 150,
                'exp|+': 150,
                'power|%': 20
            },
            'level': 100,
            'set': 'Abyssal',
            'value': 50000,
            'max_stars': 37
        },
        {
            'id': 3620,
            'name': 'Nami Vest',
            'type': EquipmentType.VEST,
            'stats': {
                'power|+': 850,
                'exp|+': 560,
                'power|%': 25,
                'exp|%': 25
            },
            'level': 150,
            'set': 'Nami',
            'value': 100000,
            'max_stars': 42
        },
        {
            'id': 4100,
            'name': 'Dark Pants',
            'type': EquipmentType.PANTS,
            'stats': {
                'power|+': 7,
                'exp|+': 8,
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
            'id': 4510,
            'name': 'Abyssal Pants',
            'type': EquipmentType.PANTS,
            'stats': {
                'power|+': 150,
                'exp|+': 150,
                'power|%': 20,
            },
            'level': 100,
            'set': 'Abyssal',
            'value': 50000,
            'max_stars': 37
        },
        {
            'id': 4520,
            'name': 'Nami Pants',
            'type': EquipmentType.PANTS,
            'stats': {
                'power|+': 560,
                'exp|+': 850,
                'exp|%': 25,
                'power|%': 25,
            },
            'level': 150,
            'set': 'Nami',
            'value': 100000,
            'max_stars': 42
        },
        {
            'id': 5100,
            'name': 'Dark Boots',
            'type': EquipmentType.BOOTS,
            'stats': {
                'exp|+': 5,
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
                'exp|+': 850,
                'exp|%': 25,
                'crit|+': 35
            },
            'level': 100,
            'set': None,
            'value': 50000,
            'max_stars': 37
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
            'id': 5510,
            'name': 'Nami Boots',
            'type': EquipmentType.BOOTS,
            'stats': {
                'luck|+': 10,
                'speed|+': 10,
                'crit|+': 10,
                'luck|%': 25,
                'crit|%': 25
            },
            'level': 150,
            'set': 'Nami',
            'value': 100000,
            'max_stars': 42
        },
        {
            'id': 5520,
            'name': 'Peachtree Boots',
            'type': EquipmentType.BOOTS,
            'stats': {
                'exp|+': 60,
                'crit|+': 10,
            },
            'level': 100,
            'set': 'Peachtree',
            'value': 25000,
            'max_stars': 32
        },
        {
            'id': 6100,
            'name': 'Dark Gloves',
            'type': EquipmentType.GLOVES,
            'stats': {
                'exp|+': 5,
                'exp|%': 5,
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
            'max_stars': 0
        },
        {
            'id': 6500,
            'name': 'Damian Gloves',
            'type': EquipmentType.GLOVES,
            'stats': {
                'exp|+': 20,
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
        {
            'id': 6610,
            'name': 'Nami Gloves',
            'type': EquipmentType.GLOVES,
            'stats': {
                'power|+': 100,
                'exp|+': 10,
                'luck|+': 15,
                'crit|+': 15,
                'luck|%': 25,
                'crit|%': 25,
                'speed|+': 15
            },
            'level': 150,
            'set': 'Nami',
            'value': 100000,
            'max_stars': 42
        },
        {
            'id': 6620,
            'name': 'Peachtree Gloves',
            'type': EquipmentType.GLOVES,
            'stats': {
                'exp|+': 60,
                'luck|+': 10,
            },
            'level': 100,
            'set': 'Peachtree',
            'value': 25000,
            'max_stars': 32
        },
        {
            'id': 7000,
            'name': 'Beginner Drill',
            'type': EquipmentType.DRILL,
            'stats': {
                'drill power|+': 10,
                'drill exp|+': 10,
            },
            'level': 10,
            'set': None,
            'value': 1000,
            'max_stars': 7
        },
        {
            'id': 7001,
            'name': 'Expert Drill',
            'type': EquipmentType.DRILL,
            'stats': {
                'drill power|+': 20,
                'drill exp|+': 20,
            },
            'level': 15,
            'set': None,
            'value': 1000,
            'max_stars': 7
        },
        {
            'id': 7010,
            'name': 'Ancient Drill',
            'type': EquipmentType.DRILL,
            'stats': {
                'drill power|+': 25,
                'drill exp|+': 150,
            },
            'level': 40,
            'set': 'Ancient',
            'value': 25000,
            'max_stars': 18
        },
        {
            'id': 7020,
            'name': 'Volcanic Drill',
            'type': EquipmentType.DRILL,
            'stats': {
                'drill power|+': 40,
                'drill exp|+': 250,
            },
            'level': 60,
            'set': None,
            'value': 25000,
            'max_stars': 24
        },
        {
            'id': 7030,
            'name': 'Peachtree Drill',
            'type': EquipmentType.DRILL,
            'stats': {
                'drill power|+': 40,
                'drill exp|+': 2000,
            },
            'level': 100,
            'set': 'Peachtree',
            'value': 25000,
            'max_stars': 32
        },
        {
            'id': 8000,
            'name': 'Peachtree Belt',
            'type': EquipmentType.BELT,
            'stats': {
                'exp|+': 100,
                'luck|+': 10,
            },
            'level': 100,
            'set': 'Peachtree',
            'value': 25000,
            'max_stars': 32
        },
        {
            'id': 8010,
            'name': 'Fallen Angelic Belt',
            'type': EquipmentType.BELT,
            'stats': {
                'exp|+': 50,
                'power|+': 50,
                'exp|%': 5,
                'power|%': 5,
                'crit|+': 5,
            },
            'level': 50,
            'set': 'Fallen Angelic',
            'value': 25000,
            'max_stars': 24
        },
        {
            'id': 8020,
            'name': 'Angelic Belt',
            'type': EquipmentType.BELT,
            'stats': {
                'exp|+': 500,
                'power|+': 500,
                'exp|%': 20,
                'power|%': 20,
                'crit|+': 50,
            },
            'level': 50,
            'set': 'Angelic',
            'value': 25000,
            'max_stars': 32
        },
        {
            'id': 9000,
            'name': 'Peachtree Cape',
            'type': EquipmentType.CAPE,
            'stats': {
                'exp|+': 150,
                'crit|+': 15,
            },
            'level': 100,
            'set': 'Peachtree',
            'value': 25000,
            'max_stars': 32
        },
        {
            'id': 9010,
            'name': 'Fallen Angelic Cape',
            'type': EquipmentType.CAPE,
            'stats': {
                'exp|+': 50,
                'power|+': 50,
                'exp|%': 5,
                'power|%': 5,
                'crit|+': 5,
            },
            'level': 50,
            'set': 'Fallen Angelic',
            'value': 25000,
            'max_stars': 24
        },
        {
            'id': 9020,
            'name': 'Angelic Cape',
            'type': EquipmentType.CAPE,
            'stats': {
                'exp|+': 500,
                'power|+': 500,
                'exp|%': 20,
                'power|%': 20,
                'crit|+': 50,
            },
            'level': 50,
            'set': 'Angelic',
            'value': 25000,
            'max_stars': 32
        },
    ]

    sets = {
        'Origin': [
            {
                'exp|+': 50
            },
            {
                'exp|+': 75
            },
            {
                'exp|%': 20
            },
            {
                'exp|+': 200
            }
        ],
        'Ancient': [
            {
            },
            {
                'power|+': 15
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
                'exp|+': 20,
                'luck|+': 5,
            },
            {
                'exp|+': 25,
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
                'exp|+': 25,
                'power|%': 5,
            },
            {
                'exp|+': 25,
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
        'Abyssal': [
            {
            },
            {
                'exp|+': 100,
                'power|+': 250,
            },
            {
                'exp|+': 150,
                'power|%': 50,
                'power|+': 250
            },
            {
                'exp|+': 150,
                'exp|%': 10,
                'power|%': 50,
                'power|+': 250
            },
        ],
        'Nami': [
            {
            },
            {
                'exp|+': 500,
            },
            {
                'exp|+': 500,
            },
            {
                'exp|+': 500,
                'power|+': 500
            },
            {
                'exp|+': 500,
                'power|+': 500
            },
            {
                'exp|+': 500,
                'power|%': 50,
                'luck|+': 50,
                'crit|+': 100
            },
        ],
        'Peachtree': [
            {
            },
            {
                'exp|+': 100,
                'crit|+': 20,
            },
            {
                'exp|+': 100,
                'crit|+': 20,
            },
            {
                'exp|+': 200,
                'power|+': 200,
                'crit|+': 20
            },
            {
                'crit|+': 100,
                'crit|%': 10
            },
        ],
        'Fallen Angelic': [
            {
            },
            {
                'exp|%': 10,
                'power|%': 10,
                'crit|%': 10,
            },
        ],
        'Angelic': [
            {
            },
            {
                'exp|%': 50,
                'power|%': 50,
                'crit|%': 50,
            },
        ],
    }

    # Rollable stat types from bonuses. Does not represent all available stats in game.
    stat_types = ['power', 'speed', 'luck', 'exp', 'crit']

    drill_stat_types = ['power', 'speed', 'luck', 'exp', 'crit', 'drill power', 'drill exp']

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
    def get_star_bonus(stars: int, multiplier=1):
        adder = 0
        star_bonus = 0
        for i in range(stars):
            if i % 5 == 0:
                if i >= 20:
                    adder += 4 * (i // 10 + 1)
                else:
                    adder += 1 * (i // 10 + 1)
            star_bonus += int((adder + adder * (multiplier - 1) * 0.25))
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
            if base_equipment['type'].value == 'drill':
                stat = random.choice(Equipment.drill_stat_types)
            else:
                stat = random.choice(Equipment.stat_types)
            modifier = random.choices(['+', '%'], [.75, .25])[0]
            if modifier == '+':
                if stat == 'crit' or stat == 'speed' or stat == 'luck':
                    value = random.randint(max(int(base_equipment['level'] / 8), 1), max(int(base_equipment['level'] / 4), 1))
                else:
                    value = random.randint(int(base_equipment['level'] / 2), int(base_equipment['level']))
            else:
                value = random.randint(int(base_equipment['level'] / 4), int(base_equipment['level'] / 2))
            bonus += f'{stat}|{modifier}|{value},'
        return bonus
