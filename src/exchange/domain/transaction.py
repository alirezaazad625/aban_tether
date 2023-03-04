from datetime import datetime

from sqlalchemy import FLOAT, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column

from src.exchange.domain.base import Base
from src.exchange.domain.buy_coin_request import BuyCoinRequest
from src.exchange.domain.user import User


class Transaction(Base):
    __tablename__ = "transactions"
    id: Mapped[int] = mapped_column(primary_key=True)
    user_id: Mapped[int] = mapped_column(ForeignKey(f"{User.__tablename__}.id"))
    amount: Mapped[float] = mapped_column(FLOAT)
    coin: Mapped[str] = mapped_column(String)
    created_at: Mapped[datetime] = mapped_column(TIMESTAMP)

    def __init__(self, request: BuyCoinRequest):
        super().__init__()
        self.user_id = request.user_id
        self.amount = request.amount
        self.coin = request.coin
        self.created_at = datetime.now()
