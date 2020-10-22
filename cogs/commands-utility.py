import discord
from discord.ext import commands
import platform
import random

import cogs._json

class Utility(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog had been loaded\n-----")

    @commands.group(invoke_without_command=True)
    @commands.guild_only()
    @commands.has_guild_permissions(administrator = True)
    @commands.bot_has_guild_permissions(manage_channels = True)
    async def build(self, ctx):
        """
        This builds items in the server
        """
        await ctx.send("Invalid sub-command passed.")

    @build.command()
    @commands.guild_only()
    @commands.has_guild_permissions(administrator = True)
    @commands.bot_has_guild_permissions(manage_channels = True)
    async def category(self, ctx, role: discord.Role, *, name):
        """
        This builds a category item in the server
        """
        overwrites = {
        ctx.guild.default_role: discord.PermissionOverwrite(read_messages = False),
        ctx.guild.me: discord.PermissionOverwrite(read_messages = True),
        role: discord.PermissionOverwrite(read_messages = True)
        }
        category = await ctx.guild.create_category(name = name, overwrites = overwrites)
        await ctx.send(f"Hey, I made {category.name} for you!")

    @build.command()
    @commands.guild_only()
    @commands.has_guild_permissions(administrator = True)
    @commands.bot_has_guild_permissions(manage_channels = True)
    async def channel(self, ctx, role: discord.Role, *, name):
        """
        This builds a channel item in the server
        """
        overwrites = {
        ctx.guild.default_role: discord.PermissionOverwrite(read_messages = False),
        ctx.guild.me: discord.PermissionOverwrite(read_messages = True),
        role: discord.PermissionOverwrite(read_messages = True)
        }
        channel = await ctx.guild.create_text_channel(name = name, overwrites = overwrites, category = self.client.get_channel(709002944879656960))
        await ctx.send(f"Hey, I made {channel.name} for you!")

    @commands.group(invoke_without_command = True)
    @commands.guild_only()
    @commands.has_guild_permissions(administrator = True)
    @commands.bot_has_guild_permissions(manage_channels = True)
    async def delete(self, ctx):
        """
        This deletes items in the server
        """
        await ctx.send("Invalid sub-command passed.")

    @delete.command(name = 'category')
    @commands.guild_only()
    @commands.has_guild_permissions(administrator = True)
    @commands.bot_has_guild_permissions(manage_channels = True)
    async def _category(self, ctx, category: discord.CategoryChannel, *, reason=None):
        """
        This deletes a category item in the server
        """
        await category.delete(reason = reason)
        await ctx.send(f"Hey, I deleted {category.name} for you!")

    @delete.command(name = 'channel')
    @commands.guild_only()
    @commands.has_guild_permissions(administrator = True)
    @commands.bot_has_guild_permissions(manage_channels = True)
    async def _channel(self, ctx, channel: discord.TextChannel = None, *, reason = None):
        """
        This deletes a channel item in the server
        """
        channel = channel or ctx.channel
        await channel.delete(reason = reason)
        await ctx.send(f"Hey, I deleted {channel.name} for you!")

def setup(client):
    client.add_cog(Utility(client))
