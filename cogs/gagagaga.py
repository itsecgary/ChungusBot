import discord
from discord.ext import commands, tasks
import string
import json
import requests
import sys
import help_info
from config_vars import *
sys.path.append("..")

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
    async def chungusisgod(self, ctx):
        await ctx.channel.send('`' + flag + '`')
        await ctx.channel.send(file=discord.File("morris.PNG"))

    @gagagaga.command()
    @in_channel()
    async def chunga(self, ctx):
        await ctx.channel.send("chungachungachungachungachungachungachunga")

#################################### SETUP #####################################
def setup(bot):
    bot.add_cog(Gagagaga(bot))
