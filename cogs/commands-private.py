import discord
from discord.ext import commands
import platform
import random

import cogs._json

class Private(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print("Commands-private Cog had been loaded\n-----")

    @commands.command(aliases = ['disconnect', 'close', 'stopbot'])
    @commands.is_owner()
    async def logout(self, ctx):
        """
        Turns off bot {owner only}
        """
        await ctx.send(f"Hey {ctx.author.mention}, I am now logging out :wave:")
        await self.client.logout()

    @commands.command(aliases = ['purge'])
    @commands.is_owner()
    async def clear(self, ctx, *, amount):
        """
        Clears messages {owner only}
        """
        num = int(amount) + 1
        # await ctx.channel.purge(limit = 1)
        await ctx.channel.purge(limit = num)

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

    @commands.command()
    @commands.is_owner()
    #@commands.has_permissions(administrator=True)
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def prefix(self, ctx, *, pre='-'):
        """
        Set a custom prefix for a guild
        """
        data = cogs._json.read_json('prefixes')
        data[str(ctx.message.guild.id)] = pre
        cogs._json.write_json(data, 'prefixes')
        await ctx.send(f"The guild prefix has been set to `{pre}`. Use `{pre}prefix <prefix>` to change it again!")

def setup(client):
    client.add_cog(Private(client))
