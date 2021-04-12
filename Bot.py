import discord
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext import commands
import random
import re
from random import choice, randrange
import json
import requests
import aiohttp
import io
import urllib
import datetime
from datetime import datetime
import asyncio



noPerms = "s-sorry daddy... you are missing perms... >w<"

client = commands.Bot(command_prefix=">")
client.remove_command("help")



@client.command()
async def help(ctx):
    embed=discord.Embed(title="Commands", url="https://discord.com/invite/cum", color=0xebcbe9)
    embed.set_author(name="Fembot Help", url="https://discord.com/invite/cum", icon_url="https://cdn.discordapp.com/avatars/790766377245474846/b3381956ade77026f8e750ee80814768.png?size=2048")
    embed.add_field(name="Image stuff", value="avatar (user) -- sends users avatar\nwasted (user) -- adds gta's WASTED to a users avatar\ngay (user) -- turns a user's avatar gay\nred (user) -- turns a users avatar red\npixelate (user) -- pixelates a user's avatar\ngreen (user) -- turns a users avatar green\nblue (user) -- turns a user's avatar blue\ncomment (text) -- makes a youtube comment with the specified text\ntriggered (user) -- makes user triggered\ngreyscale (user) -- turns a users avatar grey\ninvert (user) -- inverts the colors of a users avatar", inline=True)
    embed.set_footer(text="Fembot | >credits | zokluke/FTABot")
    await ctx.send(embed=embed)


numbers = [
    "zero",
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]



noPerms = "s-sorry daddy... you are missing perms... >w<"

@client.event
async def on_member_join(member):
    created = member.created_at
    now = datetime.now() 
    susss = (now - created).days

    if susss < 10:
        await member.send("hi rai der")
        await member.ban(reason="hi")
        await ctx.guild.get_channel(821255568324034581).send(f'{member.id} banned for: Account age is under 10.')

@client.command()
@has_permissions(manage_messages=True)
async def kick(ctx, member: discord.Member, *, reason=None):
    print("Kicked user")
    await member.send(
        f"you were kicked from the federal troll agency | {reason} | kicked by: {ctx.message.author}"
    )
    await ctx.guild.get_channel(821255568324034581).send(f"{member.id}({member.name}) was kicked by {ctx.message.author} | {reason}")
    await member.kick(reason=f"{reason} - Responsible User | {ctx.message.author}")

@client.command(name="whois", aliases=["memberinfo"])
async def whois(ctx, member:discord.Member =  None):

    

    if member is None:
        member = ctx.author
        roles = [role for role in ctx.author.roles]

    else:
        roles = [role for role in member.roles]

    embed = discord.Embed(title=f"{member}", colour=member.colour, timestamp=ctx.message.created_at)
    embed.set_footer(text=f"Requested by: {ctx.author}", icon_url=ctx.author.avatar_url)
    embed.set_author(name="User Info: ")
    embed.add_field(name="ID:", value=member.id, inline=False)
    embed.add_field(name="User Name:",value=member.display_name, inline=False)
    embed.add_field(name="Discriminator:",value=member.discriminator, inline=False)
    embed.add_field(name="Current Status:", value=str(member.status).title(), inline=False)
    embed.add_field(name="Current Activity:", value=f"{str(member.activity.type).title().split('.')[1]} {member.activity.name}" if member.activity is not None else "None", inline=False)
    embed.add_field(name="Created At:", value=member.created_at.strftime("%a, %d, %B, %Y, %I, %M, %p UTC"), inline=False)
    embed.add_field(name="Joined At:", value=member.joined_at.strftime("%a, %d, %B, %Y, %I, %M, %p UTC"), inline=False)
    embed.add_field(name=f"Roles [{len(roles)}]", value=" **|** ".join([role.mention for role in roles]), inline=False)
    embed.add_field(name="Top Role:", value=member.top_role, inline=False)
    embed.add_field(name="Bot?:", value=member.bot, inline=False)

    await ctx.send(embed=embed)
    return

