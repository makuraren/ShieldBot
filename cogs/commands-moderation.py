import discord
from discord.ext import commands
from datetime import datetime
import platform
import random

import cogs._json

class Moderation(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog had been loaded\n-----")

    @commands.command(aliases = ['purge'])
    @commands.is_owner()
    @commands.has_permissions(administrator = True)
    async def clear(self, ctx, *, amount):
        """
        Clears messages
        """
        num = int(amount) + 1
        # await ctx.channel.purge(limit = 1)
        await ctx.channel.purge(limit = num)
        channel = self.client.get_channel(753051691590352902)
        await channel.send(f"```yaml\n{ctx.author.name} removed messages from {ctx.message.channel.name}\nAmount: {amount}\nTime: {datetime.now().strftime('%m-%d-%Y %H:%M:%S')}\n```")
        #await ctx.channel.send(f"```yaml\n{ctx.author.name} removed {amount} messages from {ctx.message.channel.name}\nAmount: {reason}\nTime: {datetime.now().strftime('%m-%d-%Y %H:%M:%S')}\n```")

    @commands.command()
    @commands.is_owner()
    @commands.has_permissions(administrator = True)
    async def kick(self, ctx, member: discord.Member, *, reason = None):
        """
        A command that kicks a user
        """
        await ctx.guild.kick(user = member, reason = reason)
        channel = self.client.get_channel(753051691590352902)
        await channel.send(f"```yaml\n{ctx.author.name} kicked {member.name} from {member.guild}\nReason: {reason}\nTime: {datetime.now().strftime('%m-%d-%Y %H:%M:%S')}\n```")
        #await ctx.channel.send(f"```yaml\n{ctx.author.name} kicked {member.name} from {member.guild}\nReason: {reason}\nTime: {datetime.now().strftime('%m-%d-%Y %H:%M:%S')}\n```")

    @commands.command()
    @commands.is_owner()
    @commands.has_permissions(administrator = True)
    async def ban(self, ctx, member: discord.Member, *, reason = None):
        """
        A command that bans a user
        """
        await ctx.guild.ban(user = member, reason = reason)
        channel = self.client.get_channel(753051691590352902)
        await channel.send(f"```yaml\n{ctx.author.name} banned {member.name} from {member.guild}\nReason: {reason}\nTime: {datetime.now().strftime('%m-%d-%Y %H:%M:%S')}\n```")
        #await ctx.channel.send(f"```yaml\n{ctx.author.name} banned {member.name} from {member.guild}\nReason: {reason}\nTime: {datetime.now().strftime('%m-%d-%Y %H:%M:%S')}\n```")

    @commands.command()
    @commands.is_owner()
    @commands.has_permissions(administrator = True)
    async def unban(self, ctx, member, *, reason = None):
        """
        A command that unbans a user
        """
        member = await self.client.fetch_user(int(member))
        await ctx.guild.unban(member, reason = reason)
        channel = self.client.get_channel(753051691590352902)
        await channel.send(f"```yaml\n{ctx.author.name} unbanned {member.name} from {ctx.message.guild.name}\nReason: {reason}\nTime: {datetime.now().strftime('%m-%d-%Y %H:%M:%S')}\n```")
        #await ctx.channel.send(f"```yaml\n{ctx.author.name} unbanned {member.name} from {member.guild}\nReason: {reason}\nTime: {datetime.now().strftime('%m-%d-%Y %H:%M:%S')}\n```")

    @commands.command()
    @commands.is_owner()
    @commands.has_permissions(administrator = True)
    @commands.cooldown(1, 5, commands.BucketType.guild)
    async def prefix(self, ctx, *, pre='-'):
        """
        Set a custom prefix for a guild
        """
        data = cogs._json.read_json('prefixes')
        data[str(ctx.message.guild.id)] = pre
        cogs._json.write_json(data, 'prefixes')
        await ctx.send(f"The guild prefix has been set to `{pre}`. Use `{pre}prefix <prefix>` to change it again!")
        channel = self.client.get_channel(753051691590352902)
        await channel.send(f"```yaml\n{ctx.author.name} changed the prefix for the server\nNew Prefix: {pre}\nTime: {datetime.now().strftime('%m-%d-%Y %H:%M:%S')}\n```")
        #await ctx.channel.send(f"```yaml\n{ctx.author.name} changed the prefix for the server\nNew Prefix: {pre}\nTime: {datetime.now().strftime('%m-%d-%Y %H:%M:%S')}\n```")

def setup(client):
    client.add_cog(Moderation(client))
