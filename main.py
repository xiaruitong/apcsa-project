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
import random

import config

# load local config file
conf = config.Config()

intents = discord.Intents.default()
intents.message_content = True

bot = commands.Bot(command_prefix='.', intents=intents, proxy=conf.get_proxy())


@bot.command()
async def echo(context, arg):
    await context.reply(arg)


@bot.command()
async def add(context, arg1: int, arg2: int):
    logging.info(f"Execution: add with arguments: {arg1} + {arg2}")
    result: int = arg1 + arg2
    await context.reply(str(result))


@bot.command()
async def roll(context, expr: str):
    # "AdB"
    # A: how many dice to roll - int
    # B: how many face each die have - int

    async def handle_invalid_expr():
        await context.reply("Not a invalid dice expression.")

    # locate the first instance of d in the expr
    try:
        idx: int = expr.index("d")
        strA: str = expr[0: idx]
        strB: str = expr[idx + 1:]

        if strA == "":
            A: int = 1
        else:
            try:
                A: int = int(strA)
            except ValueError:
                await handle_invalid_expr()
                return

        if strB == "":
            B: int = 6
        else:
            try:
                B: int = int(strB)
            except ValueError:
                await handle_invalid_expr()
                return

        result_list: list[int] = []

        for i in range(0, A):
            result_list.append(random.randint(1, B))

        result = f"Result: {sum(result_list)}\n\nDetails: {result_list}"
        await context.reply(result)

    except ValueError:
        await handle_invalid_expr()




bot.run(token=conf.get_token(), log_handler=None)
