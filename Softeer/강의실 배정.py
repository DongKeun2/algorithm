# 강의실 배정 Lv3

import sys
from heapq import heappop, heappush
input = sys.stdin.readline

N = int(input())
h = []
for i in range(N):
    st, et = list(map(int, input().split()))
    heappush(h, (-et, st))

t = 0
result = 1
while h:
    et, st = heappop(h)
    et = -et
    if t >= et:
        result += 1
        t = st
    elif t < st:
        t = st
print(result)