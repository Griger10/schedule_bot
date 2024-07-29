from db import Base
from sqlalchemy import Integer
from sqlalchemy.orm import Mapped, mapped_column


class Group(Base):
    __tablename__ = 'groups'

    id: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str]