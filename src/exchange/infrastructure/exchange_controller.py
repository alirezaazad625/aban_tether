from flask import request as http_request, Flask

from src.exchange.application.exchange_application import ExchangeApplication
from src.exchange.domain.buy_coin_request import BuyCoinRequest


def coin_exchange_controller(app: Flask):
    application = ExchangeApplication()

    @app.route('/coins/buy', methods=['POST'])
    def buy_coin():
        request = BuyCoinRequest(http_request)
        application.buy_coin(request)
        return {}, 200

def perform_queued_purchases():
    application = ExchangeApplication()
    application.perform_queued_purchases()