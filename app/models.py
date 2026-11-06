from sqlalchemy  import Integer, String, Boolean
from sqlalchemy.orm import DeclarativeBase, Mapped, mapped_column

class Base(DeclarativeBase):
    pass

class User(Base):

    __tablename__ = "Users"

    id: Mapped [int] = mapped_column(
        primary_key =True, index=True
    )

    student_id: Mapped[str] = mapped_column(
        String(7), unique=True, nullable=False
    )

    equipment_id: Mapped[int] = mapped_column(
        Integer, unique=True, nullable=False
    )

    description: Mapped[str] = mapped_column(
        String, unique=True, nullable=False
    )