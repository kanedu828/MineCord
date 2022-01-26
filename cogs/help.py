import discord
from discord.ext import commands


class Help(commands.Cog):
    
    def __init__(self, client):
        self.client = client

    @commands.command(name='help')
    async def help(self, ctx):
        message_embed = discord.Embed(title='Help', color=discord.Color.from_rgb(245, 211, 201))
        message_embed.description = '''
            View https://github.com/kanedu828/Isla-Bot-2.0/blob/master/README.md for help.'''
        await ctx.send(embed=message_embed)


def setup(client):
    client.add_cog(Help(client))
