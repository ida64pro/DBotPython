import disnake
from disnake.ext import commands, tasks

class Statsboost(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.boost_count = 0

    @tasks.loop(seconds=10)
    async def update_boost_count(self):
        guild = self.bot.get_guild(1237477778597744743)  # ID вашего сервера
        if guild:
            if self.boost_count != guild.premium_subscription_count:
                self.boost_count = guild.premium_subscription_count
                channel = self.bot.get_channel(1240753384990970006)  # ID канала, который будет изменяться
                if channel:
                    await channel.edit(name=f'🚀 - Бусты: {guild.premium_subscription_count}')

    @commands.Cog.listener()
    async def on_ready(self):
        self.update_boost_count.start()

    def cog_unload(self):
        self.update_boost_count.cancel()

class Statistic(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.count = 0

    @tasks.loop(seconds=10)
    async def update_member_count(self):
        guild = self.bot.get_guild(1237477778597744743)  # ID сервера
        if self.count != guild.member_count:
            self.count = guild.member_count
            channel = self.bot.get_channel(1240753406222667896)  # ID канала, у которого будет меняться название
            await channel.edit(name=f'👥 - Участники: {guild.member_count}')

    @commands.Cog.listener()
    async def on_ready(self):
        self.update_member_count.start()


def setup(bot):
    bot.add_cog(Statsboost(bot))
    bot.add_cog(Statistic(bot))