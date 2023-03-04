from flask import Flask
from flask_restx import Api

from src.exchange.infrastructure.exchange_controller import coin_exchange_controller
from src.migrations import run_migrations

app = Flask(__name__)
api = Api(app)
coin_exchange_controller(app)
run_migrations()

if __name__ == '__main__':
    app.run(host="0.0.0.0")
