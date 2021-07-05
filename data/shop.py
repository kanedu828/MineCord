from data.caves import Drop
from data.equipment import Equipment


class Shop:

    _shop = [
        {
            'type': Drop.EQUIPMENT,
            'id': 2150,
            'cost': (Drop.GOLD, Equipment.get_equipment_from_id(2150)['value'])
        },
        {
            'type': Drop.EQUIPMENT,
            'id': 1700,
            'cost': (Drop.GOLD, Equipment.get_equipment_from_id(2150)['value'])
        },
        {
            'type': Drop.EQUIPMENT,
            'id': 3400,
            'cost': (Drop.GOLD, Equipment.get_equipment_from_id(2150)['value'])
        },
        {
            'type': Drop.EQUIPMENT,
            'id': 4300,
            'cost': (Drop.GOLD, Equipment.get_equipment_from_id(2150)['value'])
        },
        {
            'type': Drop.EQUIPMENT,
            'id': 5300,
            'cost': (Drop.GOLD, Equipment.get_equipment_from_id(2150)['value'])
        },
        {
            'type': Drop.EQUIPMENT,
            'id': 6600,
            'cost': (Drop.GOLD, Equipment.get_equipment_from_id(2150)['value'])
        },
    ]

    @staticmethod
    def get_shop_str_list():
        shop_list = []
        for i in Shop._shop:
            if i['type'] == Drop.EQUIPMENT:
                base_equipment = Equipment.get_equipment_from_id(i["id"])
                item_str = f'`{base_equipment["type"].value.title()}: '
                item_str += f'{base_equipment["name"]}: {i["cost"][1]} {i["cost"][0].value}`'
                shop_list.append(item_str)
        return shop_list

    @staticmethod
    def get_shop_item_from_name(item_name: str):
        for i in Shop._shop:
            if i['type'] == Drop.EQUIPMENT:
                base_equipment = Equipment.get_equipment_from_id(i["id"])
                if base_equipment['name'] == item_name:
                    return i
        return None
