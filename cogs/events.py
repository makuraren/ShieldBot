import discord
from discord.ext import commands
import random
import datetime

# In cogs we make our own class
# for d.py which subclasses commands.Cog

class Events(commands.Cog):

    def __init__(self, client):
        self.client = client

    @commands.Cog.listener()
    async def on_ready(self):
        print(f"{self.__class__.__name__} Cog had been loaded\n-----")

    @commands.Cog.listener()
    async def on_member_join(self, member):
        channel = discord.utils.get(member.guild.text_channels, name = 'welcome')
        if channel:
            embed = discord.Embed(description = f'Welcome to {member.guild}!', color = random.choice(self.client.color_list))
            embed.set_thumbnail(url = member.avatar_url)
            embed.set_author(name = member.name, icon_url = member.avatar_url)
            embed.set_footer(text = member.guild, icon_url = member.guild.icon_url)
            embed.timestamp = datetime.datetime.utcnow()

            await channel.send(embed = embed)

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        channel = discord.utils.get(member.guild.text_channels, name = 'welcome')
        if channel:
            embed = discord.Embed(description = 'Goodbye from all of us..', color = random.choice(self.client.color_list))
            embed.set_thumbnail(url = member.avatar_url)
            embed.set_author(name = member.name, icon_url = member.avatar_url)
            embed.set_footer(text = member.guild, icon_url = member.guild.icon_url)
            embed.timestamp = datetime.datetime.utcnow()

            await channel.send(embed = embed)

    @commands.Cog.listener()
    async def on_command_error(self, ctx, error):
        #Ignore these errors
        ignored = (commands.CommandNotFound, commands.UserInputError)
        if isinstance(error, ignored):
            return

        #Begin error handling
        if isinstance(error, commands.CommandOnCooldown):
            m, s = divmod(error.retry_after, 60)
            h, m = divmod(m, 60)
            if int(h) == 0 & int(m) == 0:
                await ctx.send(f'You must wait {int(s)} seconds to use this command!')
            elif int(h) == 0 & int(m) != 0:
                await ctx.send(f'You must wait {int(m)} minutes and {int(s)} seconds to use this command!')
            else:
                await ctx.send(f'You must wait {int(h)} hours, {int(m)} minutes and {int(s)} seconds to use this command!')
        elif isinstance(error, commands.CheckFailure):
            await ctx.send("Hey! You lack permission to use this command.")
        raise error



def setup(client):
    client.add_cog(Events(client))
