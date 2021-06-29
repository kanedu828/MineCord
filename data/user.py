import math
from data.equipment import Equipment
from collections import Counter


class User:
    def __init__(self, user, equipment, items):
        pass

    @staticmethod
    def exp_to_level(exp: int):
        # a = 10
        # b = 10
        # c = -exp
        # level = (-b + math.sqrt(b ** 2 - 4 * a * c)) / (2 * a)
        return int(math.log((exp + 164) / 165, 1.15))

    @staticmethod
    def level_to_exp(level: int):
        # return 10 * level + 10 * level ** 2
        return math.ceil(165 * 1.15 ** level - 164)

    @staticmethod
    def get_exp_bar(exp: int):
        current_level = User.exp_to_level(exp)
        next_level = current_level + 1
        current_level_exp = User.level_to_exp(current_level)
        next_level_exp = User.level_to_exp(next_level)
        percentage = int((exp - current_level_exp) / (next_level_exp - current_level_exp) * 100)
        percentage_ticks = int(percentage / 5)
        exp_bar = '|'
        for i in range(percentage_ticks):
            exp_bar += '■'
        for i in range(20 - percentage_ticks):
            exp_bar += '-'
        exp_bar += '|'
        return exp_bar

    @staticmethod
    def get_total_stats(user, equipment_list):
        '''
            Returns a dictionary of the total values of each stat.
        '''
        stats = Counter()
        bonus_percentages = Counter()
        equipped_gear = [e for e in equipment_list if e['location'] != 'inventory']
        for e in equipped_gear:
            base_equipment = Equipment.get_equipment_from_id(e['equipment_id'])
            for key, value in base_equipment['stats'].items():
                stat, modifier = key.split('|')
                if modifier == '+':
                    stats[stat] += value + Equipment.get_star_bonus(e['stars'])
                elif modifier == '%':
                    bonus_percentages[stat] += value
            for bonus in e['bonus'].split(','):
                if bonus != '':
                    stat, modifier, value = bonus.split('|')
                    if modifier == '+':
                        stats[stat] += int(value)
                    elif modifier == '%':
                        bonus_percentages[stat] += int(value)
        for key, value in bonus_percentages.items():
            stats[key] = int(stats[key] + stats[key] * (value / 100))
        return stats

    @staticmethod
    def get_equipment_in_location(equipment_list, location):
        for e in equipment_list:
            if e['location'] == location:
                return e
        return None

    @staticmethod
    def get_equipped_gear_str(equipment_list):
        equipped_gear = [
            Equipment.get_equipment_from_id(gear['equipment_id']) for gear
            in equipment_list
            if not gear['location'] == 'inventory'
        ]
        gear_str = '\n'.join([
            f'`{gear["type"].value.title()}:` `Lv: {gear["level"]}` `{gear["name"]}`'
            for gear in equipped_gear])
        return gear_str

    @staticmethod
    def get_inventory_str(equipment_list):
        equipped_gear = [
            Equipment.get_equipment_from_id(gear['equipment_id']) for gear
            in equipment_list
            if gear['location'] == 'inventory'
        ]
        gear_str = '\n'.join([
            f'`{gear["type"].value.title()}:` `Lv: {gear["level"]}` `{gear["name"]}`'
            for gear in equipped_gear])
        return gear_str

    @staticmethod
    def get_equipment_stats_str(equipment_list, equipment_name):
        base_equipment = Equipment.get_equipment_from_name(equipment_name)
        equipment = User.get_equipment_from_name(equipment_list, equipment_name)
        stats_str = ''
        if equipment:
            stats_str += f'**__{base_equipment["name"]}__**\n'
            stats_str += f'`Lv: {base_equipment["level"]}`\n'
            for i in range(equipment['stars']):
                stats_str += '★'
            for i in range(max(base_equipment['max_stars'] - equipment['stars'], 0)):
                stats_str += '☆'
            stats_str += '\n'
            for key, value in base_equipment['stats'].items():
                stat, modifier = key.split('|')
                if modifier == '+':
                    stats_str += f'`{stat}: {modifier}{value + Equipment.get_star_bonus(equipment["stars"])}'
                    stats_str += f' ({value} + {Equipment.get_star_bonus(equipment["stars"])})`\n'
                elif modifier == '%':
                    stats_str += f'`{stat}: {value}{modifier}`\n'
            stats_str += '----------Bonuses----------\n'
            for bonus in equipment['bonus'].split(','):
                if bonus != '':
                    stat, modifier, value = bonus.split('|')
                    if modifier == '+':
                        stats_str += f'`{modifier}{value} {stat}`\n'
                    elif modifier == '%':
                        stats_str += f'`{value}{modifier} {stat}`\n'
            return stats_str
        else:
            return None

    @staticmethod
    def get_equipment_from_name(equipment_list, equipment_name):
        equipment = Equipment.get_equipment_from_name(equipment_name)
        if equipment is not None:
            for e in equipment_list:
                if e['equipment_id'] == equipment['id']:
                    return e
        return None

    @staticmethod
    def get_equipment_from_id(equipment_list, equipment_id):
        for e in equipment_list:
            if e['equipment_id'] == equipment_id:
                return e
        return None

    @staticmethod
    def get_lines_for_equipment(equipment_list, equipment_name):
        equipment = User.get_equipment_from_name(equipment_list, equipment_name)
        return len([bonus for bonus in equipment['bonus'].split(',') if not bonus == ''])
