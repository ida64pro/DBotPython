import disnake
from disnake.ext import commands
import shutil
import os
import asyncio


class BackupCog(commands.Cog):
    def __init__(self, bot):
        self.guild = None
        self.author = None
        self.bot = bot

    @commands.command(name='backup', aliases=['bu'])
    async def archive_folder(self, ctx):
        author = ctx.author
        role = disnake.utils.get(ctx.guild.roles, id=1242201679353483446)
        if role in author.roles:
            folder_path = "./"
            os.mkdir('./backup')
            archive_path = "./backup"
            try:
                shutil.make_archive(archive_path, 'zip', folder_path)
            except:
                await author.send('Произошла ошибка при создании архива.')
                return

            try:
                await author.send(file=disnake.File('./backup.zip'))
            except disnake.HTTPException:
                await author.send(
                    "Не удалось отправить архив в личные сообщения. Пожалуйста, убедитесь, что у вас открыты личные сообщения от бота.",
                    ephemeral=True)
                return

            embedEdit = disnake.Embed()
            embedEdit.add_field(name='**Успешно!**  ', value='Архив собран и отправлен Вам.', inline=True)
            await author.send(embed=embedEdit)
            os.remove('./backup.zip')
            os.remove('./backup')
        else:
            await author.send("Роль не найдена!", ephemeral=True)
            return


def setup(bot):
    bot.add_cog(BackupCog(bot))
