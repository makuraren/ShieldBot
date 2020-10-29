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
        print(f"{self.__class__.__name__} Cog had been loaded\n-----")

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
        embed.add_field(name = 'Bot Owner:', value = "<@300251178107928576>")

        embed.set_footer(text = f"{self.client.user.name} | {self.client.user.id}")
        embed.set_author(name = self.client.user.name, icon_url = self.client.user.avatar_url)

        await ctx.send(embed = embed)

    @commands.command(aliases = ['cstats'])
    @commands.bot_has_guild_permissions(manage_channels=True)
    async def channelstats(self, ctx):
        """
        Sends a some channel stats
        """
        channel = ctx.channel
        embed = discord.Embed(title=f"Stats for **{channel.name}**", description=f"{'Category: {}'.format(channel.category.name) if channel.category else 'This channel is not in a category'}", color=random.choice(self.client.color_list))
        embed.add_field(name="Channel Guild", value=ctx.guild.name, inline=False)
        embed.add_field(name="Channel Id", value=channel.id, inline=False)
        embed.add_field(name="Channel Topic", value=f"{channel.topic if channel.topic else 'No topic.'}", inline=False)
        embed.add_field(name="Channel Position", value=channel.position, inline=False)
        embed.add_field(name="Channel Slowmode Delay", value=channel.slowmode_delay, inline=False)
        embed.add_field(name="Channel is nsfw?", value=channel.is_nsfw(), inline=False)
        embed.add_field(name="Channel is news?", value=channel.is_news(), inline=False)
        embed.add_field(name="Channel Creation Time", value=channel.created_at, inline=False)
        embed.add_field(name="Channel Permissions Synced", value=channel.permissions_synced, inline=False)
        embed.add_field(name="Channel Hash", value=hash(channel), inline=False)

        await ctx.send(embed=embed)

    @commands.command(aliases = ['d'])
    async def directory(self, ctx):
        """
        Grabs README.md from directory
        """
        dir_link = "https://makuraren.github.io/ShieldBot/"
        await ctx.send(f'The directory can be found on this cite:\n{dir_link}')

def setup(client):
    client.add_cog(Info(client))
