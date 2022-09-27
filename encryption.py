from typing import Tuple
import numpy as np
from random import randint

from utils.numberOperations import inverse_in_space
from utils.primeNumberGenerator import generate_prime_number


def get_public_key(source) -> Tuple[int, int]:
    """Get public key related to a source"""

    with open(f'publicKeys/{source}PublicKey.csv', 'r') as f:
        key_public, space = f.read().split(',')
        return int(key_public), int(space)


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
            f"=> space:\n{self.space}"
        )

    def publish(self, sender_id) -> None:
        """Share public key (and space) required for decrypting"""

        publish_address = f"publicKeys/{sender_id}PublicKey.csv"
        with open(publish_address, 'w') as f:
            f.write(f"{self.key_public}, {self.space}")

    def encrypt(self, x) -> int:
        """x^k in Z_m"""

        if self.key_private > 0:
            return pow(x, self.key_private, self.space)
        else:
            return inverse_in_space(pow(x, -self.key_private, self.space), self.space)
