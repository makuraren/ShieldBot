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

client.version = '0.2.4'

client.blacklisted_users = []

client.theme_color = 0xFE258A

client.colors = {
  'GEOG1': 0x08F7FE,
  'GEOG2': 0x09FBD3,
  'GEOG3': 0xFE53BB,
  'GEOG4': 0xF5D300,
  'NEON1' : 0xFFACFC,
  'NEON2' : 0xF148FB,
  'NEON3' : 0x7122FA,
  'NEON4' : 0x560A86,
  'PSYC1' : 0x75D5FD,
  'PSYC2' : 0xB76CFD,
  'PSYC3' : 0xFF2281,
  'PSYC4' : 0x011FFD,
  'VIVD1' : 0xFDC7D7,
  'VIVD2' : 0xFF9DE6,
  'VIVD3' : 0xA5D8F3,
  'VIVD4' : 0xE8E500,
  'ABST1' : 0x00FECA,
  'ABST2' : 0xFDF200,
  'ABST3' : 0xFF85EA,
  'ABST4' : 0x7B61F8,
  'COTT1' : 0xFFD300,
  'COTT2' : 0xDE38C8,
  'COTT3' : 0x652EC7,
  'COTT4' : 0x33135C,
  'BRST1' : 0x3B27BA,
  'BRST2' : 0xE847AE,
  'BRST3' : 0x13CA91,
  'BRST4' : 0xFF9472,
}
client.color_list = [c for c in client.colors.values()]

@client.event
async def on_ready():
    print(f"-----\nLogged in as: {client.user.name} <@{client.user.id}>\n-----\nMy current prefix is: -\n-----")
    await client.change_presence(activity=discord.Activity(type = discord.ActivityType.listening, name = f"code breaking")) # This changes the bots 'activity'

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
