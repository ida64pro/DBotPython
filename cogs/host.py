import disnake
from disnake.ext import commands
import platform
import psutil

DEV_ID = 1215982951167299694

class Host(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name='host', description='Выдает информацию о боте.')
    async def host_info(self, ctx):
        # Проверяем, является ли автор вызова указанным пользователем
        if ctx.author.id != DEV_ID or ctx.author.id != 771825925993136148:
            await ctx.send("Куда ручки полезли?")
            return
        
        embed = disnake.Embed(title="Характеристики хоста")
        embed.add_field(name="Платформа", value=platform.platform())
        embed.add_field(name="Архитектура", value=platform.architecture()[0])  # Возвращает строку с архитектурой
        embed.add_field(name="Процессор", value=platform.processor())
        embed.add_field(name="Система", value=f"{platform.system()} {platform.release()}")
        
        # Информация о CPU
        cpu_usage = psutil.cpu_percent(interval=1)
        cpu_count = psutil.cpu_count(logical=False)
        cpu_logical_count = psutil.cpu_count(logical=True)
        embed.add_field(name="Использование CPU (%)", value=f"{cpu_usage}%")
        embed.add_field(name="Количество физических ядер", value=cpu_count)
        embed.add_field(name="Количество логических ядер", value=cpu_logical_count)
        
        # Информация о памяти
        memory = psutil.virtual_memory()
        total_memory = round(memory.total / (1024 ** 3), 2)
        used_memory = round(memory.used / (1024 ** 3), 2)
        available_memory = round(memory.available / (1024 ** 3), 2)
        embed.add_field(name="Общий объем памяти (GB)", value=total_memory)
        embed.add_field(name="Использовано памяти (GB)", value=used_memory)
        embed.add_field(name="Доступно памяти (GB)", value=available_memory)
        
        # Информация о диске
        disk = psutil.disk_usage('/')
        total_disk_space = round(disk.total / (1024 ** 3), 2)
        used_disk_space = round(disk.used / (1024 ** 3), 2)
        free_disk_space = round(disk.free / (1024 ** 3), 2)
        embed.add_field(name="Общий объем диска (GB)", value=total_disk_space)
        embed.add_field(name="Использовано диска (GB)", value=used_disk_space)
        embed.add_field(name="Доступно диска (GB)", value=free_disk_space)
        
        # Кластер и другие характеристики могут быть добавлены по вашему желанию
        
        await ctx.send(embed=embed)

def setup(bot):
    bot.add_cog(Host(bot))
