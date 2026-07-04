from binance.exceptions import BinanceAPIException

from bot.logging_config import setup_logger

logger = setup_logger()


class OrderService:

    def __init__(self, client):
        self.client = client.client

    def place_market_order(
        self,
        symbol,
        side,
        quantity
    ):

        try:

            logger.info(
                f"MARKET request | "
                f"{symbol} {side} {quantity}"
            )

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="MARKET",
                quantity=quantity
            )

            logger.info(response)

            return response

        except BinanceAPIException as e:
            logger.exception(e)
            raise

    def place_limit_order(
        self,
        symbol,
        side,
        quantity,
        price
    ):

        try:

            logger.info(
                f"LIMIT request | "
                f"{symbol} {side} "
                f"{quantity} @ {price}"
            )

            response = self.client.futures_create_order(
                symbol=symbol,
                side=side,
                type="LIMIT",
                quantity=quantity,
                price=price,
                timeInForce="GTC"
            )

            logger.info(response)

            return response

        except BinanceAPIException as e:
            logger.exception(e)
            raise
