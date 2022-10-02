import numpy as np
import random
import unittest

from encryption import RSAAlgorithm, gcd_extended


class GCDTests(unittest.TestCase):
    def test_correct(self):
        for _ in range(10):
            b = random.randint(1000, 1000000)
            a = b + random.randint(1000, 10000000)
            gcd, x, y = gcd_extended(a, b)

            self.assertEqual(gcd, x*a + y*b, "Supposed to be: gcd = xa + yb")


class RSAAlgorithmTests(unittest.TestCase):
    def test_rsa(self):
        for _ in range(10):
            rsa_algorithm = RSAAlgorithm(512)
            message = random.randint(0, 1000)
            encrypted_message = rsa_algorithm.encrypt(message)
            decrypted_message = pow(encrypted_message, rsa_algorithm.key_public, rsa_algorithm.space)

            self.assertEqual(message, decrypted_message, "Decrypted message incorrect.")

    def test_e_coprime(self):
        for _ in range(10):
            rsa_algorithm = RSAAlgorithm(512)
            e = rsa_algorithm.key_public
            phi_m = rsa_algorithm.phi_m

            self.assertEqual(1, np.gcd(e, phi_m), "Public key not invertible.")

    def test_inversion(self):
        for _ in range(10):
            rsa_algorithm = RSAAlgorithm(512)
            e = rsa_algorithm.key_public
            d = rsa_algorithm.key_private
            phi_m = rsa_algorithm.phi_m

            self.assertEqual(1, (e * d) % phi_m, "Private key not inversion of public key.")


if __name__ == '__main__':
    unittest.main()
