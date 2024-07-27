import enum

from db.base import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship


class Days(enum.Enum):
    MONDAY = 1
    TUESDAY = 2
    WEDNESDAY = 3
    THURSDAY = 4
    FRIDAY = 5


class LessonTypes(enum.Enum):
    NUMERATOR = 1
    DENOMINATOR = 2


class LessonNumbers(enum.Enum):
    FIRST = 1
    SECOND = 2
    THIRD = 3
    FOURTH = 4
    FIFTH = 5


class Schedule(Base):
    __tablename__ = 'schedule'

    id: Mapped[int] = mapped_column(primary_key=True)
    day: Mapped[Days]
    number_of_lesson: Mapped[LessonNumbers]
    audience: Mapped[str]
    lesson_id: Mapped[int] = mapped_column(ForeignKey("lesson.id"))
    type: Mapped[LessonTypes | None] = mapped_column(nullable=True)