@client.command()
@has_permissions(manage_messages=True)
async def ban(ctx, member: discord.Member, *, reason=None):
    print("Kicked user")
    await ctx.send(f"FREE {member.name.upper()} HE DINDU NUFFIN")
    await member.send(
        f"you were banned from the federal troll agency | {reason} | banned by: {ctx.message.author}"
    )
    await ctx.guild.get_channel(821255568324034581).send(f"{member.id}({member.name}) was BANNED by {ctx.message.author} | {reason}")
    await member.ban(reason=f"{reason} - Responsible User | {ctx.message.author}")

@client.command()
@has_permissions(manage_messages=True)
async def zokmethod(ctx, member: discord.Member, *, reason=None):
    reason = "rule 10"
    print("Kicked user")
    await ctx.send(f"{member.name} was banned for rule 10")
    await member.send(
        f"you were banned from the federal troll agency | {reason} | banned by: {ctx.message.author}"
    )
    await ctx.guild.get_channel(821255568324034581).send(f"{member.id}({member.name}) was BANNED by {ctx.message.author} | {reason}")
    await member.ban(reason=f"{reason} - Responsible User | {ctx.message.author}")





@client.command()
async def banner(ctx, *, message):
    """Emojify the text"""
    if not "nigger" in message:
        try:
            bigtext = map(
                lambda c: f":{numbers[c]}: " if (c.isdigit()) \
                else f":regional_indicator_{c.lower()}: " if (c.isalpha()) \
                else "  " if (c == " ") \
                else "",
                message,
            )
            await ctx.send("".join(bigtext)[:-1])
        except Exception as e:
            await ctx.send(e)





@client.command()
async def nukecount(ctx):
    await ctx.send("fta has been nuked 7 tiems!11!1 :3")



@client.command()
@has_permissions(manage_messages=True)
async def addrole(ctx, *, rolename):
    role = discord.utils.get(ctx.guild.roles, name=rolename)
    if not role:
        try:
            await ctx.guild.create_role(name=rolename)
            await ctx.channel.send(
                f"c-created role {rolename}... are you proud of me? UwU"
            )
        except MissingPermissions:
            await ctx.channel.send(noPerms)
    else:
        await ctx.channel.send("that role already exists silly x3")


@client.command()
async def createchannel(ctx, name):
    if ctx.message.author.id == 530876049983143945:
        await ctx.guild.create_text_channel(name)
        await ctx.channel.send(f"made channel {name}... enjoy... <3")


@client.command()
async def delchannel(ctx, name):
    if ctx.message.author.id == 530876049983143945:
        existing_channel = discord.utils.get(ctx.guild.channels, name=name)
        await existing_channel.delete()


@client.command()
async def banggang(ctx):
    await ctx.send(
        "https://cdn.discordapp.com/attachments/823736494610972692/823756133704400956/rprifo34ef.gif"
    )


@client.command()
@has_permissions(manage_messages=True)
async def delrole(ctx, *, rolename):
    role = discord.utils.get(ctx.guild.roles, name=rolename)
    if role:
        try:
            await role.delete()
            await ctx.channel.send(
                f"hey {ctx.message.author.mention}... i deleted the role {rolename}...  <3"
            )
        except MissingPermissions:
            await ctx.channel.send(noPerms)
    else:
        await ctx.channel.send("that role doesnt exist dummy!!")


@client.command()
async def attic(ctx):
    await ctx.send(
        "https://cdn.discordapp.com/attachments/805610014814240818/823805119946686514/image0.png"
    )


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


@client.command()
async def kanye(ctx):
    res = requests.get("https://api.kanye.rest/")
    res = res.json()
    quote = res["quote"]
    embed = discord.Embed(description=f"{quote} -- Kanye West")
    embed.set_footer(text="random kanye west quote")
    await ctx.send(embed=embed)



