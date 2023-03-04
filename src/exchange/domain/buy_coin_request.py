import flask
from flask_restx import reqparse


class BuyCoinRequest:
    def __init__(self, request: flask.Request):
        parser = reqparse.RequestParser()
        parser.add_argument('coin', required=True)
        parser.add_argument('amount', type=float, required=True)
        parser.add_argument('user_id', type=int, required=True, help="A")
        args = parser.parse_args(request)
        self.coin: str = args["coin"]
        self.amount: float = args["amount"]
        self.user_id: int = args["user_id"]
