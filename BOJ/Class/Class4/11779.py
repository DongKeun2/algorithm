# 최소비용 구하기 2 / 골드3

import sys
from heapq import heappush, heappop
input = sys.stdin.readline

def sol(start, end):
    lst[start] = 0
    heap = [(0, start, [start])]
    result = []
    while heap:
        r, s, road = heappop(heap)
        if s == end:
            result = road
            break
        if lst[end] <= r:
            continue
        for e, c in arr[s]:
            if lst[e] > (r + c):
                lst[e] = r + c
                heappush(heap, (lst[e], e, road + [e]))
    return result


N = int(input())
M = int(input())
arr = [[] for _ in range(N+1)]
for _ in range(M):
    a, b, c = map(int, input().split())
    arr[a].append((b,c))
start, end = map(int, input().split())

lst = [100000001]*(N+1)
result = sol(start, end)

print(lst[end])
print(len(result))
print(*result)