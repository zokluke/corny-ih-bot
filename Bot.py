import discord
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext import commands
import random
import re
from random import choice
import json
import requests
import aiohttp
import io

noPerms = "s-sorry daddy... you are missing perms... >w<"

client = commands.Bot(command_prefix='>')

@client.command()
async def rape(ctx, *, message=None):
    sus=message.lower()
    await ctx.channel.send(f"{ctx.message.author.mention} raped {sus} 😈")

@client.command()
async def say(ctx, *, message=None):
    await ctx.send(message)

 #choose
            

@client.command()
async def banner(ctx, *, message):
        """Emojify the text"""
        try:
            bigtext = ""
            append = " "
            for i, char in enumerate(message):
                char = char.lower()
                if i+1 == len(message):
                    append = ""
                if char.isdigit():
                    char = f":{List.digits[char]}:"
                elif char.isalpha():
                    char = f":regional_indicator_{char}:"
                elif char == " ":
                    char *= 2
                else:
                    char = ""
                bigtext += char + append
            await ctx.send(bigtext)
        except Exception as e:
            await ctx.send(e)
	
#clap
    
@client.command()
async def clap(ctx, *, message):
        """Make the bot say whatever you want with claps!"""
        try:
            message = re.sub(r"\s+", " ", message)
            await ctx.send((" :clap: ").join(message.split(" ")) + " :clap: ")
        except Exception as e:
            await ctx.send(e)
	
#8ball
    
@client.command(aliases=['8ball', 'question'])
async def _8ball(ctx, *, question):
        """Ask fta your questions"""
        responses = [
        'It is certain.', 'It is decidedly so.', 'Without a doubt.',
        'Yes - definitely.', 'You may rely on it.', 'As I see it, yes.',
        'Most likely.', 'Outlook good.', 'Yes.', 'Signs point to yes.',
        'Reply hazy, try again.', 'Ask again later.',
        'Better not tell you now.', 'Cannot predict now.',
        'Concentrate and ask again.', "Don't count on it.", 'My reply is no.',
        'My sources say no.', 'Outlook not so good.', 'Very doubtful.', 'O̴̡͉̓̆̉̿̅̇̋͘͝͠͝ṷ̴̡̢̨͔͔̘̱͍͓̺͎́̕ṱ̸̙̆͌̎̄̃̈͆̀̎̂͜l̵̛͕̍͊́̌̐͒̓̊̀̚͝o̵͍̖̠̜̝̹̤͋̀̉̄͑͗͜͝͝o̵̧̲̺̲̻̝͗̍̓̋̂̄̈́͗̕k̶̡̡͔̦̹̬̩̥̐́̈́ͅ ̵̡̧̩̟͈͓̰͉̰̹̬̜̰͓͓̔̅͑̌̐̊̔͘n̴̲̟̙̣̖̮͖̔́͌̾́̎͗͂̽͐͠o̷̭͖̦̠̥̒̿͐ţ̸̹̞͕̫̩͙͍͖̓̈́̀̎̀́̓̾̎̃͌͘̕̕͜͜͝ ̸̨̨̹̲͍̪̯̥͖͙̈́̌̌̊́̋̅͑̑͠͠s̶̨̡͔̰̘̻̣̞͈̯̮̺̪̫͌̈̈́̅͐̓͝o̷̧̜̥͔̳̯͈̿ ̸̢̛̬͙̲͕̲͇͙̝̯̺͙̈̋̿̓̓͂̂̋͝ǧ̴̢̱̥͙͇́̄́̽͒͒̓̚ó̷͚͓̾́̀̅̎̆͑̍͑̓́͠͝ͅò̷̤̲͔̱͍̦͔̈́̆͘̕͠͝d̵̢̡̛̺̖͇͔͈̰̩̀.̷̧̡̮͕͖͍̳͎̜͔̭͊͋͐̅̽̋̂̋', 'C̶̢̥̤͔͖̖̠͚̦̺̲̮̪̈́ͅa̶͇̣͍̩̭͕̪̰̼̭̣̰͉͚̔̊̄͊n̵̲̗̭̊́͊̌̀̎͗͆͘̚͠n̵̮̏̽̋̾͂̈́́̋̇̿̚͠ͅơ̶̧̨̫͎̩̳̬̤̊̈́͗́̐͑̂̕̕͠͝t̶̳͓̦̟̬̲͓̄̿͗̓̃̈́͑ͅ ̸̧͙̖̺̤̜̯̫̟̘̋̍̈́͘p̸̪͌͗̈́̂͆̂̊̐̚r̴̛̛̛̺̣̄͌̿̔̏̈́̂͌͋̔̆͝ė̶̢̢͕̪̼̙͈͕̼̏̌̒̈́͝d̸͔͕͖͓̭͙̯̗͚̱͕̫̰͚͖̉̎̓͛̓î̶̢̛̱͎̮͈͙̟̖̬̓̐̈́̄̿̔͌̓̏͝͝ͅͅc̸̫͈̣̜͈͚͚͚̘͚̞͔͉̋̂̈́͜ṫ̷̪͔̌͑̌̽̾̏̊̐ ̷̧̰̟̱͇̳̮̩͎̯̼̰̀̑̑́̍̅̅̀̀̀̐͠͝ǹ̵̨͔͎̣̰̹̭̎̀͊̒̓͐͛͑̓̏̔́͝o̶̭̬̥̘̪͔̲͎̹̓̑̂̒̄͂͊̔̈̽̈́̏̏͜w̷̰̯̪̬͇̻͛̌̏́̒́̈́̋̐̚.̶̠̙̒̄̀̀̔',
        'I̵̢̛͎̽̈́́̿͊̂̊̋̾̀̌t̷͖̺͔͎͕̞̙̿͂́̅͛͐̽̇̽̃̓͌́̈́͐ ̵̧̜̤̩͚̖͚̖̯̞̈́͛͑̈̐͐́͒́͛͘i̵̧̛͇̖̤̗͙͕̫̰̳͕̖̗̔̌̀̓s̶̤͌̀̄͊͊̾̆͊͒̐̍̃͜ ̶̨͈̤̮̙͙͕̖̮̑͂c̸̨̢̜̝͎̝̣͚̳͍̙͈͖̖͆̃͗̾̏̉̿͌̇̊͘̕ȩ̶̡̛͕͖̪̗̗̲̜̪̼̝͎̺̀̆̎͂̓̍̍̌̉̀͗͝ŕ̵̛̞̟̇̀̆t̷̳̣̮̻̹͈̗̦̣͊̀̈́̎ͅȧ̴̢͎̘̯̺̹̝̣͓̗̇̈́̾͌̔̐̈́͋̆̇͂̈́͝ḯ̷̩̬͎̯̙̙͙̩̦͇̣̘̰̱̼̊̀̅̊̀͒̀͘͝n̶̨̞̲̰̹͎̬̩̲̍̅̒̄͋̋͆̚͘.̸̮̅̀', 'Cᔑリリ𝙹ℸ ̣  !¡∷ᒷ↸╎ᓵℸ ̣  リ𝙹∴.', 'Aᓭꖌ ᔑ⊣ᔑ╎リ ꖎᔑℸ ̣ ᒷ∷.'
        ]
        try:
            await ctx.send(f'Question: {question}\nAnswer: {random.choice(responses)}')
        except Exception as e:
            await ctx.send(e)

