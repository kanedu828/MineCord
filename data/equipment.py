from enum import Enum

class EquipmentType(Enum):
    PICKAXE = 'pickaxe'
    HELMET = 'helmet'
    VEST = 'vest'
    PANTS = 'pants'
    BOOTS = 'boots'
    GLOVES = 'gloves'


class Equipment:

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
            'max_stars': 25
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
            'value': 0,
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
            'value': 100,
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
        }

    ]

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
