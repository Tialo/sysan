from itertools import product
from math import log2 as log

def task():
    Hab = Ha = Hb = Ha_b = 0
    probs = [[0] * 37 for _ in range(13)]
    for i, j in product(range(1, 7), range(1, 7)):
        probs[i + j][i * j] += 1 / 36
        Hab += -log(1 / 36) / 36
    for i in range(1, 13):
        Ha_i = 0
        for j in range(1, 37):
            Ha_i += probs[i][j]
        if abs(Ha_i) > 1e-16:
            Ha += -Ha_i * log(Ha_i)
    for j in range(1, 37):
        Hb_j = 0
        for i in range(1, 13):
            Hb_j += probs[i][j]
        if abs(Hb_j) > 1e-16:
            Hb += -Hb_j * log(Hb_j)
    Ha_b = Hab - Ha
    print(f"H(A) = {Ha}")
    print(f"H(AB) = {Hab}")
    print(f"Ha(B) = {Ha_b}")
    print(f"H(B) = {Hb}")
    print(f"I(A,B) = {Hb - Ha_b}") 

task()