@client.command()
@has_permissions(manage_messages=True)
async def kick(ctx, member : discord.Member, *, reason=None):
  print("Kicked user")
  await member.send(f"you were kicked from the federal troll agency | {reason} | kicked by: {ctx.message.author}")
  await member.kick(reason=f"{reason} - Responsible User | {ctx.message.author}")

@client.command()
async def nukecount(ctx):
  await ctx.channel.send("fta has been nuked 7 tiems!11!1 :3")

@client.command()
@has_permissions(manage_messages=True)
async def ban(ctx, member : discord.Member, *, reason=None):
  print("Kicked user")
  await ctx.channel.send(f"FREE {member.name.upper()} HE DINDU NUFFIN")
  await member.send(f"you were banned from the federal troll agency | {reason} | banned by: {ctx.message.author}")
  await member.ban(reason=f"{reason} - Responsible User | {ctx.message.author}")

@client.command()
@has_permissions(manage_messages=True)
async def addrole(ctx, *, rolename):
  role = discord.utils.get(ctx.guild.roles, name=rolename)
  if not role:
    try:
      await ctx.guild.create_role(name=rolename)
      await ctx.channel.send(f"c-created role {rolename}... are you proud of me? UwU")
    except discord.MissingPermissions:
      await ctx.channel.send(noPerms)
  else:
    await ctx.channel.send("that role already exists silly x3")

@client.command()
async def createchannel(ctx, name):
  if ctx.message.author.id==530876049983143945:
    await ctx.guild.create_text_channel(name)
    await ctx.channel.send("made channel {}... enjoy... <3".format(name))

@client.command()
async def delchannel(ctx, name):
  if ctx.message.author.id==530876049983143945:
    existing_channel = discord.utils.get(ctx.guild.channels, name=name)
    await existing_channel.delete()
    await ctx.channel.send("")


@client.command()
async def banggang(ctx):
  await ctx.channel.send("https://cdn.discordapp.com/attachments/823736494610972692/823756133704400956/rprifo34ef.gif")

