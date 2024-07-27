import asyncio
from aiogram import Bot, Dispatcher
from db import Base
from middlewares import DatabaseMiddleware, TrackAllUsersMiddleware
from sqlalchemy import text
from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker
from aiogram.client.default import DefaultBotProperties
from aiogram.enums import ParseMode
from keyboards.main_menu import set_main_menu
from read_config import get_config, BotConfig, DbConfig
from handlers import user_handlers, other_handlers


async def main():
    db_config = get_config(DbConfig, 'db')

    bot_config = get_config(BotConfig, "bot")

    engine = create_async_engine(url=db_config.url.dsn, echo=db_config.is_echo)

    async with engine.begin() as connection:
        await connection.execute(text('SELECT 1'))

    async with engine.begin() as connection:
        await connection.run_sync(Base.metadata.create_all)

    session_maker = async_sessionmaker(engine, expire_on_commit=False)

    bot = Bot(token=bot_config.token.get_secret_value(), default=DefaultBotProperties(parse_mode=ParseMode.HTML))
    dp = Dispatcher()

    dp.update.outer_middleware(DatabaseMiddleware(session_maker))
    dp.message.outer_middleware(TrackAllUsersMiddleware())

    await set_main_menu(bot)

    dp.include_router(user_handlers.router)
    dp.include_router(other_handlers.router)

    await bot.delete_webhook(drop_pending_updates=True)
    print('start polling...')
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
