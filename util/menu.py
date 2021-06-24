from discord.ext import menus
import discord

class PageMenu(menus.Menu):

    def __init__(self, title, color, pages):
        super().__init__(timeout=60.0, delete_message_after=True)
        self.message_embed = discord.Embed(title=title, color=color)
        self.pages = pages
        self.current_page = 0

    async def send_initial_message(self, ctx, channel):
        self.message_embed.description = self.pages[0]
        self.message_embed.set_footer(text=f'page {self.current_page + 1}/{len(self.pages)}')
        return await channel.send(embed=self.message_embed)

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

    @menus.button('🛑')
    async def on_stop(self, payload):
        self.stop()
