import discord
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext import commands
from replit import db

noPerms = "s-sorry daddy... you are missing perms... >w<"

client = commands.Bot(command_prefix='>')

@client.command()
async def rape(ctx, *, message=None):
    sus=message.lower()
      await ctx.channel.send(f"{ctx.message.author.mention} raped {sus} 😈")

@client.command()
async def say(ctx, *, message=None):
    await ctx.send(message)



#banner

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

@client.command()
@has_permissions(manage_messages=True)
async def contain(ctx, user : discord.Member, *, reason = None):
  cntained = discord.utils.get(ctx.guild.roles, name="dumbass")
  if not cntained in user.roles:
    print(f"User contained: {user}")
    trollrole = discord.utils.get(ctx.guild.roles, name="Troll")
    fedrole = discord.utils.get(ctx.guild.roles, name="Federal")
    therole = discord.utils.get(ctx.guild.roles, name="The")
    elrole = discord.utils.find(lambda r: r.name == 'Elite Trolls!', ctx.guild.roles)
    if trollrole in user.roles:
      db[user.id] = "troll" # sets the role "troll" in database as user saved role
    elif fedrole in user.roles:
      db[user.id] = "federal" # sets the role "federal" in database as user saved role
    elif therole in user.roles:
      db[user.id] = "the" # sets the role "the" in database as user savmatches = db.prefix("prefix")ed role
    elif elrole in user.roles:
      db[user.id] = "elite" # sets the role "elite trolls!" in database as user saved role

    if db[user.id] == "troll":
      await client.remove_roles(user, trollrole)
      await client.add_roles(user, cntained)
    elif db[user.id] == "federal":
      await client.add_roles(user, cntained)
    elif db[user.id] == "the":
      await client.add_roles(user, cntained)
      await client.remove_roles(user, trollrole, fedrole, therole)
    elif db[user.id] == "elite":
      await client.add_roles(user, cntained)
      await client.remove_roles(user, trollrole, fedrole, therole, elrole)
    await ctx.send(f"damn homie! you really just contained {user.name}!")
  else:
    ctx.send(f"sorry homie! {user.name} is already contained!")

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
@has_permissions(manage_messages=True)
async def unban(ctx, *, member):
	banned_users = await ctx.guild.bans()
	


	for ban_entry in banned_users:
		user = ban_entry.user

		if (user.id) == (member.id):
			await ctx.guild.unban(user)
			await ctx.channel.send(f"unbanned {user.mention}! i love you !! :3")
			return


client.run("")
  
  
