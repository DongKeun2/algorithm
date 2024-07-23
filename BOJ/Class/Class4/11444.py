# 피보나치 수 6 / 골드2

import sys
sys.setrecursionlimit(10**8)

def sol(x):
    if not x in dct:
        if x%2: dct[x] = (((sol((x+1)//2)**2) + (sol((x-1)//2)**2))) % 1000000007
        else: dct[x] = (sol(x//2) % 1000000007) * ((sol(x//2) + sol(x//2 - 1)*2) % 1000000007) % 1000000007
    return dct[x]

n = int(input())
dct = {0: 0, 1: 1}
print(sol(n))