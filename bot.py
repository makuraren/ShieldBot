# Libs
import discord # For discord
from discord.ext import commands # For discord
import json # For interacting with jason
from pathlib import Path # For paths
import platform # For stats
import logging # For loggin
import datetime
import os

import cogs._json

cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f"{cwd}\n-----")

def get_prefix(client, message):
    data = cogs._json.read_json('prefixes')
    if not str(message.guild.id) in data:
        return commands.when_mentioned_or('-')(client, message)
    return commands.when_mentioned_or(data[str(message.guild.id)])(client, message)


# Defining a few things
secret_file = json.load(open(cwd+'/client_config/secrets.json'))
client = commands.Bot(command_prefix=get_prefix, case_insensitive=True, owner_id = 300251178107928576)
client.config_token = secret_file['token']
logging.basicConfig(level=logging.INFO)

client.version = '0.2.0'

client.blacklisted_users = []

client.colors = {
  'WHITE': 0xFFFFFF,
  'AQUA': 0x1ABC9C,
  'GREEN': 0x2ECC71,
  'BLUE': 0x3498DB,
  'PURPLE': 0x9B59B6,
  'LUMINOUS_VIVID_PINK': 0xE91E63,
  'GOLD': 0xF1C40F,
  'ORANGE': 0xE67E22,
  'RED': 0xE74C3C,
  'NAVY': 0x34495E,
  'DARK_AQUA': 0x11806A,
  'DARK_GREEN': 0x1F8B4C,
  'DARK_BLUE': 0x206694,
  'DARK_PURPLE': 0x71368A,
  'DARK_VIVID_PINK': 0xAD1457,
  'DARK_GOLD': 0xC27C0E,
  'DARK_ORANGE': 0xA84300,
  'DARK_RED': 0x992D22,
  'DARK_NAVY': 0x2C3E50
}
client.color_list = [c for c in client.colors.values()]

@client.event
async def on_ready():
    print(f"-----\nLogged in as: {client.user.name} <@{client.user.id}>\n-----\nMy current prefix is: -\n-----")
    await client.change_presence(activity=discord.Activity(type = discord.ActivityType.listening, name = f"\"Haha code go boom!\" -{client.user.name}")) # This changes the bots 'activity'

@client.event
async def on_message(message):
    # Ignore ourselves
    if message.author.id == client.user.id:
        return

    # A way to blacklist users from the bot by not processing commands
    if message.author.id in client.blacklisted_users:
        return

    # Whenevver the bot is tagged, respond with its prefix
    if f"<@!{client.user.id}>" in message.content:
        data = cogs._json.read_json('prefixes')
        if str(message.guild.id) in data:
            prefix = data[str(message.guild.id)]
        else:
            prefix = '-'
        prefixMsg = await message.channel.send(f"My prefix here is `{prefix}`")
        await prefixMsg.add_reaction('👀')

    # returns message to user if messaged help
    if message.content.lower().startswith("help"):
        await message.channel.send("Hey! Why don't you run the help command with `-help`")

    await client.process_commands(message)

if __name__ == '__main__':
    # When running this file, if it is the 'main' filename
    # I.E. its not being imported from another python file run this
    for file in os.listdir(cwd+"/cogs"):
        if file.endswith(".py") and not file.startswith("_"):
            client.load_extension(f"cogs.{file[:-3]}")
    client.run(client.config_token)
