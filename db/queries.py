from db import User, Schedule, Lesson, Group
from sqlalchemy import select
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


async def update_group(session, telegram_id, group_id):
    user = await session.get(User, telegram_id)
    user.group = group_id
    await session.commit()


async def get_group(session, telegram_id):
    user = await session.get(User, telegram_id)
    return user.group


async def get_groups(session):
    stmt = select(Group.id, Group.name).select_from(Group)
    result = await session.execute(stmt)
    return '\n'.join([f'{group.id}-{group.name}' for group in result])


async def get_lessons(session, telegram_id, type_of_week, day):
    types_of_week = {'numerator': 1, 'denominator': 2}
    group = await get_group(session, telegram_id)
    s = aliased(Schedule)
    ls = aliased(Lesson)
    tables = join(Schedule, Lesson, Schedule.lesson_id == Lesson.id)
    query = (select(s.number_of_lesson, s.audience, ls.name).select_from(tables).
             where(s.group == group, s.day == days[day[1:]],
                   s.type.in_([types_of_week[type_of_week], None]))
             .order_by(s.number_of_lesson))
    result = await session.execute(query)
    return result.all()
