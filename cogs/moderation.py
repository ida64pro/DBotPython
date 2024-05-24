import disnake
from disnake.ext import commands
from collections import defaultdict
from datetime import datetime, timedelta

class ModerationCog(commands.Cog):

    def __init__(self, bot):
        self.bot = bot
        self.user_infractions = defaultdict(int)
        self.allowed_domains = ['media.discordapp.net', 'tenor.com', 'imgur.com']
        self.exempt_role_id = 1237479690114175006  # ID роли, которую нужно исключить

    @commands.Cog.listener()
    async def on_message(self, message):

        if message.author.bot:
            return

        # Проверяем, есть ли у пользователя исключенная роль
        if self.exempt_role_id in [role.id for role in message.author.roles]:
            return

        if any(url in message.content for url in ('http://', 'https://')):
            if any(domain in message.content for domain in self.allowed_domains):
                return
            self.user_infractions[message.author.id] += 1
            await message.delete()
            embed = disnake.Embed(
                title=f"Не нарушайте!, {message.author.display_name}!",
                description=
                f"Уважаемый {message.author.mention}, пожалуйста, не отправляйте ссылки здесь. Это ваше предупреждение номер {self.user_infractions[message.author.id]}.",
                color=0x000000)
            await message.channel.send(embed=embed, delete_after=10)
            if self.user_infractions[message.author.id] >= 3:
                until = datetime.now() + timedelta(hours=1)
                await message.author.timeout(until=until, reason="3 infractions")
                embed = disnake.Embed(
                    title=f"Вы получили тайм-аут, {message.author.display_name}!",
                    description=
                    f"Уважаемый {message.author.mention}, вы получили тайм-аут на 1 час за нарушения.",
                    color=0x000000)
                await message.channel.send(embed=embed, delete_after=10)
                self.user_infractions[message.author.id] = 0
            return

        domains = ['.com', '.net', '.ng', '.xyz', '.gg', '.fun', '.ru']
        if any(domain in message.content for domain in domains):
            if any(allowed_domain in domains for allowed_domain in self.allowed_domains):
                return
            self.user_infractions[message.author.id] += 1
            await message.delete()
            embed = disnake.Embed(
                title=f"Не нарушайте!, {message.author.display_name}!",
                description=
                f"Уважаемый {message.author.mention}, пожалуйста, не отправляйте сообщения, содержащие эти домены. Это ваше предупреждение номер {self.user_infractions[message.author.id]}.",
                color=0x000000)
            await message.channel.send(embed=embed, delete_after=10)
            if self.user_infractions[message.author.id] >= 3:
                until = datetime.now() + timedelta(hours=1)
                await message.author.timeout(until=until, reason="3 infractions")
                embed = disnake.Embed(
                    title=f"Вы получили тайм-аут, {message.author.display_name}!",
                    description=
                    f"Уважаемый {message.author.mention}, вы получили тайм-аут на 1 час за нарушения.",
                    color=0x000000)
                await message.channel.send(embed=embed, delete_after=10)
                self.user_infractions[message.author.id] = 0
            return

        if len(message.content) > 500:
            self.user_infractions[message.author.id] += 1
            await message.delete()
            embed = disnake.Embed(
                title=f"Не нарушайте!, {message.author.display_name}!",
                description=
                f"Уважаемый {message.author.mention}, пожалуйста, не отправляйте такие длинные сообщения. Это ваше предупреждение номер {self.user_infractions[message.author.id]}.",
                color=0x000000)
            await message.channel.send(embed=embed, delete_after=10)
            if self.user_infractions[message.author.id] >= 3:
                until = datetime.now() + timedelta(hours=1)
                await message.author.timeout(until=until, reason="3 infractions")
                embed = disnake.Embed(
                    title=f"Вы получили тайм-аут, {message.author.display_name}!",
                    description=
                    f"Уважаемый {message.author.mention}, вы получили тайм-аут на 1 час за нарушения.",
                    color=0x000000)
                await message.channel.send(embed=embed, delete_after=10)
                self.user_infractions[message.author.id] = 0
            return


def setup(bot):
    bot.add_cog(ModerationCog(bot))
