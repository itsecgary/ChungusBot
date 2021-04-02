import discord
from discord.ext import commands, tasks
import string
import json
import requests
import sys
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

class Chungy(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.group()
    async def chungy(self, ctx):
        if ctx.invoked_subcommand is None:
            await ctx.channel.send("Invalid command. Run `>help chungy` for information on **chungy** commands.")

#################################### SETUP #####################################
def setup(bot):
    bot.add_cog(Chungy(bot))
