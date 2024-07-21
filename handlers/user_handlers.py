from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from keyboards.keyboards import build_command_keyboard
from lexicon.lexicon import LEXICON

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer(text=LEXICON['start'])


@router.message(Command(commands=['help']))
async def help_handler(message: Message):
    await message.answer(text=LEXICON['help'])


@router.message(Command(commands=['monday']))
async def monday_handler(message: Message):
    await message.answer(text='Выберите тип недели',
                         reply_markup=build_command_keyboard
                         ('monday-numerator',
                          'monday-denominator')
                         )


@router.message(Command(commands=['tuesday']))
async def tuesday_handler(message: Message):
    await message.answer(text='Выберите тип недели',
                         reply_markup=build_command_keyboard
                         ('tuesday-numerator',
                          'tuesday-denominator')
                         )


@router.message(Command(commands=['wednesday']))
async def tuesday_handler(message: Message):
    await message.answer(text='Выберите тип недели',
                         reply_markup=build_command_keyboard
                         ('wednesday-numerator',
                          'wednesday-denominator')
                         )


@router.message(Command(commands=['thursday']))
async def tuesday_handler(message: Message):
    await message.answer(text='Выберите тип недели',
                         reply_markup=build_command_keyboard
                         ('thursday-numerator',
                          'thursday-denominator')
                         )


@router.message(Command(commands=['tuesday']))
async def tuesday_handler(message: Message):
    await message.answer(text='Выберите тип недели',
                         reply_markup=build_command_keyboard
                         ('tuesday-numerator',
                          'tuesday-denominator')
                         )


@router.callback_query(F.data.startswith('monday'))
async def monday_schedule_handler(callback_query: CallbackQuery):
    if callback_query.data == 'monday-numerator':
        await callback_query.message.edit_text(text='Это расписание на понедельник числительный')
    else:
        await callback_query.message.edit_text(text='Это расписание на понедельник знаменательный')


@router.callback_query(F.data.startswith('tuesday'))
async def monday_schedule_handler(callback_query: CallbackQuery):
    if callback_query.data == 'tuesday-numerator':
        await callback_query.message.edit_text(text='Это расписание на вторник числительный')
    else:
        await callback_query.message.edit_text(text='Это расписание на вторник знаменательный')


@router.callback_query(F.data.startswith('wednesday'))
async def monday_schedule_handler(callback_query: CallbackQuery):
    if callback_query.data == 'wednesday-numerator':
        await callback_query.message.edit_text(text='Это расписание на среду числительную')
    else:
        await callback_query.message.edit_text(text='Это расписание на среду знаменательную')


@router.callback_query(F.data.startswith('thursday'))
async def monday_schedule_handler(callback_query: CallbackQuery):
    if callback_query.data == 'thursday-numerator':
        await callback_query.message.edit_text(text='Это расписание на четверг числительный')
    else:
        await callback_query.message.edit_text(text='Это расписание на четверг знаменательный')


@router.callback_query(F.data.startswith('friday'))
async def monday_schedule_handler(callback_query: CallbackQuery):
    if callback_query.data == 'friday-numerator':
        await callback_query.message.edit_text(text='Это расписание на пятницу числительную')
    else:
        await callback_query.message.edit_text(text='Это расписание на пятницу знаменательную')
