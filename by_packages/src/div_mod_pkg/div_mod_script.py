#!/usr/bin/python
"""
A custom divide/modulo script.

Example usage:
div_mod_script.py 10 3
"""
import sys
from div_mod_pkg.div_mod import div_mod


def div_mod_example():
    """
    For testing `console_scripts` only.
    """
    print(__doc__)


if __name__ == "__main__":
    if len(sys.argv) != 3:
        print("Please provide and only provide the dividend and quotient.")
        sys.exit(1)

    dividend = sys.argv[1]
    divisor = sys.argv[2]

    try:
        quotient, remainder = div_mod(dividend, divisor)
    except Exception as e:
        print(e)
        sys.exit(1)

    print(f"{dividend} = {divisor} x {quotient} + {remainder}")
