from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from db.models import lesson
from db.queries import update_group, get_lessons
from keyboards.keyboards import build_command_keyboard
from lexicon.lexicon import LEXICON

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(text=LEXICON['start'])


@router.message(Command(commands=['help']))
async def help_handler(message: Message):
    await message.answer(text=LEXICON['help'])


@router.message(Command(commands=['monday', 'tuesday', 'wednesday', 'thursday', 'friday']))
async def day_handler(message: Message, session):
    await message.answer(text='Выберите тип недели',
                         reply_markup=build_command_keyboard
                         (f'{message.text}-numerator',
                          f'{message.text}-denominator')
                         )


@router.callback_query(F.data.endswith('numerator') | F.data.endswith('denominator'))
async def schedule_handler(callback_query: CallbackQuery, session):
    day = callback_query.data.split('-')[0]

    if callback_query.data.endswith('numerator'):
        lessons_data = await get_lessons(session, callback_query.from_user.id, 'numerator', day)

    else:
        lessons_data = await get_lessons(session, callback_query.from_user.id, 'denominator', day)

    result = '\n'.join(f'{item[0]} - {item[2]} - {item[1]}' for item in lessons_data)
    await callback_query.answer('Расписание на день:\n\n' + result)


@router.message(Command(commands=['set_group']))
async def set_group_handler(message: Message, session):
    await update_group(session, message.from_user.id, message.text.split()[1])
    await message.answer('Ваша группа успешно установлена!')


