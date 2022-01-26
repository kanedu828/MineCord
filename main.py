import asyncpg
import asyncio
import discord
from discord.ext import commands
import os
from dotenv import load_dotenv
import logging


load_dotenv()
logger = logging.getLogger('discord')
logger.setLevel(logging.DEBUG)
handler = logging.FileHandler(filename='discord.log', encoding='utf-8', mode='w')
handler.setFormatter(logging.Formatter('%(asctime)s:%(levelname)s:%(name)s: %(message)s'))
logger.addHandler(handler)
intents = discord.Intents.default()  # All but the two privileged ones
intents.members = True  # Subscribe to the Members intent


extensions = [
    'cogs.mining',
    'cogs.help',
    'cogs.admin',
    'cogs.shop',
]


def check_if_me(ctx):
    return ctx.message.author.id == 124668192948748288


def load_extensions(client):
    for extension in extensions:
        try:
            client.load_extension(extension)
            print(f'{extension} successfully loaded')
        except Exception as exception:
            print(f'{extension} cannot be loaded. [{exception}]')


async def start():
    PRODUCTION = os.getenv('PRODUCTION')
    if PRODUCTION == 'False':
        TOKEN = os.getenv('TOKEN_DEVELOPMENT')
        game = discord.Game('<3!')
        client = commands.Bot(command_prefix='-', intents=intents, activity=game)
    else:
        TOKEN = os.getenv('TOKEN')
        client = commands.Bot(command_prefix=';', intents=intents)

    client.remove_command('help')
    PSQL_CONNECTION_URL = os.getenv('PSQL_CONNECTION_URL')
    async with asyncpg.create_pool(dsn=PSQL_CONNECTION_URL) as pool:
        client.pool = pool
        load_extensions(client)
        await client.start(TOKEN)
        

if __name__ == '__main__':
    asyncio.run(start())
