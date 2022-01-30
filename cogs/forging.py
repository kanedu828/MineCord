import discord
from discord.ext import commands
from data.forge import Forge
from data.items import Item
from data.user import User
from util.dbutil import DBUtil
from util.menu import PageMenu, ConfirmationMenu


class Forging(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.db = DBUtil(client.pool)

    @commands.command(name='fragments')
    async def fragments(self, ctx):
        async with self.db.get_conn() as conn:
            async with conn.transaction():
                result = await conn.fetch('SELECT * FROM item WHERE user_id=$1', ctx.author.id)
        message_embed = discord.Embed(title='Fragments', color=discord.Color.from_rgb(245, 211, 201))
        paginator = commands.Paginator('', '', 1800, '\n')
        for r in result:
            paginator.add_line(f'`{Item.get_item_from_id(r["item_id"])["name"]} x{r["count"]}`')
        menu = PageMenu('Fragments', discord.Color.from_rgb(245, 211, 201), paginator.pages)
        await menu.start(ctx)

    @commands.command(name='forge')
    async def forge(self, ctx, *, equipment_name=None):
        if equipment_name:
            equipment_name = equipment_name.title()
            user = await self.db.get_user(ctx.author.id)
            message_embed = discord.Embed(title='Forge', color=discord.Color.dark_gray())
            base_equipment = Forge.get_forgable(equipment_name)
            if base_equipment:
                message_embed.description = f'Would you like to forge {base_equipment["name"]} '
                message_embed.description += f'for `5 {base_equipment["set"]} fragments`'
                result = await ConfirmationMenu(message_embed).prompt(ctx)
                if result:
                    fragment = Item.get_item_from_name(base_equipment['set'] + ' Fragment')
                    fragment_count = await self.db.update_item_count(ctx.author.id, fragment['id'], 0)
                    if fragment_count[0]['count'] >= 5:
                        await self.db.update_item_count(ctx.author.id, fragment['id'], -5)
                        equipment_list = await self.db.get_equipment_for_user(ctx.author.id)
                        equipment = User.get_equipment_from_id(equipment_list, base_equipment['id'])
                        if equipment:
                            if equipment['stars'] < base_equipment['max_stars']:
                                await self.db.update_equipment_stars(ctx.author.id, base_equipment['id'], 1)
                                message_embed.description = f'{base_equipment["name"]}\'s star level increased!\n'
                            else:
                                message_embed.description = f'{base_equipment["name"]} is already at max star level.\n'
                                message_embed.description += 'You have been refunded.'
                                await self.db.update_item_count(ctx.author.id, fragment['id'], 5)
                        else:
                            await self.db.insert_equipment(ctx.author.id, base_equipment['id'], 'inventory')
                            message_embed.description = f'You have recieved {base_equipment["name"]}'
                    else:
                        message_embed.description = 'You dont have enough fragments...'
            else:
                message_embed.description = 'This item either does not exist or cannot be forged.'
            await ctx.send(embed=message_embed)
        else:
            paginator = commands.Paginator('', '', 1800, '\n')
            for item in Forge.get_forge_str_list():
                paginator.add_line(item)
            menu = PageMenu('Shop', discord.Color.dark_gray(), paginator.pages)
            await menu.start(ctx)


def setup(client):
    client.add_cog(Forging(client))
