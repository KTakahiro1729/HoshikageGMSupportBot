from discord.ext import commands
from dotenv import load_dotenv
import os

load_dotenv()

bot = commands.Bot(command_prefix='..', description='A simple Discord bot')

token = os.getenv('DISCORD_BOT_TOKEN')

@bot.command()
async def hello(ctx):
    await ctx.send("Hello!")

bot.run(token)