@client.command()
@has_permissions(manage_messages=True)
async def delrole(ctx, *, rolename):
  role = discord.utils.get(ctx.guild.roles, name=rolename)
  if role:
    try:
      await role.delete()
      await ctx.channel.send(f"hey {ctx.message.author.mention}... i deleted the role {rolename}...  <3")
    except discord.MissingPermissions:
      await ctx.channel.send(noPerms)
  else:
    await ctx.channel.send("that role doesnt exist dummy!!")

@client.command()
async def attic(ctx):
	await ctx.channel.send("https://cdn.discordapp.com/attachments/805610014814240818/823805119946686514/image0.png")

@client.command()
@has_permissions(manage_messages=True)
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	


	for ban_entry in banned_users:
		user = ban_entry.user

		if (user.id) == (member.id):
			await ctx.guild.unban(user)
			await ctx.channel.send(f"unbanned {user.mention}! i love you !! :3")
			return


@client.command(pass_context=True)
async def kanye(ctx):
	res = requests.get("https://api.kanye.rest/")
	res = res.json()
	quote = res["quote"]
	embed = discord.Embed(description=f"{quote} -- Kanye West")
	embed.set_footer(text="random kanye west quote")
	await ctx.send(embed=embed)
	
	
@client.command(pass_context=True, aliases=["yt"])
async def youtube(ctx,*,query):
		      		async with aiohttp.ClientSession() as cs:
		      			async with cs.get(f'https://normal-api.ml/youtube/searchvideo?query={query}') as r:
		      				response = await r.text()
		      				res = json.loads(response)
		      				if res["status"] != "200":
		      					await ctx.send("can't find video #sad")
		      					return
		      				url = res["url"]
		      				await ctx.send(f"{url}")
		      				
		      				
@client.command(pass_context=True,aliases=['memes'])
async def meme(ctx):
    url = "https://meme-api.herokuapp.com/gimme"
    response = requests.request("GET", url)
    memedat = json.loads(response.text)
    postlink = memedat["postLink"]
    subreddit = memedat["subreddit"]
    title = memedat["title"]
    url = memedat["url"]

    embed = discord.Embed(
        title=f"{title}",
        url=f"{postlink}")
    embed.set_footer(text=f"r/{subreddit}")
    embed.set_image(url=url)
    await ctx.send(embed=embed)
    
    
@client.command(pass_context=True)
@commands.cooldown(1, 30, commands.BucketType.guild)
async def neko(ctx):
    
    url = "https://waifu.pics/api/sfw/neko"
    res1 = requests.request("GET", url)
    res = json.loads(res1.text)
    link = res['url']
    embed = discord.Embed(title="nyaa~",url=link)
    embed.set_image(url=link)
    await ctx.send(embed=embed)
    
    

@client.command(pass_context=True, aliases=['w'])
@commands.cooldown(1, 30, commands.BucketType.guild)
async def waifu(ctx):
    url = "https://waifu.pics/api/sfw/waifu"
    res1 = requests.request("GET", url)
    res = json.loads(res1.text)
    waifu = res['url']
    embed = discord.Embed(title="here's your waifu",url=waifu)
    embed.set_image(url=waifu)
    await ctx.send(embed=embed)

#ping
    
@client.command()
async def ping(ctx):
        """Check the bot's latency."""
        try:
            await ctx.send(f'Pong! {round(client.latency * 1000)} ms')
        except Exception as e:
            await ctx.send(e)
            
#avatar


    
@client.command(aliases=['av'])
async def avatar(ctx, user : discord.Member=None):
        '''Check someone's avatar'''
        try: 
            if user == None:
                embed1 = discord.Embed(title=f"Here's is the avatar of {ctx.author}", color=discord.Colour.blue())
                embed1.set_image(url=ctx.author.avatar_url)

                await ctx.send(embed=embed1)
                return True

            else:
                if isinstance(user, discord.member.Member):
                    _embed = discord.Embed(title=f" Here is the avatar of {user}", color=discord.Colour.blue())
                    _embed.set_image(url=user.avatar_url)

                    await ctx.send(embed=_embed)
                    return True

                await ctx.send(f"Couldn't find the user as `{user}`")
                
        except Exception as e:
            await ctx.send(e)
	
@client.command()
async def wasted(ctx, member: discord.Member=None):
  if not member:
    member = ctx.author
  wastedsession = aiohttp.ClientSession()
  async with wastedsession.get(f"https://some-random-api.ml/canvas/wasted?avatar={member.avatar_url_as(format='png')}") as img:
    if img.status != 200:
          await ctx.send("no image!! absolute FAILURE")
          await wastedsession.close()      
    else:
      data = io.BytesIO(await img.read())
      await ctx.send(file=discord.File(data, 'wasted.png'))
      await wastedsession.close()
			       
