# 최소비용 구하기
# 56320KB, 288ms

# deque 활용으로 시간초과
# 다익스트라에서는 heapq 활용하여 해결하여야 한다.
import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def sol(start, end):
    tmp[start] = 0
    heap = [(0, start)]
    while heap:
        r, s = heappop(heap)
        if tmp[end] <= r:
            continue
        for e, c in arr[s]:
            if tmp[e] > (r + c):
                tmp[e] = r + c
                heappush(heap, (tmp[e], e))
    return tmp[end]


N = int(input())
M = int(input())

arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    arr[a].append((b,c))

start, end = map(int, input().split())

tmp = [100000001]*(N+1)
result = sol(start, end)

print(result)
