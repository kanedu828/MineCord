from discord.ext import menus
import discord


class PageMenu(discord.ui.View):

    def __init__(self, title, color, pages):
        super().__init__()
        self.message_embed = discord.Embed(title=title, color=color)
        self.pages = pages
        self.current_page = 0
        self.msg = await ctx.send(embed=embed, view=self)

    @discord.ui.button(label='◀')
    async def back_button(self, button, interaction):
        if self.current_page > 0:
            self.current_page -= 1
            self.message_embed.description = self.pages[self.current_page]
            self.message_embed.set_footer(text=f'page {self.current_page + 1}/{len(self.pages)}')
            await msg.edit(embed=self.message_embed, view=self)

    @discord.ui.button(label='▶')
    async def next_button(self, button, interaction):
        if self.current_page < len(self.pages) - 1:
            self.current_page += 1
            self.message_embed.description = self.pages[self.current_page]
            self.message_embed.set_footer(text=f'page {self.current_page + 1}/{len(self.pages)}')
            await msg.edit(embed=self.message_embed, view=self)


class ConfirmationMenu(discord.ui.View):
    def __init__(self):
        super().__init__()
        self.result = None

    @discord.ui.button(label='Confirm')
    async def confirm_button(self, buttom, interaction):
        self.result = True
        self.stop()

    @discord.ui.button(label='Cancel')
    async def deny_button(self, button, interaction):
        self.result = False
        self.stop()
