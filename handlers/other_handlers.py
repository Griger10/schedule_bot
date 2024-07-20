from aiogram import Router
from aiogram.types import Message

router = Router()


@router.message()
async def process_other_answer(message: Message):
    await message.answer('Бот не знает такой команды :(')
