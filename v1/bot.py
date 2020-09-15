# libs
import discord
import random
import os
from pathlib import Path
from discord.ext import commands

cwd = Path(__file__).parents[0]
cwd = str(cwd)
print(f'{cwd}\n-----')


client = commands.Bot(command_prefix = '.', case_insensitive = False, owner_id = 300251178107928576)

client.blacklisted_users = []
client.cwd = cwd

client.version = '1.0.1'

# This event detects when the bot has become online
@client.event
async def on_ready():
    print('Bot is running\n-----')

# This event detects when a user has joined a guild
@client.event
async def on_member_join(member):
    print(f'{member} has joined a server.')

# This event detects when a user has left a guild
@client.event
async def on_member_remove(member):
    print(f'{member} has left a server.')

# This event detects when a user has been banned from a guild
@client.event
async def on_member_ban(guild, member):
    print(f'{member} was banned from {guild}')

# This event detects when a user has been unbanned from a guild
@client.event
async def on_member_unban(guild, member):
    print(f'{member} was unbanned from {guild}')

if __name__ == '__main__':
    for file in os.listdir(cwd + '/cogs'):
        if file.endswith('.py') and not file.startswith('_'):
            client.load_extension(f'cogs.{file[:-3]}')
            
client.run('NzU0ODc2MzcxODI5Nzg0NzE3.X17HZw.abW3BRqzz1MExaglEGflreeA42w')


