import click

from bot.client import BinanceFuturesClient
from bot.orders import OrderService
from bot.validators import (
    validate_symbol,
    validate_side,
    validate_order_type,
    validate_quantity,
    validate_price
)


@click.command()
@click.option(
    "--symbol",
    prompt=True,
    help="Example: BTCUSDT"
)
@click.option(
    "--side",
    prompt=True,
    help="BUY or SELL"
)
@click.option(
    "--order-type",
    prompt=True,
    help="MARKET or LIMIT"
)
@click.option(
    "--quantity",
    prompt=True,
    type=float
)
@click.option(
    "--price",
    required=False,
    type=float
)
def main(
    symbol,
    side,
    order_type,
    quantity,
    price
):

    try:

        symbol = validate_symbol(symbol)
        side = validate_side(side)
        order_type = validate_order_type(order_type)
        quantity = validate_quantity(quantity)
        price = validate_price(
            price,
            order_type
        )

        print("\nORDER REQUEST")
        print("----------------")
        print(f"Symbol: {symbol}")
        print(f"Side: {side}")
        print(f"Type: {order_type}")
        print(f"Quantity: {quantity}")

        if price:
            print(f"Price: {price}")

        client = BinanceFuturesClient()
        service = OrderService(client)

        if order_type == "MARKET":

            response = service.place_market_order(
                symbol,
                side,
                quantity
            )

        else:

            response = service.place_limit_order(
                symbol,
                side,
                quantity,
                price
            )

        print("\nORDER RESPONSE")
        print("----------------")

        print(
            f"Order ID: "
            f"{response.get('orderId')}"
        )

        print(
            f"Status: "
            f"{response.get('status')}"
        )

        print(
            f"Executed Qty: "
            f"{response.get('executedQty')}"
        )

        print(
            f"Average Price: "
            f"{response.get('avgPrice')}"
        )

        print("\nSUCCESS")

    except Exception as e:

        print("\nFAILED")
        print(e)


if __name__ == "__main__":
    main()
