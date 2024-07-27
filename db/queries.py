from db import User
from sqlalchemy.dialects.postgresql import insert as upsert


async def upsert_user(session, telegram_id, first_name, group):
    stmt = upsert(User).values(telegram_id=telegram_id,
                               first_name=first_name,
                               group=group)
    stmt.
