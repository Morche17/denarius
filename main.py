import os
import discord

my_secret = os.environ['TOKEN']

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)
    
@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    print('\nMy bot is ready :)')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('¡hola'):
        await message.channel.send('¡Saludos!')

    if message.content.startswith('¡ping'):
        await message.channel.send('Pong')


client.run(my_secret)