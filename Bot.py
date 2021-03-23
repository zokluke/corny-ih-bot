import discord
from discord.ext.commands import has_permissions, MissingPermissions
from discord.ext import commands
import random
import re
from random import choice

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
 async def choose(ctx, *choices: str):
      """Choose between multiple options.
        To denote options which include whitespace, you should use
        double quotes.
      """
      try:
        choices = [(c) for c in choices]
        if len(choices) < 2:
            await ctx.send("Not enough options to pick from.")
        else:
            await ctx.send(f' 🤔 | My choice is `{choice(choices)}`')
      except Exception as e:
            await ctx.send(e)

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
  
  
