class Item:

    _items = [
        {
            'id': 0,
            'name': 'Abyssal Fragment',
            'type': 'fragment',
        },
        {
            'id': 1,
            'name': 'Nami Fragment',
            'type': 'fragment',
        },
        {
            'id': 2,
            'name': 'Peachtree Fragment',
            'type': 'fragment',
        },
        {
            'id': 3,
            'name': 'Fallen Angelic Fragment',
            'type': 'fragment',
        },
        {
            'id': 4,
            'name': 'Angelic Fragment',
            'type': 'fragment',
        },
    ]

    @staticmethod
    def get_item_from_id(id: int):
        for i in Item._items:
            if i['id'] == id:
                return i
        return None

    @staticmethod
    def get_item_from_name(name: str):
        for i in Item._items:
            if i['name'] == name:
                return i
        return None
