from aiogram.types import BotCommand
from lexicon.lexicon import LEXICON_COMMANDS


async def set_main_menu(bot):
    main_menu_commands = [BotCommand(command=command, description=text) for command, text in LEXICON_COMMANDS.items()]
    await bot.set_my_commands(main_menu_commands)
