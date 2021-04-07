import discord
from discord.ext import commands, tasks
import string
import json
import requests
import sys
import time
import help_info
import subprocess

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

class Chungy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def chungy(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.channel.send("Invalid command. Run `>help chungy` for information on **chungy** commands.")

    @chungy.command()
    @in_dms()
    async def mcchungus(self, ctx):
        tic = time.perf_counter()
        try:
            f = open(f'userfiles/{ctx.author.name}_time', 'r')
            stuff = f.read()
            count = len(stuff.split('\n'))

            if count == 3:
                f = open(f'userfiles/{ctx.author.name}_time', 'a')
                f.write(f'{tic}\n')
            else:
                await ctx.channel.send("Uh ohhh (count not 3)")
        except:
            await ctx.channel.send("Uh ohhh (no file)")

#################################### SETUP #####################################
def setup(bot):
    bot.add_cog(Chungy(bot))
