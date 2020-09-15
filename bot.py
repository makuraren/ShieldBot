# Libs
import discord # For discord
from discord.ext import commands # For discord
import json # For interacting with jason
from pathlib import Path # For paths
import platform # For stats
import logging # For logging

cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n-----")

# Defining a few things
secret_file = json.load(open(cwd+'/client_config/secrets.json'))
client = commands.Bot(command_prefix='.', case_insensitive=True, owner_id = 300251178107928576)
client.config_token = secret_file['token']
logging.basicConfig(level=logging.INFO)

client.version = '0.0.1'

@client.event
async def on_ready():
    print(f"-----\nLogged in as: {client.user.name} <@{client.user.id}>\n-----\nMy current prefix is: .\n-----")
    await client.change_presence(activity=discord.Game(name=f"\"Don'\t hurt me\" -{client.user.name}")) # This changes the bots 'activity'

@client.event
async def on_command_error(ctx, error):
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

@client.command(name='hi', aliases=['hello'])
async def _hi(ctx):
    """
    A simple command which says hi to the author.
    """
    await ctx.send(f"Hi {ctx.author.mention}!")

@client.command()
async def stats(ctx):
    """
    A usefull command that displays bot statistics.
    """
    pythonVersion = platform.python_version()
    dpyVersion = discord.__version__
    serverCount = len(client.guilds)
    memberCount = len(set(client.get_all_members()))

    embed = discord.Embed(title = f'{client.user.name} Stats', description = '\uFEFF', colour = ctx.author.colour, timestamp = ctx.message.created_at)

    embed.add_field(name = 'Bot Version:', value = client.version)
    embed.add_field(name = 'Python Version:', value = pythonVersion)
    embed.add_field(name = 'Discord.Py Version', value = dpyVersion)
    embed.add_field(name = 'Total Guilds:', value = serverCount)
    embed.add_field(name = 'Total Users:', value = memberCount)
    embed.add_field(name = 'Bot Developers:', value = "<@300251178107928576>")

    embed.set_footer(text = f"Carpe Noctem | {client.user.name}")
    embed.set_author(name = client.user.name, icon_url = client.user.avatar_url)

    await ctx.send(embed = embed)
@client.command(aliases = ['disconnect', 'close', 'stopbot'])
@commands.is_owner()
async def logout(ctx):
    """
    If the user running the command owns the bot then this will disconnect the bot from discord.
    """
    await ctx.send(f"Hey {ctx.author.mention}, I am now logging out :wave:")
    await client.logout()

@client.command()
async def echo(ctx, *, message=None):
    """
    A simple command that repeats the users input back to them.
    """
    message = message or "Please provide the message to be repeated."
    await ctx.message.delete()
    await ctx.send(message)

client.run(client.config_token)
