import discord
from datetime import datetime
from discord.ext import commands
from data.user import User
import util.dbutil as db


class Drilling(commands.Cog):
    def __init__(self, client):
        self.client = client

    @commands.command(name='drill')
    async def drill(self, ctx):
        message_embed = discord.Embed(title='Drilling', color=discord.Color.dark_orange())
        user = await db.get_user(ctx.author.id)
        equipment_list = await db.get_equipment_for_user(ctx.author.id)
        total_stats = User.get_total_stats(ctx.author.id, equipment_list, user['blessings'])
        level = User.exp_to_level(user['exp'])
        since_last_drill = datetime.now() - user['last_drill']
        num_ten_min = since_last_drill.seconds // 600
        num_ten_min = min(num_ten_min, 10 * 6 * 24) # set max of 24 hours worth of idle mining
        base_exp = int((level ** 1.3)) * num_ten_min
        exp_gained = base_exp + total_stats["drill exp"] * num_ten_min
        gold = int(10 + total_stats["drill_power"]) * num_ten_min
        if num_ten_min > 0:
            message_embed.description = (
                f'`Time Since Last Successful Drill: {str(since_last_drill).split(".")[0]}`\n'
                f'`{exp_gained} exp ({base_exp} + {total_stats["drill exp"] * num_ten_min})`\n'
                f'`{gold} gold ({10 * num_ten_min} + {total_stats["drill_power"] * num_ten_min})`'
            )
            await db.update_user_exp(ctx.author.id, exp_gained)
            await db.update_user_gold(ctx.author.id, gold)
            await db.set_user_last_drill(ctx.author.id, datetime.now())
        else:
            message_embed.description = 'There are no rewards yet, check again later!'

        await ctx.send(embed=message_embed)


def setup(client):
    client.add_cog(Drilling(client))
