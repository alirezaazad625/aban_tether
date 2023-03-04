from sqlalchemy import FLOAT
from sqlalchemy.orm import Mapped, mapped_column
from werkzeug.exceptions import BadRequest

from src.exchange.domain.base import Base


class User(Base):
    __tablename__ = "users"
    id: Mapped[int] = mapped_column(primary_key=True)
    balance: Mapped[float] = mapped_column(FLOAT)

    def decrease_balance(self, amount: float):
        if self.balance < amount:
            raise BadRequest("you don't have enough money to withdraw")
        self.balance -= amount
