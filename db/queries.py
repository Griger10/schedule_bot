from db import User, Schedule, Lesson
from sqlalchemy import select
from sqlalchemy.dialects.postgresql import insert as upsert
from sqlalchemy.orm import aliased


async def upsert_user(session, telegram_id, first_name, group=None):
    stmt = upsert(User).values(telegram_id=telegram_id,
                               first_name=first_name,
                               group=group)
    stmt.on_conflict_do_update(index_elements=['telegram_id'],
                               set_={'first_name': first_name})

    await session.execute(stmt)
    await session.commit()


async def update_group(session, telegram_id, group_id):
    user = await session.get(User, {'telegram_id': telegram_id})
    user.group = group_id
    await session.commit()


async def get_group(session, telegram_id):
    user = await session.get(User, {'telegram_id': telegram_id})
    return user.group


async def get_lessons(session, telegram_id, type_of_week):
    group = await get_group(session, telegram_id)
    s = aliased(Schedule)
    ls = aliased(Lesson)
    query = (select(s.number_of_lesson, s.audience, ls.name).join(ls, ls.id == s.lesson_id).
             where(s.group == group, s.type.in_([type_of_week, None]))
             .order_by(s.number_of_lesson))
    result = await session.execute(query)
    return result.all()
