import discord
from discord.ext import commands
import util.dbutil as db
from data.equipment import Equipment
from data.caves import Cave
from data.user import User
from data.blacklist import blacklist as bl


class Admin(commands.Cog):
    def __init__(self, client):
        self.client = client

    def check_if_me(ctx):
        return ctx.message.author.id == 124668192948748288

    @commands.command(name='ping')
    @commands.check(check_if_me)
    async def ping(self, ctx):
        await ctx.send(':ping_pong: Pong! {0} ms'.format(round(self.client.latency * 1000)))

    @commands.command(name='give')
    @commands.check(check_if_me)
    async def give(self, ctx, user: discord.Member, type: str, value: int):
        if type.lower() == 'gold':
            await db.update_user_gold(user.id, value)
            await ctx.send('Given.')
        elif type.lower() == 'exp':
            await db.update_user_exp(user.id, value)
            await ctx.send('Given.')
        elif type.lower() == 'equipment':
            base_equipment = Equipment.get_equipment_from_id(value)
            if base_equipment:
                equipment_list = await db.get_equipment_for_user(ctx.author.id)
                equipment = User.get_equipment_from_id(equipment_list, value)
                if equipment:
                    if equipment['stars'] < base_equipment['max_stars']:
                        await db.update_equipment_stars(ctx.author.id, value, 1)
                else:
                    await db.insert_equipment(user.id, value, 'inventory')
                    await ctx.send('Given.')
            else:
                await ctx.send('Invalid equipment.')

    @commands.command(name='blacklist')
    @commands.check(check_if_me)
    async def blacklist(self, ctx, user: discord.Member):
        if user.id in bl:
            bl.pop(user.id)
            await ctx.send(f'Removed {user.name} from blacklist.')
        else:
            bl[user.id] = True
            await ctx.send(f'Added {user.name} from blacklist.')

    @commands.command(name='set-cave')
    @commands.check(check_if_me)
    async def set_cave(self, ctx, cave_name: str, quantity):
        is_set = Cave.set_cave_quantity(cave_name, quantity)
        await ctx.send(f'Set cave status: {is_set}')

    @commands.command(name='reset-caves')
    @commands.check(check_if_me)
    async def reset_caves(self, ctx):
        Cave.populate_caves()
        await ctx.send('Caves reset.')

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
