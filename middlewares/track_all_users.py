from typing import cast
from aiogram import BaseMiddleware
from aiogram.types import Message
from cachetools import TTLCache
from sqlalchemy.ext.asyncio import AsyncSession

from db.queries import upsert_user


class TrackAllUsersMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()
        self.cache = TTLCache(
            maxsize=1000,
            ttl=60 * 60 * 24,  # 6 часов
        )

    async def __call__(self, handler, event, data, ):
        event = cast(Message, event)
        user_id = event.message.from_user.id

        if user_id not in self.cache:
            session: AsyncSession = data["session"]
            await upsert_user(
                session=session,
                telegram_id=event.from_user.id,
                first_name=event.from_user.first_name
            )
            self.cache[user_id] = None

        return await handler(event, data)
