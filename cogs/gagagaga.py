import discord
from discord.ext import commands, tasks
import string
import json
import requests
import sys
import time
import help_info
from config_vars import *

def in_dms():
    async def tocheck(ctx):
        # A check for ctf context specific commands
        if str(ctx.channel.type) == "private":
            return True
        else:
            await ctx.send("This command is only available over DM!")
            return False

    return commands.check(tocheck)

def in_channel():
    async def tocheck(ctx):
        # A check for ctf context specific commands
        if not str(ctx.channel.type) == "private":
            return True
        else:
            await ctx.send("This command is not available over DM!")
            return False

    return commands.check(tocheck)

class Gagagaga(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def gagagaga(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.channel.send("Invalid command. Run `>help gagagaga` for information on **gagagaga** commands.")

    @gagagaga.command()
    @in_dms()
    async def giveittome(self, ctx):
        try:
            f = open(f'userfiles/{ctx.author.name}_time', 'r')
            stuff = f.read()
            head = stuff.split('\n')[0]
            tail = stuff.split('\n')[3]
            print(head)
            print(tail)

            if float(tail) - float(head) < 15:
                await ctx.channel.send('`' + flag + '`')
                await ctx.channel.send(file=discord.File("morris.PNG"))
                f = open(f'userfiles/{ctx.author.name}_time', 'w')
                f.write("")
        except:
            await ctx.channel.send("Uh ohhh (no file)")

    @gagagaga.command()
    @in_channel()
    async def chunga(self, ctx):
        await ctx.channel.send("chungachungachungachungachungachungachunga")

    @gagagaga.command()
    @in_dms()
    async def chungusisgod(self, ctx):
        tic = time.perf_counter()
        try:
            f = open(f'userfiles/{ctx.author.name}_time', 'r')
            stuff = f.read()
            count = len(stuff.split('\n'))
            print(stuff)

            if count == 4:
                f = open(f'userfiles/{ctx.author.name}_time', 'a')
                f.write(f'{tic}\n')
            else:
                await ctx.channel.send("Uh ohhh (count not 4)")
        except:
            await ctx.channel.send("Uh ohhh (no file)")

#################################### SETUP #####################################
def setup(bot):
    bot.add_cog(Gagagaga(bot))
