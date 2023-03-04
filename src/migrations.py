from sqlalchemy import MetaData, Table, Integer, Column, Float, String, TIMESTAMP, ForeignKey
from sqlalchemy.orm import Session

from src.configs.database import Database
from src.exchange.domain.queued_purchase import QueuedPurchase
from src.exchange.domain.transaction import Transaction
from src.exchange.domain.user import User


def run_migrations():
    engine = Database.instance()
    with Session(engine) as session:
        metadata = MetaData()
        if not engine.dialect.has_table(session.connection(), User.__tablename__):
            Table(User.__tablename__, metadata,
                  Column('id', Integer, primary_key=True, autoincrement=True),
                  Column('balance', Float))
        if not engine.dialect.has_table(session.connection(), Transaction.__tablename__):
            Table(Transaction.__tablename__, metadata,
                  Column('id', Integer, primary_key=True, autoincrement=True),
                  Column('user_id', Integer, ForeignKey(f'{User.__tablename__}.id')),
                  Column('amount', Float),
                  Column('coin', String),
                  Column('created_at', TIMESTAMP),
                  )
        if not engine.dialect.has_table(session.connection(), QueuedPurchase.__tablename__):
            Table(QueuedPurchase.__tablename__, metadata,
                  Column('id', Integer, primary_key=True, autoincrement=True),
                  Column('amount', Float),
                  Column('coin', String)
                  )
        metadata.create_all(engine)
