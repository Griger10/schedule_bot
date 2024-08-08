from aiogram import Router, F
from aiogram.filters import MagicData, Command
from aiogram.types import Message
from db.queries import add_group, add_lesson, delete_lesson
from fluentogram import TranslatorRunner
from sqlalchemy.ext.asyncio import AsyncSession

router = Router(name='admin_handlers')

router.message.filter(MagicData(F.event.chat.id == F.admin_id))


@router.message(Command(commands=['admin']))
async def admin_handler(message: Message, i18n: TranslatorRunner):
    await message.answer(i18n.admin.admin())


@router.message(Command(commands=['add_group']))
async def add_group_handler(message: Message, session: AsyncSession, i18n: TranslatorRunner):
    elements = message.text.split()
    group_name = elements[1]
    await add_group(session, group_name)
    await message.answer(i18n.group.added(group=group_name))


@router.message(Command(commands=['add_lesson']))
async def add_lesson_handler(message: Message, session: AsyncSession, i18n: TranslatorRunner):
    lesson_name = message.text.split()[1].strip()
    await add_lesson(session, lesson_name)
    await message.answer(i18n.lesson.added(lesson=lesson_name))


@router.message(Command(commands=['delete_lesson']))
async def delete_lesson_handler(message: Message, session: AsyncSession, i18n: TranslatorRunner):
    lesson_name = message.text.split()[1].strip()
    await delete_lesson(session, lesson_name)
    await message.answer(i18n.lesson.deleted(lesson=lesson_name))