@client.command()
async def gay(ctx, member: discord.Member=None):
  if not member:
    member = ctx.author
          
  wastedsession = aiohttp.ClientSession()
  async with wastedsession.get(f"https://some-random-api.ml/canvas/gay?avatar={member.avatar_url_as(format='png')}") as img:
    if img.status != 200:
      await ctx.send("no image!! absolute FAILURE")
      await wastedsession.close()      
    else:
      data = io.BytesIO(await img.read())
      await ctx.send(file=discord.File(data, 'gay.png'))
      await wastedsession.close()

@client.command()
async def triggered(ctx, member: discord.Member=None):
  if not member:
    member = ctx.author
          
  wastedsession = aiohttp.ClientSession()
  async with wastedsession.get(f"https://some-random-api.ml/canvas/triggered?avatar={member.avatar_url_as(format='png')}") as img:
    if img.status != 200:
      await ctx.send("no image!! absolute FAILURE")
      await wastedsession.close()      
    else:
      data = io.BytesIO(await img.read())
      await ctx.send(file=discord.File(data, 'triggered.gif'))
      await wastedsession.close()

@client.command(pass_context=True)
async def hentai(ctx):
    if ctx.message.channel.is_nsfw():
        url = "https://waifu.pics/api/nsfw/waifu"
        res1 = requests.request("GET", url)
        res = json.loads(res1.text)
        waifu = res['url']
        embed = discord.Embed(title="owo",url=waifu)
        embed.set_image(url=waifu)
        await ctx.send(embed=embed)
    else:
        await ctx.channel.send("this channel is sfw :((")

@client.command(pass_context=True)
async def traphentai(ctx):
    if ctx.message.channel.is_nsfw():
        url = "https://waifu.pics/api/nsfw/trap"
        res1 = requests.request("GET", url)
        res = json.loads(res1.text)
        waifu = res['url']
        embed = discord.Embed(title="😳",url=waifu)
        embed.set_image(url=waifu)
        await ctx.send(embed=embed)
    else:
        await ctx.channel.send("this channel is sfw :((")

@client.command(pass_context=True)
async def bjhentai(ctx):
    if ctx.message.channel.is_nsfw():
        url = "https://waifu.pics/api/nsfw/blowjob"
        res1 = requests.request("GET", url)
        res = json.loads(res1.text)
        waifu = res['url']
        embed = discord.Embed(title="woag",url=waifu)
        embed.set_image(url=waifu)
        await ctx.send(embed=embed)
    else:
        await ctx.channel.send("this channel is sfw :((")

        


@client.command(pass_context=True)
async def nekohentai(ctx):
    if ctx.message.channel.is_nsfw():
        url = "https://waifu.pics/api/nsfw/neko"
        res1 = requests.request("GET", url)
        res = json.loads(res1.text)
        waifu = res['url']
        embed = discord.Embed(title="uwu",url=waifu)
        embed.set_image(url=waifu)
        await ctx.send(embed=embed)
    else:
        await ctx.channel.send("this channel is sfw :((")

@client.command(aliases=["lrcs"])
async def lyrics(ctx, *, arg):
    """
    An Example of Lyrics Command using discord.py Calling SRA's Lyrics Endpoint.
    Usage : [command_prefix]lyrics <song name>
    """
    await ctx.trigger_typing()
    arg = arg.replace(" ", "+")

    lrcsession = aiohttp.ClientSession()
    async with lrcsession.get(
        f"https://some-random-api.ml/lyrics?title={arg}"
    ) as lrcgetlnk:
        lrcdata = await lrcgetlnk.json()
    try:
        lyrrc = str(lrcdata["lyrics"])
        for chunk in [lyrrc[i : i + 2000] for i in range(0, len(lyrrc), 2000)]:
            embed = discord.Embed(
                title=f"**{(str(lrcdata['title']))} by {(str(lrcdata['author']))}**",
                description=chunk,
                color = 0x000000,
            )
            embed.set_footer(
                text=f"Requested by {ctx.author}",
                icon_url=ctx.author.avatar_url,
            )
            await ctx.send(embed=embed)
    except discord.HTTPException:
        embe = discord.Embed(
            title=f"**{(str(lrcdata['title']))} by {(str(lrcdata['author']))}**",
            color=0x000000,
            description=chunk,
        )
        embe.set_footer(
            text=f"Requested by {ctx.author}",
            icon_url=ctx.author.avatar_url,
        )
        embe.timestamp = datetime.datetime.utcnow()
        await ctx.send(embed=embe)
    await lrcsession.close()
			       #thanks 2 randomapi
		      				
client.run("")
  
  
