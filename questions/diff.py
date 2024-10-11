import random


class ToyCipher:
    def __init__(self, num_rounds, round_keys):
        self.num_rounds = num_rounds
        assert len(round_keys) == num_rounds + 1, "invalid number of round keys"
        self.__key = round_keys
        self.sbox = {
            0: 6,
            1: 4,
            2: 12,
            3: 5,
            4: 0,
            5: 7,
            6: 2,
            7: 14,
            8: 1,
            9: 15,
            10: 3,
            11: 13,
            12: 8,
            13: 10,
            14: 9,
            15: 11,
        }
        perms = list(range(16))
        random.shuffle(perms)
        self.sbox = {i:perms[i] for i in range(16)}
        self.inv_sbox = {self.sbox[i]: i for i in range(16)}

    def enc(self, m):
        c = m ^ self.__key[0]
        for i in range(1, self.num_rounds + 1):
            c = self.sbox[c] ^ self.__key[i]
        return c

    def dec(self, c):
        m = c ^ self.__key[-1]
        for i in range(self.num_rounds - 1, -1, -1):
            m = self.inv_sbox[m] ^ self.__key[i]
        return m
