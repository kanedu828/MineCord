from data.equipment import Equipment


class Forge:

    _forge = [
        {
            'set': 'Abyssal',
            'equipment': [1810, 2410, 3610, 4510]
        },
        {
            'set': 'Nami',
            'equipment': [1820, 2420, 3620, 4520, 5510, 6610]
        },
        {
            'set': 'Hornet',
            'equipment': [5520, 6620, 7030, 8000, 9000]
        },
        {
            'set': 'Angelic',
            'equipment': [8020, 9020]
        },
        {
            'set': 'Fallen Angelic',
            'equipment': [8010, 9010]
        }
    ]

    @staticmethod
    def get_forge_str_list():
        forge_list = []
        for i in Forge._forge:
            item_str = f'`{i["set"]} '
            item_str += ', '.join([Equipment.get_equipment_from_id(e)['type'].value for e in i['equipment']])
            item_str += '`\n'
            forge_list.append(item_str)
        return forge_list

    @staticmethod
    def get_forgable(equipment_name):
        base_equipment = Equipment.get_equipment_from_name(equipment_name)
        if not base_equipment:
            return None
        for f in Forge._forge:
            for e in f['equipment']:
                if base_equipment['id'] == e:
                    return base_equipment
        else:
            return None
