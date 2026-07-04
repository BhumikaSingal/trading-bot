from bot.exceptions import ValidationError


VALID_SIDES = {"BUY", "SELL"}
VALID_TYPES = {"MARKET", "LIMIT"}


def validate_symbol(symbol: str):
    symbol = symbol.upper()

    if not symbol.endswith("USDT"):
        raise ValidationError(
            "Only USDT pairs are supported."
        )

    return symbol


def validate_side(side: str):
    side = side.upper()

    if side not in VALID_SIDES:
        raise ValidationError(
            "Side must be BUY or SELL."
        )

    return side


def validate_order_type(order_type: str):
    order_type = order_type.upper()

    if order_type not in VALID_TYPES:
        raise ValidationError(
            "Order type must be MARKET or LIMIT."
        )

    return order_type


def validate_quantity(quantity: float):
    if quantity <= 0:
        raise ValidationError(
            "Quantity must be greater than zero."
        )

    return quantity


def validate_price(price, order_type):

    if order_type == "LIMIT":

        if price is None:
            raise ValidationError(
                "Price is required for LIMIT orders."
            )

        if price <= 0:
            raise ValidationError(
                "Price must be positive."
            )

    return price
