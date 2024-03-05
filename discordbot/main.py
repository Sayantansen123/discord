import discord
import requests
import json
from jokesapi import *
from discord.ui import Button, View
from discord import Member
from discord import FFmpegPCMAudio
from discord.ext.commands import MissingPermissions,has_permissions
from discord.ext import commands
import os



intents = discord.Intents.all()
intents.members = True

client = commands.Bot(command_prefix= '$',intents=intents)

queues={}

def check_queue(ctx,id):
    if queues[id]!=[]:
        voice=ctx.guild.voice_client
        source=queues[id].pop(0)
        player=voice.play(source)



@client.event
async def on_ready():
    await client.change_presence(status=discord.Status.idle,activity=discord.Game('with your mom'))
    print('yea i am fucking go')

@client.event
async def on_member_join(member: discord.Member):
    

    channel = client.get_channel(1201937991694811218)
    
    await member.send(json.loads(response2.text)['images'][0])
    await member.send( "welcome to our server lets dance bro")
    await channel.send(json.loads(response2.text)['images'][0])
    await channel.send("hello😄😄😄, " + member.mention  )
    await channel.send(json.loads(jokes1.text)['joke'])
    


@client.event
async def on_member_remove(member: discord.Member):
    channel = client.get_channel(1201937991694811218)
    await channel.send("Goodbye kiddo 😝😝😝😝 " + member.mention )

@client.event
async def on_message(message):
    await client.process_commands(message)
    
    author = message.author
    if ("nigga") in (message.content).lower() :
        await author.send("sun be laure maa chod dunga")
        await message.delete()
        await message.channel.send("dont send this message again or u will get fucked")  
    if ("you suck") in (message.content).lower() :
        await author.send("your mom sucks")
        await message.channel.send("tera mummy aj mera ghar aya")      

  

@client.command(pass_context = True)
async def join(ctx):
    if(ctx.author.voice):
        channel = ctx.message.author.voice.channel
        voice = await channel.connect()
        
    else:
        await ctx.send("Hey, nigga join the channel first")   

@client.command()
async def jokes(ctx):
    embed = discord.Embed(title=json.loads(jokes1.text)['joke'],colour=0xf55142)
    await ctx.send(embed = embed)

@client.command()
async def image(ctx,message="discord"):
      url = "https://google-search72.p.rapidapi.com/imagesearch"

      querystring = {"q":message,"gl":"us","lr":"lang_en","num":"10","start":"0"}

      headers = {
	    "X-RapidAPI-Key": "238b5f8336msh80c2347c3e41953p1c4f10jsna37138f632a4",
	    "X-RapidAPI-Host": "google-search72.p.rapidapi.com"
      }
      response = requests.get(url, headers=headers, params=querystring)
      await ctx.send(json.loads(response.text)['items'][0]['originalImageUrl'])



@client.command(pass_context = True)
async def leave(ctx):
    if(ctx.voice_client):
        await ctx.guild.voice_client.disconnect()
        await ctx.send("i am disconnected you pervert")
    else:
        await ctx.send("i am not in channel you dance daddy")         

@client.command(pass_context = True)
async def pause(ctx):
    voice = discord.utils.get(client.voice_clients,guild = ctx.guild)
    if voice.is_played():
        voice.pause()
    else:
        await ctx.send("at that moment , song is not playing broo")    

@client.command(pass_context = True)
async def resume(ctx):
    voice = discord.utils.get(client.voice_clients,guild = ctx.guild)
    if voice.is_paused():
        voice.resume()
    else:
        await ctx.send("at that moment , song is not paused broo")   

@client.command(pass_context = True)
async def stop(ctx):
    voice = discord.utils.get(client.voice_clients,guild = ctx.guild)
    voice.stop()


@client.command(pass_context = True)
async def play(ctx,arg = "metamorphosis"):
    try:
        if(ctx.author.voice):
            channel = ctx.author.voice.channel
            if(ctx.voice_client and ctx.voice_client.channel == channel):
              voice = ctx.guild.voice_client
              source = FFmpegPCMAudio( str(arg).lower() + '.mp3')
              player=voice.play(source,after=lambda x=None: check_queue(ctx,ctx.message.guild.id))
            else:
               await ctx.send("I need to join the channel first , please use the function join ")
          
        else:
           await ctx.send("Hey, nigga join the channel first") 
    except:
        await ctx.send("A song is already playing")


@client.command()
async def hello(ctx):
    await ctx.send('hello bro')



@client.command(pass_context = True)
async def queue(ctx,arg):
    voice=ctx.guild.voice_client
    song=str(arg).lower()+'.mp3'
    source=FFmpegPCMAudio(song)

    guild_id=ctx.message.guild.id
    if guild_id in queues:
        queues[guild_id].append(source)
    else:
        queues[guild_id]=[source]
    await ctx.send("added to queues")

@client.command()
@commands.has_permissions(kick_members=True)
async def kick(ctx,member: discord.Member,*,reason=None):
    await member.kick(reason=reason)
    await ctx.send(f'User {member} has been hospitalised')

@kick.error
async def kick_error(ctx,error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("you are unpriviliged")    

@client.command()
@commands.has_permissions(ban_members=True)
async def ban(ctx,member: discord.Member,*,reason=None):
    await member.ban(reason=reason)
    await ctx.send(f'User {member} has died')



@ban.error
async def ban_error(ctx,error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("you are unpriviliged")

@client.command()
async def message(ctx,user:discord.Member,*,message =None):
    
    embed = discord.Embed(title=message)
    await user.send(embed = embed)        



@client.command()
@commands.has_permissions(manage_roles=True)
async def addRole(ctx,user: discord.Member,*,role:discord.Role):
    if role in user.roles:
        await ctx.send(f"{user.mention} already has the role")
    else:
        await user.add_roles(role)
        await ctx.send(f"{role} is added to {user.mention}")

@addRole.error
async def role_error(ctx,error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("You dont have permission to run the command")        

@client.command()
@commands.has_permissions(manage_roles=True)
async def removeRole(ctx,user: discord.Member,*,role:discord.Role):
    if role in user.roles:
        await user.remove_roles(role)
        await ctx.send(f"removed {role} from {user.mention}")
    else:

        await ctx.send(f"{role} is not given to {user.mention}")

@removeRole.error
async def removeRole_error(ctx,error):
    if isinstance(error,commands.MissingPermissions):
        await ctx.send("You dont have permission to run the command")  

@client.command()
async def button(ctx):
    # Create a button and set its label
    button = Button(label="Click me!", style=discord.ButtonStyle.primary, custom_id="button")

    # Create a view and add the button to it
    view = View()
    view.add_item(button)

    # Send a message with the button and view
    await ctx.send("Here's an example button:", view=view)

@client.event
async def on_button_click(interaction):
    # Handle button click events
    if interaction.custom_id == "button":
        await interaction.response.send_message("Button clicked!")        



client.run('Your Bot Token')    
