from out import enc, R
from math import prod
from numpy import base_repr

def aa(n):
    return sum(int(i) for i in str(base_repr(n, base=3)))

flag = ''
for i in range(355):
    if i%5 == 0:
        flag += chr(enc[i//5] ^ prod([aa(_) for _ in R[i//5]]))
print(flag)
