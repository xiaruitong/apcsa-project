import os, logging
from datetime import datetime

time_start = datetime.now()
log_filename = f"{time_start.year}-{str(time_start.month).zfill(2)}-{str(time_start.day).zfill(2)}_{str(time_start.hour).zfill(2)}_{str(time_start.minute).zfill(2)}_{str(time_start.second).zfill(2)}"

os.makedirs("./logs/", exist_ok=True)

with open(f"./logs/{log_filename}.log", 'w', encoding='utf-8') as f:
    f.truncate(0)

logging.basicConfig(level='INFO', format='[%(asctime)s] [%(thread)d - %(threadName)s] [%(levelname)s] %(message)s',
                    encoding='utf-8',
                    handlers=[
                        logging.FileHandler(f"./logs/{log_filename}.log", encoding='utf-8'),
                        logging.StreamHandler()
                    ])

import discord
from discord.ext import commands

import config

# load local config file
conf = config.Config()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents, proxy=conf.get_proxy())


@bot.command()
async def test(ctx, arg):
    await ctx.send(arg)


@bot.command()
async def add(ctx, arg1: int, arg2: int):
    logging.info(f"Execution: add with arguments: {arg1} + {arg2}")
    result: int = arg1 + arg2
    await ctx.send(str(result))


bot.run(token=conf.get_token(), log_handler=None)
