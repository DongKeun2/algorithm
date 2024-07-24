# GCD 합

import math

t = int(input())

for _ in range(t):
    n = list(map(int, input().split()))

    gcd_l = [0]
    for i in range(1, len(n)-1):
        for j in range(i+1, len(n)):
            gcd_l.append(math.gcd(n[i], n[j]))

    print(sum(gcd_l))
