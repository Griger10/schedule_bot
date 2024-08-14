from db import User, Schedule, Lesson, Group
from sqlalchemy import select, cast, Integer, delete, true, or_
from sqlalchemy.dialects.postgresql import insert as upsert
from sqlalchemy.orm import aliased, join

days = {
    'monday': 1, 'tuesday': 2,
    'wednesday': 3, 'thursday': 4,
    'friday': 5
}


async def upsert_user(session, user_id, first_name, group=None):
    stmt = upsert(User).values(id=user_id,
                               first_name=first_name,
                               group=group)
    stmt.on_conflict_do_update(index_elements=['telegram_id'],
                               set_={'first_name': first_name})

    await session.execute(stmt)
    await session.commit()


async def update_group(session, telegram_id, group_name):
    user = await session.get(User, telegram_id)
    stmt = select(Group.id).select_from(Group).where(Group.name == group_name)
    result = await session.execute(stmt)  # тип ChunkedIteratorResult
    user.group = next(result)[0]
    await session.commit()


async def get_group(session, telegram_id):
    user = await session.get(User, telegram_id)
    return user.group


async def get_groups(session):
    stmt = select(Group.id, Group.name).select_from(Group)
    result = await session.execute(stmt)
    return '\n\n'.join([f'{group.name}' for group in result])


async def get_lessons(session, telegram_id, type_of_week, day):
    types_of_week = {'numerator': 1, 'denominator': 2}
    group = await get_group(session, telegram_id)
    s = aliased(Schedule)
    ls = aliased(Lesson)
    tables = join(ls, s, s.lesson_id == ls.id)
    query = (select(s.number_of_lesson, s.audience, ls.name).select_from(tables).
             where(s.group == group, s.day == days[day[1:]],
                   or_(s.type.is_(None), s.type == types_of_week[type_of_week]))
             .order_by(s.number_of_lesson)).distinct()
    print(query)
    result = await session.execute(query)
    return result.all()


async def add_group(session, group_name):
    stmt = upsert(Group).values(name=group_name.lower())
    await session.execute(stmt)
    await session.commit()


async def add_lesson(session, lesson_name):
    stmt = upsert(Lesson).values(name=lesson_name.lower())
    await session.execute(stmt)
    await session.commit()


async def delete_lesson(session, lesson_name):
    stmt = delete(Lesson).where(Lesson.name == lesson_name.lower())
    await session.execute(stmt)
    await session.commit()
