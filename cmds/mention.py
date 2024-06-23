import discord
from discord import app_commands as apc
from discord.ext import commands
from time import sleep


class LeagueGroup(apc.Group):
    """Manage general commands"""

    def __init__(self, bot: commands.Bot):
        super().__init__()
        self.bot = bot

    @apc.command()
    async def hello(self, interaction: discord.Interaction):
        await interaction.response.send_message('Hello my friend')


    @apc.command()
    async def hungry(self, interaction: discord.Interaction, mention: discord.Member):
        """ Print interaction """
        print([mention])
        await interaction.response.send_message(f"interaction: {mention}", ephemeral=True)


async def setup(bot, guilds):
    bot.tree.add_command(LeagueGroup(bot), guild=guilds)

