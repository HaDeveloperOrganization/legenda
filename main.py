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
    embed_warning=discord.Embed(description= '<#815189981169319947>-ba írjad a zenét', color=0x02547e)
    embed_warning.set_author(name=message.author)
    embed_warning.set_thumbnail(url="https://cms.sulinet.hu/get/d/e1109224-6b00-1700-5531-61727661746f/1/9/b/Normal/11_092_24_k_1_2_0_0.jpg")
    await message.channel.send(embed=embed_warning)


client.run(os.getenv('TOKEN'))