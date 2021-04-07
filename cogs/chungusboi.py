import discord
from discord.ext import commands, tasks
import string
import json
import requests
import sys
import time
import help_info

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

class Chungusboi(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def chungusboi(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.channel.send("Invalid command. Run `>help chungusboi` for information on **chungusboi** commands.")

    @chungusboi.command()
    @in_dms()
    async def kyle(self, ctx):
        tic = time.perf_counter()
        with open(f'userfiles/{ctx.author.name}_time', 'w') as f:
            f.write(f'{tic}\n')

#################################### SETUP #####################################
def setup(bot):
    bot.add_cog(Chungusboi(bot))
