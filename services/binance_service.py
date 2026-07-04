from binance.client import Client
from config.settings import API_KEY, SECRET_KEY
from utils.logger import get_logger


logger = get_logger(__name__)


class BinanceService:

    def __init__(self):
        self.client = Client(API_KEY, SECRET_KEY)

        # Connect to Futures Testnet
        self.client.FUTURES_URL = "https://testnet.binancefuture.com/fapi"

    def get_balance(self):
        try:
            balances = self.client.futures_account_balance()

            usdt = next(
                item for item in balances
                if item["asset"] == "USDT"
            )

            logger.info(f"Balance: {usdt['balance']} USDT")

            return usdt

        except Exception as e:
            logger.error(e)
            raise

    def place_market_order(self, symbol, side, quantity):

        try:
            order = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

            logger.info(f"Order executed: {order}")

            return order

        except Exception as e:
            logger.error(e)
            raise
