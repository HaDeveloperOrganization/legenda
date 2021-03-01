import discord
import os
import asyncio
import re

client = discord.Client()
joska_id = 815189981169319947
grv_commands = ['-p', '-play', '-skip', '-stop', '-resume', '-volume']


@client.event
async def on_ready():
  print(f'We have logged in as {client}')
  print('Peri')

@client.event
async def on_message(message):
  stripped_music = ''.join(re.findall('\s(.*)', message.content))

  if message.channel.id != joska_id and message.author == client.user:

    await asyncio.sleep(15)
    await message.delete()

  elif message.channel.id == joska_id and message.author != client.user:
    await client.get_channel(joska_id).send(f'{message.author.mention} ezt kérte {stripped_music}') 


  if message.channel.id != joska_id and re.findall('[^\s]*',message.content.lower())[0] in grv_commands or message.content.lower() in grv_commands:
    await asyncio.sleep(2)
    await message.delete()
    await message.channel.send(f'Joskaba irjad a zenet te {message.author.mention}!')
    if not message.content.lower() in grv_commands:
      await client.get_channel(joska_id).send(f'{message.author.mention} ezt kérte {stripped_music}')



client.run(os.getenv('TOKEN'))