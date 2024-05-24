import disnake
from pymongo import MongoClient
from disnake.ext import commands


class PingCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

cluster = MongoClient("mongodb+srv://skew:1@cluster0.bvbbau6.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
collection = cluster.warn.warns


@commands.slash_command(name='ping', description='Slash command')
async def ping(self, ctx):
    await ctx.respond(f'Pong!')
    pattern = {
        "_id": ctx.author.id,
        "username": ctx.author.name,
        "guild": ctx.guild.id
    }
    collection.insert_one(pattern)


def setup(bot):
    bot.add_cog(PingCog(bot))
