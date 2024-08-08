from aiogram.types import BotCommand
from fluentogram import TranslatorRunner
from lexicon.lexicon import LEXICON_COMMANDS

days = ('monday', 'tuesday', 'wednesday', 'thursday', 'friday')


async def set_main_menu(bot, i18n: TranslatorRunner):
    main_menu_commands = [
        BotCommand(command='/monday', description=i18n.monday.monday()),
        BotCommand(command='/tuesday', description=i18n.tuesday.tuesday()),
        BotCommand(command='/wednesday', description=i18n.wednesday.wednesday()),
        BotCommand(command='/thursday', description=i18n.thursday.thursday()),
        BotCommand(command='/friday', description=i18n.friday.friday())
    ]
    await bot.set_my_commands(main_menu_commands)
