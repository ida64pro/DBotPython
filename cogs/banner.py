import disnake
from disnake.ext import commands

class BannerCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot

    @commands.slash_command(description='Баннер пользователя')
    async def banner(self, interaction, member: disnake.Member):

        user = await self.bot.fetch_user(member.id)
        embed = disnake.Embed(
            title='Баннер', color=disnake.Colour.from_rgb(43, 45, 49)
        )
        try:
            embed.set_image(url=user.banner.with_size(2048))
            await interaction.response.send_message(embed=embed)
        except:
            fembed = disnake.Embed(
                title='Ошибка', description='У выбранного пользователя нет баннера',
                color=disnake.Colour.from_rgb(43, 45, 49)
            )
            await interaction.response.send_message(embed=fembed, ephemeral=True)

def setup(bot):
    bot.add_cog(BannerCog(bot))