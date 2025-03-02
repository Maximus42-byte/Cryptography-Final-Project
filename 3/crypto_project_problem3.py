# -*- coding: utf-8 -*-
"""Crypto_project_problem3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/15aT6Wrj6HLV_ULtqqtYDDvEFj_SlYYzP

**part1**
"""

# Commented out IPython magic to ensure Python compatibility.
# %pip install cryptography

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

"""**part2**"""

import os , math

def gcdExtended(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = gcdExtended(b % a, a)
        return (g, x - (b // a) * y, y)

def modInverse(a, m):
    g, x, y = gcdExtended(a, m)
    if g != 1:
        raise Exception("Inverse doesn't exist")
    else:
        return x % m

file = open("/content/sig1.txt",'r')

lines = file.readlines()

type(lines) , len(lines)

lines[0]

n = int(lines[0][2:len(lines[0])-1])
n

lines[1], len(lines[1])

e = int(lines[1][2:len(lines[1])])
e

lines[2]

m = int(lines[2][2:len(lines[2])])
m

lines[3]

sign = int(lines[3][4:len(lines[3])])
sign

def get_data(file_path):
  file = open(file_path,'r')
  lines = file.readlines()
  n = int(lines[0][2:len(lines[0])])
  e = int(lines[1][2:len(lines[1])])
  m = int(lines[2][2:len(lines[2])])
  sign = int(lines[3][4:len(lines[3])])
  return n , e , m , sign

file1 = "/content/sig1.txt"
file2 = "/content/sig2.txt"
file3 = "/content/sig3.txt"

#checking for sig1.txt
n1, e1, m1, sign1 = get_data(file1)
mm1 = pow(sign1, e1, n1)
if (m1 == mm1 ):
  print("correct signiture")

#checking for sig2.txt
n2, e2, m2, sign2 = get_data(file2)
mm2 = pow(sign2, e2, n2)
if (m2 == mm2 ):
  print("correct signiture")
else:
  print("Incorrect signiture")

#checking for sig3.txt
n3, e3, m3, sign3 = get_data(file3)
mm3 = pow(sign3, e3, n3)
if (m3 == mm3 ):
  print("correct signiture")
else:
  print("Incorrect signiture")

"""paper's approach"""

n3, e3, m3, sign3 = get_data(file3)

q = math.gcd(n3, (pow(sign3, e3, n3) - m3))

q

p = n3 // q

p

fi3 = (p-1)*(q-1)

fi3

d3 = modInverse(e3, fi3)

d3