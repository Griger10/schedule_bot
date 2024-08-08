from aiogram import Router
from aiogram.types import Message
from fluentogram import TranslatorRunner

router = Router()


@router.message()
async def process_other_answer(message: Message, i18n: TranslatorRunner):
    await message.answer(text=i18n.no.answer())
