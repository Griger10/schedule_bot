from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from db.models import lesson
from db.queries import update_group, get_lessons, get_groups
from fluentogram import TranslatorRunner
from keyboards.keyboards import build_command_keyboard
from keyboards.main_menu import set_main_menu
from lexicon.lexicon import LEXICON

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message, i18n: TranslatorRunner):
    username = message.from_user.full_name
    await set_main_menu()
    await message.answer(text=i18n.start.start(username=username))


@router.message(Command(commands=['help']))
async def help_handler(message: Message, session, i18n: TranslatorRunner):
    groups = await get_groups(session)
    await message.answer(text=i18n.help.full() + groups + '\n\n' + i18n.example.example())


@router.message(Command(commands=['monday', 'tuesday', 'wednesday', 'thursday', 'friday']))
async def day_handler(message: Message, session, i18n: TranslatorRunner):
    await message.answer(text=i18n.choose.week(),
                         reply_markup=build_command_keyboard
                         (numerator=i18n.numerator.numerator(),
                          denominator=i18n.denominator.denominator(),
                          data_first=f'{message.text}-numerator',
                          data_second=f'{message.text}-denominator')
                         )


@router.callback_query(F.data.endswith('numerator') | F.data.endswith('denominator'))
async def schedule_handler(callback_query: CallbackQuery, session, i18n: TranslatorRunner):
    day = callback_query.data.split('-')[0]

    if callback_query.data.endswith('numerator'):
        lessons_data = await get_lessons(session, callback_query.from_user.id, 'numerator', day)
    else:
        lessons_data = await get_lessons(session, callback_query.from_user.id, 'denominator', day)

    result = '\n'.join(f'{item[0]} - {item[2]} - {item[1]}' for item in lessons_data)
    await callback_query.message.edit_text(i18n.day.schedule() + '\n\n' + result)


@router.message(Command(commands=['set_group']))
async def set_group_handler(message: Message, session, i18n: TranslatorRunner):
    await update_group(session, message.from_user.id, message.text.split()[1])
    await message.answer(i18n.group.success())





