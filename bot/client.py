import os

from dotenv import load_dotenv
from binance.client import Client

load_dotenv()


class BinanceFuturesClient:

    def __init__(self):

        api_key = os.getenv("BINANCE_API_KEY")
        secret_key = os.getenv("BINANCE_SECRET_KEY")

        self.client = Client(api_key, secret_key)

        self.client.FUTURES_URL = (
            "https://testnet.binancefuture.com/fapi"
        )
