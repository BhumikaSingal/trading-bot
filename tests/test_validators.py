import pytest

from bot.validators import (
    validate_side,
    validate_quantity
)


def test_valid_side():

    assert validate_side("BUY") == "BUY"


def test_invalid_side():

    with pytest.raises(Exception):
        validate_side("LONG")


def test_quantity():

    assert validate_quantity(1) == 1


def test_negative_quantity():

    with pytest.raises(Exception):
        validate_quantity(-1)
