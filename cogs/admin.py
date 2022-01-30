import discord
from discord.ext import commands
from data.equipment import Equipment
from data.caves import Cave
from data.user import User
from data.blacklist import blacklist as bl
from util.dbutil import DBUtil


class Admin(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.db = DBUtil(client.pool)

    # @commands.Cog.listener()
    # async def on_ready():
    #     print("Bot is ready")

    @commands.command()
    @commands.is_owner()
    async def load(ctx, extension):
        try:
            client.load_extension(extension)
            await ctx.send(f'{extension} successfully loaded')
            print(f'{extension} successfully loaded')
        except Exception as exception:
            await ctx.send(f'{extension} cannot be loaded. [{exception}]')
            print(f'{extension} cannot be loaded. [{exception}]')


    @commands.command()
    @commands.is_owner()
    async def unload(ctx, extension):
        try:
            client.unload_extension(extension)
            await ctx.send(f'{extension} successfully unloaded')
            print(f'{extension} successfully unloaded')
        except Exception as exception:
            await ctx.send(f'{extension} cannot be unloaded. [{exception}]')
            print(f'{extension} cannot be unloaded. [{exception}]')


    @commands.command()
    @commands.is_owner()
    async def reload(ctx, extension):
        try:
            client.reload_extension(extension)
            await ctx.send(f'{extension} successfully reloaded')
            print(f'{extension} successfully reloaded')
        except Exception as exception:
            await ctx.send(f'{extension} cannot be reloaded. [{exception}]')
            print(f'{extension} cannot be reloaded. [{exception}]')

    @commands.command(name='ping')
    @commands.is_owner()
    async def ping(self, ctx):
        await ctx.send(':ping_pong: Pong! {0} ms'.format(round(self.client.latency * 1000)))

    @commands.command(name='give')
    @commands.is_owner()
    async def give(self, ctx, user: discord.Member, type: str, value: int):
        if type.lower() == 'gold':
            await self.db.update_user_gold(user.id, value)
            await ctx.send('Given.')
        elif type.lower() == 'exp':
            await self.db.update_user_exp(user.id, value)
            await ctx.send('Given.')
        elif type.lower() == 'equipment':
            base_equipment = Equipment.get_equipment_from_id(value)
            if base_equipment:
                equipment_list = await self.db.get_equipment_for_user(ctx.author.id)
                equipment = User.get_equipment_from_id(equipment_list, value)
                if equipment:
                    if equipment['stars'] < base_equipment['max_stars']:
                        await self.db.update_equipment_stars(ctx.author.id, value, 1)
                else:
                    await self.db.insert_equipment(user.id, value, 'inventory')
                    await ctx.send('Given.')
            else:
                await ctx.send('Invalid equipment.')

    @commands.command(name='blacklist')
    @commands.is_owner()
    async def blacklist(self, ctx, user: discord.Member):
        if user.id in bl:
            bl.pop(user.id)
            await ctx.send(f'Removed {user.name} from blacklist.')
        else:
            bl[user.id] = True
            await ctx.send(f'Added {user.name} from blacklist.')

    @commands.command(name='set-cave')
    @commands.is_owner()
    async def set_cave(self, ctx, cave_name: str, quantity):
        is_set = Cave.set_cave_quantity(cave_name, quantity)
        await ctx.send(f'Set cave status: {is_set}')

    @commands.command(name='reset-caves')
    @commands.is_owner()
    async def reset_caves(self, ctx):
        Cave.populate_caves()
        await ctx.send('Caves reset.')

    @commands.command(name='reset-dungeons')
    @commands.is_owner()
    async def reset_dungeons(self, ctx):
        async with self.db.get_conn() as conn:
            async with conn.transaction():
                result = await conn.fetch(
                    '''DELETE FROM dungeon_instance'''
                )
        await ctx.send(f'Reset {result} dungeon instances')


    @give.error
    async def give_error(self, ctx, error):
        if isinstance(error, commands.errors.MemberNotFound):
            await ctx.send('Not a member.')

    @blacklist.error
    async def blacklist_error(self, ctx, error):
        if isinstance(error, commands.errors.MemberNotFound):
            await ctx.send('Not a member.')


def setup(client):
    client.add_cog(Admin(client))
