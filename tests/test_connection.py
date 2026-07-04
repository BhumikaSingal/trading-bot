from services.binance_service import BinanceService


def test_connection():

    bot = BinanceService()

    balance = bot.get_balance()

    assert balance is not None
