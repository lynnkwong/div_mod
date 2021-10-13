"""
A custom divide/modulo function.

Example usage:
from div_mod import div_mod
quotient, remainder = div_mod(10, 3)
"""
from typing import Tuple


def div_mod(dividend: int, divisor: int) -> Tuple[int, int]:
    """
    Get the quotient and remainder of the dividend and divisor.

    :param dividend: the dividend, must be an integer.
    :param divisor: the divisor, must a non-zero integer.
    :return: the quotient and remainder of the dividend and divisor.
    """
    try:
        quotient = int(dividend) // int(divisor)
        remainder = int(dividend) % int(divisor)
    except (TypeError, ValueError, ZeroDivisionError):
        raise Exception(
            "The dividend and divisor must be interger, "
            "and the divisor cannot be zero."
        )

    return quotient, remainder
