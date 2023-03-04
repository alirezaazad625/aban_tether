from sqlalchemy import select, delete
from sqlalchemy.orm import Session

from src.configs.database import Database
from src.exchange.application.exchange_service import ExchangeService
from src.exchange.domain.buy_coin_request import BuyCoinRequest
from src.exchange.domain.queued_purchase import QueuedPurchase
from src.exchange.domain.transaction import Transaction
from src.exchange.domain.user import User


class ExchangeApplication:
    def buy_coin(self, request: BuyCoinRequest):
        with Session(Database.instance()) as session:
            exchange_service = ExchangeService()
            price = exchange_service.get_coin_price(request.coin) * request.amount
            user = session.scalars((select(User).where(User.id == request.user_id))).one()
            user.decrease_balance(price)
            session.add(user)
            transaction = Transaction(request)
            session.add(transaction)
            if price < 10:
                session.add(QueuedPurchase(transaction))
            else:
                exchange_service.buy_from_exchange(request.coin, request.amount)
            session.commit()

    def perform_queued_purchases(self):
        with Session(Database.instance()) as session:
            exchange_service = ExchangeService()
            from sqlalchemy import func
            coin_list = session.query(QueuedPurchase.coin, func.sum(QueuedPurchase.amount),
                                      func.max(QueuedPurchase.id)).group_by(
                QueuedPurchase.coin).all()
            for coin in coin_list:
                price_per_coin = exchange_service.get_coin_price(coin[0])
                price = price_per_coin * int(coin[1])
                if price >= 10:
                    exchange_service.buy_from_exchange(coin[0], coin[1])
                    session \
                        .query(QueuedPurchase) \
                        .filter(QueuedPurchase.coin == coin[0]) \
                        .filter(QueuedPurchase.id <= coin[2]) \
                        .delete()
                    session.commit()
