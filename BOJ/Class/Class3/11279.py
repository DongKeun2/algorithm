# 최대 힙 / 실버2

from heapq import heappop, heappush
import sys
input = sys.stdin.readline

N = int(input())
heap = []
for _ in range(N):
    n = int(input())
    if n:
        heappush(heap, -n)
    else:
        if heap:
            print(-heappop(heap))
        else:
            print(0)