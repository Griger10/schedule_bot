import enum

from db.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Schedule(Base):
    __tablename__ = 'schedule'

    id: Mapped[int] = mapped_column(primary_key=True)
    day: Mapped[int]
    number_of_lesson: Mapped[int]
    audience: Mapped[str]
    lesson_id: Mapped[int] = mapped_column(ForeignKey("lessons.id"))
    type: Mapped[int | None] = mapped_column(nullable=True)
    group: Mapped[int] = mapped_column(ForeignKey("groups.id"))
