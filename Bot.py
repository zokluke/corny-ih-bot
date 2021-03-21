import discord
from discord.ext import commands
from replit import db

client = commands.Bot(command_prefix=':')

@client.command()
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
      await user.remove_roles(trollrole)
      await user.add_roles(cntained)
    elif db[user.id] == "federal":
      await user.add_roles(cntained)
      await user.remove_roles(trollrole)
      await user.remove_roles(fedrole)
    elif db[user.id] == "the":
      await user.add_roles(cntained)
      await user.remove_roles(trollrole)
      await user.remove_roles(fedrole)
      await user.remove_roles(therole)
    elif db[user.id] == "elite":
      await user.add_roles(cntained)
      await user.remove_roles(elrole)
      await user.remove_roles(therole)
      await user.remove_roles(fedrole)
      await user.remove_roles(trollrole)
    await ctx.send(f"damn homie! you really just contained {user.name}!")
  else:
    ctx.send(f"sorry homie! {user.name} is already contained!")

xd=open("Token.json, "r"")
xd.read()

client.run("")
  
  
