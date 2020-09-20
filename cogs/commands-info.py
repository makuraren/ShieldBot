import discord
from discord.ext import commands
import platform
import random

import cogs._json

class Info(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Commands-info Cog had been loaded\n-----")

    @commands.command()
    async def stats(self, ctx):
        """
        A useful command that displays bot statistics.
        """
        pythonVersion = platform.python_version()
        dpyVersion = discord.__version__
        serverCount = len(self.client.guilds)
        memberCount = len(set(self.client.get_all_members()))

        embed = discord.Embed(title = f'{self.client.user.name} Stats', description = '\uFEFF', colour = ctx.author.colour, timestamp = ctx.message.created_at)

        embed.add_field(name = 'Bot Version:', value = self.client.version)
        embed.add_field(name = 'Python Version:', value = pythonVersion)
        embed.add_field(name = 'Discord.py Version', value = dpyVersion)
        embed.add_field(name = 'Total Guilds:', value = serverCount)
        embed.add_field(name = 'Total Users:', value = memberCount)
        embed.add_field(name = 'Bot\'s Father:', value = "<@300251178107928576>")

        embed.set_footer(text = f"{self.client.user.name} | {self.client.user.id}")
        embed.set_author(name = self.client.user.name, icon_url = self.client.user.avatar_url)

        await ctx.send(embed = embed)

def setup(client):
    client.add_cog(Info(client))
