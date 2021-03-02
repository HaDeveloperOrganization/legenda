import discord
import os
import asyncio
import re
from discord.ext import commands
from discord.utils import get


client = discord.Client()
joska_id = 815189981169319947
grv_commands = ['-p', '-play', '-skip', '-stop', '-resume', '-volume']


@client.event
async def on_ready():
  print(f'We have logged in as {client}')
  user = await client.fetch_user(224506156272451586)
  

@client.event
async def on_message(message):  

  if message.author.id == 234395307759108106: #groovy's id
    

    for embed in message.embeds:
      embed_content = re.findall('(?<=\[)(.*?)(?=\])',embed.to_dict()['description'])[0]
      embed_author_id = re.findall('(?<=\[)(.*?)(?=\])',embed.to_dict()['description'])[-1][2:-1]
      embed_author = await client.fetch_user(embed_author_id)
      embed_link = ''.join(re.findall('(?<=\()(http.*?)(?=\))', embed.to_dict()['description']))
      await message.delete()

    print(embed_author_id)
    

    
    
    embed_display=discord.Embed(title=embed_content, url= embed_link, description= '', color=0x02547e)
    embed_display.set_author(name='A következő nóta:', url='')
    embed_display.set_footer(text = f'{embed_author.name} kérésére')
    await message.channel.send(embed=embed_display)
    
 

  if message.channel.id != joska_id and message.author == client.user:

    await asyncio.sleep(15)
    await message.delete()
    


  if message.channel.id != joska_id and re.findall('[^\s]*',message.content.lower())[0] in grv_commands or message.content.lower() in grv_commands:

    await asyncio.sleep(2)
    await message.delete()
    await message.channel.send(f'Joskaba irjad a zenet te {message.author.mention}!')
     


client.run(os.getenv('TOKEN'))