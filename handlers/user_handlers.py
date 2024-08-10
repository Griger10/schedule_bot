import logging
from aiogram import Router, F, Bot
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery
from db.queries import update_group, get_lessons, get_groups
from fluentogram import TranslatorRunner
from keyboards.keyboards import build_command_keyboard
from keyboards.main_menu import set_main_menu
from sqlalchemy.ext.asyncio import AsyncSession
from utils.utils import formatter

router = Router()

logger = logging.getLogger(__name__)


@router.message(CommandStart())
async def start_handler(message: Message, i18n: TranslatorRunner, bot: Bot):
    try:
        username = message.from_user.full_name
        await set_main_menu(bot, i18n)
        await message.answer(text=i18n.start.start(username=username))

    except Exception as e:
        logger.error('Error while processing start command', exc_info=e)


@router.message(Command(commands=['help']))
async def help_handler(message: Message, session, i18n: TranslatorRunner):
    try:
        groups = await get_groups(session)
        await message.answer(text=i18n.help.full() + '\n\n' + groups + '\n\n' + i18n.example.example())

    except Exception as e:
        logger.error('Error while processing help command', exc_info=e)


@router.message(Command(commands=['monday', 'tuesday', 'wednesday', 'thursday', 'friday']))
async def day_handler(message: Message, i18n: TranslatorRunner):
    try:
        await message.answer(text=i18n.choose.week(),
                             reply_markup=build_command_keyboard
                             (numerator=i18n.numerator.numerator(),
                              denominator=i18n.denominator.denominator(),
                              data_first=f'{message.text}-numerator',
                              data_second=f'{message.text}-denominator')
                             )
    except Exception as e:
        logger.error('Error while processing day command', exc_info=e)


@router.callback_query(F.data.endswith('numerator') | F.data.endswith('denominator'))
async def schedule_handler(callback_query: CallbackQuery, session: AsyncSession, i18n: TranslatorRunner):
    try:
        day = callback_query.data.split('-')[0]
        type_of_week = callback_query.data.split('-')[1]

        lessons_data = await get_lessons(session, callback_query.from_user.id, type_of_week, day)

        result = await formatter(lessons_data)

        await callback_query.message.edit_text(i18n.day.schedule() + '\n\n' + result)

        await callback_query.answer()

    except Exception as e:
        await callback_query.message.edit_text(i18n.day.failure())
        logger.error('Error while processing schedule command', exc_info=e)


@router.message(Command(commands=['set_group']))
async def set_group_handler(message: Message, session: AsyncSession, i18n: TranslatorRunner):
    try:
        await update_group(session, message.from_user.id, message.text.split()[1])
        await message.answer(i18n.group.success())
    except Exception as e:
        logger.error('Error while processing set_group command', exc_info=e)
