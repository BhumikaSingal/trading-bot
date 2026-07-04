from services.binance_service import BinanceService


def main():

    bot = BinanceService()

    # Check account balance
    bot.get_balance()

    # Place test order
    bot.place_market_order(
        symbol="BTCUSDT",
        side="BUY",
        quantity=0.001
    )


if __name__ == "__main__":
    main()
