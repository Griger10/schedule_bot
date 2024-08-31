from aiogram.types import BotCommand
from fluentogram import TranslatorRunner


async def set_main_menu(bot, i18n: TranslatorRunner):
    main_menu_commands = [
        BotCommand(command='/monday', description=str(i18n.monday.monday())),
        BotCommand(command='/tuesday', description=str(i18n.tuesday.tuesday())),
        BotCommand(command='/wednesday', description=str(i18n.wednesday.wednesday())),
        BotCommand(command='/thursday', description=str(i18n.thursday.thursday())),
        BotCommand(command='/friday', description=str(i18n.friday.friday())),
        BotCommand(command='/set_group', description=str(i18n.set.group())),
        BotCommand(command='/help', description=str(i18n.help.short()))
    ]
    await bot.set_my_commands(main_menu_commands)
