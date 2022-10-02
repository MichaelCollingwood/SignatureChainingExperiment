from typing import Tuple


def gcd_extended(a, b) -> Tuple[int, int, int]:
    """gcd(a,b) = x*a + y*b"""

    if a == 0:
        return b, 0, 1

    gcd, x1, y1 = gcd_extended(b % a, a)
    x = y1 - (b // a) * x1
    y = x1

    return gcd, x, y


def inverse_in_space(x, space) -> int:
    """x^-1 in Z_{space}"""

    inverse = gcd_extended(space, x)[2]

    return inverse
