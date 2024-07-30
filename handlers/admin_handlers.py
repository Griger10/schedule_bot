from aiogram import Router, F
from aiogram.filters import MagicData, Command
from aiogram.types import Message
from lexicon.lexicon import ADMIN_LEXICON

router = Router(name='admin_handlers')

router.message.filter(MagicData(F.event.chat.id == F.admin_id))


@router.message(Command(commands=['admin']))
async def admin_handler(message: Message):
    await message.answer(ADMIN_LEXICON['admin'])


@router.message(Command(commands=['add_group']))
async def add_group_handler(message: Message):
    elements = message.text.split()
    group_name = elements[1]
    await add_group(group_name)
    await message.answer('Группа успешно добавлена в БД!')
