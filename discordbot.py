import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True
intents.guilds = True  # Make sure this is enabled to handle guild events like member join
intents.members = True  # Enable members intent for tracking member joins

bot = commands.Bot(command_prefix='!', intents=intents, heartbeat_timeout=60)

@bot.event
async def on_ready():
    print(f'Logged in as {bot.user}')

@bot.event
async def on_member_join(member):
    channel = discord.utils.get(member.guild.text_channels, name='welcome-channel')  # Use the exact channel name
    if channel:
        await channel.send(f'Welcome to the server, {member.mention}!')

@bot.event
async def on_message(message):
    if message.content.lower() == 'hi' and not message.author.bot:
        await message.channel.send('Hello there!')
    await bot.process_commands(message)

@bot.command()
async def hello(ctx):
    await ctx.send('Hello there!')

@bot.command()
async def announce(ctx, *, message):
    channel = discord.utils.get(ctx.guild.text_channels, name='announcements')  # Use the exact channel name
    if channel:
        await channel.send(f'📢 Announcement: {message}')
    else:
        await ctx.send("Announcement channel not found.")

bot.run('DISCORD_BOT_TOKEN')
