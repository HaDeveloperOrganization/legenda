import discord
import os
import asyncio
import re



client = discord.Client()
joska_id = 815189981169319947
grv_commands = ['-p', '-play', '-skip', '-stop', '-resume', '-volume', '!add', '!add-playlist', '!clear-queue', '!play', '!skip', '!resume', '!replay', '!pause', '!stop']

@client.event
async def on_ready():
  print(f'We have logged in as {client}')

  

@client.event
async def on_message(message):

  if message.channel.id != joska_id and message.author == client.user:

    await asyncio.sleep(20) 
    await message.delete()  #removes bot messages from non-music tc's

  if message.channel.id != joska_id: #detects messages in non-music tc's
    if re.findall('[^\s]*',message.content.lower())[0] in grv_commands or message.content.lower() in grv_commands: # checks if messages are commands
      await asyncio.sleep(3)
      await message.delete() #removes commands from non music tc's

      #makes warning message
      embed_warning=discord.Embed(description= f'<#815189981169319947>-ba írjad a zenét, kedves [{message.author.mention}]', color=0x02547e)
      embed_warning.set_author(name='Figyelem', icon_url="https://cms.sulinet.hu/get/d/e1109224-6b00-1700-5531-61727661746f/1/9/b/Normal/11_092_24_k_1_2_0_0.jpg")
      embed_warning.set_thumbnail(url="https://cms.sulinet.hu/get/d/e1109224-6b00-1700-5531-61727661746f/1/9/b/Normal/11_092_24_k_1_2_0_0.jpg")

      await message.channel.send(embed=embed_warning) #warns user to put command in music tc

  if message.author.id == 234395307759108106 or message.author.id == 159985870458322944: #groovy's id
    
    for embed in message.embeds: 
      embed_content = re.findall('(?<=\[)(.*?)(?=\])',embed.to_dict()['description'])[0]
      embed_author_id = re.findall('(?<=\[)(.*?)(?=\])',embed.to_dict()['description'])[-1][2:-1]
      embed_author = await client.fetch_user(embed_author_id)
      embed_link = ''.join(re.findall('(?<=\()(http.*?)(?=\))', embed.to_dict()['description']))
      await message.delete() #deletes bot embed

    #display embed for music tc
    embed_display=discord.Embed(title=embed_content, url= embed_link, description= '', color=0x02547e)
    embed_display.add_field(name=f'__**{embed_author.name}**__ kérésére', value="󠀠󠀠󠀠:cd:", inline=True)    
    embed_display.set_author(name="A következő nóta:", icon_url="https://cms.sulinet.hu/get/d/e1109224-6b00-1700-5531-61727661746f/1/9/b/Normal/11_092_24_k_1_2_0_0.jpg")
    embed_display.set_thumbnail(url="https://cms.sulinet.hu/get/d/e1109224-6b00-1700-5531-61727661746f/1/9/b/Normal/11_092_24_k_1_2_0_0.jpg")

    #only puts display embed in music tc
    if message.channel.id != joska_id:
      await client.get_channel(joska_id).send(embed=embed_display)
    elif message.channel.id == joska_id:
      await message.channel.send(embed=embed_display)    


      



client.run(os.getenv('TOKEN'))