# 달팽이는 올라가고 싶다

import math

A, B, V = list(map(int, input().split()))


if V <= A:
    print(1)
else:
    print(math.ceil((V-A)/(A-B) + 1))
