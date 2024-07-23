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


@router.message(Command(commands=['monday', 'tuesday', 'wednesday', 'thursday', 'friday']))
async def day_handler(message: Message):
    await message.answer(text='Выберите тип недели',
                         reply_markup=build_command_keyboard
                         (f'{message.text}-numerator',
                          f'{message.text}-denominator')
                         )


@router.callback_query(F.data.endswith('numerator') | F.data.endswith('denominator'))
async def schedule_handler(callback_query: CallbackQuery):
    await callback_query.message.edit_text(text=f'Это расписание на {callback_query.message.split('-')[0]}')


