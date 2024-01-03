import os
#os.system("pip install discord.py==1.7.3") 
import sys
import discord
from discord.ext import commands
import asyncio
import requests
import pyfiglet
import random
import aiohttp
from datetime import datetime, timedelta


intents = discord.Intents.all()

aizerr = (".")

client = commands.Bot(command_prefix=aizerr, case_insensitive=True, self_bot=True, intents=intents)

client.remove_command("help")

@client.event
async def on_ready():
    print(f"Logged in as {client.user}")
@client.command(name="ping", aliases=["pong", "latency"])
async def ping(ctx):
    latency = round(client.latency * 1000)
    await ctx.send(f"Pong! Latency is {latency}ms")

@client.command(name="help", aliases=["h"])
async def help(ctx):
    help_message = (
        "**```js\n"
        "🚀 AIZER SELF BOT 🚀\n"
        " - DISCORD.GG/NTOP - \n\n"
        "• Gnrl\n"
        "• Nuke\n\n"
        "! ALSO CHECK COMMANDS ALIASES IN CODE !\n"
        "```**"
    )
    await ctx.send(help_message)

@client.command(name="gnrl", aliases=["G"])
async def gnrl(ctx):
    gnrl_message = (
        "**```js\n"
        "🚀 AIZER SELF BOT 🚀\n"
        " - DISCORD.GG/NTOP - \n\n"
        "ping\n"
        "say  \n"
        "userinfo  \n"
        "vouch\n"
        "asci \n"
        "calculator \n"
        "ltcprice \n"
        "sclear \n"
        "status \n"
        "stopstatus \n"
        "\n\n"
        "! ALSO CHECK COMMANDS ALIASES IN CODE !\n"
        "```**"
    )

    await ctx.send(gnrl_message)

@client.command(name="nuke", aliases=["n"])
async def nuke(ctx):
         
         nuke_message = (
        "**```js\n"
        "🚀 AIZER SELF BOT 🚀\n"
        " - DISCORD.GG/NTOP - \n\n"
        "spam \n"
        "sendhook \n"
        "iplookup \n"
        "role \n"
        "leave\n"
        "prune\n"
        "banall\n"
        "kickall\n"
        "delroles\n"
        "spamchannels\n"
        "delchannles\n"
        "spamroles\n"
        "spamall\n"
        "checkprune\n\n"
        "! ALSO CHECK COMMANDS ALIASES IN CODE !\n"
        "```**"
    )
         await ctx.send(nuke_message)

@client.command(name="say")
async def say(ctx, *, message):
    await ctx.send(message)

@client.command(name="userinfo", aliases=["ui"])
async def user_info(ctx, member: discord.Member = None):
    member = member or ctx.author

    joined_discord = member.created_at.strftime("%m/%d/%Y")
    joined_server = member.joined_at.strftime("%m/%d/%Y") if member.joined_at else "Not available"

    message = (
        f"👤**User Info**👤\n"
        f"• **Username:** `{member.name}`{member.discriminator}`\n"
        f"• **ID:** `{member.id}`\n"
        f"• **Discriminator:** `{member.discriminator}`\n"
        f"• **Nickname:** `{member.nick or 'None'}`\n"
        f"• **Status:** {status_emoji(member.status)} `{str(member.status).capitalize()}`\n"
        f"• **Joined Discord:** `{joined_discord}`\n"
        f"• **Joined Server:** `{joined_server}`"
    )

    await ctx.send(message)

def status_emoji(status):
    if status == discord.Status.online:
        return "🟢"
    elif status == discord.Status.idle:
        return "🟡"
    elif status == discord.Status.dnd:
        return "🔴"
    elif status == discord.Status.offline:
        return "⚫"
    else:
        return "❓"  

@client.command(name="vouch")
async def vouch(ctx, *message):
    message = " ".join(message)
    vouch_message = f"``+rep {ctx.author.id} LEGIT GOT | {message} • LEGIT ASF TYSM ``"
    await ctx.send(vouch_message)

@client.command(name="calculator", aliases=["calc"])
async def calculator(ctx, *, expression):
    try:
        result = eval(expression)
        await ctx.send(f"**``{result}``**")
    except Exception as e:
        await ctx.send(f"❌ An error occurred: {e}")

@client.command(name="ltcprice")
async def ltc_price(ctx):
    try:
        response_usd = requests.get("https://api.coingecko.com/api/v3/simple/price", params={"ids": "litecoin", "vs_currencies": "usd"})
        data_usd = response_usd.json()
        ltc_price_usd = data_usd["litecoin"]["usd"]

        response_inr = requests.get("https://api.coingecko.com/api/v3/simple/price", params={"ids": "litecoin", "vs_currencies": "inr"})
        data_inr = response_inr.json()
        ltc_price_inr = data_inr["litecoin"]["inr"]
        await ctx.send(f"**📈 Current Litecoin (LTC) Price:**\n"
                       f"• USD: ${ltc_price_usd:.2f}\n"
                       f"• INR: ₹{ltc_price_inr:.2f}")
    except Exception as e:
        await ctx.send(f"❌ An error occurred: {e}")

