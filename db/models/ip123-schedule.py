from db.base import Base
from sqlalchemy.orm import Mapped, mapped_column


class Schedule(Base):
    __tablename__ = 'ip123-schedule'

    id: Mapped[int] = mapped_column(primary_key=True)
    day: Mapped[int]
    number_of_lesson: Mapped[int]

