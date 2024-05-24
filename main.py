import disnake
import os
from pymongo import MongoClient
from disnake.ext import commands
from colorama import init

# Инициализируем colorama
init(autoreset=True)
intents = disnake.Intents.all()
bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Бот {bot.user} успешно запущен!\nID: {bot.user.id}")


# Загружаем расширения из папки "cogs"
for file in os.listdir("./cogs"):
    if file.endswith(".py"):
        bot.load_extension(f"cogs.{file[:-3]}")

bot.run("Your token")
