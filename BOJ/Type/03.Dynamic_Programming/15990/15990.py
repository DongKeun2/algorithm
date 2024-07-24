# 1, 2, 3 더하기 5

import sys
input = sys.stdin.readline

T = int(input())

nl = [[0 for _ in range(3)] for _ in range(100001)]

nl[1] = [1, 0, 0]
nl[2] = [0, 1, 0]
nl[3] = [1, 1, 1]

for i in range(4, 100001):
    nl[i][0] = nl[i-1][1]%1000000009 + nl[i-1][2]%1000000009
    nl[i][1] = nl[i-2][2]%1000000009 + nl[i-2][0]%1000000009
    nl[i][2] = nl[i-3][0]%1000000009 + nl[i-3][1]%1000000009

for _ in range(T):
    n = int(input())
    print(sum(nl[n])%1000000009)