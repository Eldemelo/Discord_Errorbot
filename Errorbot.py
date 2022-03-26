#Errorbot made by Ethan DeMelo

# List of import code (to be added over time)
# 1. {0.author.mention}'.format(message)   - tags author of command

import discord
import random

TOKEN = "MzgxODg1NDYyODE1NTcxOTgx.DdezBQ.JR6wRiplLh2Z9UzTT4uHam6kN04"
client = discord.Client()
prefix = "!"
nocommand = "Error! Command not found. Please type !help to view a list of commands"

# Sets role on user join
@client.event
async def on_member_join(member):
    role = discord.utils.get(member.server.roles, name='Finite Member')
    await client.add_roles(member, role)

# all commands
@client.event
async def on_message(message):

    # we do not want the bot to reply to itself
    if message.author == client.user:
        return

    # Registers the Prefix to read commands found below:
    if message.content.startswith(prefix + 'help'):
        msg = '''***Below can be found a list of commands***
!help
!hello'''
        await client.send_message(message.channel,msg)

    elif message.content.startswith(prefix + 'hello'):
        msg = 'Hello {0.author.mention}'.format(message)
        await client.send_message(message.channel,msg)

    elif message.content.startswith(prefix):
        msg = 'Invalid Command. Type !help to view a list of commands'
        await client.send_message(message.channel,msg)
    
        
        

@client.event
async def on_ready():
    print('Logged in as')
    print('Errorbot with the ID of:')
    print(client.user.id)
    print('------')

client.run(TOKEN)f
