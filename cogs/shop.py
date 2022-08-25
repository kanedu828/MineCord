import discord
from discord.ext import commands
from util.menu import PageMenu, ConfirmationMenu
from data.shop import Shop as SD
from data.equipment import Equipment
from data.caves import Drop
from data.user import User
from util.dbutil import DBUtil


class Shop(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.db = DBUtil(client.pool)

    @commands.hybrid_command(name='lookup')
    async def look_up(self, ctx: commands.Context, *, item_name: str):
        message_embed = discord.Embed(title='Look Up', color=discord.Color.gold())
        if item_name:
            item_name = item_name.title()
            item = Equipment.get_equipment_from_name(item_name)
            if item:
                file_name = item_name.replace(' ', '_') + '.png'
                try:
                    image_file = discord.File(f'assets/images/{file_name}', f'{file_name}')
                except:
                    file_name = 'Default.png'
                    image_file = discord.File(f'assets/images/{file_name}', f'{file_name}')
                message_embed.set_thumbnail(url=f'attachment://{file_name}')
                message_embed.description = Equipment.get_base_equipment_stats_str(item_name)
                message_embed.set_footer(text=f'ID: {item["id"]}')
                await ctx.send(file=image_file, embed=message_embed)

    @commands.hybrid_command(name='shop')
    async def shop(self, ctx: commands.Context, *, item_name: str = None):
        message_embed = discord.Embed(title='Shop', color=discord.Color.gold())
        if item_name:
            item_name = item_name.title()
            shop_item = SD.get_shop_item_from_name(item_name)
            if shop_item:
                if shop_item['type'] == Drop.EQUIPMENT:
                    file_name = item_name.replace(' ', '_') + '.png'
                    try:
                        image_file = discord.File(f'assets/images/{file_name}', f'{file_name}')
                    except:
                        file_name = 'Default.png'
                        image_file = discord.File(f'assets/images/{file_name}', f'{file_name}')
                    message_embed.set_thumbnail(url=f'attachment://{file_name}')
                    message_embed.description = Equipment.get_base_equipment_stats_str(item_name)
                    message_embed.description += f'**Cost:** `{shop_item["cost"][1]} {shop_item["cost"][0].value}`'
                await ctx.send(file=image_file, embed=message_embed)
        else:
            paginator = commands.Paginator('', '', 1800, '\n')
            for item in SD.get_shop_str_list():
                paginator.add_line(item)
            menu = PageMenu('Shop', discord.Color.gold(), paginator.pages)
            await menu.start(ctx)

    @commands.hybrid_command(name='buy')
    async def buy(self, ctx: commands.Context, *, item_name: str):
        item_name = item_name.title()
        user = await self.db.get_user(ctx.author.id)
        message_embed = discord.Embed(title='Buy Shop Item', color=discord.Color.gold())
        shop_item = SD.get_shop_item_from_name(item_name)
        if shop_item:
            message_embed.description = f'Would you like to purchase {item_name} '
            message_embed.description += f'for {shop_item["cost"][1]} {shop_item["cost"][0].value}'
            result = await ConfirmationMenu(message_embed).prompt(ctx)
            if result:
                if shop_item['cost'][0] == Drop.GOLD:
                    if user['gold'] >= shop_item['cost'][1]:
                        await self.db.update_user_gold(ctx.author.id, -shop_item['cost'][1])
                    else:
                        message_embed.description = 'Not enough gold!'
                        await ctx.send(embed=message_embed)
                        return
                if shop_item['type'] == Drop.EQUIPMENT:
                    equipment_list = await self.db.get_equipment_for_user(ctx.author.id)
                    equipment = User.get_equipment_from_id(equipment_list, shop_item['id'])
                    base_equipment = Equipment.get_equipment_from_id(shop_item['id'])
                    if equipment:
                        if equipment['stars'] < base_equipment['max_stars']:
                            await self.db.update_equipment_stars(ctx.author.id, shop_item['id'], 1)
                            message_embed.description = f'{base_equipment["name"]}\'s star level increased!\n'
                        else:
                            message_embed.description = f'{base_equipment["name"]} is already at max star level.\n'
                            message_embed.description += 'You have been refunded.'
                            await self.db.update_user_gold(ctx.author.id, shop_item['cost'][1])
                    else:
                        await self.db.insert_equipment(ctx.author.id, shop_item['id'], 'inventory')
                        message_embed.description = f'You have recieved {base_equipment["name"]}'
                    await ctx.send(embed=message_embed)


async def setup(client):
    await client.add_cog(Shop(client))
