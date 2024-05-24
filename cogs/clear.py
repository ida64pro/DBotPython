import disnake
from disnake.ext import commands

class Clear(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command()
    async def clear(self, interaction, amount: int):
        # Получаем объект роли администратора по её ID
        admin_role = interaction.guild.get_role(1230566356366262432)  # Замените ROLE_ID_HERE на фактический ID роли администратора

        # Проверяем, имеет ли участник роль администратора
        if admin_role in interaction.author.roles:
            # Если имеет, продолжаем выполнение команды
            embed = disnake.Embed(title="Очистка", description=f"Вы удалили {amount} сообщений.", color=0x00ff00)
            embed.set_thumbnail(url=self.bot.user.avatar.url)
            await interaction.response.send_message(embed=embed, ephemeral=True)
            await interaction.channel.purge(limit=amount + 1)
        else:
            # Если не имеет, отправляем сообщение об ошибке
            await interaction.response.send_message("У вас нет прав для выполнения этой команды.", ephemeral=True)

def setup(bot):
    bot.add_cog(Clear(bot))