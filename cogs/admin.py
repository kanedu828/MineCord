import discord
from discord.ext import commands
from data.equipment import Equipment
from data.caves import Cave
from data.user import User
from data.blacklist import blacklist as bl
from util.dbutil import DBUtil
from typing import Optional, Literal


class Admin(commands.Cog):

    def __init__(self, client):
        self.client = client
        self.db = DBUtil(client.pool)

    # @commands.Cog.listener()
    # async def on_ready():
    #     print("Bot is ready")

    @commands.hybrid_command()
    @commands.is_owner()
    async def load(self, ctx: commands.Context, extension: str):
        try:
            self.client.load_extension(extension)
            await ctx.send(f'{extension} successfully loaded')
            print(f'{extension} successfully loaded')
        except Exception as exception:
            await ctx.send(f'{extension} cannot be loaded. [{exception}]')
            print(f'{extension} cannot be loaded. [{exception}]')


    @commands.hybrid_command()
    @commands.is_owner()
    async def unload(self, ctx: commands.Context, extension: str):
        try:
            self.client.unload_extension(extension)
            await ctx.send(f'{extension} successfully unloaded')
            print(f'{extension} successfully unloaded')
        except Exception as exception:
            await ctx.send(f'{extension} cannot be unloaded. [{exception}]')
            print(f'{extension} cannot be unloaded. [{exception}]')


    @commands.hybrid_command()
    @commands.is_owner()
    async def reload(self, ctx: commands.Context, extension: str):
        try:
            self.client.reload_extension(extension)
            await ctx.send(f'{extension} successfully reloaded')
            print(f'{extension} successfully reloaded')
        except Exception as exception:
            await ctx.send(f'{extension} cannot be reloaded. [{exception}]')
            print(f'{extension} cannot be reloaded. [{exception}]')

    @commands.hybrid_command(name='ping')
    @commands.is_owner()
    async def ping(self, ctx: commands.Context):
        await ctx.send(':ping_pong: Pong! {0} ms'.format(round(self.client.latency * 1000)))

    @commands.hybrid_command(name='give')
    @commands.is_owner()
    async def give(self, ctx: commands.Context, user: discord.Member, type: str, value: int):
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

    @commands.hybrid_command(name='blacklist')
    @commands.is_owner()
    async def blacklist(self, ctx: commands.Context, user: discord.Member):
        if user.id in bl:
            bl.pop(user.id)
            await ctx.send(f'Removed {user.name} from blacklist.')
        else:
            bl[user.id] = True
            await ctx.send(f'Added {user.name} from blacklist.')

    @commands.hybrid_command(name='set-cave')
    @commands.is_owner()
    async def set_cave(self, ctx: commands.Context, cave_name: str, quantity: int):
        is_set = Cave.set_cave_quantity(cave_name, quantity)
        await ctx.send(f'Set cave status: {is_set}')

    @commands.hybrid_command(name='reset-caves')
    @commands.is_owner()
    async def reset_caves(self, ctx: commands.Context):
        Cave.populate_caves()
        await ctx.send('Caves reset.')

    @commands.hybrid_command(name='reset-dungeons')
    @commands.is_owner()
    async def reset_dungeons(self, ctx: commands.Context, clear_rate: str):
        async with self.db.get_conn() as conn:
            async with conn.transaction():
                result = await conn.fetch(
                    '''DELETE FROM dungeon_instance WHERE clear_rate=$1''',
                    clear_rate
                )
        await ctx.send(f'Reset {result} dungeon instances')

    @commands.hybrid_command(name='sync')
    @commands.guild_only()
    @commands.is_owner()
    async def sync(
    self, ctx: commands.Context, guilds: commands.Greedy[discord.Object], spec: Optional[Literal["~", "*", "^"]] = None) -> None:
        if not guilds:
            if spec == "~":
                synced = await ctx.bot.tree.sync(guild=ctx.guild)
            elif spec == "*":
                ctx.bot.tree.copy_global_to(guild=ctx.guild)
                synced = await ctx.bot.tree.sync(guild=ctx.guild)
            elif spec == "^":
                ctx.bot.tree.clear_commands(guild=ctx.guild)
                await ctx.bot.tree.sync(guild=ctx.guild)
                synced = []
            else:
                synced = await ctx.bot.tree.sync()

            await ctx.send(
                f"Synced {len(synced)} commands {'globally' if spec is None else 'to the current guild.'}"
            )
            return

        ret = 0
        for guild in guilds:
            try:
                await ctx.bot.tree.sync(guild=guild)
            except discord.HTTPException:
                pass
            else:
                ret += 1

        await ctx.send(f"Synced the tree to {ret}/{len(guilds)}.")

    @give.error
    async def give_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.errors.MemberNotFound):
            await ctx.send('Not a member.')

    @blacklist.error
    async def blacklist_error(self, ctx: commands.Context, error):
        if isinstance(error, commands.errors.MemberNotFound):
            await ctx.send('Not a member.')


async def setup(client):
    await client.add_cog(Admin(client))
