import discord
import asyncio
from discord.ext import commands, tasks
import random
from data.caves import Cave, Drop
from data.dungeons import Dungeon
from data.equipment import Equipment
from data.items import Item
from data.user import User
from util.custom_cooldown_mapping import CustomCooldownMapping
from util.dbutil import DBUtil
from collections import Counter
from data.blacklist import blacklist
from util.menu import PageMenu, ConfirmationMenu
from datetime import datetime, timedelta
import pytz


# class MiningCooldown:
#     def __init__(self, db):
#         self.db = db
#         async def mining_cooldown(message):
#             equipment_list = await self.db.get_equipment_for_user(message.author.id)
#             total_stats = User.get_total_stats(message.author.id, equipment_list)
#             speed = total_stats['speed']
#             cooldown = max(10 - 10 * (speed / 100), 3)
#             return commands.Cooldown(1, cooldown, commands.BucketType.user)
#         self.mapping = CustomCooldownMapping(mining_cooldown)
#
#     async def __call__(self, ctx: commands.Context):
#         bucket = await self.mapping.get_bucket(ctx.message)
#         retry_after = bucket.update_rate_limit()
#         if retry_after:
#             raise commands.CommandOnCooldown(bucket, retry_after)
#         return True


class Mining(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.db = DBUtil(client.pool)
        self.cooldowns = {} # Dynamic cooldowns don't work with db calls, so this is the current sol.
        self.daily_task.start()

    monster_failures = Counter()

    @tasks.loop(hours=24)
    async def daily_task(self):
        self.cooldowns = {}

    async def indicate_level_up(ctx, exp1: int, exp2: int):
        level1 = User.exp_to_level(exp1)
        level2 = User.exp_to_level(exp2)
        if User.check_if_level_up(exp1, exp2):
            message_embed = discord.Embed(title='Level Up!', color=discord.Color.blue())
            pre_cave_list = Cave.list_caves_by_level(level1)
            post_cave_list = Cave.list_caves_by_level(level2)
            unlocked_caves = list(set(post_cave_list) - set(pre_cave_list))
            message_embed.description = f'You leveled up to level `{level2}`!'
            if unlocked_caves:
                cave_str = '\n'.join([cave for cave in unlocked_caves])
                message_embed.description += f'\n**__New Caves unlocked:__**\n {cave_str}'
            await ctx.send(embed=message_embed)

    # async def mining_cooldown(message):
    #     equipment_list = asyncio.run(self.db.get_equipment_for_user(message.author.id))
    #     total_stats = User.get_total_stats(message.author.id, equipment_list)
    #     speed = total_stats['speed']
    #     cooldown = max(10 - 10 * (speed / 100), 3)
    #     return commands.Cooldown(1, cooldown)
    def check_blacklist(ctx):
        return not ctx.author.id in blacklist

    async def get_mine_cooldown(self, ctx):
        if ctx.author.id in self.cooldowns:
            equipment_list = await self.db.get_equipment_for_user(ctx.author.id)
            total_stats = User.get_total_stats(ctx.author.id, equipment_list)
            speed = total_stats['speed']
            cooldown = max(10 - 10 * (speed / 100), 3)
            cd_td = timedelta(seconds=cooldown)
            delta = datetime.now() - self.cooldowns[ctx.author.id]
            if delta < cd_td:
                return (cd_td - delta).total_seconds()
            else:
                self.cooldowns[ctx.author.id] = datetime.now()
                return 0
        else:
            self.cooldowns[ctx.author.id] = datetime.now()
            return 0

    async def monster_encounter(self, ctx):
        emoji_list = ['🤡', '👹', '👽', '👾', '🤖', '👻', '💩']
        action_list = [emoji_list.pop(random.randrange(len(emoji_list))) for i in range(3)]
        correct_action = random.choice(action_list)
        message_embed = discord.Embed(title='Monster!', color=discord.Color.red())
        message_embed.description = f'''
            {ctx.author.mention} has encountered a monster while mining!
            React with {correct_action} within a minute to prevent the
            monster from stealing coin!'''
        message = await ctx.send(embed=message_embed)
        for action in action_list:
            await message.add_reaction(action)

        def check(reaction, user):
            return user.id == ctx.author.id and reaction.message.id == message.id

        try:
            reaction, react_user = await self.client.wait_for('reaction_add', check=check, timeout=60.0)
            if reaction.emoji != correct_action:
                raise(asyncio.TimeoutError)
        except asyncio.TimeoutError:
            await self.db.set_user_gold(ctx.author.id, int(user['gold'] * 0.9))
            exp_lost = (user['exp'] - User.level_to_exp(User.exp_to_level(user['exp']))) * 0.1
            await self.db.update_user_exp(ctx.author.id, -exp_lost)
            message_embed.description = f'''
                Ouch! You did not react correctly.
                You lost {int(user["gold"] * 0.9)} gold!
                You also lost {exp_lost} exp!'''
            await message.edit(embed=message_embed)
            self.monster_failures[ctx.author.id] += 1
            if self.monster_failures[ctx.author.id] >= 5:
                blacklist[ctx.author.id] = True
        else:
            message_embed.description = 'Whew! You defended yourself against the monster!'
            await message.edit(embed=message_embed)
            self.monster_failures[ctx.author.id] = 0

    @commands.command(name='dmine', aliases=['dm'])
    @commands.check(check_blacklist)
    async def dmine(self, ctx):
        message_embed = discord.Embed(title='Dungeon Mine!', color=discord.Color.purple())
        cd = await self.get_mine_cooldown(ctx)
        if cd:
            message_embed.description = f'You are too tired to mine. Please wait {round(cd, 2)} seconds!'
            await ctx.send(embed=message_embed)
            return
        user = await self.db.get_user(ctx.author.id)
        dungeon = Dungeon.from_dungeon_name(user['dungeon'])
        equipment_list = await self.db.get_equipment_for_user(ctx.author.id)
        total_stats = User.get_total_stats(ctx.author.id, equipment_list, user['blessings'])
        if dungeon:
            result = await self.db.get_dungeon_instance(ctx.author.id, dungeon['name'])
            if not result:
                result = await self.db.insert_dungeon_instance(ctx.author.id, dungeon['name'], dungeon['durability'], dungeon['clear_rate'])
            dungeon_instance = result[0]
            if dungeon_instance['durability'] > 0:
                message_embed.description = f'**{dungeon["name"]}**\n'
                m = 1  # multiplier
                odds = random.randrange(100)
                if odds <= total_stats['crit']:
                    message_embed.description += 'Critical Strike!\n'
                    overflow = max(total_stats['crit'] - 100, 0)
                    m *= 2 + (overflow / 100)
                power = int(total_stats['power'] * m)
                power = min(power, dungeon_instance['durability'])
                result = await self.db.update_dungeon_durability(ctx.author.id, dungeon['name'], -power)
                message_embed.description += f'`Dungeon Durability: {result[0]["durability"]}/{dungeon["durability"]}`\n'
                message_embed.description += f'You mined and dealt `{power} damage` to the dungeon\'s durability!'
                odds = random.randrange(100)
                if odds <= 5:
                    await self.monster_encounter(ctx)
                if result[0]['durability'] <= 0:
                    message_embed.description += '\n**Dungeon Cleared!**\n'
                    await self.db.update_user_exp(ctx.author.id, dungeon['exp'])
                    await self.db.update_user_gold(ctx.author.id, dungeon['gold'])
                    await Mining.indicate_level_up(ctx, user['exp'], user['exp'] + dungeon['exp'])
                    message_embed.description += f'You gained:\n `{dungeon["exp"]} exp`\n`{dungeon["gold"]} gold`\n'
                    rolls = (total_stats['luck'] // 100) + 1
                    drop = random.choices([True, False], [dungeon['drop_rate'], 1 - dungeon['drop_rate']], k=rolls)
                    num_fragments = drop.count(True)
                    if num_fragments:
                        message_embed.description += f'`{num_fragments} {Item.get_item_from_id(dungeon["fragment_drop"])["name"]}(s)`'
                        await self.db.update_item_count(ctx.author.id, dungeon['fragment_drop'], num_fragments)
            else:
                message_embed.description = f'You have already cleared {dungeon["name"]}!'

        await ctx.send(embed=message_embed)

    @commands.command(name='mine', aliases=['m'])
    @commands.check(check_blacklist)
    # @commands.dynamic_cooldown(mining_cooldown, commands.BucketType.user)
    async def mine(self, ctx):
        message_embed = discord.Embed(title='Mine!', color=discord.Color.dark_orange())
        cd = await self.get_mine_cooldown(ctx)
        if cd:
            message_embed.description = f'You are too tired to mine. Please wait {round(cd, 2)} seconds!'
            await ctx.send(embed=message_embed)
            return
        user = await self.db.get_user(ctx.author.id)
        cave = Cave.from_cave_name(user['cave'])
        if cave.cave['current_quantity'] == 0:
            message_embed.description = f'{cave.cave["name"]} cannot be mined anymore.'
            await ctx.send(embed=message_embed)
            return
        equipment_list = await self.db.get_equipment_for_user(ctx.author.id)
        total_stats = User.get_total_stats(ctx.author.id, equipment_list, user['blessings'])
        drop_type, drop_value = cave.mine_cave(total_stats['luck'])
        message_embed.description = f'**{ctx.author.mention} mined at {cave.cave["name"]} and found:**\n'
        m = 1  # multiplier
        odds = random.randrange(100)
        if odds <= total_stats['crit']:
            overflow = max(total_stats['crit'] - 100, 0)
            m *= 2 + (overflow / 100)
            message_embed.description += 'Critical mine! Extra exp gained.\n'
        if datetime.now(pytz.utc).hour == 23:
            m *= 2
            message_embed.title = 'Happy Hour Mining!'
        if cave.cave['exp'] > 0:
            exp_gained = cave.cave['exp'] + total_stats['exp']
            exp_gained *= m
            exp_gained = int(exp_gained)
            await self.db.update_user_exp(ctx.author.id, exp_gained)
            message_embed.description += f'`{exp_gained} exp '
            message_embed.description += f'({int(cave.cave["exp"] * m)} + {int(total_stats["exp"] * m)})`'
            message_embed.description += '\n'
        if drop_type == Drop.GOLD:
            gold = drop_value + min(drop_value * 10, total_stats['power'])
            await self.db.update_user_gold(ctx.author.id, gold)
            message_embed.description += f'`{gold} gold ({drop_value} + {min(drop_value * 10, total_stats["power"])})`\n'
        elif drop_type == Drop.EQUIPMENT:
            equipment_list = await self.db.get_equipment_for_user(ctx.author.id)
            equipment = User.get_equipment_from_id(equipment_list, drop_value)
            base_equipment = Equipment.get_equipment_from_id(drop_value)
            if equipment:
                if equipment['stars'] < base_equipment['max_stars']:
                    await self.db.update_equipment_stars(ctx.author.id, drop_value, 1)
                    message_embed.description += f'`{base_equipment["name"]}. Equipment star level increased!`\n'
                else:
                    message_embed.description += f'`{base_equipment["name"]}. Equipment is already at max star level.'
                    message_embed.description += 'Gold recieved instead.`'
                    message_embed.description += f'\n`{base_equipment["value"]} gold`'
                    await self.db.update_user_gold(ctx.author.id, base_equipment["value"])
            else:
                await self.db.insert_equipment(ctx.author.id, drop_value, 'inventory')
                message_embed.description += f'`You mined a {base_equipment["name"]}!`\n'
        elif drop_type == Drop.EXP:
            exp_gained = drop_value + total_stats['exp']
            exp_gained *= m
            exp_gained = int(exp_gained)
            await self.db.update_user_exp(ctx.author.id, exp_gained)
            message_embed.description += f'`{exp_gained} exp ({int(drop_value * m)} + {int(total_stats["exp"] * m)})`\n'
        await ctx.send(embed=message_embed)
        await Mining.indicate_level_up(ctx, user['exp'], user['exp'] + exp_gained)
        # Monster attack to prevent automation.
        odds = random.randrange(100)
        if odds <= 5:
            await self.monster_encounter(ctx)

    @commands.command(name='drill', aliases=['d'])
    async def drill(self, ctx):
        message_embed = discord.Embed(title='Drilling', color=discord.Color.dark_orange())
        user = await self.db.get_user(ctx.author.id)
        equipment_list = await self.db.get_equipment_for_user(ctx.author.id)
        total_stats = User.get_total_stats(ctx.author.id, equipment_list, user['blessings'])
        level = User.exp_to_level(user['exp'])
        since_last_drill = datetime.now() - user['last_drill']
        num_ten_min = int(since_last_drill.total_seconds()) // 600
        num_ten_min = min(num_ten_min, 6 * 24) # set max of 24 hours worth of idle mining
        base_exp = int((level ** 1.3)) * num_ten_min
        exp_gained = base_exp + total_stats["drill exp"] * num_ten_min
        gold = int(10 + total_stats["drill power"]) * num_ten_min
        if num_ten_min > 0:
            message_embed.description = (
                f'`Time Since Last Successful Drill: {str(since_last_drill).split(".")[0]}`\n'
                f'`{exp_gained} exp ({base_exp} + {total_stats["drill exp"] * num_ten_min})`\n'
                f'`{gold} gold ({10 * num_ten_min} + {total_stats["drill power"] * num_ten_min})`'
            )
            await self.db.update_user_exp(ctx.author.id, exp_gained)
            await self.db.update_user_gold(ctx.author.id, gold)
            await self.db.set_user_last_drill(ctx.author.id, datetime.now())
        else:
            message_embed.description = 'There are no rewards yet, check again later!'
        await ctx.send(embed=message_embed)
        await Mining.indicate_level_up(ctx, user['exp'], user['exp'] + exp_gained)

    @commands.command(name='cave', aliases=['c'])
    async def cave(self, ctx, *, cave_name=''):
        cave_name = cave_name.title()
        user = await self.db.get_user(ctx.author.id)
        cave = Cave.from_cave_name(user['cave'])
        cave_quantity = cave.cave['current_quantity']
        user_level = User.exp_to_level(user['exp'])
        if cave_quantity == -1:
            cave_quantity = 'Infinite'
        message_embed = discord.Embed(title='Cave', color=discord.Color.dark_orange())
        to_cave = Cave.from_cave_name(cave_name)
        if cave_name and Cave.verify_cave(cave_name) and user_level >= to_cave.cave['level_requirement']:
            await self.db.update_user_cave(ctx.author.id, cave_name)
            message_embed.description = f'You have switched to {cave_name}.'
            await ctx.send(embed=message_embed)
        else:
            paginator = commands.Paginator('', '', 1800, '\n')
            paginator.add_line(
                f'''**Current Cave**: `{user["cave"]}`\n
                **Remaining Mines:**`{cave_quantity}`\n
                **__Available Caves:__**\n''')
            for cave in Cave.list_caves_by_level(user_level):
                paginator.add_line(cave)
            menu = PageMenu('Caves', discord.Color.dark_orange(), paginator.pages)
            await menu.start(ctx)

    @commands.command(name='dungeon')
    async def dungeon(self, ctx, *, dungeon_name=''):
        dungeon_name = dungeon_name.title()
        user = await self.db.get_user(ctx.author.id)
        dungeon = Dungeon.from_dungeon_name(dungeon_name)
        user_level = User.exp_to_level(user['exp'])
        message_embed = discord.Embed(title='Dungeon', color=discord.Color.purple())
        if dungeon and user_level >= dungeon['level_requirement']:
            durability = dungeon['durability']
            await self.db.update_user_dungeon(ctx.author.id, dungeon['name'])
            message_embed.description = f'You have switched to {dungeon["name"]}.'
            await ctx.send(embed=message_embed)
        else:
            paginator = commands.Paginator('', '', 1800, '\n')
            if user['dungeon']:
                dungeon_instance = await self.db.get_dungeon_instance(ctx.author.id, user['dungeon'])
                user_dungeon = Dungeon.from_dungeon_name(user['dungeon'])
                if dungeon_instance:
                    current_durability = dungeon_instance[0]['durability']
                else:
                    current_durability = user_dungeon['durability']
                paginator.add_line(
                    f'''**Current Dungeon**: `{user["dungeon"]}`\n
                    **Durability:**`{current_durability}/{user_dungeon["durability"]}`\n
                    **Clear Rate:** `{user_dungeon["clear_rate"]}`\n
                    **__Available Dungeons:__**\n''')
            else:
                paginator.add_line('**Current Dungeon:** None\n**__Available Dungeons:__**\n')
            for dun in Dungeon.list_dungeons_by_level(user_level):
                paginator.add_line(dun)
            menu = PageMenu('Dungeons', discord.Color.purple(), paginator.pages)
            await menu.start(ctx)


    @commands.command(name='stats')
    async def stats(self, ctx, member: discord.Member = None):
        if not member:
            member = ctx.author
        message_embed = discord.Embed(title=f'{member}\'s Stats', color=discord.Color.dark_teal())
        user = await self.db.get_user(member.id)
        equipment_list = await self.db.get_equipment_for_user(member.id)
        stats_ordering = {
            'exp': 0,
            'power': 1,
            'crit': 2,
            'speed': 3,
            'luck': 4,
            'drill exp': 5,
            'drill power': 6,
        }
        stats_list = [
            (key, value)
            for key, value
            in User.get_total_stats(user, equipment_list, user['blessings']).items()]
        stats_list.sort(key=lambda s: stats_ordering[s[0]])
        user_stats = '\n'.join(
            [f'`{key}`: `{value}`'
                for key, value
                in stats_list])
        stats = f'''
            `Level: {User.exp_to_level(user["exp"])}` \n
            `{User.get_exp_bar(user["exp"])}`\n
            `Total EXP: {user["exp"]}`\n
            `Gold: {user["gold"]}` \n
            `Blessings: {user["blessings"]}`\n
            **__Stats:__**\n
            {user_stats}
        '''
        message_embed.description = stats
        await ctx.send(embed=message_embed)

    @commands.command(name='equip', aliases=['e'])
    async def equip(self, ctx, *, equipment_name):
        equipment_name = equipment_name.title()
        message_embed = discord.Embed(title='Equip', color=discord.Color.from_rgb(245, 211, 201))  # peachy color
        equipment_list = await self.db.get_equipment_for_user(ctx.author.id)
        equipment = User.get_equipment_from_name(equipment_list, equipment_name)
        if equipment:
            type = Equipment.get_equipment_from_name(equipment_name)['type'].value
            current_in_location = User.get_equipment_in_location(equipment_list, type)
            if current_in_location:
                await self.db.update_equipment_location(ctx.author.id, current_in_location['equipment_id'], 'inventory')
            await self.db.update_equipment_location(ctx.author.id, equipment['equipment_id'], type)
            message_embed.description = f'You have equipped your {equipment_name}'
        else:
            message_embed.description = 'You do not have this equipment!'
        await ctx.send(embed=message_embed)

    @commands.command(name='gear', aliases=['g'])
    async def gear(self, ctx, *, equipment_name=''):
        equipment_name = equipment_name.title()
        message_embed = discord.Embed(title='Gear', color=discord.Color.from_rgb(245, 211, 201))  # peachy color
        equipment_list = await self.db.get_equipment_for_user(ctx.author.id)
        gear_str = User.get_equipment_stats_str(equipment_list, equipment_name)
        if equipment_name and gear_str:
            message_embed.color = Equipment.lines_to_color[User.get_lines_for_equipment(equipment_list, equipment_name)]
            message_embed.description = gear_str
            file_name = equipment_name.replace(' ', '_') + '.png'
            try:
                image_file = discord.File(f'assets/images/{file_name}', f'{file_name}')
            except:
                file_name = 'Default.png'
                image_file = discord.File(f'assets/images/{file_name}', f'{file_name}')
            message_embed.set_thumbnail(url=f'attachment://{file_name}')
            await ctx.send(file=image_file, embed=message_embed)
        else:
            message_embed.description = '**__Equipped Gear__**:\n' + User.get_equipped_gear_str(equipment_list)
            await ctx.send(embed=message_embed)

    @commands.command(name='inventory', aliases=['i'])
    async def inventory(self, ctx, *, equipment_name=''):
        equipment_name = equipment_name.title()
        message_embed = discord.Embed(title='Inventory', color=discord.Color.from_rgb(245, 211, 201))  # peachy color
        equipment_list = await self.db.get_equipment_for_user(ctx.author.id)
        equipment_str = User.get_equipment_stats_str(equipment_list, equipment_name)
        if not equipment_list:
            message_embed.description = 'You have nothing in your inventory.'
            await ctx.send(embed=message_embed)
            return
        if equipment_name and equipment_str:
            message_embed.description = equipment_str
            await ctx.send(embed=message_embed)
        else:
            paginator = commands.Paginator('', '', 1800, '\n')
            for item in User.get_inventory_list(equipment_list):
                paginator.add_line(item)
            menu = PageMenu('Inventory', discord.Color.from_rgb(245, 211, 201), paginator.pages)
            await menu.start(ctx)

    @commands.command(name='leaderboard')
    async def leaderboard(self, ctx):
        user_list = await self.db.get_top_users_for_exp(50)
        leaderboard_str = ''
        pages = []
        count = 0
        for i in range(len(user_list)):
            leaderboard_str += f'**{i + 1}.** `{self.client.get_user(user_list[i]["user_id"])}` '
            leaderboard_str += f'**Level**: `{User.exp_to_level(user_list[i]["exp"])}` '
            leaderboard_str += f'**EXP:** `{user_list[i]["exp"]}`\n'
            count += 1
            if count >= 10:
                pages.append(leaderboard_str)
                leaderboard_str = ''
                count = 0
        pages.append(leaderboard_str)
        menu = PageMenu('Leaderboard', discord.Color.blue(), pages)
        await menu.start(ctx)

    @commands.command(name='bonus', aliases=['b'])
    async def bonus(self, ctx, *, equipment_name):
        equipment_name = equipment_name.title()
        user = await self.db.get_user(ctx.author.id)
        equipment_list = await self.db.get_equipment_for_user(ctx.author.id)
        equipment = User.get_equipment_from_name(equipment_list, equipment_name)
        message_embed = discord.Embed(title='Equipment Bonusing', color=discord.Color.from_rgb(245, 211, 201))
        if equipment:
            base_equipment = Equipment.get_equipment_from_name(equipment_name)
            if base_equipment['level'] < 20:
                cost = 150
            elif base_equipment['level'] < 40:
                cost = 500
            elif base_equipment['level'] < 100:
                cost = 1000
            else:
                cost = 4000
            message_embed.description = f'Would you like to bonus your {equipment_name} for {cost} gold?'
            result = await ConfirmationMenu(message_embed).prompt(ctx)
            if result:
                if user['gold'] >= 1000:
                    await self.db.update_user_gold(ctx.author.id, -1000)
                    current_lines = User.get_lines_for_equipment(equipment_list, equipment_name)
                    bonus = Equipment.get_bonus_for_weapon(equipment_name, current_lines)
                    await self.db.update_equipment_bonus(ctx.author.id, equipment['equipment_id'], bonus)
                    equipment_list = await self.db.get_equipment_for_user(ctx.author.id)
                    message_embed.description = User.get_equipment_stats_str(equipment_list, equipment_name)
                    message_embed.color = Equipment.lines_to_color[User.get_lines_for_equipment(
                        equipment_list,
                        equipment_name)]
                    file_name = equipment_name.replace(' ', '_') + '.png'
                    try:
                        image_file = discord.File(f'assets/images/{file_name}', f'{file_name}')
                    except:
                        file_name = 'Default.png'
                        image_file = discord.File(f'assets/images/{file_name}', f'{file_name}')
                    message_embed.set_thumbnail(url=f'attachment://{file_name}')
                    await ctx.send(file=image_file, embed=message_embed)
                    return
                else:
                    message_embed.description = 'You do not have enough gold...'
        else:
            message_embed.description = 'You do not own this piece of equipment...'
        await ctx.send(embed=message_embed)

    @commands.command(name='star')
    async def star(self, ctx, *, equipment_name):
        equipment_name = equipment_name.title()
        user = await self.db.get_user(ctx.author.id)
        equipment_list = await self.db.get_equipment_for_user(ctx.author.id)
        equipment = User.get_equipment_from_name(equipment_list, equipment_name)
        message_embed = discord.Embed(title='Equipment Bonusing', color=discord.Color.from_rgb(245, 211, 201))
        if equipment:
            base_equipment = Equipment.get_equipment_from_name(equipment_name)
            if equipment['stars'] >= base_equipment['max_stars']:
                message_embed.description = 'This equipment already has max stars!'
            else:
                gold_cost = base_equipment['level'] * 10 * (equipment['stars'] // 5 + 1)
                if equipment['stars'] >= 20:
                    gold_cost *= 4
                odds = round(100 / (equipment['stars'] // 5 + 1), 2)
                message_embed.description = (
                    f'Would you like to star your {equipment_name} for {gold_cost} gold?\n'
                    f'There is a `{odds}% chance to upgrade stars.`'
                )
                result = await ConfirmationMenu(message_embed).prompt(ctx)
                if result:
                    if user['gold'] >= gold_cost:
                        await self.db.update_user_gold(ctx.author.id, -gold_cost)
                        if random.choices([True, False], [odds, 100 - odds])[0]:
                            await self.db.update_equipment_stars(ctx.author.id, equipment['equipment_id'], 1)
                            message_embed.description = '**SUCCESS!**\n'
                        else:
                            message_embed.description = '**FAILURE!**\n'
                        equipment_list = await self.db.get_equipment_for_user(ctx.author.id)
                        message_embed.description += User.get_equipment_stats_str(equipment_list, equipment_name)
                        message_embed.color = Equipment.lines_to_color[User.get_lines_for_equipment(
                            equipment_list,
                            equipment_name)]
                        file_name = equipment_name.replace(' ', '_') + '.png'
                        try:
                            image_file = discord.File(f'assets/images/{file_name}', f'{file_name}')
                        except:
                            file_name = 'Default.png'
                            image_file = discord.File(f'assets/images/{file_name}', f'{file_name}')
                        message_embed.set_thumbnail(url=f'attachment://{file_name}')
                        await ctx.send(file=image_file, embed=message_embed)
                        return
                    else:
                        message_embed.description = 'You do not have enough gold...'
        else:
            message_embed.description = 'You do not own this piece of equipment...'
        await ctx.send(embed=message_embed)

    @commands.command(name='reset')
    async def reset(self, ctx):
        user = await self.db.get_user(ctx.author.id)
        level = User.exp_to_level(user['exp'])
        blessings = max(int(((level - 50) / 5) ** 1.5), 0)
        message_embed = discord.Embed(title='Resetting', color=discord.Color.from_rgb(245, 211, 201))
        message_embed.description = f'{ctx.author.mention}, you will recieve `{blessings}` blessings if you reset exp. '
        message_embed.description += 'You gain 1% exp stat for each blessing you have.'
        result = await ConfirmationMenu(message_embed).prompt(ctx)
        if result:
            await self.db.set_user_exp(ctx.author.id, 0)
            await self.db.update_user_blessings(ctx.author.id, blessings)
            await self.db.update_user_cave(ctx.author.id, 'Beginner Cave')

    @mine.error
    async def mine_error(self, ctx, error):
        if isinstance(error, commands.CommandOnCooldown):
            message_embed = discord.Embed(
                color=discord.Color.dark_orange(),
                title='Mine',
                description=f'You are too tired to mine. {error}')
            await ctx.send(embed=message_embed)
        else:
            print(error)

    @stats.error
    async def stats_error(self, ctx, error):
        if isinstance(error, commands.errors.MemberNotFound):
            message_embed = discord.Embed(
                color=discord.Color.dark_teal(),
                title='Stats',
                description='Cannot find member!')
            await ctx.send(embed=message_embed)
        else:
            print(error)


def setup(client):
    client.add_cog(Mining(client))
