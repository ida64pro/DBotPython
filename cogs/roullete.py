import disnake
from disnake.ext import commands
import random
from datetime import datetime, timedelta
import asyncio

last_spin_times = {}

class RouletteCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.allowed_channel_id = 1239594955328979058

    @commands.slash_command(
        name="roulette",
        description="Игра в рулетку"
    )
    async def roulette(self, ctx):
        # Проверяем, выполняется ли команда в разрешенном канале
        if ctx.channel.id != self.allowed_channel_id:
            embed1 = disnake.Embed()
            embed1.add_field(name="**Произошла ошибка!**", value="Эта команда доступна только в определенном канале!", inline=True)
            embed1.add_field(name="**Доступный канал:**", value="https://discord.com/channels/1237477778597744743/1239594955328979058", inline=True)
            await ctx.send(embed=embed1, ephemeral=True)
            return

        user_id = str(ctx.author.id)
        if user_id in last_spin_times:
            last_spin_time = last_spin_times[user_id]
            if datetime.now() - last_spin_time < timedelta(hours=2):
                datetimes = last_spin_time
                embed2 = disnake.Embed()
                embed2.add_field(name='Произошла ошибка!', value=f'{ctx.author.mention}, Вы уже прокручивали рулетку в последние 2 часа!', inline=True)
                embed2.add_field(name='Дата последней активации рулетки:', value=datetimes, inline=True)
                await ctx.send(embed=embed2, ephemeral=True)
                print('Кулдаун активен.')
                return
        # Список с вариантами рулетки и их шансами
        roulette_options = [
            {'name': 'Чепсеки лейс 🦀 ', 'chance': 99},
            {'name': 'LoggerMod 💾 ', 'chance': 0.1},
            {'name': 'LoggerMod 🚀 ', 'chance': 0.1},
            {'name': 'FUD Crypt 🔐 ', 'chance': 0.2},
        ]

        result = random.choices([option['name'] for option in roulette_options],
                                [option['chance'] for option in roulette_options])[0]
        embed = disnake.Embed(title='Крутим рулетку...')
        embed.set_image(url="https://www.viber.com/app/uploads/spinning_wheel_gif.gif")
        await ctx.send(embed=embed, ephemeral=True)
        last_spin_times[user_id] = datetime.now()

        await asyncio.sleep(5)

        embed = disnake.Embed(title=f"Шедеврулетка by reJava Team , Bogov",  description="**Правила:** Напиши `/roulette`, чтобы начать игру!\n"
                           "\n"
                            "**Призы ( 🏆 ):**\n"
                                                 "\n"  
                            "- Логгер ( 💾 )\n"           
                            "- Лоадер ( 🚀 )\n"                                                         
                            "- Крипт ( 🔐 )\n"                                  
                            "- Стиллер ( ♻️ )\n"                                
                            "- Чепсеки лейс ( 🦀 )\n"
                                                                                          "\n"
                              f"**Приз: **" + result + "**Ты победил?**"
                                                   "\n"
                                                       "\n"
                            "**Забрать приз можно у:** <@1215982951167299694>\n"
                                                                         "\n"
                            "Мои создатели: **@ynetds** **&** **@bogovnew** **&** **@sk3ww**\n"
                                                                           "\n"
                            "- **Made by reJava Team** ")
        embed.set_thumbnail(url="https://media1.tenor.com/m/X6hWPXlAYGkAAAAC/roulette-game.gif")
        await ctx.edit_original_response(embed=embed)
        channel = await self.bot.fetch_channel(1239859458428108801)
        embedLog = disnake.Embed()
        embedLog.add_field(name=f'Победитель (пинг): ', value=ctx.author.mention, inline=True)
        embedLog.add_field(name=f'Победитель (индетификатор): ', value=ctx.author.id, inline=True)
        embedLog.add_field(name=f'Приз: ', value=result, inline=True)
        if(result != 'Чепсеки лейс 🦀 '):
            await channel.send('@everyone', embed=embedLog)
        else:
            await channel.send(embed=embedLog)

def setup(bot):
    bot.add_cog(RouletteCog(bot))
