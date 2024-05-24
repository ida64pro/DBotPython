import disnake
from disnake.ext import commands

class ServerInfo(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(name="сервер", description="Информация о сервере")
    async def server_info(self, inter):
        guild = inter.guild

        # Информация об овнере сервера
        owner = guild.owner

        # Подсчет участников в голосовых каналах
        voice_members = sum(1 for member in guild.members if member.voice)

        # Подсчет текстовых и голосовых каналов
        text_channels = len(guild.text_channels)
        voice_channels = len(guild.voice_channels)

        # Подсчет количества ролей
        num_roles = len(guild.roles)

        # Формирование ответа в виде эмбеда
        embed = disnake.Embed(title=f"Информация о гильдии - {guild.name}", color=inter.author.color)
        embed.add_field(name="Владелец", value=owner.mention)
        embed.add_field(name="Количество пользователей", value=guild.member_count)
        embed.add_field(name="Количество участников в голосовых каналах", value=voice_members)
        embed.add_field(name="Текстовые каналы", value=text_channels)
        embed.add_field(name="Голосовые каналы", value=voice_channels)
        embed.add_field(name="Количество ролей", value=num_roles)

        # Добавление аватарки сервера
        if guild.icon:
            embed.set_thumbnail(url=guild.icon_url)

        # Добавление большого баннера (если есть)
        if guild.banner:
            embed.set_image(url=guild.banner_url)

        await inter.response.send_message(embed=embed)

def setup(bot):
    bot.add_cog(ServerInfo(bot))