@client.command(aliases=["yt"])
async def youtube(ctx, *, query):
    async with aiohttp.ClientSession() as cs:
        async with cs.get(
            f"https://normal-api.ml/youtube/searchvideo?query={urllib.parse.urlencode(query)}"
        ) as r:
            response = await r.text()
            res = json.loads(response)
            if res["status"] != "200":
                await ctx.send("can't find video #sad")
                return
            url = res["url"]
            await ctx.send(f"{url}")

@client.command(aliases=["ttf"])
async def translatetofrench(ctx, *, query):
    async with aiohttp.ClientSession() as cs:
        async with cs.get(
            f"https://normal-api.ml/translate?text={query}&to=fr"
        ) as r:
            response = await r.text()
            res = json.loads(response)
            if res["status"] != "200":
                await ctx.send("can't find video #sad")
                return
            url = res["translated"]
            await ctx.send(f"{url}")

@client.command(aliases=["sfn"])
async def safenote(ctx, *, query):
    async with aiohttp.ClientSession() as cs:
        async with cs.get(
            f"https://normal-api.ml/safenote?note={query}"
        ) as r:
            response = await r.text()
            res = json.loads(response)
            if res["status"] != "200":
                await ctx.send("da shih broke my homie!!")
                return
            url = res["url"]
            await ctx.send(f"{url}")
@client.command(aliases=["img"])
@has_permissions(manage_messages=True)
async def image(ctx, *, query):
    await ctx.trigger_typing()
    async with aiohttp.ClientSession() as cs:
        async with cs.get(
            f"https://normal-api.ml/image-search?query={query}"
        ) as r:
            response = await r.text()
            res = json.loads(response)
            if res["status"] != "200":
                await ctx.send("da shih broke my homie!!")
                return
            url = res["image"]
            await ctx.send(f"{url}")

suasodaisduaisudaisds="hhhhhhhhhhhhh"
@client.command(aliases=["ii"])
async def inviteinfo(ctx, *, query):
    try:
        async with aiohttp.ClientSession() as cs:
            async with cs.get(
                f"https://normal-api.ml/inviteinfo?code={query}"
            ) as r:
                response = await r.text()
                res = json.loads(response)
                if res["status"] != "200":
                    await ctx.send("error!!! gay!!!")
                    return
                code = res["code"]
                
                gname = res["guild_name"]
                iname = res["inviter_tag"]
                channame = res["channel_name"]
                guild_members=res["guild_members"]
                await ctx.send(f"invite code: {code}\nserver name: {gname}\ninviter name: {iname}\nchannel name: {channame}\nmember count: {guild_members}")
    except Exception as e:
        await ctx.send(f"error:({e})")



@client.command(aliases=["memes"])
async def meme(ctx):
    url = "https://meme-api.herokuapp.com/gimme"
    response = requests.request("GET", url)
    memedat = json.loads(response.text)
    postlink = memedat["postLink"]
    subreddit = memedat["subreddit"]
    title = memedat["title"]
    url = memedat["url"]

    embed = discord.Embed(title=f"{title}", url=f"{postlink}")
    embed.set_footer(text=f"r/{subreddit}")
    embed.set_image(url=url)
    await ctx.send(embed=embed)


@client.command()

async def neko(ctx):
    url = "https://waifu.pics/api/sfw/neko"
    res1 = requests.request("GET", url)
    res = json.loads(res1.text)
    link = res["url"]
    embed = discord.Embed(title="nyaa~", url=link)
    embed.set_image(url=link)
    await ctx.send(embed=embed)


@client.command(aliases=["w"])

async def waifu(ctx):
    url = "https://waifu.pics/api/sfw/waifu"
    res1 = requests.request("GET", url)
    res = json.loads(res1.text)
    waifu = res["url"]
    embed = discord.Embed(title="here's your waifu", url=waifu)
    embed.set_image(url=waifu)
    await ctx.send(embed=embed)


@client.command()
async def ping(ctx):
    """Check the bot's latency."""
    try:
        await ctx.send(f"Pong! {round(client.latency * 1000)} ms")
    except Exception as e:
        await ctx.send(e)


