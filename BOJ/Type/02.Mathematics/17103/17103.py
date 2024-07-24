# 골드바흐 파티션
# pypy3

import math

def gb_cnt(n):
    cnt = 0
    for i in range(2, len(pn_l)):
        if pn_l[i] and pn_l[n-i]:
            cnt += 1
    return math.ceil(cnt/2)

T = int(input())

pn_l = [1]*1000001
pn_l[1] = 0
for i in range(2, 1001):
    if pn_l[i] != 0:
        for j in range(2*i, 1000001, i):
            pn_l[j] = 0

for _ in range(T):
    n = int(input())
    print(gb_cnt(n))
