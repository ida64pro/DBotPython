import disnake
from disnake.ext import commands, tasks
import datetime
import pytz  # Импортируем модуль pytz для работы с часовыми поясами

class StatusCog(commands.Cog):
    def __init__(self, bot):
        self.bot = bot
        self.update_status.start()  # Запускаем задачу автоматически при загрузке Cog

    def cog_unload(self):
        self.update_status.cancel()  # Отменяем задачу при выгрузке Cog

    @tasks.loop(seconds=60)  # Задаем интервал выполнения задачи (здесь каждую минуту)
    async def update_status(self):
        guild = self.bot.get_guild(1237477778597744743)  # Замените GUILD_ID на ID вашего сервера

        if guild:
            members_count = len(guild.members)
            voice_members_count = sum(1 for member in guild.members if member.voice)

            # Получаем текущее время по Московскому часовому поясу
            msk_timezone = pytz.timezone('Europe/Moscow')
            msk_time = datetime.datetime.now(msk_timezone)

            # Формируем строку для статуса бота
            new_state = f'👥: {members_count} | 🔊: {voice_members_count} | {msk_time.strftime("%H:%M")} МСК'

            activity = disnake.Activity(
                type=disnake.ActivityType.custom,
                name='Я  <',
                state=new_state
            )

            await self.bot.change_presence(activity=activity)

    @update_status.before_loop
    async def before_update_status(self):
        await self.bot.wait_until_ready()  # Ждем, пока бот полностью подключится к Discord

    @commands.Cog.listener()
    async def on_member_join(self, member):
        await self.update_status()  # Вызываем обновление статуса при присоединении нового участника

    @commands.Cog.listener()
    async def on_member_remove(self, member):
        await self.update_status()  # Вызываем обновление статуса при выходе участника

    @commands.Cog.listener()
    async def on_voice_state_update(self, member, before, after):
        # Проверяем, произошло ли изменение состояния голосового чата (вход или выход из канала)
        if before.channel != after.channel:
            await self.update_status()  # Вызываем обновление статуса при изменении состояния голосового чата

def setup(bot):
    bot.add_cog(StatusCog(bot))
