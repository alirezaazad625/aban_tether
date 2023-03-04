from sqlalchemy import FLOAT, String
from sqlalchemy.orm import Mapped, mapped_column

from src.exchange.domain.base import Base
from src.exchange.domain.transaction import Transaction


class QueuedPurchase(Base):
    __tablename__ = "queued_purchases"
    id: Mapped[int] = mapped_column(primary_key=True)
    amount: Mapped[float] = mapped_column(FLOAT)
    coin: Mapped[str] = mapped_column(String)

    def __init__(self, transaction: Transaction):
        super().__init__()
        self.amount = transaction.amount
        self.coin = transaction.coin
