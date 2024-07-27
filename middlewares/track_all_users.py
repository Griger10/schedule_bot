from typing import cast
from aiogram import BaseMiddleware
from aiogram.types import Message
from sqlalchemy.ext.asyncio import AsyncSession

from db.queries import upsert_user


class TrackAllUsersMiddleware(BaseMiddleware):
    def __init__(self):
        super().__init__()

    async def __call__(self, handler, event, data, ):
        event = cast(Message, event)
        session: AsyncSession = data["session"]
        try:
            await upsert_user(
                session=session,
                telegram_id=event.from_user.id,
                first_name=event.from_user.first_name,
                group=None,
                )
        except Exception as e:
            print(e)

        return await handler(event, data)
