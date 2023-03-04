from sqlalchemy import create_engine, Engine


class Database(object):
    _instance = None

    def __init__(self):
        raise RuntimeError('Call instance() instead')

    @classmethod
    def instance(cls) -> Engine:
        if cls._instance is None:
            cls._instance = create_engine("sqlite:///data/db.db", echo=True).connect()
        return cls._instance