async def casci(ctx, text, font):
    try:
        fig = pyfiglet.Figlet(font=font)
        ascii_result = fig.renderText(text)
        await ctx.send(f"**Font: `{font}`**\n```\n{ascii_result}\n```")
    except Exception as e:
        await ctx.send(f"❌ An error occurred: {e}")

@client.command(name="asci")
async def ascii_art(ctx, *, text):
    try:
        available_fonts = pyfiglet.Figlet().getFonts()
        additional_fonts = ["block", "caligraphy", "isometric1", "digital", "banner3-D"]
        available_fonts.extend(additional_fonts)
        random.shuffle(available_fonts)
        selected_fonts = random.sample(available_fonts, 5)

        for font in selected_fonts:
            await casci(ctx, text, font)
    except Exception as e:
        await ctx.send(f"❌ An error occurred: {e}")

@client.command(name="sclear")
async def clear_self_messages(ctx, amount: int):
    if amount <= 0 or amount > 100:
        await ctx.send("**Please provide a valid number between 1 and 100.**")
        return

    try:
        while True:
            if isinstance(ctx.channel, discord.TextChannel):
                messages = await ctx.channel.history(limit=amount + 1).flatten()
                for message in messages:
                    if message.author == client.user:
                        await message.delete()
            elif isinstance(ctx.channel, discord.DMChannel):
                messages = await ctx.channel.history(limit=amount + 1).flatten()
                for message in messages:
                    if message.author == client.user:
                        await message.delete()
            else:
                await ctx.send("**This command can only be used in a server text channel or a DM.**")
            await asyncio.sleep(5)  
    except discord.Forbidden:
        await ctx.send("**❌ | I don't have the necessary permissions to delete messages.**")
    except discord.HTTPException as e:
        await ctx.send(f"**❌ | An error occurred: {e}**")

@client.command(name="spam")
async def send_custom(ctx, message_count: int, *, content):
    try:
        if 1 <= message_count <= 100:
            for _ in range(message_count):
                await ctx.send(content)
            await ctx.send(f"✅ Sent {message_count} messages with content: {content}")
        else:
            await ctx.send("❌ Please provide a valid range between 1 and 10 messages.")
    except commands.BadArgument:
        await ctx.send("❌ Invalid message count. Please provide a valid number.")

@client.command(name="status")
async def set_status(ctx, activity_type: str, *, status: str):
    activity_type = activity_type.lower()

    if activity_type not in ["playing", "streaming", "listening", "watching"]:
        await ctx.send("`:> playing, streaming, listening, watching.`")
        return

    if activity_type == "streaming":
        await client.change_presence(activity=discord.Streaming(name=status, url="http://twitch.tv/streamer"))
    else:
        await client.change_presence(activity=discord.Game(name=status))

    await ctx.send(f"**✅ | Custom status set to `{activity_type}` `{status}`**")


@client.command(name="stopstatus")
async def stop_status(ctx):
    global current_status

    await client.change_presence(activity=None)
    current_status = None
    await ctx.send("✅ | **Custom status stopped.**")

@client.command()
async def sendhook(ctx, webhook_url, *, message):
    try:
        async with aiohttp.ClientSession() as session:
            webhook = discord.Webhook.from_url(webhook_url, adapter=discord.AsyncWebhookAdapter(session))
            await webhook.send(content=message, username="NUKERS-TERRITORY")
            await ctx.send("**✅ | Sent successfully !**")
    except Exception as e:
        await ctx.send(f"An error occurred: {e}")


# RAPIDAPI_KEY = '08c6a580-95cb-11ee-a4e6-251560f01ec5'
@client.command()
async def iplookup(ctx, ip_address):
    try:
        async with aiohttp.ClientSession() as session:
            async with session.get(f"https://ipinfo.io/{ip_address}/json") as response:
                data = await response.json()

            message = (
                f"**🌐 IP Lookup: `{ip_address}`**\n"
                f"**🔍 IP Address: `{data.get('ip', 'N/A')}`**\n"
                f"**🏙 City: `{data.get('city', 'N/A')}`**\n"
                f"**🌍 Region: `{data.get('region', 'N/A')}`**\n"
                f"**🌎 Country: `{data.get('country', 'N/A')}`**\n"
                f"**📍 Location: `{data.get('loc', 'N/A')}`**\n"
                f"**🏢 Organization: `{data.get('org', 'N/A')}`**"
            )

            await ctx.send(message)
    except Exception as e:
        await ctx.send(f"❌ An error occurred: {e}")



