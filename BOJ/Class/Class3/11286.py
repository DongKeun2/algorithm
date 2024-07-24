# 절댓값 힙, 실버1

from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    n = int(input())
    if n: heappush(heap, (-n, -1) if n < 0 else (n, 1) )
    elif len(heap):
        h, sign = heappop(heap)
        print(-h if sign < 0 else h)
    else: print(0)

