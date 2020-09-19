import discord
from discord.ext import commands
import platform

import cogs._json

class Commands(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Commands Cog had been loaded\n-----")

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

    @commands.command(name='hi', aliases=['hello'])
    async def _hi(self, ctx):
        """
        A simple command which says hi to the author.
        """
        await ctx.send(f"Hi {ctx.author.mention}!")

    @commands.command()
    async def echo(self, ctx, *, message=None):
        """
        A simple command that repeats the users input back to them.
        """
        message = message or "Please provide the message to be repeated."
        await ctx.message.delete()
        await ctx.send(message)

    @commands.command(aliases = ['disconnect', 'close', 'stopbot'])
    @commands.is_owner()
    async def logout(self, ctx):
        """
        If the user running the command owns the bot then this will disconnect the bot from discord.
        """
        await ctx.send(f"Hey {ctx.author.mention}, I am now logging out :wave:")
        await self.client.logout()

    @commands.command()
    @commands.is_owner()
    async def blacklist(self, ctx, user: discord.Member):
        """
        A command that blacklists a user {owner only}
        """
        if ctx.message.author.id == user.id:
            await ctx.send("Hey, you cannot blacklist yourself!")
            return

        self.client.blacklisted_users.append(user.id)
        data = cogs._json.read_json("blacklist")
        data["blacklistedUsers"].append(user.id)
        cogs._json.write_json(data, "blacklist")
        await ctx.send(f"Hey, I have blacklisted {user.name} for you.")

    @commands.command()
    @commands.is_owner()
    async def unblacklist(self, ctx, user: discord.Member):
        """
        A command that blacklists a user {owner only}
        """
        self.client.blacklisted_users.remove(user.id)
        data = cogs._json.read_json("blacklist")
        data["blacklistedUsers"].remove(user.id)
        cogs._json.write_json(data, "blacklist")
        await ctx.send(f"Hey, I have unblacklisted {user.name} for you.")

def setup(client):
    client.add_cog(Commands(client))