@client.command()
async def checkprune(ctx):
    if ctx.author.guild_permissions.kick_members:
        threshold = datetime.utcnow() - timedelta(days=1)

        role_inactive_members = {}
        
        for role in ctx.guild.roles:
            inactive_members = []
            
            for member in ctx.guild.members:
                if member.activity is None and member.status == discord.Status.online:
                    last_message = await ctx.channel.history(limit=1).get(author=member)
                    if last_message and last_message.created_at < threshold and role in member.roles:
                        inactive_members.append(member)

            role_inactive_members[role.name] = len(inactive_members)

        await ctx.send(f'**Prune :\n\n`{role_inactive_members}`**')
    else:
        await ctx.send('You do not have the required permissions to use this command.')

@client.command()
@commands.has_permissions(kick_members=True)
async def prune(ctx, reason="NUKERS TERRITORY | .GG/NTOP"):
    guild = ctx.guild
    members_to_prune = await guild.prune_members(days=1, compute_prune_count=True, reason=reason)

    await ctx.send(f"**Pruned `{members_to_prune}` members with reason: `{reason}`**")

@client.command(name='delchannels', aliases=["dall", "dch"])
async def delete_all_channels(ctx):
    for ch in ctx.guild.channels:
        try:
            await ch.delete()
            print(f"Deleted {ch}")
        except discord.Forbidden:
            print(f"I don't have the necessary permissions to delete {ch}")
        except discord.HTTPException as e:
            print(f"An error occurred while deleting {ch}: {e}")


@client.command(name="spamall", aliases=["sa"])
async def spam_to_all_channels(ctx, amount: int = 50, *, text="@everyone https://discord.gg/ntop"):
    for i in range(amount):
        for ch in ctx.guild.channels:
            try:
                await ch.send(text)
                print(f"Message sent to {ch}")
            except:
                print(f"Can't send message to {ch}")

@client.command(name='deleroles', aliases=["dr"])
async def delete_all_roles(ctx):
    for r in ctx.guild.roles:
        try:
            await r.delete()
            print(f"Deleted {r}")
        except discord.Forbidden:
            print(f"I don't have the necessary permissions to delete {r}")
        except discord.HTTPException as e:
            print(f"An error occurred while deleting {r}: {e}")

@client.command(name="spamchannels", aliases=["sch"])
async def spamchannels(ctx, amount: int = 25, *, name="NUKERS-TERRITORY"):
    for i in range(amount):
        try:
            await ctx.guild.create_text_channel(name=name)
            print(f"Created channel")
        except discord.Forbidden:
            print(f"I don't have the necessary permissions to create channels")
        except discord.HTTPException as e:
            print(f"An error occurred while creating channel: {e}")

@client.command(name="spamroles", aliases=["sr"])
async def spam_with_roles(ctx, amount: int = 25, *, name="NUKERS-TERRITORY"):
    for i in range(amount):
        try:
            await ctx.guild.create_role(name=name)
            print(f"Created role")
        except discord.Forbidden:
            print(f"I don't have the necessary permissions to create roles")
        except discord.HTTPException as e:
            print(f"An error occurred while creating role: {e}")


@client.command(name='banall', aliases=["be", "baneveryone"])
async def ban_everyone(ctx):
    for m in ctx.guild.members:
        try:
            await m.ban()
            print(f"Banned {m}")
        except discord.Forbidden:
            print(f"I don't have the necessary permissions to ban {m}")
        except discord.HTTPException as e:
            print(f"An error occurred while banning {m}: {e}")

@client.command(name='kickall', aliases=["ke", "kickeveryone"])
async def kick_everyone(ctx):
    for m in ctx.guild.members:
        try:
            await m.kick()
            print(f"Kicked {m}")
        except discord.Forbidden:
            print(f"I don't have the necessary permissions to kick {m}")
        except discord.HTTPException as e:
            print(f"An error occurred while kicking {m}: {e}")



@client.command()
async def leave(ctx, guild_id: int):
    guild = client.get_guild(guild_id)
    if guild:
        await guild.leave()
        await ctx.send(f"**✅ | `{client.user.name}` left `{guild.name}`.**")
    else:
        await ctx.send("Unable to find the specified server.")



token = "MTEzMjY0MTcxNjA1NTMyNjgxMQ.GHgEic.rNXKZtNA5yYfqGVaTilEY2Ctddtj7BFv20nFXw"
client.run(token,bot=False)