@client.command(aliases=["av"])
async def avatar(ctx, user: discord.Member = None):
    """Check someone's avatar"""
    try:
        if user == None:
            embed1 = discord.Embed(
                title=f"Here's the avatar of {ctx.author}",
                color=discord.Colour.blue(),
            )
            embed1.set_image(url=ctx.author.avatar_url)

            await ctx.send(embed=embed1)
            return True

        else:
            if isinstance(user, discord.member.Member):
                _embed = discord.Embed(
                    title=f" Here the avatar of {user}", color=discord.Colour.blue()
                )
                _embed.set_image(url=user.avatar_url)

                await ctx.send(embed=_embed)
                return True

            await ctx.send(f"Couldn't find the user as `{user}`")

    except Exception as e:
        await ctx.send(e)


@client.command()
async def wasted(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author
    wastedsession = aiohttp.ClientSession()
    async with wastedsession.get(
        f"https://some-random-api.ml/canvas/wasted?avatar={member.avatar_url_as(format='png')}"
    ) as img:
        if img.status != 200:
            await ctx.send("no image!! absolute FAILURE")
            await wastedsession.close()
        else:
            data = io.BytesIO(await img.read())
            await ctx.send(file=discord.File(data, "wasted.png"))
            await wastedsession.close()


@client.command()
async def gay(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author

    wastedsession = aiohttp.ClientSession()
    async with wastedsession.get(
        f"https://some-random-api.ml/canvas/gay?avatar={member.avatar_url_as(format='png')}"
    ) as img:
        if img.status != 200:
            await ctx.send("no image!! absolute FAILURE")
            await wastedsession.close()
        else:
            data = io.BytesIO(await img.read())
            await ctx.send(file=discord.File(data, "gay.png"))
            await wastedsession.close()

@client.command()
async def red(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author

    wastedsession = aiohttp.ClientSession()
    async with wastedsession.get(
        f"https://some-random-api.ml/canvas/red?avatar={member.avatar_url_as(format='png')}"
    ) as img:
        if img.status != 200:
            await ctx.send("no image!! absolute FAILURE")
            await wastedsession.close()
        else:
            data = io.BytesIO(await img.read())
            await ctx.send(file=discord.File(data, "red.png"))
            await wastedsession.close()

@client.command()
async def pixelate(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author

    wastedsession = aiohttp.ClientSession()
    async with wastedsession.get(
        f"https://some-random-api.ml/canvas/pixelate?avatar={member.avatar_url_as(format='png')}"
    ) as img:
        if img.status != 200:
            await ctx.send("no image!! absolute FAILURE")
            await wastedsession.close()
        else:
            data = io.BytesIO(await img.read())
            await ctx.send(file=discord.File(data, "pixelate.png"))
            await wastedsession.close()

@client.command()
async def green(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author

    wastedsession = aiohttp.ClientSession()
    async with wastedsession.get(
        f"https://some-random-api.ml/canvas/green?avatar={member.avatar_url_as(format='png')}"
    ) as img:
        if img.status != 200:
            await ctx.send("no image!! absolute FAILURE")
            await wastedsession.close()
        else:
            data = io.BytesIO(await img.read())
            await ctx.send(file=discord.File(data, "green.png"))
            await wastedsession.close()

@client.command()
async def blue(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author

    wastedsession = aiohttp.ClientSession()
    async with wastedsession.get(
        f"https://some-random-api.ml/canvas/blue?avatar={member.avatar_url_as(format='png')}"
    ) as img:
        if img.status != 200:
            await ctx.send("no image!! absolute FAILURE")
            await wastedsession.close()
        else:
            data = io.BytesIO(await img.read())
            await ctx.send(file=discord.File(data, "blue.png"))
            await wastedsession.close()

@client.command()
async def comment(ctx, *, comment):
    member = ctx.author

    wastedsession = aiohttp.ClientSession()
    async with wastedsession.get(
        f"https://some-random-api.ml/canvas/youtube-comment?avatar={member.avatar_url_as(format='png')}&comment={comment}&username={member.name}"
    ) as img:
        if img.status != 200:
            await ctx.send("no image!! absolute FAILURE")
            await wastedsession.close()
        else:
            data = io.BytesIO(await img.read())
            await ctx.send(file=discord.File(data, "youtube.png"))
            await wastedsession.close()

            

@client.command()
async def triggered(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author

    wastedsession = aiohttp.ClientSession()
    async with wastedsession.get(
        f"https://some-random-api.ml/canvas/triggered?avatar={member.avatar_url_as(format='png')}"
    ) as img:
        if img.status != 200:
            await ctx.send("no image!! absolute FAILURE")
            await wastedsession.close()
        else:
            data = io.BytesIO(await img.read())
            await ctx.send(file=discord.File(data, "triggered.gif"))
            await wastedsession.close()


@client.command()
async def hentai(ctx):
    if ctx.message.channel.is_nsfw():
        url = "https://waifu.pics/api/nsfw/waifu"
        res1 = requests.request("GET", url)
        res = json.loads(res1.text)
        waifu = res["url"]
        embed = discord.Embed(title="owo", url=waifu)
        embed.set_image(url=waifu)
        await ctx.send(embed=embed)
    else:
        await ctx.channel.send("this channel is sfw :((")


@client.command()
async def traphentai(ctx):
    if ctx.message.channel.is_nsfw():
        url = "https://waifu.pics/api/nsfw/trap"
        res1 = requests.request("GET", url)
        res = json.loads(res1.text)
        waifu = res["url"]
        embed = discord.Embed(title="😳", url=waifu)
        embed.set_image(url=waifu)
        await ctx.send(embed=embed)
    else:
        await ctx.channel.send("this channel is sfw :((")


@client.command()
async def bjhentai(ctx):
    if ctx.message.channel.is_nsfw():
        url = "https://waifu.pics/api/nsfw/blowjob"
        res1 = requests.request("GET", url)
        res = json.loads(res1.text)
        waifu = res["url"]
        embed = discord.Embed(title="woag", url=waifu)
        embed.set_image(url=waifu)
        await ctx.send(embed=embed)
    else:
        await ctx.channel.send("this channel is sfw :((")


@client.command()
async def nekohentai(ctx):
    if ctx.message.channel.is_nsfw():
        url = "https://waifu.pics/api/nsfw/neko"
        res1 = requests.request("GET", url)
        res = json.loads(res1.text)
        waifu = res["url"]
        embed = discord.Embed(title="uwu", url=waifu)
        embed.set_image(url=waifu)
        await ctx.send(embed=embed)
    else:
        await ctx.channel.send("this channel is sfw :((")

@client.command()
async def killbot(ctx):
    if ctx.message.author.id==530876049983143945:
        await client.logout()



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
        f"https://some-random-api.ml/lyrics?title={urllib.parse.urlencode(arg)}"
    ) as lrcgetlnk:
        lrcdata = await lrcgetlnk.json()
    try:
        lyrrc = str(lrcdata["lyrics"])
        for chunk in [lyrrc[i : i + 2000] for i in range(0, len(lyrrc), 2000)]:
            embed = discord.Embed(
                title=f"**{(str(lrcdata['title']))} by {(str(lrcdata['author']))}**",
                description=chunk,
                color=0x000000,
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
    # thanks 2 randomapi


    

@client.command()
async def credits(ctx):
    await ctx.send(
        "main bot developer: zokluke#4082. People that contributed to the bot are listed on github. Link to the github page: https://github.com/zokluke/FTABot"
    )


@client.command()
async def amogus(ctx):
    await ctx.send(
        "ඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞ red is sus! ඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞඞ"
    )


@client.command()
async def kendrick(ctx):
    await ctx.send("https://open.spotify.com/artist/2YZyLoL8N0Wb9xBt1NhZWg")


@client.command()
async def ltc(ctx):
    """Generates a random person and info"""
    response = requests.request("GET", "https://randomuser.me/api")
    ruinfo = json.loads(response.text)[0]
    pname = (
        f"{ruinfo['name']['title']}. {ruinfo['name']['first']} {ruinfo['name']['last']}"
    )
    pbio = f"{ruinfo['dob']['age']} y.o. living in {ruinfo['location']['city']}, {ruinfo['location']['state']}, {ruinfo['location']['country']}"

    embed = discord.Embed(title=pname, description=pbio)
    embed.set_footer(text=f"LTC alt # {randrange(1, 1000000000)}")
    embed.set_image(url="https://thispersondoesnotexist.com/image")
    await ctx.send(embed=embed)

#thispersondoesnotexist
   
@client.command(aliases = ['tpdne'])
async def thispersondoesnotexist(ctx):
      """Send an AI generated image of a person."""
      try: 
        headers = {'User-Agent': "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36 Edg/88.0.705.63"}
  
        f = open('face.png', 'wb')
        img = urllib.request.urlopen(urllib.request.Request('https://thispersondoesnotexist.com/image', headers = headers))
        f.write(img.read())
        embed = discord.Embed(title = 'This person does not exist.', color=discord.Color.orange())
        embed.set_image(url = 'attachment://face.png')
        await ctx.send(file=discord.File('face.png'),embed = embed)
        f.close()
      except Exception as e:
        await ctx.send(e)
@client.command(aliases= ["guilds"])
async def servers(ctx):
    await ctx.send( f"fembot is in {len(client.guilds)} servers! >w<")

@client.command()
@has_permissions(manage_messages=True)
async def pettymethod(ctx, member: discord.Member, *, reason=None):
    reason="BECAUSE THEY FUCKING SUCK PUSSY!!!!"
    print("Kicked user")
    await ctx.send(f"I BANNED {member.name.upper()} BECAUSE THE FUCKING SUCK AND ARE A PUSSY!!!")
    await member.send(
        f"you were banned from the federal troll agency | BECAUSE YOU FUCKING SUCK PUSSY!!! | banned by: {ctx.message.author}"
    )
    await ctx.guild.get_channel(821255568324034581).send(f"{member.id}({member.name}) was BANNED by {ctx.message.author} | {reason}")
    await member.ban(reason=f"{reason} - Responsible User | {ctx.message.author}")

@client.command()
async def chatbot(ctx, *, arg):
    """
    Chats with you!
    """
    arg = arg.replace(" ", "+")

    lrcsession = aiohttp.ClientSession()
    async with lrcsession.get(
        f"https://some-random-api.ml/chatbot?message={arg}&key=9ee3lZlMolKl0oRpHsQgar9AI"
    ) as sgetlnk:
        lrcdata = await sgetlnk.json()
    await ctx.send(lrcdata['response'])
    await lrcsession.close()

@client.command()
async def greyscale(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author

    wastedsession = aiohttp.ClientSession()
    async with wastedsession.get(
        f"https://some-random-api.ml/canvas/greyscale?avatar={member.avatar_url_as(format='png')}"
    ) as img:
        if img.status != 200:
            await ctx.send("no image!! absolute FAILURE")
            await wastedsession.close()
        else:
            data = io.BytesIO(await img.read())
            await ctx.send(file=discord.File(data, "greyscale.png"))
            await wastedsession.close()

@client.command()
async def invert(ctx, member: discord.Member = None):
    if not member:
        member = ctx.author

    wastedsession = aiohttp.ClientSession()
    async with wastedsession.get(
        f"https://some-random-api.ml/canvas/invert?avatar={member.avatar_url_as(format='png')}"
    ) as img:
        if img.status != 200:
            await ctx.send("no image!! absolute FAILURE")
            await wastedsession.close()
        else:
            data = io.BytesIO(await img.read())
            await ctx.send(file=discord.File(data, "invert.png"))
            await wastedsession.close()

client.run
