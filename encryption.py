from typing import Tuple
import numpy as np
from random import randint

from utils.prime_number_generator import generate_prime_number


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


class RSAAlgorithm:
    """Algorithm for encrypting messages and publishing public keys"""

    def __init__(
            self,
            n_prime,
            **test_conditions
    ):
        p1 = generate_prime_number(n_prime) if 'p1' not in test_conditions else test_conditions['p1']
        p2 = generate_prime_number(n_prime) if 'p2' not in test_conditions else test_conditions['p2']

        self.space = p1 * p2
        self.phi_m = (p1 - 1) * (p2 - 1)  # Secret

        if 'e' not in test_conditions:
            while True:
                self.key_public = randint(0, self.phi_m - 1)
                if np.gcd(self.key_public, self.phi_m) == 1:
                    break
        else:
            self.key_public = test_conditions['e']

        self.key_private = inverse_in_space(self.key_public, self.phi_m)  # Secret
        print(
            f"RSA Algorithm Variables\n"
            f"=> public key:\n{self.key_public}\n"
            f"=> space:\n{self.space}\n"
        )

    def publish(self, sender_id) -> None:
        """Share public key (and space) required for decrypting"""

        publish_address = f"public_keys/{sender_id}_public_key.csv"
        with open(publish_address, 'w') as f:
            f.write(f"{self.key_public}, {self.space}")

    def encrypt(self, x) -> int:
        """x^k in Z_m"""

        if self.key_private > 0:
            return pow(x, self.key_private, self.space)
        else:
            return inverse_in_space(pow(x, -self.key_private, self.space), self.space)
