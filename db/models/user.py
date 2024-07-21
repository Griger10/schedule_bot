import enum
from db.base import Base
from sqlalchemy import BigInteger
from sqlalchemy.orm import Mapped, mapped_column


class Groups(enum.Enum):
    IP123 = 1
    IP223 = 2


class User(Base):
    __tablename__ = 'users'

    id: Mapped[int] = mapped_column(BigInteger, primary_key=True)
    first_name: Mapped[str]
    last_name: Mapped[str | None]
    group: Mapped[Groups | int | None]

