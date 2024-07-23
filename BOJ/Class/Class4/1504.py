# 특정한 최단 경로 / 골드4
# 최단 경로, 다익스트라

from heapq import heappop, heappush
import sys
input = sys.stdin.readline

def sol(start, end):
    vst = [10**16] * (N+1)
    vst[start] = 0
    heap = []
    heappush(heap, (0, start))
    while heap:
        tot, s = heappop(heap)
        for e, t in arr[s]:
            if vst[e] > tot + t:
                vst[e] = tot + t
                heappush(heap, (tot+t, e)) 
    return vst[end]

N, E = map(int, input().split())
arr = [[] for _ in range(N+1)]
for _ in range(E):
    a, b, c = map(int, input().split())
    arr[a].append((b, c))
    arr[b].append((a, c))
u, v = map(int, input().split())

answer = min(sol(1, v) + sol(u, N), sol(1, u) + sol(v, N)) + sol(u, v)
print(answer if answer < 10**16 else -1)