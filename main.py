import discord
import os
import asyncio
import re



client = discord.Client()
joska_id = 815189981169319947
grv_commands = ['-p', '-play', '-skip', '-stop', '-resume', '-volume', '-clear', '!add', '!add-playlist', '!clear-queue', '!play', '!skip', '!resume', '!replay', '!pause', '!stop']
music_bot_ids = {'grv_id': 234395307759108106, 'mee6_id': 159985870458322944 }

@client.event
async def on_ready():
  print(f'We have logged in as {client}')

  

@client.event
async def on_message(message):

  if message.channel.id != joska_id and message.author == client.user: #removes bot messages from non-music tc's

    await asyncio.sleep(20) 
    await message.delete()  

  if message.channel.id != joska_id: #detects messages in non-music tc's
    if re.findall('[^\s]*',message.content.lower())[0] in grv_commands or message.content.lower() in grv_commands: # checks if messages are commands
      await asyncio.sleep(3)
      await message.delete() #removes commands from non music tc's

      #makes warning message
      embed_warning=discord.Embed(description= f'<#815189981169319947>-ba írjad a zenét, kedves [{message.author.mention}]', color=0x02547e)
      embed_warning.set_author(name='Figyelem', icon_url="https://cms.sulinet.hu/get/d/e1109224-6b00-1700-5531-61727661746f/1/9/b/Normal/11_092_24_k_1_2_0_0.jpg")
      embed_warning.set_thumbnail(url="https://cms.sulinet.hu/get/d/e1109224-6b00-1700-5531-61727661746f/1/9/b/Normal/11_092_24_k_1_2_0_0.jpg")

      await message.channel.send(embed=embed_warning) #warns user to put command in music tc

  if message.author.id in music_bot_ids.values(): #checks for bot embed
    
    
    if message.author.id == music_bot_ids['grv_id']: #checks if bot is groovy
      for embed in message.embeds: 
        embed_content = re.findall('(?<=\[)(.*?)(?=\])',embed.to_dict()['description'])[0]
        embed_author_id = re.findall('(?<=\[)(.*?)(?=\])',embed.to_dict()['description'])[-1][2:-1]
        embed_author = await client.fetch_user(embed_author_id)
        embed_link = ''.join(re.findall('(?<=\()(http.*?)(?=\))', embed.to_dict()['description']))
        

    elif message.author.id == music_bot_ids['mee6_id']: #checks if bot is mee6

      try: #if it's the first song
        
        embed_content = re.findall('(?<=\[)(.*?)(?=\])',message.embeds[0].to_dict()['description'])
        embed_link = ''.join(re.findall('(?<=\()(http.*?)(?=\))', message.embeds[0].to_dict()['description']))
      except: #if something's already playing
        
        embed_content = message.embeds[0].to_dict()['title']
        embed_link = message.embeds[0].to_dict()['url']
        embed_author = message.embeds[0].to_dict()['footer']['text'][9:]

    await message.delete() #deletes bot embed from music tc
    
    #display embed for music tc
    embed_display=discord.Embed(title=embed_content, url= embed_link, description= '', color=0x02547e)
    embed_display.add_field(name=f' **{embed_author}**  kérésére', value="󠀠󠀠󠀠:cd:", inline=True)    
    embed_display.set_author(name="A következő nóta:", icon_url="https://cms.sulinet.hu/get/d/e1109224-6b00-1700-5531-61727661746f/1/9/b/Normal/11_092_24_k_1_2_0_0.jpg")
    embed_display.set_thumbnail(url="https://cms.sulinet.hu/get/d/e1109224-6b00-1700-5531-61727661746f/1/9/b/Normal/11_092_24_k_1_2_0_0.jpg")

    #only puts display embed in music tc
    if message.channel.id != joska_id:
      await client.get_channel(joska_id).send(embed=embed_display)
    elif message.channel.id == joska_id:
      await message.channel.send(embed=embed_display)    


      



client.run(os.getenv('TOKEN'))