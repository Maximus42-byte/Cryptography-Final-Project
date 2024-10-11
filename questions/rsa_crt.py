from cryptography.hazmat.primitives.asymmetric import rsa
from sympy.ntheory.modular import crt
from random import randint
from math import log2


class FastRSA:
    def __init__(self):
        private_key = rsa.generate_private_key(
            public_exponent=2**16 + 1,
            key_size=4096,
        )
        private_numbers = private_key.private_numbers()
        public_numbers = private_key.public_key().public_numbers()
        p, q, d = private_numbers.p, private_numbers.q, private_numbers.d
        self.n, self.e = public_numbers.n, public_numbers.e
        self.__dp = d % (p - 1)
        self.__dq = d % (q - 1)
        self.__p = p
        self.__q = q

    def sign(self, m, inject_fault=False):
        m1 = pow(m, self.__dp, self.__p)
        m2 = pow(m, self.__dq, self.__q)
        if inject_fault:
            m2 ^= 1 << randint(0, int(log2(m2)))
        return crt([self.__p, self.__q], [m1, m2])[0]
