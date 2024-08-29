import asyncio
import sys
import logging.config
import yaml
from aiogram import Bot, Dispatcher
from db import Base
from middlewares import DatabaseMiddleware, TrackAllUsersMiddleware
from middlewares.i18n import TranslatorRunnerMiddleware
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from read_config import get_config, BotConfig, DbConfig
from handlers import user_handlers, other_handlers, admin_handlers
from utils.i18n import create_translator_hub

with open('logging_config.yaml', 'rt') as f:
    config = yaml.safe_load(f.read())

logging.config.dictConfig(config)


async def main():
    try:
        db_config = get_config(DbConfig, 'db')

        bot_config = get_config(BotConfig, "bot")

        engine = create_async_engine(url=str(db_config.dsn), echo=db_config.is_echo)

        async with engine.begin() as connection:
            await connection.execute(text('SELECT 1'))

        session_maker = async_sessionmaker(engine, expire_on_commit=False)
        translator_hub = create_translator_hub()
        bot = Bot(token=bot_config.token.get_secret_value(), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
        dp = Dispatcher(admin_id=bot_config.admin_id)

        dp.update.outer_middleware(DatabaseMiddleware(session_maker))
        dp.update.middleware(TranslatorRunnerMiddleware())
        dp.message.outer_middleware(TrackAllUsersMiddleware())

        dp.include_router(admin_handlers.router)
        dp.include_router(user_handlers.router)
        dp.include_router(other_handlers.router)

        print('start polling...')
        await dp.start_polling(bot, _translator_hub=translator_hub)

    except Exception as e:
        print('Exception occurred: {}'.format(e))


if __name__ == '__main__':
    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    asyncio.run(main())
