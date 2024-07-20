from aiogram import Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, User
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
    await message.answer(text='Выберите тип недели')
