from discord.ext import menus
from discord.ext.menus.views import ViewMenu
import discord


class PageMenu(ViewMenu):

    def __init__(self, title, color, pages):
        super().__init__(delete_message_after=True)
        self.message_embed = discord.Embed(title=title, color=color)
        self.pages = pages
        self.current_page = 0

    async def send_initial_message(self, ctx, channel):
        self.message_embed.description = self.pages[0]
        self.message_embed.set_footer(text=f'page {self.current_page + 1}/{len(self.pages)}')
        return await self.send_with_view(channel, embed=self.message_embed)

    @menus.button('◀')
    async def on_back(self, payload):
        if self.current_page > 0:
            self.current_page -= 1
            self.message_embed.description = self.pages[self.current_page]
            self.message_embed.set_footer(text=f'page {self.current_page + 1}/{len(self.pages)}')
            await self.message.edit(embed=self.message_embed)

    @menus.button('▶')
    async def on_next(self, payload):
        if self.current_page < len(self.pages) - 1:
            self.current_page += 1
            self.message_embed.description = self.pages[self.current_page]
            self.message_embed.set_footer(text=f'page {self.current_page + 1}/{len(self.pages)}')
            await self.message.edit(embed=self.message_embed)


class ConfirmationMenu(ViewMenu):
    def __init__(self, message_embed):
        super().__init__(delete_message_after=True)
        self.message_embed = message_embed
        self.result = None

    async def send_initial_message(self, ctx, channel):
        return await self.send_with_view(channel, embed=self.message_embed)

    @menus.button('\N{WHITE HEAVY CHECK MARK}')
    async def do_confirm(self, payload):
        self.result = True
        self.stop()

    @menus.button('\N{CROSS MARK}')
    async def do_deny(self, payload):
        self.result = False
        self.stop()

    async def prompt(self, ctx):
        await self.start(ctx, wait=True)
        return self.result
