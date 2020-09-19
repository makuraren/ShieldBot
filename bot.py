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

client.version = '0.1.1'

client.blacklisted_users = []

@client.event
async def on_ready():
    print(f"-----\nLogged in as: {client.user.name} <@{client.user.id}>\n-----\nMy current prefix is: .\n-----")
    data = read_json("blacklist")
    client.blacklist_users = data["blacklistedUsers"]
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

@client.event
async def on_message(message):
    #Ignore ourselves
    if message.author.id == client.user.id:
        return

    #Blacklist system
    if message.author.id in client.blacklist_users:
        return

    if message.content.lower().startswith("help"):
        await message.channel.send("Hey! Why don't you run the help command with `-help`")

    await client.process_commands(message)

@client.command()
@commands.is_owner()
async def blacklist(ctx, user: discord.Member):
    """
    A command that blacklists a user {owner only}
    """
    if ctx.message.author.id == user.id:
        await ctx.send("Hey, you cannot blacklist yourself!")
        return

    client.blacklisted_users.append(user.id)
    data = read_json("blacklist")
    data["blacklistedUsers"].append(user.id)
    write_json(data, "blacklist")
    await ctx.send(f"Hey, I have blacklisted {user.name} for you.")

@client.command()
@commands.is_owner()
async def unblacklist(ctx, user: discord.Member):
    """
    A command that blacklists a user {owner only}
    """
    client.blacklisted_users.remove(user.id)
    data = read_json("blacklist")
    data["blacklistedUsers"].remove(user.id)
    write_json(data, "blacklist")
    await ctx.send(f"Hey, I have unblacklisted {user.name} for you.")

@client.command(name='hi', aliases=['hello'])
async def _hi(ctx):
    """
    A simple command which says hi to the author.
    """
    await ctx.send(f"Hi {ctx.author.mention}!")

@client.command()
async def stats(ctx):
    """
    A useful command that displays bot statistics.
    """
    pythonVersion = platform.python_version()
    dpyVersion = discord.__version__
    serverCount = len(client.guilds)
    memberCount = len(set(client.get_all_members()))

    embed = discord.Embed(title = f'{client.user.name} Stats', description = '\uFEFF', colour = ctx.author.colour, timestamp = ctx.message.created_at)

    embed.add_field(name = 'Bot Version:', value = client.version)
    embed.add_field(name = 'Python Version:', value = pythonVersion)
    embed.add_field(name = 'Discord.py Version', value = dpyVersion)
    embed.add_field(name = 'Total Guilds:', value = serverCount)
    embed.add_field(name = 'Total Users:', value = memberCount)
    embed.add_field(name = 'Bot\'s Father:', value = "<@300251178107928576>")

    embed.set_footer(text = f"{client.user.name} | {client.user.id}")
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

def read_json(filename):
    with open(f"{cwd}/client_config/{filename}.json", "r") as file:
        data = json.load(file)
    return data

def write_json(data, filename):
    with open(f"{cwd}/client_config/{filename}.json", "w") as file:
        json.dump(data, file, indent=4)

client.run(client.config_token)
